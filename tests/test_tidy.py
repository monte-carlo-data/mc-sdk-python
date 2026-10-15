# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0

"""Tests for tools/gendocs/tidy: pydantic's metadata comes off types, its descriptions stay."""

# The generated code spells types with typing.Optional and Union, so the tests do too.
# ruff: noqa: UP007, UP045

from __future__ import annotations

import operator
from typing import Annotated, Optional, Union

from pydantic import Field, StrictStr

from tools.gendocs import tidy


def test_unwrap_strips_annotated_at_any_depth() -> None:
    nested = Optional[Annotated[str, Field(description="x")]]
    assert tidy.unwrap(nested) == Optional[str]
    assert (
        tidy.unwrap(Union[None, Annotated[float, "m"], tuple[float, float]])
        == Union[None, float, tuple[float, float]]
    )
    # A PEP 604 union, built at runtime: `Annotated[...] | None` doesn't type-check.
    assert tidy.unwrap(operator.or_(Annotated[int, "m"], None)) == int | None
    assert tidy.unwrap(StrictStr) is str


def test_description_finds_the_field_description_at_any_depth() -> None:
    assert tidy.description(Optional[Annotated[str, Field(description="Id.")]]) == "Id."
    assert tidy.description(str) == ""
