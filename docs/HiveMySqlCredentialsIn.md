# HiveMySqlCredentialsIn

What to create credentials for a Hive metastore on MySQL with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | MySQL database that holds the Hive metastore. | 

## Example

```python
from pycarlo2.models.hive_my_sql_credentials_in import HiveMySqlCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of HiveMySqlCredentialsIn from a JSON string
hive_my_sql_credentials_in_instance = HiveMySqlCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(HiveMySqlCredentialsIn.to_json())

# convert the object into a dict
hive_my_sql_credentials_in_dict = hive_my_sql_credentials_in_instance.to_dict()
# create an instance of HiveMySqlCredentialsIn from a dict
hive_my_sql_credentials_in_from_dict = HiveMySqlCredentialsIn.from_dict(hive_my_sql_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


