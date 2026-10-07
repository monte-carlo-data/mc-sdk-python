# AzureSqlDatabaseCredentialsValidateIn

Candidate Azure SQL Database credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Used for this check and not kept. | 
**db_name** | **str** | Database to connect to. | 

## Example

```python
from pycarlo2.models.azure_sql_database_credentials_validate_in import AzureSqlDatabaseCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSqlDatabaseCredentialsValidateIn from a JSON string
azure_sql_database_credentials_validate_in_instance = AzureSqlDatabaseCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureSqlDatabaseCredentialsValidateIn.to_json())

# convert the object into a dict
azure_sql_database_credentials_validate_in_dict = azure_sql_database_credentials_validate_in_instance.to_dict()
# create an instance of AzureSqlDatabaseCredentialsValidateIn from a dict
azure_sql_database_credentials_validate_in_from_dict = AzureSqlDatabaseCredentialsValidateIn.from_dict(azure_sql_database_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


