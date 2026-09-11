# AwsCollectionAgentIn

Details Monte Carlo needs to reach a collection agent you have deployed on AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment to register the collection agent on. It must already hold an unregistered AWS collection agent. | 
**lambda_function_arn** | **str** | ARN of the Lambda function Monte Carlo should invoke. | 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 
**role_arn** | **str** | ARN of the role Monte Carlo assumes to invoke the function. Its trust policy must already carry the deployment&#39;s external id. | 

## Example

```python
from montecarlo.models.aws_collection_agent_in import AwsCollectionAgentIn

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionAgentIn from a JSON string
aws_collection_agent_in_instance = AwsCollectionAgentIn.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionAgentIn.to_json())

# convert the object into a dict
aws_collection_agent_in_dict = aws_collection_agent_in_instance.to_dict()
# create an instance of AwsCollectionAgentIn from a dict
aws_collection_agent_in_from_dict = AwsCollectionAgentIn.from_dict(aws_collection_agent_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


