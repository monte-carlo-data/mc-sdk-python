# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0
"""Writes the pycarlo2 reference site, which publish-docs.yml publishes to apidocs at /v2/python/.

pdoc renders a page per module; the landing page and the guides in guides/ are added here. The
site's CSP allows no inline script or style and no `data:` image, so search is off, the templates
link one stylesheet and one script, and pdoc's icons become files.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import os
import pkgutil
import re
import shutil
import subprocess
import sys
import urllib.parse
import warnings
from dataclasses import dataclass
from pathlib import Path

import pdoc
import pdoc.doc
import pdoc.render
import pdoc.render_helpers
from markupsafe import Markup
from pygments.formatters import HtmlFormatter

import pycarlo2
from tools.gendocs import tidy

HERE = Path(__file__).parent
TEMPLATES = HERE / "templates"
STYLESHEET = "pdoc.css"
# Copied as they are: montecarlo.ai's icons, as the REST and CLI references use, and the script
# that sets the light or dark theme.
STATIC_FILES = ("favicon.png", "apple-touch-icon.png", "theme.js")


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

# pdoc 16's stylesheets, in the order its frame template's style block includes them.
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

# The CLI reference's dark palette, in pdoc's variables. `{root}` is the selector that turns it on.
_DARK_PALETTE = """
{root} {{
    color-scheme: dark;
    --pdoc-background: #0d1117;
}}
{root} .pdoc {{
    --text: #e6edf3;
    --muted: #9198a1;
    --link: #4493f8;
    --link-hover: #79b8ff;
    --code: #151b23;
    --active: #4b3e00;
    --accent: #151b23;
    --accent2: #3d444d;
    --nav-hover: rgba(255, 255, 255, 0.08);
    --name: #79c0ff;
    --def: #7ee787;
    --annotation: #a5d6ff;
}}
"""

# Dark when the reader chose it, or when the OS prefers it and the reader chose nothing.
_DARK_CHOSEN = ':root[data-theme="dark"]'
_DARK_BY_OS = ':root:not([data-theme="light"])'

_DATA_SVG = re.compile(r'url\("data:image/svg\+xml,([^"]*)"\)')


def modules() -> list[str]:
    """Every module that gets a page: all of pycarlo2 except REEXPORTING and private modules."""
    found = pkgutil.walk_packages(pycarlo2.__path__, "pycarlo2.")
    return sorted(m.name for m in found if m.name not in REEXPORTING and "._" not in m.name)


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


def _write_modules(out: Path) -> None:
    """What `pdoc.pdoc` does, with the generated modules tidied before they render."""
    docs = {name: pdoc.doc.Module.from_name(name) for name in modules()}
    for module in docs.values():
        tidy.tidy(module)
        page = out / f"{module.fullname.replace('.', '/')}.html"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(pdoc.render.html_module(module, docs))
    (out / "index.html").write_text(pdoc.render.html_index(docs))


def _write_guides(out: Path) -> None:
    template = pdoc.render.env.get_template("guide.html.jinja2")
    for g in GUIDES:
        body = Markup((HERE / "guides" / g.file).read_text())
        (out / g.file).write_text(template.render(guide=g, body=body, all_modules=modules()))


def dark_css() -> str:
    """The dark palette and code highlighting, for both ways dark is turned on."""

    def rules(root: str) -> str:
        code = HtmlFormatter(style="github-dark").get_style_defs(f"{root} .pdoc-code")
        # Drop the unprefixed rules Pygments adds for line numbers and <pre>.
        scoped = "\n".join(line for line in code.splitlines() if line.startswith(root))
        return _DARK_PALETTE.format(root=root) + scoped + "\n"

    return (
        rules(_DARK_CHOSEN) + "@media (prefers-color-scheme: dark) {\n" + rules(_DARK_BY_OS) + "}\n"
    )


def _write_stylesheet(out: Path) -> None:
    """Writes pdoc's CSS as one file, with each inline SVG icon as a file beside it."""

    def to_file(m: re.Match[str]) -> str:
        svg = urllib.parse.unquote(m.group(1))
        name = f"icon-{hashlib.sha256(svg.encode()).hexdigest()[:12]}.svg"
        (out / name).write_text(svg)
        return f'url("{name}")'

    css = _DATA_SVG.sub(to_file, pdoc.render.env.from_string(_CSS).render()) + dark_css()
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
        # The generated docstrings are reST field lists around the spec's Markdown.
        docformat="restructuredtext",
        search=False,
        show_source=False,
        footer_text=f"pycarlo2 {version}",
        template_directory=TEMPLATES,
    )
    pdoc.render.env.globals.update(
        docs_version=version,
        guides=GUIDES,
        operations=operations(),
        spec_intro=Markup(pdoc.render_helpers.to_html(tidy.spec_intro())),
    )
    with warnings.catch_warnings():
        # The generated models annotate a private ClassVar with a name pdoc cannot resolve.
        warnings.filterwarnings("ignore", message="Error parsing type annotation")
        _write_modules(out)
    _write_guides(out)
    _write_stylesheet(out)
    for name in STATIC_FILES:
        shutil.copyfile(HERE / name, out / name)


def main(argv: list[str] | None = None) -> int:
    # pdoc renders the generated set constants in hash order, so the bytes depend on the seed.
    if os.environ.get("PYTHONHASHSEED") != "0":
        args = sys.argv[1:] if argv is None else argv
        env = {**os.environ, "PYTHONHASHSEED": "0"}
        return subprocess.run(
            [sys.executable, "-m", "tools.gendocs.gendocs", *args], env=env
        ).returncode
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", type=Path, required=True, help="empty directory to write")
    parser.add_argument("--version", required=True, help='shown on every page, e.g. "v1.2.3"')
    args = parser.parse_args(argv)
    build(args.output, args.version)
    return 0


if __name__ == "__main__":
    sys.exit(main())
