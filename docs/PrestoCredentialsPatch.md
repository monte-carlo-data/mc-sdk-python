# PrestoCredentialsPatch

A change to existing Presto or Trino credentials.  A field left out is unchanged. A field set to null is cleared, except `host`, `port` and `user`, which cannot be. `password` set to null is unchanged. Changing `host`, `http_scheme` or `ssl_skip_verification` requires sending `password` again when one is stored. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the Presto or Trino coordinator. Changing it requires sending &#x60;password&#x60; again when one is stored. | [optional] 
**port** | **int** | Port the coordinator listens on. | [optional] 
**user** | **str** | User Monte Carlo signs in as. | [optional] 
**password** | **str** | New password of &#x60;user&#x60;. | [optional] 
**catalog** | **str** | Catalog Monte Carlo queries. | [optional] 
**var_schema** | **str** | Schema Monte Carlo queries by default. | [optional] 
**http_scheme** | **str** | Whether to reach the coordinator over &#x60;http&#x60; or &#x60;https&#x60;. Changing it requires sending &#x60;password&#x60; again when one is stored. | [optional] 
**metadata_catalog_id** | **str** | Name of the catalog in the metadata store, when it differs from &#x60;catalog&#x60;. Requires &#x60;catalog&#x60;, which may then hold only lowercase letters, digits, &#x60;_&#x60; and &#x60;-&#x60;. | [optional] 
**ssl_skip_verification** | **bool** | Connect over TLS without checking the server&#39;s certificate. Changing it requires sending &#x60;password&#x60; again when one is stored. | [optional] 

## Example

```python
from pycarlo2.models.presto_credentials_patch import PrestoCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PrestoCredentialsPatch from a JSON string
presto_credentials_patch_instance = PrestoCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(PrestoCredentialsPatch.to_json())

# convert the object into a dict
presto_credentials_patch_dict = presto_credentials_patch_instance.to_dict()
# create an instance of PrestoCredentialsPatch from a dict
presto_credentials_patch_from_dict = PrestoCredentialsPatch.from_dict(presto_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


