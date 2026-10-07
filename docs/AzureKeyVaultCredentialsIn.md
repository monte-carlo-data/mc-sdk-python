# AzureKeyVaultCredentialsIn

Credentials kept in your Azure Key Vault. Monte Carlo stores where to find them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;, or one of your custom connector types. Fixed once created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**akv_secret** | **str** | Name of the Azure Key Vault secret holding the connection&#39;s credentials. | 
**akv_vault_name** | **str** | Name of the key vault. Send this, &#x60;akv_vault_url&#x60;, or both. | [optional] 
**akv_vault_url** | **str** | URL of the key vault. Send this, &#x60;akv_vault_name&#x60;, or both. | [optional] 

## Example

```python
from pycarlo2.models.azure_key_vault_credentials_in import AzureKeyVaultCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultCredentialsIn from a JSON string
azure_key_vault_credentials_in_instance = AzureKeyVaultCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultCredentialsIn.to_json())

# convert the object into a dict
azure_key_vault_credentials_in_dict = azure_key_vault_credentials_in_instance.to_dict()
# create an instance of AzureKeyVaultCredentialsIn from a dict
azure_key_vault_credentials_in_from_dict = AzureKeyVaultCredentialsIn.from_dict(azure_key_vault_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


