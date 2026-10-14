# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0

"""Tests for tools/gendocs: the reference site loads under apidocs' CSP and covers the SDK."""

from __future__ import annotations

import ast
import dataclasses
import html
import inspect
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest

import pycarlo2
from pycarlo2.auth import Options
from pycarlo2.profile import ENVIRONMENT_KEYS
from tools.gendocs import gendocs

# The REST reference, one level above the site at /v2/index.html.
REST_REFERENCE = "../index.html"

CSS_URL = re.compile(r"url\(([^)]*)\)")
CODE = re.compile(r"(?s)<pre><code class=\"language-python\">(.*?)</code></pre>")
ENV_NAME = re.compile(r"\bMCD_[A-Z_]+")


# Tags the CSP blocks outright, or that would load what it blocks.
BLOCKED_TAGS = {"style", "img", "iframe", "object", "embed"}


@dataclasses.dataclass
class Tag:
    name: str
    attrs: dict[str, str]
    body: str = ""


class _TagParser(HTMLParser):
    """Collects every start tag. HTMLParser lowercases tag and attribute names, as browsers do,
    so a check on its output can't be dodged by case or spacing."""

    def __init__(self) -> None:
        super().__init__()
        self.tags: list[Tag] = []
        self._open: Tag | None = None  # the <script> or <style> whose body is being read

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.tags.append(Tag(tag, {k: v or "" for k, v in attrs}))
        self._open = self.tags[-1] if tag in ("script", "style") else None

    def handle_endtag(self, tag: str) -> None:
        self._open = None

    def handle_data(self, data: str) -> None:
        if self._open:
            self._open.body += data


def tags(markup: str) -> list[Tag]:
    parser = _TagParser()
    parser.feed(markup)
    parser.close()
    return parser.tags


def csp_problems(markup: str, root: str) -> list[str]:
    """What `default-src 'none'` with same-origin images, scripts and styles would block. The
    one script allowed is theme.js, from `root`, with nothing inline."""
    found = tags(markup)
    problems = [f"<{t.name}>" for t in found if t.name in BLOCKED_TAGS]
    for t in found:
        problems += [f"<{t.name} {a}=>" for a in t.attrs if a == "style" or a.startswith("on")]
    scripts = [(t.attrs, t.body) for t in found if t.name == "script"]
    if scripts != [({"src": f"{root}theme.js"}, "")]:
        problems.append(f"scripts {scripts}")
    return problems


def test_csp_check_is_not_fooled_by_case_or_spacing() -> None:
    ok = '<head><script src="theme.js"></script></head>'
    assert csp_problems(ok, "") == []
    for bad in (
        "<SCRIPT>alert(1)</SCRIPT >",
        '<p STYLE="color: red">',
        "<Style>p {}</Style>",
        '<a OnClick="x()">',
        "<IMG src=x.png>",
    ):
        assert csp_problems(ok + bad, ""), bad


def build(path: Path, version: str = "v1.2.3") -> Path:
    gendocs.build(path, version)
    return path


@pytest.fixture(scope="module")
def site(tmp_path_factory: pytest.TempPathFactory) -> Path:
    return build(tmp_path_factory.mktemp("site"))


def pages(site: Path) -> list[Path]:
    return sorted(site.rglob("*.html"))


def test_every_api_class_and_model_has_a_page(site: Path) -> None:
    exported = [getattr(pycarlo2, name) for name in pycarlo2.__all__]
    classes = [
        c
        for c in exported
        if inspect.isclass(c) and c.__module__.startswith(("pycarlo2.api.", "pycarlo2.models."))
    ]
    assert len(classes) > 200
    for c in classes:
        page = site / (c.__module__.replace(".", "/") + ".html")
        assert f'id="{c.__name__}"' in page.read_text(), f"{c.__name__} has no entry on {page}"


def test_landing_page_lists_every_operation(site: Path) -> None:
    landing = (site / "index.html").read_text()
    for api in gendocs.operations():
        assert api.operations, f"{api.name} has no operations"
        for op in api.operations:
            assert op.summary, f"{api.name}.{op.name} has no summary"
            assert f'href="{api.page}#{api.name}.{op.name}"' in landing
            assert f'id="{api.name}.{op.name}"' in (site / api.page).read_text()


def test_every_guide_has_a_page_linked_from_the_landing_page(site: Path) -> None:
    landing = (site / "index.html").read_text()
    for g in gendocs.GUIDES:
        assert (site / g.file).is_file(), g.file
        assert f'href="{g.file}"' in landing, g.file


