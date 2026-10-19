# FivetranCredentialsPatch

A change to existing Fivetran API credentials.  A field left out is unchanged. `base_url` set to null is cleared. `api_key` and `api_password` set to null are unchanged. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Key of the Fivetran API key. Stored by Monte Carlo and never returned. | [optional] 
**api_password** | **str** | Secret of the Fivetran API key. Stored by Monte Carlo and never returned. | [optional] 
**base_url** | **str** | URL of the Fivetran REST API. Leave it out for https://api.fivetran.com/v1/. Changing it requires sending the credentials&#39; secrets again. | [optional] 

## Example

```python
from pycarlo2.models.fivetran_credentials_patch import FivetranCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of FivetranCredentialsPatch from a JSON string
fivetran_credentials_patch_instance = FivetranCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(FivetranCredentialsPatch.to_json())

# convert the object into a dict
fivetran_credentials_patch_dict = fivetran_credentials_patch_instance.to_dict()
# create an instance of FivetranCredentialsPatch from a dict
fivetran_credentials_patch_from_dict = FivetranCredentialsPatch.from_dict(fivetran_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


