# Contributing to mc-sdk-python

The generated files track the API and are not edited by hand. A fix to one of them belongs in
the API or in the generator, so please open an issue describing what is wrong rather than a
patch. Changes to the hand-written files (`auth.py`, `oauth.py`, `profile.py`, `paging.py`, the
reference site in `tools/gendocs/`, and their tests) are welcome as pull requests.

## Development

```bash
uv sync
uv run pytest
uv run ruff check . && uv run ruff format --check .
uv run pyright
rm -rf site && uv run python -m tools.gendocs.gendocs -o site --version "preview of local"
```

The last command builds the SDK reference into `site/`, for previewing it locally; the
[`dev` branch](#the-dev-branch) publishes a preview to dev apidocs.

## What is generated and what is not

| Path | |
|---|---|
| `pycarlo2/api/`, `pycarlo2/models/`, `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `__init__.py` | Generated. Do not edit. One module per operation group and one per schema. |
| `docs/` | The generator's Markdown reference; see below. |
| `.openapi-generator/` | Generator bookkeeping. |
| `pycarlo2/auth.py`, `oauth.py`, `profile.py` | Hand-written. `new_client`, `Options`, and the credential resolution behind them. |
| `pycarlo2/paging.py` | Hand-written. `paginate`, which walks a paginated list. |
| `tests/` | Hand-written tests for the hand-written surface. |
| `tools/gendocs/` | Hand-written. Builds the SDK reference site. |

The generator writes at the repository root, replacing any path it emits and deleting nothing.
Every hand-written file it would otherwise emit (`pyproject.toml`, `README.md`, `.gitignore`,
and the four modules inside the package) is listed in `.openapi-generator-ignore`; other
hand-written files (`tests/`, `tools/`, `AGENTS.md`, `CONTRIBUTING.md`, `LICENSE`, `VERSION`,
the CI workflows and scripts) are names the generator never emits and need no entry. Adding a
file that shares a generated path without listing it risks a silent overwrite.

## The generator's Markdown reference

The hosted [SDK reference](https://apidocs.getmontecarlo.com/v2/python/index.html) is built from
the package by `tools/gendocs`. `docs/` is the generator's Markdown copy, one page per operation
group and per schema:

- [`CollectionAgentsApi`](docs/CollectionAgentsApi.md)
- [`CollectionDataStoresApi`](docs/CollectionDataStoresApi.md)
- [`CredentialsApi`](docs/CredentialsApi.md)
- [`DeploymentsApi`](docs/DeploymentsApi.md)
- [`UsersApi`](docs/UsersApi.md)
- [`WarehousesApi`](docs/WarehousesApi.md)

Each generated page's "All URIs are relative to *http://localhost*" line and its example block
are generator boilerplate: the example builds `Configuration` and `ApiClient` directly and sets
`access_token` on the configuration, which `to_debug_report()` then renders. Ignore both and
build the client with `pycarlo2.new_client` as the README shows; the real base URL is whatever
`endpoint` you pass.

## The `dev` branch

`dev` publishes a preview of the SDK reference to dev apidocs and is never released. Pull
requests, and regeneration from the spec, target `main`. To preview a branch, merge `main` and
the branch into `dev` and push it:

```bash
git fetch origin && git switch -C dev origin/dev && git merge origin/main
git merge <branch> && git push origin dev
```

Nothing keeps `dev` in step with `main`. When abandoned previews pile up, reset it with
`git push --force-with-lease origin origin/main:dev`; that push publishes `main`'s reference to
dev again.
