# PrestoCredentialsIn

What to create Presto or Trino credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the Presto or Trino coordinator. | 
**port** | **int** | Port the coordinator listens on. | 
**user** | **str** | User Monte Carlo signs in as. | 
**password** | **str** | Password of &#x60;user&#x60;. Leave it out for a cluster that takes none. Stored by Monte Carlo and never returned. | [optional] 
**catalog** | **str** | Catalog Monte Carlo queries. | [optional] 
**var_schema** | **str** | Schema Monte Carlo queries by default. | [optional] 
**http_scheme** | **str** | Whether to reach the coordinator over &#x60;http&#x60; or &#x60;https&#x60;. | [optional] 
**metadata_catalog_id** | **str** | Name of the catalog in the metadata store, when it differs from &#x60;catalog&#x60;. Requires &#x60;catalog&#x60;, which may then hold only lowercase letters, digits, &#x60;_&#x60; and &#x60;-&#x60;. | [optional] 
**ssl_skip_verification** | **bool** | Connect over TLS without checking the server&#39;s certificate. | [optional] 

## Example

```python
from pycarlo2.models.presto_credentials_in import PrestoCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of PrestoCredentialsIn from a JSON string
presto_credentials_in_instance = PrestoCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(PrestoCredentialsIn.to_json())

# convert the object into a dict
presto_credentials_in_dict = presto_credentials_in_instance.to_dict()
# create an instance of PrestoCredentialsIn from a dict
presto_credentials_in_from_dict = PrestoCredentialsIn.from_dict(presto_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


