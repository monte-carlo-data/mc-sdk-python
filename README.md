# mc-sdk-python

Official Python SDK for the Monte Carlo REST API.

The SDK is one package, `montecarlo`. Most of it is generated from the API's OpenAPI spec;
client construction and credentials are hand-written, so every request is authenticated.

> For the GraphQL API, use [pycarlo](https://pypi.org/project/pycarlo/) instead.
> This SDK targets the REST API. Its name is provisional and it is not yet published.

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

import montecarlo

client = montecarlo.new_client(
    montecarlo.Options(
        endpoint="https://api.getmontecarlo.com",
        token_id=os.environ["MCD_ID"],
        token_secret=os.environ["MCD_TOKEN"],
    )
)
me = montecarlo.UsersApi(client).get_current_user()
```

With OAuth 2.0 client credentials, where `instance` selects the deployment the gateway routes
to:

```python
client = montecarlo.new_client(
    montecarlo.Options(
        endpoint="https://api.getmontecarlo.com",
        client_id=os.environ["MCD_CLIENT_ID"],
        client_secret=os.environ["MCD_CLIENT_SECRET"],
        instance="us1",
    )
)
```

Tokens are fetched and renewed as needed, so a long-lived client does not go stale.

The operations and the request and response models they take are all importable from the
package, so one import covers everything: `montecarlo.DeploymentIn`, `montecarlo.ProblemOut`,
and so on. Errors from the API raise `montecarlo.ApiException`; a misconfiguration raises
`montecarlo.auth.CredentialsError` when the client is built.

### Using credentials you have already configured

If you have configured the Monte Carlo CLI, the SDK reads the same `mcd_id` and `mcd_token`
from `~/.mcd/profiles.ini`. You still pass `endpoint` yourself, since the CLI's `configure`
command never writes one:

```python
client = montecarlo.new_client(montecarlo.Options(endpoint="https://api.getmontecarlo.com"))
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

This SDK does not read `MCD_API_ENDPOINT`, even though the CLI and pycarlo both do. That
variable carries the GraphQL endpoint, and `endpoint` here is the REST base URL.

To pick a profile other than `default`, set `profile`, or the `MCD_DEFAULT_PROFILE`
environment variable. A profile you name in `profile` has to exist; the SDK reports that rather
than quietly falling back to different credentials. `MCD_DEFAULT_PROFILE` only selects which
section is read when a profile is consulted at all.

## What is generated and what is not

| Path | |
|---|---|
| `montecarlo/api/`, `montecarlo/models/`, `api_client.py`, `api_response.py`, `configuration.py`, `exceptions.py`, `rest.py`, `__init__.py` | Generated. Do not edit. One module per operation group and one per schema. |
| `docs/` | Generated API reference; see below. |
| `.openapi-generator/` | Generator bookkeeping. |
| `montecarlo/auth.py`, `oauth.py`, `profile.py` | Hand-written. `new_client`, `Options`, and the credential resolution behind them. |
| `tests/` | Hand-written tests for the hand-written surface. |

The generator writes at the repository root, replacing any path it emits and deleting nothing.
Every hand-written file it would otherwise emit (`pyproject.toml`, `README.md`, `.gitignore`,
and the three modules inside the package) is listed in `.openapi-generator-ignore`; other
hand-written files (`tests/`, `AGENTS.md`, `LICENSE`, the CI workflow) are names the generator
never emits and need no entry. Adding a file that shares a generated path without listing it
risks a silent overwrite.

## API reference

`docs/` holds one page per operation group and per schema:

- [`CollectionAgentsApi`](docs/CollectionAgentsApi.md)
- [`CollectionDataStoresApi`](docs/CollectionDataStoresApi.md)
- [`DeploymentsApi`](docs/DeploymentsApi.md)
- [`UsersApi`](docs/UsersApi.md)

Each generated page's "All URIs are relative to *http://localhost*" line and its example block
are generator boilerplate: the example builds `Configuration` and `ApiClient` directly and sets
`access_token` on the configuration, which `to_debug_report()` then renders. Ignore both and
build the client with `montecarlo.new_client` as shown under [Usage](#usage); the real base URL
is whatever `endpoint` you pass.

## Contributing

The generated files track the API and are not edited by hand. A fix to one of them belongs in
the API or in the generator, so please open an issue describing what is wrong rather than a
patch. Changes to the hand-written files (`auth.py`, `oauth.py`, `profile.py` and their tests)
are welcome as pull requests.
