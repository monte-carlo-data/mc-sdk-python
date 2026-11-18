# DeploymentPatch

A change to an existing deployment. Sent when renaming one or changing its protection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the deployment. Left out, the name is unchanged. | [optional] 
**deletion_protection** | **bool** | Whether deleting the deployment is refused once it has been &#x60;READY&#x60;. Left out, it is unchanged. Only an &#x60;AGENT_OBSERVABILITY&#x60; deployment can be protected. Any other type accepts only &#x60;false&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.deployment_patch import DeploymentPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentPatch from a JSON string
deployment_patch_instance = DeploymentPatch.from_json(json)
# print the JSON string representation of the object
print(DeploymentPatch.to_json())

# convert the object into a dict
deployment_patch_dict = deployment_patch_instance.to_dict()
# create an instance of DeploymentPatch from a dict
deployment_patch_from_dict = DeploymentPatch.from_dict(deployment_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


