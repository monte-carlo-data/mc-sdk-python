# HiveCredentialsOut

HiveServer2 credentials Monte Carlo stores. Hive needs no secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the HiveServer2. | 
**port** | **int** | Port the HiveServer2 listens on in binary mode. Null means the client&#39;s default. | 
**user** | **str** | User Monte Carlo signs in as. Hive takes no password. | 
**db_name** | **str** | Database Monte Carlo connects to. Null means the default database. | 
**auth_mode** | [**HiveAuthMode**](HiveAuthMode.md) | How Monte Carlo signs in. | 

## Example

```python
from pycarlo2.models.hive_credentials_out import HiveCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of HiveCredentialsOut from a JSON string
hive_credentials_out_instance = HiveCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(HiveCredentialsOut.to_json())

# convert the object into a dict
hive_credentials_out_dict = hive_credentials_out_instance.to_dict()
# create an instance of HiveCredentialsOut from a dict
hive_credentials_out_from_dict = HiveCredentialsOut.from_dict(hive_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


