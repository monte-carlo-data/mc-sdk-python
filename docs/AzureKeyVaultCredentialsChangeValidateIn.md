# AzureKeyVaultCredentialsChangeValidateIn

A change to existing Azure Key Vault credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**akv_secret** | **str** | Name of the Azure Key Vault secret holding the connection&#39;s credentials. | [optional] 
**akv_vault_name** | **str** | Name of the key vault. Send this, &#x60;akv_vault_url&#x60;, or both. | [optional] 
**akv_vault_url** | **str** | URL of the key vault. Send this, &#x60;akv_vault_name&#x60;, or both. | [optional] 

## Example

```python
from pycarlo2.models.azure_key_vault_credentials_change_validate_in import AzureKeyVaultCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultCredentialsChangeValidateIn from a JSON string
azure_key_vault_credentials_change_validate_in_instance = AzureKeyVaultCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultCredentialsChangeValidateIn.to_json())

# convert the object into a dict
azure_key_vault_credentials_change_validate_in_dict = azure_key_vault_credentials_change_validate_in_instance.to_dict()
# create an instance of AzureKeyVaultCredentialsChangeValidateIn from a dict
azure_key_vault_credentials_change_validate_in_from_dict = AzureKeyVaultCredentialsChangeValidateIn.from_dict(azure_key_vault_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


