# EnvVarCredentialsPatch

A change to environment variable credentials.  A field left out is unchanged. An optional field set to null is cleared. `env_var_name` cannot be cleared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**env_var_name** | **str** | Name of the environment variable on the deployment that holds the connection&#39;s credentials. Must start with &#x60;MCD_&#x60;. | [optional] 
**kms_key_id** | **str** | AWS KMS key the variable&#39;s value is encrypted with. Omit it for a value stored in the clear. | [optional] 

## Example

```python
from montecarlo.models.env_var_credentials_patch import EnvVarCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarCredentialsPatch from a JSON string
env_var_credentials_patch_instance = EnvVarCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(EnvVarCredentialsPatch.to_json())

# convert the object into a dict
env_var_credentials_patch_dict = env_var_credentials_patch_instance.to_dict()
# create an instance of EnvVarCredentialsPatch from a dict
env_var_credentials_patch_from_dict = EnvVarCredentialsPatch.from_dict(env_var_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


