# AzureSqlDatabaseCredentialsIn

What to create Azure SQL Database credentials with.

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
from pycarlo2.models.azure_sql_database_credentials_in import AzureSqlDatabaseCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlDatabaseCredentialsIn from a JSON string
azure_sql_database_credentials_in_instance = AzureSqlDatabaseCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AzureSqlDatabaseCredentialsIn.to_json())

# convert the object into a dict
azure_sql_database_credentials_in_dict = azure_sql_database_credentials_in_instance.to_dict()
# create an instance of AzureSqlDatabaseCredentialsIn from a dict
azure_sql_database_credentials_in_from_dict = AzureSqlDatabaseCredentialsIn.from_dict(azure_sql_database_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


