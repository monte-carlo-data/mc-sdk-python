# Copyright Monte Carlo AI, Inc.
# SPDX-License-Identifier: Apache-2.0

"""Tests for tools/gendocs: the reference site loads under apidocs' CSP and covers the SDK."""

from __future__ import annotations

import ast
import dataclasses
import html
import importlib
import inspect
import os
import pkgutil
import re
import subprocess
import sys
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


REPO_ROOT = Path(__file__).parent.parent

# Rejected outright. Every <img> is, though the CSP allows same-origin images: pdoc's are
# `data:` or external.
BLOCKED_TAGS = {"style", "img", "iframe", "object", "embed"}


# Elements with no end tag, which never enclose another.
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source"}


@dataclasses.dataclass
class Tag:
    name: str
    attrs: dict[str, str]
    parent: Tag | None = None
    body: str = ""


class _TagParser(HTMLParser):
    """Collects every start tag. HTMLParser lowercases tag and attribute names, as browsers do,
    so a check on its output can't be dodged by case or spacing."""

    def __init__(self) -> None:
        super().__init__()
        self.tags: list[Tag] = []
        self._stack: list[Tag] = []
        self._open: Tag | None = None  # the <script> or <style> whose body is being read

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        t = Tag(tag, {k: v or "" for k, v in attrs}, self._stack[-1] if self._stack else None)
        self.tags.append(t)
        if tag not in VOID_TAGS:
            self._stack.append(t)
        self._open = t if tag in ("script", "style") else None

    def handle_endtag(self, tag: str) -> None:
        self._open = None
        names = [t.name for t in self._stack]
        if tag in names:
            del self._stack[len(names) - 1 - names[::-1].index(tag) :]

    def handle_data(self, data: str) -> None:
        if self._open:
            self._open.body += data


def tags(markup: str) -> list[Tag]:
    parser = _TagParser()
    parser.feed(markup)
    parser.close()
    return parser.tags


def csp_problems(markup: str, root: str) -> list[str]:
    """What `default-src 'none'` with same-origin scripts and styles would block, plus every
    <img>. The one script allowed is theme.js, from `root`, with nothing inline."""
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


def public_objects() -> list[tuple[str, object]]:
    return [
        (name, obj)
        for name in pycarlo2.__all__
        if inspect.isclass(obj := getattr(pycarlo2, name)) or inspect.isfunction(obj)
    ]


def test_every_public_name_has_an_entry(site: Path) -> None:
    objects = public_objects()
    assert len(objects) > 200
    for name, obj in objects:
        page = site / (obj.__module__.replace(".", "/") + ".html")  # type: ignore[attr-defined]
        assert f'id="{name}"' in page.read_text(), f"{name} has no entry on {page}"


def test_every_module_is_documented() -> None:
    walked = {m.name for m in pkgutil.walk_packages(pycarlo2.__path__, "pycarlo2.")}
    expected = {m for m in walked | {"pycarlo2"} if "._" not in m} - gendocs.REEXPORTING
    assert set(gendocs.modules()) == expected


def test_landing_page_lists_every_operation(site: Path) -> None:
    api_classes = {
        name: obj
        for name, obj in public_objects()
        if inspect.isclass(obj) and getattr(obj, "__module__", "").startswith("pycarlo2.api.")
    }
    # The generator gives every operation a private `_<operation>_serialize` helper.
    expected = {
        (name, method[1 : -len("_serialize")])
        for name, cls in api_classes.items()
        for method in dir(cls)
        if method.startswith("_") and method.endswith("_serialize")
    }
    assert len(expected) > 100
    documented = {(api.name, op.name) for api in gendocs.operations() for op in api.operations}
    assert expected == documented

    landing = (site / "index.html").read_text()
    for api in gendocs.operations():
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


def is_api_instance(node: ast.expr) -> bool:
    """Whether `node` is `pycarlo2.<Name>(...)` with `<Name>` a real `pycarlo2` attribute."""
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and getattr(node.func.value, "id", "") == "pycarlo2"
        and hasattr(pycarlo2, node.func.attr)
    )


def test_quoted_code_uses_only_real_names() -> None:
    """Every Python block on the landing page and the guides parses, and every `pycarlo2.<name>`,
    `from pycarlo2... import <name>`, `pycarlo2.<Api>(...).<method>` and `Options` field it
    names exists."""
    fields = {f.name for f in dataclasses.fields(Options)}
    for page in root_pages():
        blocks = CODE.findall(page.read_text())
        assert blocks, f"{page.name} quotes no code"
        for block in blocks:
            tree = ast.parse(html.unescape(block))
            for node in ast.walk(tree):
                if isinstance(node, ast.Attribute) and getattr(node.value, "id", "") == "pycarlo2":
                    assert hasattr(pycarlo2, node.attr), f"{page.name}: pycarlo2.{node.attr}"
                if isinstance(node, ast.ImportFrom) and (node.module or "").startswith("pycarlo2"):
                    module = importlib.import_module(node.module or "")
                    for alias in node.names:
                        assert hasattr(module, alias.name), f"{page.name}: {alias.name}"
                if isinstance(node, ast.Attribute) and is_api_instance(node.value):
                    api = getattr(pycarlo2, node.value.func.attr)  # type: ignore[attr-defined]
                    assert hasattr(api, node.attr), f"{page.name}: {api.__name__}.{node.attr}"
                if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "Options":
                    for kw in node.keywords:
                        assert kw.arg in fields, f"{page.name}: Options has no {kw.arg}"


