# DeploymentIn

What to create a deployment for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**DeploymentType**](DeploymentType.md) | What the deployment will host. &#x60;COLLECTION_AGENT&#x60; and &#x60;COLLECTION_DATA_STORE&#x60; can be provisioned, and an &#x60;AGENT_OBSERVABILITY&#x60; deployment can be created when your account has Monte Carlo hosted Agent Observability. Any other value is rejected. | 
**runtime_platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the deployment&#39;s collection agent or data store will run. Either can be provisioned on &#x60;AWS&#x60;, &#x60;AZURE&#x60; or &#x60;GCP&#x60;, and a collection agent also on &#x60;GENERIC&#x60;. Any other combination is rejected. Required for a collection agent or data store. Leave it out for &#x60;AGENT_OBSERVABILITY&#x60;, which Monte Carlo hosts. | [optional] 
**name** | **str** | Display name for the deployment. Monte Carlo generates one if you leave it out. | [optional] 
**deletion_protection** | **bool** | Whether deleting the deployment is refused once it has been ready. Only an &#x60;AGENT_OBSERVABILITY&#x60; deployment can be protected, and it is protected unless you send &#x60;false&#x60;. Any other type accepts only &#x60;false&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.deployment_in import DeploymentIn

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentIn from a JSON string
deployment_in_instance = DeploymentIn.from_json(json)
# print the JSON string representation of the object
print(DeploymentIn.to_json())

# convert the object into a dict
deployment_in_dict = deployment_in_instance.to_dict()
# create an instance of DeploymentIn from a dict
deployment_in_from_dict = DeploymentIn.from_dict(deployment_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


