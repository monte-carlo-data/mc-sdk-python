# AzureDedicatedSqlPoolCredentialsChangeValidateIn

A change to existing Azure Dedicated SQL Pool credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 

## Example

```python
from pycarlo2.models.azure_dedicated_sql_pool_credentials_change_validate_in import AzureDedicatedSqlPoolCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDedicatedSqlPoolCredentialsChangeValidateIn from a JSON string
azure_dedicated_sql_pool_credentials_change_validate_in_instance = AzureDedicatedSqlPoolCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureDedicatedSqlPoolCredentialsChangeValidateIn.to_json())

# convert the object into a dict
azure_dedicated_sql_pool_credentials_change_validate_in_dict = azure_dedicated_sql_pool_credentials_change_validate_in_instance.to_dict()
# create an instance of AzureDedicatedSqlPoolCredentialsChangeValidateIn from a dict
azure_dedicated_sql_pool_credentials_change_validate_in_from_dict = AzureDedicatedSqlPoolCredentialsChangeValidateIn.from_dict(azure_dedicated_sql_pool_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


