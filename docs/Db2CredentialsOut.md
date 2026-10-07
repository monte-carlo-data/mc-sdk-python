# Db2CredentialsOut

Db2 credentials Monte Carlo stores. The password is never returned.

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
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. Null when none is set. | 
**ssl_disabled** | **bool** | Connect without TLS. Null when unset. | 

## Example

```python
from pycarlo2.models.db2_credentials_out import Db2CredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of Db2CredentialsOut from a JSON string
db2_credentials_out_instance = Db2CredentialsOut.from_json(json)
# print the JSON string representation of the object
print(Db2CredentialsOut.to_json())

# convert the object into a dict
db2_credentials_out_dict = db2_credentials_out_instance.to_dict()
# create an instance of Db2CredentialsOut from a dict
db2_credentials_out_from_dict = Db2CredentialsOut.from_dict(db2_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


