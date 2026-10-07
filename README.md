# mc-sdk-python

Official Python SDK for the Monte Carlo REST API.

The SDK is one package, `pycarlo2`. Most of it is generated from the API's OpenAPI spec.
Client construction and credentials are hand-written, so every request is authenticated, and so
is the helper that walks a paginated list.

> For the GraphQL API, use [pycarlo](https://pypi.org/project/pycarlo/) instead.
> This SDK targets the REST API. It is not yet published to PyPI.

## Install

```bash
pip install git+https://github.com/monte-carlo-data/mc-sdk-python.git
```

Requires Python 3.10 or later. While this repository is internal, `pip` needs a git credential
with access.

## Usage

Every client needs an endpoint. There is no default: the API is reached at a different host per
instance.

With a Monte Carlo API token, supply the two halves separately and the SDK forms the
credential:

```python
import os

import pycarlo2

client = pycarlo2.new_client(
    pycarlo2.Options(
        endpoint="https://api.getmontecarlo.com",
        token_id=os.environ["MCD_ID"],
        token_secret=os.environ["MCD_TOKEN"],
    )
)
me = pycarlo2.UsersApi(client).get_current_user()
```

With OAuth 2.0 client credentials, where `instance` selects the deployment the gateway routes
to:

```python
client = pycarlo2.new_client(
    pycarlo2.Options(
        endpoint="https://api.getmontecarlo.com",
        client_id=os.environ["MCD_CLIENT_ID"],
        client_secret=os.environ["MCD_CLIENT_SECRET"],
        instance="us1",
    )
)
```

Tokens are fetched and renewed as needed, so a long-lived client does not go stale. Neither the token exchange nor the API client follows a redirect.

The operations and the request and response models they take are all importable from the
package, so one import covers everything: `pycarlo2.DeploymentIn`, `pycarlo2.ProblemOut`,
and so on. Errors from the API raise `pycarlo2.ApiException`; a misconfiguration raises
`pycarlo2.CredentialsError` when the client is built.

### Walking a paginated list

A list that pages returns one page per call, with `next_cursor` to ask for the next.
`paginate` follows the cursor for you and yields every item, so nothing has to track it:

```python
from pycarlo2 import WarehousesApi, new_client
from pycarlo2.paging import paginate

warehouses = WarehousesApi(new_client(options))

for warehouse in paginate(warehouses.list_warehouses):
    print(warehouse.id, warehouse.name)
```

Any other keyword arguments go to every call, so a filter a list accepts applies to the whole
walk, except `with_count`, which `paginate` drops, since a walk yields every item and never
reports a total. Each call asks for the largest page the API serves; passing `limit` overrides
it.

A failed request raises whatever the client raises, so a walk ends on an `ApiException` like
any other call. A page that promises more items without a cursor to ask for, or that repeats a
cursor already served, raises `NoCursorError` or `RepeatedCursorError` from the same module;
both subclass `PaginationError`. These guards catch a server that repeats a cursor, not one
that mints a fresh cursor forever, so bound a walk of unknown length yourself with
`itertools.islice` or a timeout passed among the keyword arguments. Call the list method
directly when you want one page, the cursor, or a total.

`paginate` is one function for every paginated list, because a page is recognised by its
attributes. The Go SDK generates an `All` method per list instead.

### Using credentials you have already configured

If you have configured the Monte Carlo CLI, the SDK reads the same `mcd_id` and `mcd_token`
from `~/.mcd/profiles.ini`. You still pass `endpoint` yourself, since the CLI's `configure`
command never writes one:

```python
client = pycarlo2.new_client(pycarlo2.Options(endpoint="https://api.getmontecarlo.com"))
```

If your profile has an `mcd_api_endpoint` key, set when the CLI or pycarlo point at a
non-default deployment, this SDK reads it too but reinterprets it: there it holds the GraphQL
endpoint (`.../graphql`), and this SDK strips the trailing `/graphql` before using it as the
REST base URL.

Resolution picks a whole credential mechanism, not individual fields. If `Options` supplies a
complete mechanism, the environment and the profile are not consulted for credentials.
Otherwise: `MCD_DEFAULT_OAUTH_CLIENT_ID` and `MCD_DEFAULT_OAUTH_CLIENT_SECRET` (with
`MCD_DEFAULT_INSTANCE_ID`) are tried first, then `MCD_DEFAULT_API_ID` and
`MCD_DEFAULT_API_TOKEN`, then a profile from `~/.mcd/profiles.ini`, which the CLI writes. A
profile supplies `instance` and the token endpoint only when it also supplied the OAuth
credentials; an endpoint left empty is always filled from the profile.

A pair is all or nothing. If you pass one half of an API token or of OAuth client credentials,
that is an error; the other half is never filled in from the environment or a profile.

This SDK does not read `MCD_API_ENDPOINT`, even though the CLI and pycarlo both do. That
variable carries the GraphQL endpoint, and `endpoint` here is the REST base URL.

To pick a profile other than `default`, set `profile`, or the `MCD_DEFAULT_PROFILE`
environment variable. A profile you name in `profile` has to exist; the SDK reports that rather
than quietly falling back to different credentials. `MCD_DEFAULT_PROFILE` only selects which
section is read when a profile is consulted at all.

### Usage telemetry

Every request carries `x-mcd-telemetry-reason: user` and `x-mcd-telemetry-service: mc-sdk-python`,
the same headers pycarlo and the CLI send, so Monte Carlo can tell which client made a call.
They carry no arguments or payload. A tool built on the SDK names itself by overriding them with
`client.set_default_header(...)`.

## What is generated and what is not

| Path | |
|---|---|
| `pycarlo2/api/`, `pycarlo2/models/`, `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `__init__.py` | Generated. Do not edit. One module per operation group and one per schema. |
| `docs/` | Generated API reference; see below. |
| `.openapi-generator/` | Generator bookkeeping. |
| `pycarlo2/auth.py`, `oauth.py`, `profile.py` | Hand-written. `new_client`, `Options`, and the credential resolution behind them. |
| `pycarlo2/paging.py` | Hand-written. `paginate`, which walks a paginated list. |
| `tests/` | Hand-written tests for the hand-written surface. |

The generator writes at the repository root, replacing any path it emits and deleting nothing.
Every hand-written file it would otherwise emit (`pyproject.toml`, `README.md`, `.gitignore`,
and the four modules inside the package) is listed in `.openapi-generator-ignore`; other
hand-written files (`tests/`, `AGENTS.md`, `LICENSE`, the CI workflow) are names the generator
never emits and need no entry. Adding a file that shares a generated path without listing it
risks a silent overwrite.

## API reference

`docs/` holds one page per operation group and per schema:

- [`CollectionAgentsApi`](docs/CollectionAgentsApi.md)
- [`CollectionDataStoresApi`](docs/CollectionDataStoresApi.md)
- [`CredentialsApi`](docs/CredentialsApi.md)
- [`DeploymentsApi`](docs/DeploymentsApi.md)
- [`UsersApi`](docs/UsersApi.md)
- [`WarehousesApi`](docs/WarehousesApi.md)

Each generated page's "All URIs are relative to *http://localhost*" line and its example block
are generator boilerplate: the example builds `Configuration` and `ApiClient` directly and sets
`access_token` on the configuration, which `to_debug_report()` then renders. Ignore both and
build the client with `pycarlo2.new_client` as shown under [Usage](#usage); the real base URL
is whatever `endpoint` you pass.

## Contributing

The generated files track the API and are not edited by hand. A fix to one of them belongs in
the API or in the generator, so please open an issue describing what is wrong rather than a
patch. Changes to the hand-written files (`auth.py`, `oauth.py`, `profile.py`, `paging.py` and
their tests) are welcome as pull requests.
