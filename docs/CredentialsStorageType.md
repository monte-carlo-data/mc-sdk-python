# CredentialsStorageType

Where the secret lives.  `MC_MANAGED` credentials are stored by Monte Carlo. Every other value names a store you run, which Monte Carlo reads from at connection time using the reference you supply.

## Enum

* `MC_MANAGED` (value: `'mc_managed'`)

* `AWS_SECRETS_MANAGER` (value: `'aws_secrets_manager'`)

* `GCP_SECRET_MANAGER` (value: `'gcp_secret_manager'`)

* `AZURE_KEY_VAULT` (value: `'azure_key_vault'`)

* `ENV_VAR` (value: `'env_var'`)

* `FILE` (value: `'file'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


