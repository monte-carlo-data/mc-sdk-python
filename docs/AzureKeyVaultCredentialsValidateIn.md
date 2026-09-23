# AzureKeyVaultCredentialsValidateIn

Candidate Azure Key Vault credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**connection_type** | **str** | What the credentials are for, hyphenated, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;. Decides which checks run. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**databricks_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**akv_secret** | **str** | Name of the Azure Key Vault secret holding the connection&#39;s credentials. | 
**akv_vault_name** | **str** | Name of the key vault. Send this, &#x60;akv_vault_url&#x60;, or both. | [optional] 
**akv_vault_url** | **str** | URL of the key vault. Send this, &#x60;akv_vault_name&#x60;, or both. | [optional] 

## Example

```python
from montecarlo.models.azure_key_vault_credentials_validate_in import AzureKeyVaultCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureKeyVaultCredentialsValidateIn from a JSON string
azure_key_vault_credentials_validate_in_instance = AzureKeyVaultCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureKeyVaultCredentialsValidateIn.to_json())

# convert the object into a dict
azure_key_vault_credentials_validate_in_dict = azure_key_vault_credentials_validate_in_instance.to_dict()
# create an instance of AzureKeyVaultCredentialsValidateIn from a dict
azure_key_vault_credentials_validate_in_from_dict = AzureKeyVaultCredentialsValidateIn.from_dict(azure_key_vault_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


