# mc-sdk-python

> The Python SDK for the Monte Carlo REST API: one package, `pycarlo2`. Generated from the API's OpenAPI spec, except client construction and credentials (`auth.py`, `oauth.py`, `profile.py`) and the pagination helper (`paging.py`), which are hand-written.

## This repository is public

Treat everything here as customer-facing, including things that are easy to forget:

- **Commit messages and pull request descriptions.** A closed pull request stays visible, a force-pushed commit stays reachable by its sha, and edited descriptions keep an edit history.
- **Docstrings and the reference site**, which are what every user reads.
- **Generated code**, which ships as-is.
- **Every merge to `main`**, which is published to PyPI; see [Releasing](#releasing).

So, **in the contents of any file committed here**: no internal file paths, no ticket identifiers, and no design rationale that only makes sense from the inside. That reasoning belongs in the ticket or in the internal repository that owns generation.

Three internal names are the exception: api-codegen, the generator; monolith, the service the API spec is exported from; and ai-agent, whose MCP tools pin this SDK. Generated files, `.api-codegen-source.json` and the dispatch workflow already name them. Name no other internal repository.

Branch names and pull request metadata may carry ticket identifiers: `<person>/<ticket-id>-<slug>` is the convention, and a merged pull request displays its head branch permanently.

## Stack

- **Language:** Python 3.10+
- **Package manager:** uv
- **Runtime dependencies:** those of the generated client: `urllib3`, `pydantic`, `python-dateutil`, `typing-extensions`

## Common Commands

```bash
uv sync
uv run pytest
uv run ruff check . && uv run ruff format .
uv run pyright
rm -rf site && uv run python -m tools.gendocs.gendocs -o site --version "preview of local"   # writes the reference site to site/
```

Ruff and pyright cover the whole package except the generator's own files, listed in `pyproject.toml`, so a new hand-written module is checked by default. A finding in generated code belongs in the API or in the generator.

## Key Directories

| Path | Purpose |
|------|---------|
| `pycarlo2/` | The whole SDK: import name and PyPI distribution `pycarlo2`. The GraphQL SDK stays `pycarlo` |
| `pycarlo2/auth.py`, `oauth.py`, `profile.py` | **Hand-written.** `new_client`, `Options`, `CredentialsError`, the OAuth token source, the CLI's profiles file |
| `pycarlo2/paging.py` | **Hand-written.** `paginate`, which walks a paginated list's pages and yields every item |
| `pycarlo2/api/`, `pycarlo2/models/` | Generated operations, one module per tag, and one module per schema |
| `pycarlo2/__init__.py`, `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `py.typed` | Generated client plumbing. `__init__.py` comes from a template override that re-exports the hand-written names |
| `docs/` | Generated API reference |
| `.openapi-generator/` | Generator bookkeeping |
| `tools/gendocs/` | **Hand-written.** Builds the SDK reference site; see [Reference docs](#reference-docs) |
| `.github/workflows/publish-docs.yml`, `.github/actions/publish-docs/` | Build the reference on every pull request and publish it |
| `.github/workflows/release.yml`, `.github/scripts/`, `VERSION` | Release every merge to `main` to PyPI and as a GitHub release; see [Releasing](#releasing) |
| `tests/` | **Hand-written.** Tests for the hand-written surface, one module each, plus `conftest.py` and `test_public_surface.py`, which pins the generated `__init__.py`'s re-export of the hand-written names |

## What is generated

Everything under `pycarlo2/` and `docs/` except the three auth modules and `paging.py`. The generator is pointed at the **repository root**, not the package: unlike the Go generator, the Python one writes its packaging scaffold beside the package. It overwrites every path it emits on each run and deletes nothing, so a fix to a generated file does not survive; it belongs in the API or in the generator that reads its spec.

**Anything hand-written the generator would overwrite, or anything we do not want emitted, must be listed in the root `.openapi-generator-ignore`.** That file is what api-codegen's `generate-python-sdk.sh` compares its `PROTECTED` array against, whole line for whole line, before it will run; this section documents the file entry for entry, and CI asserts the hand-written half. Keep the three in step by hand.

- `pyproject.toml`, `README.md`, `.gitignore`: hand-written at the root, where the generator emits its own versions. Load-bearing.
- `.github/workflows/python.yml`, `setup.py`, `setup.cfg`, `requirements.txt`, `test-requirements.txt`, `tox.ini`, `.gitlab-ci.yml`, `.travis.yml`, `git_push.sh`: suppressed, not protected. Generator scaffolding a uv project has no use for (this repository's workflow is `test.yml`); none exists in the tree, and CI asserts that. Load-bearing.
- `pycarlo2/auth.py`, `oauth.py`, `profile.py`, `paging.py`: hand-written inside the package. Defensive: the generator names its own package files `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `__init__.py`, `py.typed`, and writes under `api/` and `models/`.

Twelve root paths verified by running the generator into an empty directory with no ignore file. `generateSourceCodeOnly=true` would suppress them natively but drops `py.typed`, nests `docs/` in the package and emits a `<package>_README.md`, so the ignore file is used instead.

A hand-written file must never take one of the generator's names. Every hand-written module under `pycarlo2/` starts with `# Hand-written, not generator output.`; CI derives the ignore-file check from that marker in both directions. The same goes for identifiers: the generator emits a class per schema in the spec, a `*Api` class per tag, and the fixed names `ApiClient`, `ApiResponse`, `Configuration`, `OpenApiException`, `ApiException` and their siblings. `Options`, `new_client` and `CredentialsError` are reserved against future schemas of those names; a collision surfaces at regeneration time and its only fix is renaming the SDK's public API. `paginate` needs no such reservation: it is reachable only as `pycarlo2.paging.paginate`, never re-exported from the package root, so no generated name can reach it; its file is protected the same way as the other hand-written modules, by the `.openapi-generator-ignore` entry and the CI marker check.

`pycarlo2/__init__.py` is generated from api-codegen's `__init__package.mustache` override, which adds `Options`, `new_client` and `CredentialsError` to the generated `__all__` and imports them after the generated exports. Hand-writing the file instead would lose the automatic listing of new API classes and models. The pagination names deliberately do not join them: the package root holds the generated surface plus the three names a client cannot be built without, pagination is one optional feature, and keeping its names out of the generated `__all__` is also what keeps them out of reach of a future schema of the same name.

`pyproject.toml` always says `0.0.0`. The generation script reads it and stamps it into `__version__`, the User-Agent and the debug report, and the release overwrites all four; see [Releasing](#releasing).

Regeneration is performed by Monte Carlo's internal API code-generation tooling, run by a maintainer from outside this repository; it owns generation for every artifact built from the spec. Consult that tooling to regenerate; it is not reproduced here because it does not ship to consumers of this SDK.

## Authentication

The API publishes one credential mechanism: an `Authorization` bearer header carrying either a Monte Carlo API token or an OAuth 2.0 client-credentials access token. It is validated before a request reaches the service.

An API token has two halves, and the bearer value is the two joined by a colon. `Options` takes them separately and joins them, so a caller never handles that format.

OAuth client credentials are exchanged in the token request's form body, as mc-sdk-go does. The token is cached and renewed a minute before it expires, so a long-lived caller never holds an expired credential. The exchange is retried on connection failures and 5xx responses, never on 4xx.

Credentials are attached to each request as it goes out, by an `ApiClient` subclass, rather than stored on the generated `Configuration`. `Configuration.access_token` stays `None`, so nothing that logs the configuration can leak a credential, and a per-request credential passed through an operation's `_request_auth` wins instead of stacking into a second header. Neither the API client nor the token exchange follows a redirect. The API client returns a 3xx as an `ApiException`, since the API has one host and the credential rides on every request; the token exchange fails on a 3xx, since its request carries the client secret in its form body.

**`endpoint` defaults to `DEFAULT_ENDPOINT`**, the global API that serves every instance, once the caller and a profile have both left it empty. `Options.resolve` applies it, so `validate`'s "endpoint is required" is reached only by options that skip `resolve`. The spec declares no server, so the generated client's default host is empty and the first call fails inside urllib3 with `No host specified`, which is why a client is always built through `new_client`.

## Credentials are shared with the other tools

`~/.mcd/profiles.ini` is written by the CLI and read by pycarlo and mc-sdk-go, so this SDK reads the same file and the same section names. Most keys are shared verbatim: `mcd_id`, `mcd_token`, `mcd_oauth_client_id`, `mcd_oauth_client_secret`, `mcd_token_endpoint`, `mcd_instance_id`. `mcd_api_endpoint` is shared but reinterpreted: the CLI and pycarlo write the GraphQL endpoint there, and this SDK strips a trailing `/graphql` before treating it as the REST base URL.

Precedence is the same three tiers as pycarlo and mc-sdk-go: values passed in, then the `MCD_DEFAULT_*` environment variables, then the profile. Resolution is per mechanism, not per field, so an ambient OAuth environment never displaces an explicit API token. Half of a pair passed in is an error before the environment or the profile is consulted; neither ever completes one. Two deliberate divergences from pycarlo: this SDK does not read `MCD_API_ENDPOINT`, which carries the GraphQL endpoint rather than the REST base URL, and it sends client credentials in the form body rather than as HTTP Basic.

Tests must not read the developer's real credentials. The `isolate` fixture in `tests/conftest.py` clears every environment variable resolution consults and points `HOME` at a temporary directory; use it, and pass the directory it returns as `Options.config_dir`, in any test that builds a client or resolves options.

## Reference docs

`tools/gendocs` runs pdoc over every module in `pycarlo2` except the package roots, which re-export everything beneath them, and writes the reference at https://apidocs.getmontecarlo.com/v2/python/index.html, beside the REST reference at `/v2/`. Its templates add the landing page, which lists every operation with its summary from the spec, and the credential guides in `tools/gendocs/guides/`, which mirror the CLI reference's. Before rendering, `tools/gendocs/tidy.py` clears the generator's noise from pdoc's view of the generated modules: pydantic's `Annotated` metadata and `@validate_call`. It also lists each operation's parameters with the spec's descriptions. Run it as a module, `python -m tools.gendocs.gendocs`, from the repository root. The site is built when it is published, never committed, and `docs/` is not part of it.

The site's CSP allows no inline script or style, no `data:` image or anything loaded from elsewhere, and its host serves no directory index. So search is off, the templates link one stylesheet that `gendocs.py` writes from pdoc's own CSS with each inline icon as a file, and every link names a file. The one script, `tools/gendocs/theme.js`, sets light or dark: the reader's choice, stored as `colorMode` in `localStorage` as the REST reference stores it so the two stay in step, or else the OS preference. `tests/test_gendocs.py` checks all of that, that every API class, model and public name has an entry, that every operation is listed, that links and their `#anchors` resolve, and that the code the landing page and guides quote imports real `pycarlo2` names and calls real `pycarlo2.<name>` attributes, `pycarlo2.<SomeApi>(...)` methods, `Options` keywords and `MCD_*` environment variables. pdoc lives in the `docs` dependency group, which `dev` includes and the publish jobs install alone. pdoc renders the generated set constants in hash order, so `gendocs.py` re-runs itself under `PYTHONHASHSEED=0` to keep every build byte-identical. `/v2/python/` works because the publish also writes the landing page at key `v2/python/`.

`publish-docs.yml` builds the site on every pull request. A push to `dev` publishes a preview to https://apidocs.dev.getmontecarlo.com/v2/python/index.html. After `Test` succeeds on `main`, it publishes `main`'s head; a run for an older commit publishes nothing. It triggers on `Test` by its name, so renaming that workflow stops it. Both publishing roles also trust only this file on its branch, `.github/workflows/publish-docs.yml` on `dev` or `main`, so renaming it, or moving its publish jobs into a reusable workflow, stops publishing. The roles, buckets and distributions are Actions secrets: `DOCS_DEV_*` in the repository, `DOCS_PROD_*` in the `release` environment, the only one the prod role trusts. That environment allows only `main`; don't widen or delete it.

## Branching

Branch from `main` as `<person>/<ticket-id>-<slug>`. Never commit directly to `main`.

`dev` previews the reference docs and is never released; CONTRIBUTING.md's [`dev` branch](CONTRIBUTING.md#the-dev-branch) section says how to use and reset it.

## Releasing

Every merge to `main` is a release, as in mc-sdk-go and mc-cli, and a published version can't be replaced: PyPI never takes a version twice, even after it is deleted. A bad release can be yanked, and the fix ships as the next patch. `.github/scripts/next-tag.sh` works out the tag `v<base>.<n>`: `<base>` is the major.minor in `VERSION`, and `<n>` is one past the highest patch already tagged on that base. A merge that breaks callers, by removing or renaming an operation, a model or a field, or changing the hand-written API, must bump the minor: change `VERSION` (`0.1` to `0.2`) in the same pull request. A regeneration from api-codegen is a release too, and the same rule applies to what it changes. The same `next-tag.sh` and its test live in mc-sdk-go, mc-cli and the Terraform provider; change them together.

`pyproject.toml` always says `0.0.0`, as do the three places the generator stamps it: `__version__` in `pycarlo2/__init__.py`, the User-Agent in `api_client.py` and the debug report in `configuration.py`. The release writes its version over all four with `.github/scripts/stamp-version.sh` before it builds, much as GoReleaser stamps mc-cli's, and never commits the result. So an install from the repository reports `0.0.0`. `0.0.0` on PyPI is the empty placeholder that reserved the name.

After `Test` succeeds on `main`, `release.yml` runs:

1. `tag` tags the merge commit through the org App, which with the `apollo` team is the only actor allowed to create tags; tags are immutable.
2. `build` runs `.github/scripts/build-dist.sh` at the tag's version, without `id-token`. The script stamps the version with `stamp-version.sh`, builds the wheel and sdist, checks them with `check-dist.sh` and `twine check --strict`, then installs the wheel into a clean venv and runs `.github/scripts/smoke.py`, which imports `pycarlo2`, checks `__version__` and builds a client.
3. `publish-pypi` uploads them through PyPI's Trusted Publisher, in the `release` environment, with `skip-existing` so a retry can finish an upload that stopped halfway.
4. `smoke` checks that PyPI serves exactly the files built, installs what PyPI serves into a clean venv and runs the same `smoke.py`.
5. `github-release` runs `.github/scripts/github-release.sh`, which attaches the same wheel and sdist to a GitHub release on the tag. Only the highest version is marked latest. Releases are immutable once published, as tags are, so a rerun leaves a published release alone, replaces a draft that an interrupted run of the job left, and fails rather than delete anyone else's draft. The job gets the script and `smoke.py` from the `release-scripts` artifact, as `smoke` does.

The `package` job in `test.yml` calls the same `build-dist.sh` on every pull request, at the version the merge would get, so the two can't drift. It also runs the tests of `next-tag.sh`, `check-dist.sh`, `stamp-version.sh` and `github-release.sh`. A change that would break a release fails there, before it merges.

PyPI's Trusted Publisher names `release.yml` and the `release` environment, so renaming the file, moving `publish-pypi` into a reusable workflow or renaming the environment stops publishing, and changing the publisher needs a PyPI owner of `pycarlo2`. If a job fails after tagging, use "Re-run failed jobs", which also completes a partial upload. Re-running all jobs finds the commit already tagged and releases nothing, and a commit older than an already-tagged one is never tagged. "Re-run failed jobs" works only while the run's artifacts exist (7 days). A version whose smoke check fails gets no GitHub release, which is right if it is yanked. To create a missing release after that, use the files PyPI serves: download them, check their sha256 against PyPI's, and run `gh release create <tag> <files> --verify-tag --title <tag>` with the notes the job writes, passing `--latest` only if it is the highest version.

Running `release.yml` by hand, from any branch, is a dry run: it publishes `<next version>.dev<run id>` to TestPyPI, or the current version's when HEAD is already released, and smoke-tests it from there. It tags nothing and never reaches PyPI: `publish-testpypi` runs in no environment, and PyPI's publisher requires `release`.

To build a release locally, in a scratch copy, since stamping edits the tree:

```bash
tag=$(.github/scripts/next-tag.sh)
.github/scripts/build-dist.sh "${tag#v}"
```

The licence is Apache-2.0, matching pycarlo and mc-sdk-go.
