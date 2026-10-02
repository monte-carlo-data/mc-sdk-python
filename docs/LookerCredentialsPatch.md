# LookerCredentialsPatch

A change to existing Looker API credentials.  A field left out is unchanged. `verify_ssl` set to null is cleared. `api_client_secret` set to null is unchanged. `base_url` and `api_client_id` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | URL of the Looker API, such as https://acme.cloud.looker.com. | [optional] 
**api_client_id** | **str** | Client ID of the Looker API key. | [optional] 
**api_client_secret** | **str** | Client secret of the Looker API key. Stored by Monte Carlo and never returned. | [optional] 
**verify_ssl** | **bool** | Whether to verify Looker&#39;s TLS certificate. Verified when left out. | [optional] 

## Example

```python
from montecarlo.models.looker_credentials_patch import LookerCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of LookerCredentialsPatch from a JSON string
looker_credentials_patch_instance = LookerCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(LookerCredentialsPatch.to_json())

# convert the object into a dict
looker_credentials_patch_dict = looker_credentials_patch_instance.to_dict()
# create an instance of LookerCredentialsPatch from a dict
looker_credentials_patch_from_dict = LookerCredentialsPatch.from_dict(looker_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


