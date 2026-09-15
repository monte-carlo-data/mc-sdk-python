# CollectionAgentOut

A collection agent: the component that reaches your data on Monte Carlo's behalf.  This is the shape the cross-platform list returns. A platform-specific read returns the same fields, with the agent's address named for that platform.

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
**platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the collection agent runs. Use it to build the platform-specific path for any other operation on this agent. Null for an agent whose platform Monte Carlo has not recorded, and no platform-specific path can address one of those. | [optional] 
**endpoint** | **str** | Address Monte Carlo reaches the collection agent at, in whatever form its platform uses. On AWS that is the ARN of a Lambda function, on Azure the URL of a function app, and on GCP the URL of a Cloud Run service. Empty until the agent has been registered. Null for a generic or Snowflake agent, which connect to Monte Carlo rather than being reached. | 

## Example

```python
from montecarlo.models.collection_agent_out import CollectionAgentOut

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionAgentOut from a JSON string
collection_agent_out_instance = CollectionAgentOut.from_json(json)
# print the JSON string representation of the object
print(CollectionAgentOut.to_json())

# convert the object into a dict
collection_agent_out_dict = collection_agent_out_instance.to_dict()
# create an instance of CollectionAgentOut from a dict
collection_agent_out_from_dict = CollectionAgentOut.from_dict(collection_agent_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


