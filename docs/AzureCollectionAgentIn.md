# AzureCollectionAgentIn

Details Monte Carlo needs to reach a collection agent you have deployed on Azure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | [**AzureAgentAuthenticationType**](AzureAgentAuthenticationType.md) | How Monte Carlo authenticates when it calls the agent. Send it together with the matching credentials object. | 
**deployment_id** | **UUID** | Deployment to register the collection agent on. It must already hold an unregistered Azure collection agent. | 
**function_app_key** | [**FunctionAppKeyCredentialsIn**](FunctionAppKeyCredentialsIn.md) | Credentials for &#x60;AZURE_FUNCTION_APP_KEY&#x60;. Send this or &#x60;service_principal&#x60;, never both. | [optional] 
**function_app_url** | **str** | URL of the function app Monte Carlo should call. | 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 
**service_principal** | [**ServicePrincipalCredentialsIn**](ServicePrincipalCredentialsIn.md) | Credentials for &#x60;AZURE_FUNCTION_SERVICE_PRINCIPAL&#x60;. Send this or &#x60;function_app_key&#x60;, never both. | [optional] 

## Example

```python
from montecarlo.models.azure_collection_agent_in import AzureCollectionAgentIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCollectionAgentIn from a JSON string
azure_collection_agent_in_instance = AzureCollectionAgentIn.from_json(json)
# print the JSON string representation of the object
print(AzureCollectionAgentIn.to_json())

# convert the object into a dict
azure_collection_agent_in_dict = azure_collection_agent_in_instance.to_dict()
# create an instance of AzureCollectionAgentIn from a dict
azure_collection_agent_in_from_dict = AzureCollectionAgentIn.from_dict(azure_collection_agent_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


