# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Writes the pycarlo2 reference site, which publish-docs.yml publishes to apidocs at /v2/python/.

pdoc renders a page per module; the landing page and the guides in guides/ are added here. The
site's CSP allows no inline script or style and no `data:`
image, so search is off, the templates link one stylesheet, and pdoc's icons become files.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import pkgutil
import re
import shutil
import sys
import urllib.parse
import warnings
from dataclasses import dataclass
from pathlib import Path

import pdoc
import pdoc.render
from markupsafe import Markup

import pycarlo2

HERE = Path(__file__).parent
TEMPLATES = HERE / "templates"
STYLESHEET = "pdoc.css"
# Copied as they are. montecarlo.ai's icons, as the REST and CLI references use.
STATIC_FILES = ("favicon.png", "apple-touch-icon.png")


@dataclass(frozen=True)
class Guide:
    file: str
    title: str


# Written inside the site's layout from guides/<file>, and linked from every root page.
GUIDES = (
    Guide("credentials-oauth.html", "Set up credentials with an OAuth client"),
    Guide("credentials-api-token.html", "Set up credentials with an API token"),
)

# These re-export every class beneath them, so their pages would repeat the whole SDK.
REEXPORTING = {"pycarlo2", "pycarlo2.api", "pycarlo2.models"}

# pdoc's stylesheets, in the order its frame template includes them.
_CSS = "\n".join(
    "{% include '" + name + "' %}"
    for name in (
        "resources/bootstrap-reboot.min.css",
        "syntax-highlighting.css",
        "theme.css",
        "layout.css",
        "content.css",
        "custom.css",
    )
)

_DATA_SVG = re.compile(r'url\("data:image/svg\+xml,([^"]*)"\)')


def modules() -> list[str]:
    """Every module documented, each defining what its page shows."""
    found = pkgutil.walk_packages(pycarlo2.__path__, "pycarlo2.")
    return sorted(m.name for m in found if m.name not in REEXPORTING)


@dataclass(frozen=True)
class Operation:
    name: str
    summary: str


@dataclass(frozen=True)
class ApiClass:
    name: str
    page: str
    operations: list[Operation]


# The generator emits these beside each operation, which the landing page leaves out.
_VARIANTS = ("_with_http_info", "_without_preload_content")


def operations() -> list[ApiClass]:
    """Every `*Api` class and its operations, each with its summary from the spec."""
    apis = []
    for name in sorted(pycarlo2.__all__):
        cls = getattr(pycarlo2, name)
        if not (inspect.isclass(cls) and cls.__module__.startswith("pycarlo2.api.")):
            continue
        ops = [
            Operation(op, (inspect.getdoc(fn) or "").split("\n", 1)[0])
            for op, fn in inspect.getmembers(cls, inspect.isfunction)
            if not op.startswith("_") and not op.endswith(_VARIANTS)
        ]
        apis.append(ApiClass(name, cls.__module__.replace(".", "/") + ".html", ops))
    return apis


def write_guides(out: Path) -> None:
    template = pdoc.render.env.get_template("guide.html.jinja2")
    for g in GUIDES:
        body = Markup((HERE / "guides" / g.file).read_text())
        (out / g.file).write_text(template.render(guide=g, body=body, all_modules=modules()))


def write_stylesheet(out: Path) -> None:
    """Writes pdoc's CSS as one file, with each inline SVG icon as a file beside it."""

    def to_file(m: re.Match[str]) -> str:
        svg = urllib.parse.unquote(m.group(1))
        name = f"icon-{hashlib.sha256(svg.encode()).hexdigest()[:12]}.svg"
        (out / name).write_text(svg)
        return f'url("{name}")'

    css = _DATA_SVG.sub(to_file, pdoc.render.env.from_string(_CSS).render())
    if "data:" in css:
        raise RuntimeError("pdoc's CSS has a data: URL this script does not extract")
    (out / STYLESHEET).write_text(css)


def build(out: Path, version: str) -> None:
    if not version:
        raise ValueError("a version is required")
    if out.exists() and any(out.iterdir()):
        raise FileExistsError(f"{out} is not empty")
    out.mkdir(parents=True, exist_ok=True)
    pdoc.render.configure(
        docformat="markdown",
        search=False,
        show_source=False,
        footer_text=f"pycarlo2 {version}",
        template_directory=TEMPLATES,
    )
    pdoc.render.env.globals.update(docs_version=version, guides=GUIDES, operations=operations())
    with warnings.catch_warnings():
        # The generated models annotate a private ClassVar with a name pdoc cannot resolve.
        warnings.filterwarnings("ignore", message="Error parsing type annotation")
        pdoc.pdoc(*modules(), output_directory=out)
    write_guides(out)
    write_stylesheet(out)
    for name in STATIC_FILES:
        shutil.copyfile(HERE / name, out / name)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", type=Path, required=True, help="empty directory to write")
    parser.add_argument("--version", required=True, help='shown on every page, e.g. "v1.2.3"')
    args = parser.parse_args(argv)
    build(args.output, args.version)


if __name__ == "__main__":
    sys.exit(main())
