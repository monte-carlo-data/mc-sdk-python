# LookerCredentialsChangeValidateIn

A change to existing Looker credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**base_url** | **str** | URL of the Looker API, such as https://acme.cloud.looker.com. | [optional] 
**api_client_id** | **str** | Client ID of the Looker API key. | [optional] 
**api_client_secret** | **str** | Client secret of the Looker API key. Stored by Monte Carlo and never returned. | [optional] 
**verify_ssl** | **bool** | Whether to verify Looker&#39;s TLS certificate. Verified when left out. | [optional] 

## Example

```python
from pycarlo2.models.looker_credentials_change_validate_in import LookerCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of LookerCredentialsChangeValidateIn from a JSON string
looker_credentials_change_validate_in_instance = LookerCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(LookerCredentialsChangeValidateIn.to_json())

# convert the object into a dict
looker_credentials_change_validate_in_dict = looker_credentials_change_validate_in_instance.to_dict()
# create an instance of LookerCredentialsChangeValidateIn from a dict
looker_credentials_change_validate_in_from_dict = LookerCredentialsChangeValidateIn.from_dict(looker_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


