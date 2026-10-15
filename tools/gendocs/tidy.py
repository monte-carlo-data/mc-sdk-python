# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Clears openapi-generator's noise from pdoc's view of the generated modules, before rendering.

The generator wraps each parameter and field type in pydantic's `Annotated` metadata, keeps the
real descriptions there, and decorates every operation with `@validate_call`. pdoc would print
all of it.
"""

from __future__ import annotations

import functools
import operator
import types
import typing
from pathlib import Path

import pdoc.doc
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

HAND_WRITTEN = "# Hand-written, not generator output."


def is_generated(module: pdoc.doc.Module) -> bool:
    source = Path(module.source_file or "")
    return not (source.is_file() and source.read_text().startswith(HAND_WRITTEN))


def unwrap(annotation: object) -> object:
    """The type without pydantic's `Annotated` metadata, at any depth."""
    if typing.get_origin(annotation) is typing.Annotated:
        return unwrap(typing.get_args(annotation)[0])
    args = typing.get_args(annotation)
    if not args:
        return annotation
    inner = tuple(unwrap(a) for a in args)
    if isinstance(annotation, types.UnionType):
        return functools.reduce(operator.or_, inner)
    if isinstance(annotation, types.GenericAlias):
        return types.GenericAlias(typing.get_origin(annotation), inner)
    return annotation.copy_with(inner)  # type: ignore[attr-defined]


def description(annotation: object) -> str:
    """The `Field(description=...)` inside `annotation`, at any depth, or ""."""
    if typing.get_origin(annotation) is typing.Annotated:
        for meta in typing.get_args(annotation)[1:]:
            if isinstance(meta, FieldInfo) and meta.description:
                return meta.description
    for arg in typing.get_args(annotation):
        if found := description(arg):
            return found
    return ""


def tidy(module: pdoc.doc.Module) -> None:
    """Overrides the views pdoc renders from, for one generated module. Each is a
    `cached_property`, so a value in the object's `vars()` replaces it."""
    if not is_generated(module):
        return
    for member in module.members.values():
        if isinstance(member, pdoc.doc.Class) and member.taken_from[0] == module.modulename:
            _tidy_class(member)


def _tidy_class(cls: pdoc.doc.Class) -> None:
    fields = getattr(cls.obj, "model_fields", {})
    for member in cls.own_members:
        if isinstance(member, pdoc.doc.Function):
            _tidy_function(member)
        elif isinstance(member, pdoc.doc.Variable):
            if member.name in fields and not member.docstring:
                vars(member)["docstring"] = fields[member.name].description or ""
            member.annotation = unwrap(member.annotation)
            if member.default_value is PydanticUndefined:
                vars(member)["default_value_str"] = ""


def _type_name(annotation: object) -> str:
    """For a parameter the spec doesn't describe, such as a request body: its type."""
    name = getattr(unwrap(annotation), "__name__", "")
    return f"A `{name}`." if name else ""


def _tidy_function(fn: pdoc.doc.Function) -> None:
    sig = fn.signature
    params = list(sig.parameters.values())
    vars(fn)["signature"] = sig.replace(
        parameters=[p.replace(annotation=unwrap(p.annotation)) for p in params],
        return_annotation=unwrap(sig.return_annotation),
    )
    vars(fn)["decorators"] = [d for d in fn.decorators if d != "@validate_call"]
    if ":param " in fn.docstring:
        # The generator's field list says only "(required)" and repeats the per-request options
        # every operation takes; the landing page documents those once.
        summary = fn.docstring.split("\n:param ", 1)[0].rstrip()
        fields = [
            f":param {p.name}: {description(p.annotation) or _type_name(p.annotation)}"
            for p in params
            if p.name != "self" and not p.name.startswith("_")
        ]
        vars(fn)["docstring"] = "\n\n".join([summary, "\n".join(fields)]).strip()
