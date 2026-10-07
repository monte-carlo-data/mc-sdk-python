# DeploymentSummaryOut

A deployment: the infrastructure that connects Monte Carlo to your environment.  A deployment hosts a collection agent or a data store, or is hosted by Monte Carlo. This is the shape the list returns; reading a single deployment returns more.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the deployment. | 
**name** | **str** | Display name of the deployment. | 
**type** | [**DeploymentType**](DeploymentType.md) | What the deployment hosts. Null when nothing is provisioned on it, in which case it has to be provisioned before it can be used. | [optional] 
**runtime_platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the deployment&#39;s collection agent or data store runs. Null for a Monte Carlo hosted deployment, which runs neither, for one with nothing provisioned on it, and for one whose platform Monte Carlo has not recorded. | [optional] 
**enabled** | **bool** | Whether the deployment can serve connections. A deployment still waiting for its collection agent or data store to be registered, or with nothing provisioned on it, is not enabled. | 
**created_time** | **datetime** | When the deployment was assigned to your account. Null when Monte Carlo has no record of that. | [optional] 
**last_updated_time** | **datetime** | When Monte Carlo last updated the infrastructure behind the deployment. Null when Monte Carlo has no record of an update. | [optional] 

## Example

```python
from pycarlo2.models.deployment_summary_out import DeploymentSummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentSummaryOut from a JSON string
deployment_summary_out_instance = DeploymentSummaryOut.from_json(json)
# print the JSON string representation of the object
print(DeploymentSummaryOut.to_json())

# convert the object into a dict
deployment_summary_out_dict = deployment_summary_out_instance.to_dict()
# create an instance of DeploymentSummaryOut from a dict
deployment_summary_out_from_dict = DeploymentSummaryOut.from_dict(deployment_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


