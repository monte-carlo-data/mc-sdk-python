# DremioCredentialsOut

Dremio credentials Monte Carlo stores. The token is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the Dremio Arrow Flight endpoint, such as &#x60;data.dremio.cloud&#x60; for Dremio Cloud (&#x60;data.eu.dremio.cloud&#x60; in the EU). | 
**port** | **int** | Port Dremio serves Arrow Flight on. | 
**db_name** | **str** | Dremio project or space to connect to. Null when none is set. | 
**tls** | **bool** | Connect over TLS. Dremio Cloud requires it. Null when unset. | 

## Example

```python
from pycarlo2.models.dremio_credentials_out import DremioCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DremioCredentialsOut from a JSON string
dremio_credentials_out_instance = DremioCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(DremioCredentialsOut.to_json())

# convert the object into a dict
dremio_credentials_out_dict = dremio_credentials_out_instance.to_dict()
# create an instance of DremioCredentialsOut from a dict
dremio_credentials_out_from_dict = DremioCredentialsOut.from_dict(dremio_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


