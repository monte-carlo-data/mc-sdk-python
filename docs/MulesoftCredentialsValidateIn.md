# MulesoftCredentialsValidateIn

Candidate MuleSoft Anypoint credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**app_client_id** | **str** | Client ID of the Anypoint connected app. The app needs the View Environment, Read Deployments and Exchange Viewer scopes. | 
**app_client_secret** | **str** | Secret of the Anypoint connected app. Used for this check and not kept. | 
**region** | [**MulesoftRegion**](MulesoftRegion.md) | Anypoint Platform instance the organization lives on. US when left out. | [optional] 
**org_id** | **str** | Anypoint organization or business group to collect from. Set it when your Mule applications are deployed in a business group. Leave it out to collect the organization that owns the connected app. | [optional] 

## Example

```python
from pycarlo2.models.mulesoft_credentials_validate_in import MulesoftCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of MulesoftCredentialsValidateIn from a JSON string
mulesoft_credentials_validate_in_instance = MulesoftCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(MulesoftCredentialsValidateIn.to_json())

# convert the object into a dict
mulesoft_credentials_validate_in_dict = mulesoft_credentials_validate_in_instance.to_dict()
# create an instance of MulesoftCredentialsValidateIn from a dict
mulesoft_credentials_validate_in_from_dict = MulesoftCredentialsValidateIn.from_dict(mulesoft_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