def root_pages() -> list[Path]:
    return [gendocs.TEMPLATES / "index.html.jinja2"] + [
        gendocs.HERE / "guides" / g.file for g in gendocs.GUIDES
    ]


def test_quoted_code_uses_only_real_names() -> None:
    """Every Python block on the landing page and the guides parses, and names only `pycarlo2`
    attributes and `Options` fields that exist."""
    fields = {f.name for f in dataclasses.fields(Options)}
    for page in root_pages():
        blocks = CODE.findall(page.read_text())
        assert blocks, f"{page.name} quotes no code"
        for block in blocks:
            tree = ast.parse(html.unescape(block))
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute) and getattr(node.value, "id", "") == "pycarlo2":
                    assert hasattr(pycarlo2, node.attr), f"{page.name}: pycarlo2.{node.attr}"
                if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "Options":
                    for kw in node.keywords:
                        assert kw.arg in fields, f"{page.name}: Options has no {kw.arg}"


def test_quoted_environment_variables_are_ones_the_sdk_reads() -> None:
    for page in root_pages():
        for name in ENV_NAME.findall(page.read_text()):
            if name != "MCD_DEFAULT_":
                assert name in ENVIRONMENT_KEYS, f"{page.name}: the SDK does not read {name}"


def test_pages_load_under_csp(site: Path) -> None:
    """Nothing `default-src 'none'` with same-origin images, scripts and styles would block."""
    for page in pages(site):
        name = page.relative_to(site)
        root = "../" * (len(name.parts) - 1)
        assert csp_problems(page.read_text(), root) == [], name


def test_every_link_names_a_file_of_the_site(site: Path) -> None:
    """The host serves no directory index, so a link to a directory answers 403."""
    for page in pages(site):
        name = page.relative_to(site)
        found = tags(page.read_text())
        for tag, url in [
            (t.name, t.attrs[a]) for t in found for a in ("href", "src") if a in t.attrs
        ]:
            if url.startswith("#") or (tag == "a" and url.startswith("https://")):
                continue
            if page == site / "index.html" and url == REST_REFERENCE:
                continue
            path = url.split("#")[0]
            assert ":" not in path and not path.endswith("/"), f"{name}: <{tag}> {url!r}"
            assert (page.parent / path).is_file(), f"{name}: broken link {url!r}"


def test_every_page_links_the_static_files(site: Path) -> None:
    for page in pages(site):
        html = page.read_text()
        for name in gendocs.STATIC_FILES:
            assert name + '"' in html, f"{page.relative_to(site)} lacks {name}"


def test_stylesheet_loads_only_files_of_the_site(site: Path) -> None:
    css = (site / gendocs.STYLESHEET).read_text()
    assert "@import" not in css
    urls = [u.strip("\"'") for u in CSS_URL.findall(css)]
    assert urls, "the icons are no longer in the stylesheet"
    for url in urls:
        assert ":" not in url, url
        assert (site / url).is_file(), url


def test_stylesheet_turns_dark_by_choice_or_by_os(site: Path) -> None:
    css = (site / gendocs.STYLESHEET).read_text()
    by_os = css.split("@media (prefers-color-scheme: dark) {", 1)
    assert len(by_os) == 2, "no dark rules for the OS preference"
    assert ':root[data-theme="dark"] .pdoc {' in by_os[0]
    assert ':root:not([data-theme="light"]) .pdoc {' in by_os[1]
    assert ':root[data-theme="dark"] .pdoc-code .k {' in css, "no dark code highlighting"


def test_landing_page_links_to_the_rest_reference(site: Path) -> None:
    html = (site / "index.html").read_text()
    assert f'href="{REST_REFERENCE}"' in html
    assert "Version: v1.2.3" in html


def test_output_is_reproducible(site: Path, tmp_path: Path) -> None:
    again = build(tmp_path / "site")
    files = sorted(p.relative_to(site) for p in site.rglob("*") if p.is_file())
    assert files == sorted(p.relative_to(again) for p in again.rglob("*") if p.is_file())
    for f in files:
        assert (site / f).read_bytes() == (again / f).read_bytes(), f"{f} differs between runs"


def test_version_is_required(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        gendocs.build(tmp_path / "site", "")


def test_never_writes_into_a_directory_with_files(tmp_path: Path) -> None:
    (tmp_path / "keep.txt").write_text("")
    with pytest.raises(FileExistsError):
        gendocs.build(tmp_path, "v1.2.3")
