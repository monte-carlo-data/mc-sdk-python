# MariaDbCredentialsOut

MariaDB credentials Monte Carlo stores. The password is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**db_name** | **str** | Database to connect to. Null when none is set. | 
**user** | **str** | Database user Monte Carlo logs in as. | 

## Example

```python
from pycarlo2.models.maria_db_credentials_out import MariaDbCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of MariaDbCredentialsOut from a JSON string
maria_db_credentials_out_instance = MariaDbCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(MariaDbCredentialsOut.to_json())

# convert the object into a dict
maria_db_credentials_out_dict = maria_db_credentials_out_instance.to_dict()
# create an instance of MariaDbCredentialsOut from a dict
maria_db_credentials_out_from_dict = MariaDbCredentialsOut.from_dict(maria_db_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


