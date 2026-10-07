# mc-sdk-python

> The Python SDK for the Monte Carlo REST API: one package, `pycarlo2`. Generated from the API's OpenAPI spec, except client construction and credentials (`auth.py`, `oauth.py`, `profile.py`) and the pagination helper (`paging.py`), which are hand-written.

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

The version is spelled once, in `pyproject.toml`. The generation script reads it from there and stamps it into `__version__` and the generated debug report.

Regeneration is performed by Monte Carlo's internal API code-generation tooling, run by a maintainer from outside this repository; it owns generation for every artifact built from the spec. Consult that tooling to regenerate; it is not reproduced here because it does not ship to consumers of this SDK.

## Authentication

The API publishes one credential mechanism: an `Authorization` bearer header carrying either a Monte Carlo API token or an OAuth 2.0 client-credentials access token. It is validated before a request reaches the service.

An API token has two halves, and the bearer value is the two joined by a colon. `Options` takes them separately and joins them, so a caller never handles that format.

OAuth client credentials are exchanged in the token request's form body, as mc-sdk-go does. The token is cached and renewed a minute before it expires, so a long-lived caller never holds an expired credential. The exchange is retried on connection failures and 5xx responses, never on 4xx.

Credentials are attached to each request as it goes out, by an `ApiClient` subclass, rather than stored on the generated `Configuration`. `Configuration.access_token` stays `None`, so nothing that logs the configuration can leak a credential, and a per-request credential passed through an operation's `_request_auth` wins instead of stacking into a second header. Neither the API client nor the token exchange follows a redirect. The API client returns a 3xx as an `ApiException`, since the API has one host and the credential rides on every request; the token exchange fails on a 3xx, since its request carries the client secret in its form body.

**`endpoint` is always required**, though it can come from a profile rather than the caller. The spec declares no server, so the generated client's default host is empty and the first call fails inside urllib3 with `No host specified`; `new_client` refuses to build such a client.

## Credentials are shared with the other tools

`~/.mcd/profiles.ini` is written by the CLI and read by pycarlo and mc-sdk-go, so this SDK reads the same file and the same section names. Most keys are shared verbatim: `mcd_id`, `mcd_token`, `mcd_oauth_client_id`, `mcd_oauth_client_secret`, `mcd_token_endpoint`, `mcd_instance_id`. `mcd_api_endpoint` is shared but reinterpreted: the CLI and pycarlo write the GraphQL endpoint there, and this SDK strips a trailing `/graphql` before treating it as the REST base URL.

Precedence is the same three tiers as pycarlo and mc-sdk-go: values passed in, then the `MCD_DEFAULT_*` environment variables, then the profile. Resolution is per mechanism, not per field, so an ambient OAuth environment never displaces an explicit API token. Half of a pair passed in is an error before the environment or the profile is consulted; neither ever completes one. Two deliberate divergences from pycarlo: this SDK does not read `MCD_API_ENDPOINT`, which carries the GraphQL endpoint rather than the REST base URL, and it sends client credentials in the form body rather than as HTTP Basic.

Tests must not read the developer's real credentials. The `isolate` fixture in `tests/conftest.py` clears every environment variable resolution consults and points `HOME` at a temporary directory; use it, and pass the directory it returns as `Options.config_dir`, in any test that builds a client or resolves options.

## Branching

Branch from `main` as `<person>/<ticket-id>-<slug>`. Never commit directly to `main`.

## Releasing

**Not yet.** The distribution will publish to PyPI as `pycarlo2`. Install from the repository until then.

The licence is Apache-2.0, matching pycarlo and mc-sdk-go.
