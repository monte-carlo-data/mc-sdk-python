# MulesoftCredentialsChangeValidateIn

A change to existing MuleSoft credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**app_client_id** | **str** | Client ID of the Anypoint connected app. The app needs the View Environment, Read Deployments and Exchange Viewer scopes. | [optional] 
**app_client_secret** | **str** | Secret of the Anypoint connected app. Stored by Monte Carlo and never returned. | [optional] 
**region** | [**MulesoftRegion**](MulesoftRegion.md) | Anypoint Platform instance the organization lives on. | [optional] 
**org_id** | **str** | Anypoint organization or business group to collect from. Set it when your Mule applications are deployed in a business group. Leave it out to collect the organization that owns the connected app. | [optional] 

## Example

```python
from pycarlo2.models.mulesoft_credentials_change_validate_in import MulesoftCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of MulesoftCredentialsChangeValidateIn from a JSON string
mulesoft_credentials_change_validate_in_instance = MulesoftCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(MulesoftCredentialsChangeValidateIn.to_json())

# convert the object into a dict
mulesoft_credentials_change_validate_in_dict = mulesoft_credentials_change_validate_in_instance.to_dict()
# create an instance of MulesoftCredentialsChangeValidateIn from a dict
mulesoft_credentials_change_validate_in_from_dict = MulesoftCredentialsChangeValidateIn.from_dict(mulesoft_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


