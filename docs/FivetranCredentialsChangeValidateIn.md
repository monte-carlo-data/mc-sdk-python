# FivetranCredentialsChangeValidateIn

A change to existing Fivetran credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**api_key** | **str** | Key of the Fivetran API key. Stored by Monte Carlo and never returned. | [optional] 
**api_password** | **str** | Secret of the Fivetran API key. Stored by Monte Carlo and never returned. | [optional] 
**base_url** | **str** | URL of the Fivetran REST API. Leave it out for https://api.fivetran.com/v1/. Changing it requires sending the credentials&#39; secrets again. | [optional] 

## Example

```python
from pycarlo2.models.fivetran_credentials_change_validate_in import FivetranCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of FivetranCredentialsChangeValidateIn from a JSON string
fivetran_credentials_change_validate_in_instance = FivetranCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(FivetranCredentialsChangeValidateIn.to_json())

# convert the object into a dict
fivetran_credentials_change_validate_in_dict = fivetran_credentials_change_validate_in_instance.to_dict()
# create an instance of FivetranCredentialsChangeValidateIn from a dict
fivetran_credentials_change_validate_in_from_dict = FivetranCredentialsChangeValidateIn.from_dict(fivetran_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


