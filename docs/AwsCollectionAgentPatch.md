# AwsCollectionAgentPatch

Details to change on an AWS collection agent. Only what you send is changed.  Sending only `name` skips the checks against your function, since a name is not validated against it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lambda_function_arn** | **str** | ARN of the Lambda function Monte Carlo should invoke. | [optional] 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 
**role_arn** | **str** | ARN of the role Monte Carlo assumes to invoke the function. Its trust policy must already carry the deployment&#39;s external id. | [optional] 

## Example

```python
from montecarlo.models.aws_collection_agent_patch import AwsCollectionAgentPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionAgentPatch from a JSON string
aws_collection_agent_patch_instance = AwsCollectionAgentPatch.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionAgentPatch.to_json())

# convert the object into a dict
aws_collection_agent_patch_dict = aws_collection_agent_patch_instance.to_dict()
# create an instance of AwsCollectionAgentPatch from a dict
aws_collection_agent_patch_from_dict = AwsCollectionAgentPatch.from_dict(aws_collection_agent_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


