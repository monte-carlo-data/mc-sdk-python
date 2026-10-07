# MulesoftCredentialsPatch

A change to existing MuleSoft Anypoint credentials.  A field left out is unchanged. `org_id` set to null is cleared. `app_client_secret` set to null is unchanged. `app_client_id` and `region` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_client_id** | **str** | Client ID of the Anypoint connected app. The app needs the View Environment, Read Deployments and Exchange Viewer scopes. | [optional] 
**app_client_secret** | **str** | Secret of the Anypoint connected app. Stored by Monte Carlo and never returned. | [optional] 
**region** | [**MulesoftRegion**](MulesoftRegion.md) | Anypoint Platform instance the organization lives on. | [optional] 
**org_id** | **str** | Anypoint organization or business group to collect from. Set it when your Mule applications are deployed in a business group. Leave it out to collect the organization that owns the connected app. | [optional] 

## Example

```python
from pycarlo2.models.mulesoft_credentials_patch import MulesoftCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of MulesoftCredentialsPatch from a JSON string
mulesoft_credentials_patch_instance = MulesoftCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(MulesoftCredentialsPatch.to_json())

# convert the object into a dict
mulesoft_credentials_patch_dict = mulesoft_credentials_patch_instance.to_dict()
# create an instance of MulesoftCredentialsPatch from a dict
mulesoft_credentials_patch_from_dict = MulesoftCredentialsPatch.from_dict(mulesoft_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