def test_quoted_environment_variables_are_ones_the_sdk_reads() -> None:
    for page in root_pages():
        for name in ENV_NAME.findall(page.read_text()):
            if name != "MCD_DEFAULT_":
                assert name in ENVIRONMENT_KEYS, f"{page.name}: the SDK does not read {name}"


def test_pages_load_under_csp(site: Path) -> None:
    for page in pages(site):
        name = page.relative_to(site)
        root = "../" * (len(name.parts) - 1)
        assert csp_problems(page.read_text(), root) == [], name


def test_every_link_names_a_file_of_the_site(site: Path) -> None:
    """The host serves no directory index, so a link to a directory answers 403. A #fragment
    must be an id on its target page."""
    ids = {
        page.resolve(): {t.attrs["id"] for t in tags(page.read_text()) if "id" in t.attrs}
        for page in pages(site)
    }
    for page in pages(site):
        name = page.relative_to(site)
        found = tags(page.read_text())
        for tag, url in [
            (t.name, t.attrs[a]) for t in found for a in ("href", "src") if a in t.attrs
        ]:
            if tag == "a" and url.startswith("https://"):
                continue
            if page == site / "index.html" and url == REST_REFERENCE:
                continue
            path, _, fragment = url.partition("#")
            assert ":" not in path and not path.endswith("/"), f"{name}: <{tag}> {url!r}"
            target = (page.parent / path).resolve() if path else page.resolve()
            assert target.is_file(), f"{name}: broken link {url!r}"
            if fragment:
                assert fragment in ids.get(target, set()), f"{name}: no anchor for {url!r}"


def test_module_pages_have_the_nav_the_theme_toggle_anchors_to(site: Path) -> None:
    """theme.js inserts the toggle at `nav.pdoc > div`; `colorMode` is the key it shares with
    the REST reference."""
    found = tags((site / "pycarlo2/auth.html").read_text())
    assert any(
        t.name == "div"
        and t.parent is not None
        and t.parent.name == "nav"
        and "pdoc" in t.parent.attrs.get("class", "").split()
        for t in found
    )
    assert "colorMode" in (gendocs.HERE / "theme.js").read_text()


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


def test_no_page_shows_the_generators_noise(site: Path) -> None:
    """Its notices, pydantic's type metadata and decorator, and unparsed reST fields."""
    noise = (
        "OpenAPI Generator",
        "Do not edit",
        "Annotated[",
        "FieldInfo(",
        "@validate_call",
        "PydanticUndefined",
        ":param ",
        ":type ",
    )
    for page in pages(site):
        markup = html.unescape(page.read_text())
        for text in noise:
            assert text not in markup, f"{page.relative_to(site)} shows {text!r}"


def entry_text(page: Path, ident: str) -> str:
    """The text of the entry `ident` on `page`, up to the next entry."""
    markup = page.read_text()
    start = markup.index(f'id="{ident}"')
    end = markup.find('class="classattr"', start + len(ident) + 30)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", markup[start:end])))


def test_operations_list_their_parameters_with_the_specs_descriptions(site: Path) -> None:
    text = entry_text(
        site / "pycarlo2/api/deployments_api.html", "DeploymentsApi.delete_deployment"
    )
    assert "Parameters" in text
    assert "deployment_id : Id of the deployment" in text or "deployment_id: Id of the" in text
    params = text.split("Parameters", 1)[1]
    assert "_request_timeout" not in params, "per-call options belong on the landing page"


def test_model_fields_show_their_type_and_description(site: Path) -> None:
    text = entry_text(site / "pycarlo2/models/warehouse_out.html", "WarehouseOut.name")
    assert "name : Optional[str] Display name of the warehouse" in text


def test_landing_page_documents_errors_and_per_call_options(site: Path) -> None:
    landing = (site / "index.html").read_text()
    assert "application/problem+json" in landing and "X-Request-Id" in landing
    op = inspect.signature(pycarlo2.DeploymentsApi.delete_deployment).parameters
    listed = re.findall(r"<li><code>(_\w+)</code>", landing)
    assert listed and set(listed) == {n for n in op if n.startswith("_")}


def test_landing_page_links_to_the_rest_reference(site: Path) -> None:
    html = (site / "index.html").read_text()
    assert f'href="{REST_REFERENCE}"' in html
    assert "Version: v1.2.3" in html


def cli_build(out: Path, hash_seed: str) -> Path:
    """Builds through the script, as publish-docs.yml does, in a process with `hash_seed`."""
    subprocess.run(
        [sys.executable, "-m", "tools.gendocs.gendocs", "-o", str(out), "--version", "v1.2.3"],
        check=True,
        env={**os.environ, "PYTHONHASHSEED": hash_seed},
        cwd=REPO_ROOT,
    )
    return out


def test_cli_output_is_the_same_whatever_the_hash_seed(tmp_path: Path) -> None:
    a, b = cli_build(tmp_path / "a", "1"), cli_build(tmp_path / "b", "2")
    files = sorted(p.relative_to(a) for p in a.rglob("*") if p.is_file())
    assert files == sorted(p.relative_to(b) for p in b.rglob("*") if p.is_file())
    for f in files:
        assert (a / f).read_bytes() == (b / f).read_bytes(), f"{f} differs between runs"


def test_version_is_required(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        gendocs.build(tmp_path / "site", "")


def test_never_writes_into_a_directory_with_files(tmp_path: Path) -> None:
    (tmp_path / "keep.txt").write_text("")
    with pytest.raises(FileExistsError):
        gendocs.build(tmp_path, "v1.2.3")
