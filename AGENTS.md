# mc-sdk-python

> The Python SDK for the Monte Carlo REST API: one package, `montecarlo`. Generated from the API's OpenAPI spec, except client construction and credentials (`auth.py`, `oauth.py`, `profile.py`), which are hand-written.

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

Ruff and pyright are scoped to the hand-written files in `pyproject.toml`. Generated code is not linted: a finding there belongs in the API or in the generator.

## Key Directories

| Path | Purpose |
|------|---------|
| `montecarlo/` | The whole SDK: import name `montecarlo`, distribution `montecarlo-sdk`. Both names are provisional until the team settles them |
| `montecarlo/auth.py`, `oauth.py`, `profile.py` | **Hand-written.** `new_client`, `Options`, `CredentialsError`, the OAuth token source, the CLI's profiles file |
| `montecarlo/api/`, `montecarlo/models/` | Generated operations, one module per tag, and one module per schema |
| `montecarlo/__init__.py`, `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `py.typed` | Generated client plumbing. `__init__.py` comes from a template override that re-exports the hand-written names |
| `docs/` | Generated API reference |
| `.openapi-generator/` | Generator bookkeeping |
| `tests/` | **Hand-written.** Tests for the hand-written surface, one module each, plus `conftest.py` |

## What is generated

Everything under `montecarlo/` and `docs/` except the three auth modules. The generator is pointed at the **repository root**, not the package: unlike the Go generator, the Python one writes its packaging scaffold beside the package. It overwrites every path it emits on each run and deletes nothing, so a fix to a generated file does not survive; it belongs in the API or in the generator that reads its spec.

**Anything hand-written the generator would overwrite, or anything we do not want emitted, must be listed in the root `.openapi-generator-ignore`.** That file is what api-codegen's `generate-python-sdk.sh` compares its `PROTECTED` array against, whole line for whole line, before it will run; this section documents the file entry for entry, and CI asserts the hand-written half. Keep the three in step by hand.

- `pyproject.toml`, `README.md`, `.gitignore`: hand-written at the root, where the generator emits its own versions. Load-bearing.
- `.github/workflows/python.yml`, `setup.py`, `setup.cfg`, `requirements.txt`, `test-requirements.txt`, `tox.ini`, `.gitlab-ci.yml`, `.travis.yml`, `git_push.sh`: suppressed, not protected. Generator scaffolding a uv project has no use for (this repository's workflow is `test.yml`); none exists in the tree, and CI asserts that. Load-bearing.
- `montecarlo/auth.py`, `oauth.py`, `profile.py`: hand-written inside the package. Defensive: the generator names its own package files `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `__init__.py`, `py.typed`, and writes under `api/` and `models/`.

Twelve root paths verified by running the generator into an empty directory with no ignore file. `generateSourceCodeOnly=true` would suppress them natively but drops `py.typed`, nests `docs/` in the package and emits a `montecarlo_README.md`, so the ignore file is used instead.

A hand-written file must never take one of the generator's names. The same goes for identifiers: the generator emits a class per schema in the spec, a `*Api` class per tag, and the fixed names `ApiClient`, `ApiResponse`, `Configuration`, `OpenApiException`, `ApiException` and their siblings. `Options`, `new_client` and `CredentialsError` are reserved against future schemas of those names; a collision surfaces at regeneration time and its only fix is renaming the SDK's public API.

`montecarlo/__init__.py` is generated from api-codegen's `__init__package.mustache` override, which adds `Options` and `new_client` to the generated `__all__` and imports them after the generated exports. Hand-writing the file instead would lose the automatic listing of new API classes and models.

The version is spelled once, in `pyproject.toml`. The generation script reads it from there and stamps it into `__version__` and the generated debug report.

Regeneration is performed by Monte Carlo's internal API code-generation tooling, run by a maintainer from outside this repository; it owns generation for every artifact built from the spec. Consult that tooling to regenerate; it is not reproduced here because it does not ship to consumers of this SDK.

## Authentication

The API publishes one credential mechanism: an `Authorization` bearer header carrying either a Monte Carlo API token or an OAuth 2.0 client-credentials access token. It is validated before a request reaches the service.

An API token has two halves, and the bearer value is the two joined by a colon. `Options` takes them separately and joins them, so a caller never handles that format.

OAuth client credentials are exchanged in the token request's form body, as mc-sdk-go does. The token is cached and renewed a minute before it expires, so a long-lived caller never holds an expired credential. The exchange is retried on connection failures and 5xx responses, never on 4xx.

Credentials are attached to each request as it goes out, by an `ApiClient` subclass, rather than stored on the generated `Configuration`. `Configuration.access_token` stays `None`, so nothing that logs the configuration can leak a credential, and a per-request credential passed through an operation's `_request_auth` wins instead of stacking into a second header.

**`endpoint` is always required**, though it can come from a profile rather than the caller. The spec declares no server, so the generated client's default host is empty and a client built without one sends every request nowhere; `new_client` refuses to build it.

## Credentials are shared with the other tools

`~/.mcd/profiles.ini` is written by the CLI and read by pycarlo and mc-sdk-go, so this SDK reads the same file and the same section names. Most keys are shared verbatim: `mcd_id`, `mcd_token`, `mcd_oauth_client_id`, `mcd_oauth_client_secret`, `mcd_token_endpoint`, `mcd_instance_id`. `mcd_api_endpoint` is shared but reinterpreted: the CLI and pycarlo write the GraphQL endpoint there, and this SDK strips a trailing `/graphql` before treating it as the REST base URL.

Precedence is the same three tiers as pycarlo and mc-sdk-go: values passed in, then the `MCD_DEFAULT_*` environment variables, then the profile. Resolution is per mechanism, not per field, so an ambient OAuth environment never displaces an explicit API token. Two deliberate divergences from pycarlo: this SDK does not read `MCD_API_ENDPOINT`, which carries the GraphQL endpoint rather than the REST base URL, and it sends client credentials in the form body rather than as HTTP Basic.

Tests must not read the developer's real credentials. The `isolate` fixture in `tests/conftest.py` clears every environment variable resolution consults and points `HOME` at a temporary directory; use it, and pass the directory it returns as `Options.config_dir`, in any test that builds a client or resolves options.

## Branching

Branch from `main` as `<person>/<ticket-id>-<slug>`. Never commit directly to `main`.

## Releasing

**Not yet.** A distribution name is permanent once published to PyPI, and this SDK's name is not final. Install from the repository until then.

The licence is Apache-2.0, matching pycarlo and mc-sdk-go.
