# EnvVarCredentialsOut

Which environment variable of the deployment holds a connection's credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Null unless set. | 
**databricks_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Null unless set. | 
**env_var_name** | **str** | Name of the environment variable on the deployment that holds the connection&#39;s credentials. Must start with &#x60;MCD_&#x60;. | 
**kms_key_id** | **str** | AWS KMS key the value is encrypted with. Null for a value in the clear. | 

## Example

```python
from montecarlo.models.env_var_credentials_out import EnvVarCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of EnvVarCredentialsOut from a JSON string
env_var_credentials_out_instance = EnvVarCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(EnvVarCredentialsOut.to_json())

# convert the object into a dict
env_var_credentials_out_dict = env_var_credentials_out_instance.to_dict()
# create an instance of EnvVarCredentialsOut from a dict
env_var_credentials_out_from_dict = EnvVarCredentialsOut.from_dict(env_var_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


