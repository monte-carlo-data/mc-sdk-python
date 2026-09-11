# DeploymentOut

One deployment, with the fields only a single read returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_external_id** | **str** | Value to supply when you register an AWS collection agent or data store on this deployment. It goes in the trust policy of the role Monte Carlo assumes. Null until Monte Carlo has generated one, for a deployment on another platform, for a caller who is not permitted to register one, and if the value could not be read just now. Retry the request in that last case. | [optional] 
**created_time** | **datetime** | When the deployment was assigned to your account. Null when Monte Carlo has no record of that. | [optional] 
**enabled** | **bool** | Whether the deployment can serve connections. A deployment still waiting for its collection agent or data store to be registered, or with nothing provisioned on it, is not enabled. | 
**id** | **UUID** | Unique identifier of the deployment. | 
**last_updated_time** | **datetime** | When Monte Carlo last updated the infrastructure behind the deployment. Null when Monte Carlo has no record of an update. | [optional] 
**name** | **str** | Display name of the deployment. | 
**runtime_platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the deployment&#39;s collection agent or data store runs. Null for a Monte Carlo hosted deployment, which runs neither, for one with nothing provisioned on it, and for one whose platform Monte Carlo has not recorded. | [optional] 
**type** | [**DeploymentType**](DeploymentType.md) | What the deployment hosts. Null when nothing is provisioned on it, in which case it has to be provisioned before it can be used. | [optional] 

## Example

```python
from montecarlo.models.deployment_out import DeploymentOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentOut from a JSON string
deployment_out_instance = DeploymentOut.from_json(json)
# print the JSON string representation of the object
print(DeploymentOut.to_json())

# convert the object into a dict
deployment_out_dict = deployment_out_instance.to_dict()
# create an instance of DeploymentOut from a dict
deployment_out_from_dict = DeploymentOut.from_dict(deployment_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


