# AzureCollectionAgentPatch

Details to change on an Azure collection agent. Only what you send is changed.  A credentials object is the exception: it replaces the stored credentials instead of merging into them, so send every field of the object you send, along with the matching `authentication_type`. Sending only `name` skips the checks against your function app, since a name is not validated against it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_app_key** | [**FunctionAppKeyCredentialsIn**](FunctionAppKeyCredentialsIn.md) | Credentials for &#x60;AZURE_FUNCTION_APP_KEY&#x60;. Send this or &#x60;service_principal&#x60;, never both. | [optional] 
**service_principal** | [**ServicePrincipalCredentialsIn**](ServicePrincipalCredentialsIn.md) | Credentials for &#x60;AZURE_FUNCTION_SERVICE_PRINCIPAL&#x60;. Send this or &#x60;function_app_key&#x60;, never both. | [optional] 
**function_app_url** | **str** | URL of the function app Monte Carlo should call. | [optional] 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 
**authentication_type** | [**AzureAgentAuthenticationType**](AzureAgentAuthenticationType.md) | How Monte Carlo authenticates when it calls the agent. Send it together with the matching credentials object. | [optional] 

## Example

```python
from montecarlo.models.azure_collection_agent_patch import AzureCollectionAgentPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCollectionAgentPatch from a JSON string
azure_collection_agent_patch_instance = AzureCollectionAgentPatch.from_json(json)
# print the JSON string representation of the object
print(AzureCollectionAgentPatch.to_json())

# convert the object into a dict
azure_collection_agent_patch_dict = azure_collection_agent_patch_instance.to_dict()
# create an instance of AzureCollectionAgentPatch from a dict
azure_collection_agent_patch_from_dict = AzureCollectionAgentPatch.from_dict(azure_collection_agent_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


