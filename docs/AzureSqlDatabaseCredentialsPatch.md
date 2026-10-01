# AzureSqlDatabaseCredentialsPatch

A change to existing Azure SQL Database credentials.  A field left out is unchanged. `password` set to null is unchanged. `host`, `port`, `db_name` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 

## Example

```python
from montecarlo.models.azure_sql_database_credentials_patch import AzureSqlDatabaseCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlDatabaseCredentialsPatch from a JSON string
azure_sql_database_credentials_patch_instance = AzureSqlDatabaseCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AzureSqlDatabaseCredentialsPatch.to_json())

# convert the object into a dict
azure_sql_database_credentials_patch_dict = azure_sql_database_credentials_patch_instance.to_dict()
# create an instance of AzureSqlDatabaseCredentialsPatch from a dict
azure_sql_database_credentials_patch_from_dict = AzureSqlDatabaseCredentialsPatch.from_dict(azure_sql_database_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


