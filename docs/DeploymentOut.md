# DeploymentOut

One deployment, with the fields only a single read returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the deployment. | 
**name** | **str** | Display name of the deployment. | 
**type** | [**DeploymentType**](DeploymentType.md) | What the deployment hosts. Null when nothing is provisioned on it, in which case it has to be provisioned before it can be used. | [optional] 
**runtime_platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the deployment&#39;s collection agent or data store runs. Null for a Monte Carlo hosted deployment, &#x60;AGENT_OBSERVABILITY&#x60; included, which runs neither. Also null for one with nothing provisioned on it, and for one whose platform Monte Carlo has not recorded. | [optional] 
**enabled** | **bool** | Whether the deployment can serve connections. A deployment still waiting for its collection agent or data store to be registered, or with nothing provisioned on it, is not enabled. An &#x60;AGENT_OBSERVABILITY&#x60; deployment is enabled only while its &#x60;status&#x60; is &#x60;READY&#x60;. | 
**created_time** | **datetime** | When the deployment was assigned to your account, or for an &#x60;AGENT_OBSERVABILITY&#x60; deployment, when it was created. Null when Monte Carlo has no record of that. | [optional] 
**last_updated_time** | **datetime** | When Monte Carlo last updated the infrastructure behind the deployment. Null when Monte Carlo has no record of an update. | [optional] 
**status** | [**DeploymentStatus**](DeploymentStatus.md) | How far Monte Carlo has got with setting the deployment up. An &#x60;AGENT_OBSERVABILITY&#x60; deployment is &#x60;PROVISIONING&#x60; while Monte Carlo sets it up, then &#x60;READY&#x60; or &#x60;FAILED&#x60;. Every other deployment is &#x60;READY&#x60;. &#x60;enabled&#x60; says whether the deployment can serve connections. | 
**status_detail** | **str** | More about the status, such as why setting up the deployment failed. Null when there is nothing to add. | [optional] 
**deletion_protection** | **bool** | Whether deleting the deployment is refused once it has been &#x60;READY&#x60;. Only an &#x60;AGENT_OBSERVABILITY&#x60; deployment can be protected. Every other deployment is &#x60;false&#x60;. Turn it off with an update before deleting a protected deployment. | 
**aws_external_id** | **str** | Value to supply when you register an AWS collection agent or data store on this deployment. It goes in the trust policy of the role Monte Carlo assumes. Null until Monte Carlo has generated one, for a deployment on another platform, for a caller who is not permitted to register one, and if the value could not be read just now. Retry the request in that last case. | [optional] 

## Example

```python
from pycarlo2.models.deployment_out import DeploymentOut

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


