# AzureDedicatedSqlPoolCredentialsIn

What to create Azure Dedicated SQL Pool credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | 

## Example

```python
from montecarlo.models.azure_dedicated_sql_pool_credentials_in import AzureDedicatedSqlPoolCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDedicatedSqlPoolCredentialsIn from a JSON string
azure_dedicated_sql_pool_credentials_in_instance = AzureDedicatedSqlPoolCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AzureDedicatedSqlPoolCredentialsIn.to_json())

# convert the object into a dict
azure_dedicated_sql_pool_credentials_in_dict = azure_dedicated_sql_pool_credentials_in_instance.to_dict()
# create an instance of AzureDedicatedSqlPoolCredentialsIn from a dict
azure_dedicated_sql_pool_credentials_in_from_dict = AzureDedicatedSqlPoolCredentialsIn.from_dict(azure_dedicated_sql_pool_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


