# DremioCredentialsPatch

A change to existing Dremio credentials.  A field left out is unchanged. `db_name` or `tls` set to null is cleared. `token` set to null is unchanged. `host` and `port` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** | Dremio project or space to connect to. | [optional] 
**tls** | **bool** | Connect over TLS. Dremio Cloud requires it. | [optional] 
**host** | **str** | Hostname of the Dremio Arrow Flight endpoint, such as &#x60;data.dremio.cloud&#x60; for Dremio Cloud (&#x60;data.eu.dremio.cloud&#x60; in the EU). Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port Dremio serves Arrow Flight on. | [optional] 
**token** | **str** | New personal access token. | [optional] 

## Example

```python
from pycarlo2.models.dremio_credentials_patch import DremioCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DremioCredentialsPatch from a JSON string
dremio_credentials_patch_instance = DremioCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(DremioCredentialsPatch.to_json())

# convert the object into a dict
dremio_credentials_patch_dict = dremio_credentials_patch_instance.to_dict()
# create an instance of DremioCredentialsPatch from a dict
dremio_credentials_patch_from_dict = DremioCredentialsPatch.from_dict(dremio_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


