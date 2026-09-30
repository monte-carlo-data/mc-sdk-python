# EnvVarCredentialsValidateIn

Candidate environment-variable credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**connection_type** | **str** | What the credentials are for, hyphenated, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;. Decides which checks run. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**env_var_name** | **str** | Name of the environment variable on the deployment that holds the connection&#39;s credentials. Must start with &#x60;MCD_&#x60;. | 
**kms_key_id** | **str** | AWS KMS key the variable&#39;s value is encrypted with. Omit it for a value stored in the clear. | [optional] 

## Example

```python
from montecarlo.models.env_var_credentials_validate_in import EnvVarCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarCredentialsValidateIn from a JSON string
env_var_credentials_validate_in_instance = EnvVarCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(EnvVarCredentialsValidateIn.to_json())

# convert the object into a dict
env_var_credentials_validate_in_dict = env_var_credentials_validate_in_instance.to_dict()
# create an instance of EnvVarCredentialsValidateIn from a dict
env_var_credentials_validate_in_from_dict = EnvVarCredentialsValidateIn.from_dict(env_var_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


