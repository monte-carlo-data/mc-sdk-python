# AwsCollectionAgentOut

A collection agent running on AWS.

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
**lambda_function_arn** | **str** | ARN of the Lambda function Monte Carlo invokes. Empty until the agent has been registered. | 
**external_id** | **str** | Value to supply in the trust policy of the role Monte Carlo assumes to invoke the function. Null until Monte Carlo has generated one, for a caller who is not permitted to register an agent, and if the value could not be read just now. Retry the request in that last case. | [optional] 

## Example

```python
from montecarlo.models.aws_collection_agent_out import AwsCollectionAgentOut

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionAgentOut from a JSON string
aws_collection_agent_out_instance = AwsCollectionAgentOut.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionAgentOut.to_json())

# convert the object into a dict
aws_collection_agent_out_dict = aws_collection_agent_out_instance.to_dict()
# create an instance of AwsCollectionAgentOut from a dict
aws_collection_agent_out_from_dict = AwsCollectionAgentOut.from_dict(aws_collection_agent_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


