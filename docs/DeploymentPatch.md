# DeploymentPatch

A change to an existing deployment. Sent when renaming one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the deployment. Left out, the name is unchanged. | [optional] 

## Example

```python
from montecarlo.models.deployment_patch import DeploymentPatch

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


