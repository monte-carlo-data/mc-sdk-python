# GcpCollectionAgentOut

A collection agent running on GCP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the collection agent. | 
**name** | **str** | Display name of the collection agent. Null when it has no name. | [optional] 
**deployment_id** | **UUID** | Identifier of the deployment this collection agent runs on. | 
**authentication_type** | [**AuthenticationType**](AuthenticationType.md) | How Monte Carlo authenticates when it calls the collection agent. Null for an agent that connects out instead, such as a generic one. | 
**enabled** | **bool** | Whether Monte Carlo is using this collection agent. An agent Monte Carlo has not validated is not enabled, either because it has not been registered yet or because validation failed. | 
**created_time** | **datetime** | When the collection agent was created. That is when its deployment was provisioned, which is before you register the agent. | [optional] 
**last_updated_time** | **datetime** | When the collection agent was last changed. Registering it, renaming it, changing how Monte Carlo reaches it, and Monte Carlo picking up a new image version all update this. Null until any of those has happened. | [optional] 
**image_build** | **str** | Build of the image the collection agent is running. Null until Monte Carlo has contacted the agent. | [optional] 
**image_version** | **str** | Version of the image the collection agent is running. Null until Monte Carlo has contacted the agent. | [optional] 
**is_remote_upgradeable** | **bool** | Whether Monte Carlo can update the collection agent&#39;s image for you. | 
**cloud_run_url** | **str** | URL of the Cloud Run service Monte Carlo calls. Empty until the agent has been registered. | 

## Example

```python
from pycarlo2.models.gcp_collection_agent_out import GcpCollectionAgentOut

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionAgentOut from a JSON string
gcp_collection_agent_out_instance = GcpCollectionAgentOut.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionAgentOut.to_json())

# convert the object into a dict
gcp_collection_agent_out_dict = gcp_collection_agent_out_instance.to_dict()
# create an instance of GcpCollectionAgentOut from a dict
gcp_collection_agent_out_from_dict = GcpCollectionAgentOut.from_dict(gcp_collection_agent_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


