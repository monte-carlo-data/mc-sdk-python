# LookerCredentialsIn

What to create Looker API credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | URL of the Looker API, such as https://acme.cloud.looker.com. | 
**api_client_id** | **str** | Client ID of the Looker API key. | 
**api_client_secret** | **str** | Client secret of the Looker API key. Stored by Monte Carlo and never returned. | 
**verify_ssl** | **bool** | Whether to verify Looker&#39;s TLS certificate. Verified when left out. | [optional] 

## Example

```python
from montecarlo.models.looker_credentials_in import LookerCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of LookerCredentialsIn from a JSON string
looker_credentials_in_instance = LookerCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(LookerCredentialsIn.to_json())

# convert the object into a dict
looker_credentials_in_dict = looker_credentials_in_instance.to_dict()
# create an instance of LookerCredentialsIn from a dict
looker_credentials_in_from_dict = LookerCredentialsIn.from_dict(looker_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


