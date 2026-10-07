# AzureKeyVaultCredentialsPatch

A change to Azure Key Vault credentials.  A field left out is unchanged. An optional field set to null is cleared, as long as one of `akv_vault_name` and `akv_vault_url` remains. `akv_secret` cannot be cleared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**akv_secret** | **str** | Name of the Azure Key Vault secret holding the connection&#39;s credentials. | [optional] 
**akv_vault_name** | **str** | Name of the key vault. Send this, &#x60;akv_vault_url&#x60;, or both. | [optional] 
**akv_vault_url** | **str** | URL of the key vault. Send this, &#x60;akv_vault_name&#x60;, or both. | [optional] 

## Example

```python
from pycarlo2.models.azure_key_vault_credentials_patch import AzureKeyVaultCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultCredentialsPatch from a JSON string
azure_key_vault_credentials_patch_instance = AzureKeyVaultCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultCredentialsPatch.to_json())

# convert the object into a dict
azure_key_vault_credentials_patch_dict = azure_key_vault_credentials_patch_instance.to_dict()
# create an instance of AzureKeyVaultCredentialsPatch from a dict
azure_key_vault_credentials_patch_from_dict = AzureKeyVaultCredentialsPatch.from_dict(azure_key_vault_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


