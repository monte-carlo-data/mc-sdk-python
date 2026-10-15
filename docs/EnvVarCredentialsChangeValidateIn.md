# EnvVarCredentialsChangeValidateIn

A change to existing environment-variable credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**env_var_name** | **str** | Name of the environment variable on the deployment that holds the connection&#39;s credentials. Must start with &#x60;MCD_&#x60;. | [optional] 
**kms_key_id** | **str** | AWS KMS key the variable&#39;s value is encrypted with. Omit it for a value stored in the clear. | [optional] 

## Example

```python
from pycarlo2.models.env_var_credentials_change_validate_in import EnvVarCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarCredentialsChangeValidateIn from a JSON string
env_var_credentials_change_validate_in_instance = EnvVarCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(EnvVarCredentialsChangeValidateIn.to_json())

# convert the object into a dict
env_var_credentials_change_validate_in_dict = env_var_credentials_change_validate_in_instance.to_dict()
# create an instance of EnvVarCredentialsChangeValidateIn from a dict
env_var_credentials_change_validate_in_from_dict = EnvVarCredentialsChangeValidateIn.from_dict(env_var_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


