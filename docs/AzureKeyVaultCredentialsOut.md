# AzureKeyVaultCredentialsOut

Where in Azure Key Vault a connection's credentials live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Null unless set. | 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Null unless set. | 
**akv_secret** | **str** | Name of the Azure Key Vault secret holding the connection&#39;s credentials. | 
**akv_vault_name** | **str** | Name of the key vault. Null when unset. | 
**akv_vault_url** | **str** | URL of the key vault. Null when unset. | 

## Example

```python
from montecarlo.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultCredentialsOut from a JSON string
azure_key_vault_credentials_out_instance = AzureKeyVaultCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultCredentialsOut.to_json())

# convert the object into a dict
azure_key_vault_credentials_out_dict = azure_key_vault_credentials_out_instance.to_dict()
# create an instance of AzureKeyVaultCredentialsOut from a dict
azure_key_vault_credentials_out_from_dict = AzureKeyVaultCredentialsOut.from_dict(azure_key_vault_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


