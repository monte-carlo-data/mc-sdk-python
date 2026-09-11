# GenericCollectionAgentIn

Which deployment's generic agent to enable, once the agent is running.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment whose generic collection agent to enable. It must have been provisioned for one, and the agent must be running with a credential created for this deployment. | 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 

## Example

```python
from montecarlo.models.generic_collection_agent_in import GenericCollectionAgentIn

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentIn from a JSON string
generic_collection_agent_in_instance = GenericCollectionAgentIn.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentIn.to_json())

# convert the object into a dict
generic_collection_agent_in_dict = generic_collection_agent_in_instance.to_dict()
# create an instance of GenericCollectionAgentIn from a dict
generic_collection_agent_in_from_dict = GenericCollectionAgentIn.from_dict(generic_collection_agent_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


