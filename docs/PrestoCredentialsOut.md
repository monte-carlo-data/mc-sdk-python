# PrestoCredentialsOut

Presto or Trino credentials Monte Carlo stores. The password is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the Presto or Trino coordinator. | 
**port** | **int** | Port the coordinator listens on. | 
**user** | **str** | User Monte Carlo signs in as. | 
**catalog** | **str** | Catalog Monte Carlo queries. Null unless set. | 
**var_schema** | **str** | Schema Monte Carlo queries by default. Null unless set. | 
**http_scheme** | **str** | Whether to reach the coordinator over &#x60;http&#x60; or &#x60;https&#x60;. Null means &#x60;http&#x60;. | 
**metadata_catalog_id** | **str** | Name of the catalog in the metadata store. Null means it is &#x60;catalog&#x60;. | 
**ssl_skip_verification** | **bool** | Connect over TLS without checking the server&#39;s certificate. | 

## Example

```python
from pycarlo2.models.presto_credentials_out import PrestoCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of PrestoCredentialsOut from a JSON string
presto_credentials_out_instance = PrestoCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(PrestoCredentialsOut.to_json())

# convert the object into a dict
presto_credentials_out_dict = presto_credentials_out_instance.to_dict()
# create an instance of PrestoCredentialsOut from a dict
presto_credentials_out_from_dict = PrestoCredentialsOut.from_dict(presto_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


