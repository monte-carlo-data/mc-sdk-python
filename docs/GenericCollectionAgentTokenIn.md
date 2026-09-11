# GenericCollectionAgentTokenIn

Which deployment to mint a token for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment whose generic collection agent will present this credential. It must have been provisioned for a generic collection agent. | 
**description** | **str** | What this credential is for. Monte Carlo generates one naming the agent if you leave it out. | [optional] 

## Example

```python
from montecarlo.models.generic_collection_agent_token_in import GenericCollectionAgentTokenIn

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentTokenIn from a JSON string
generic_collection_agent_token_in_instance = GenericCollectionAgentTokenIn.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentTokenIn.to_json())

# convert the object into a dict
generic_collection_agent_token_in_dict = generic_collection_agent_token_in_instance.to_dict()
# create an instance of GenericCollectionAgentTokenIn from a dict
generic_collection_agent_token_in_from_dict = GenericCollectionAgentTokenIn.from_dict(generic_collection_agent_token_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


