# GenericCollectionAgentPatch

Details to change on a generic collection agent. The name is the only one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 

## Example

```python
from montecarlo.models.generic_collection_agent_patch import GenericCollectionAgentPatch

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentPatch from a JSON string
generic_collection_agent_patch_instance = GenericCollectionAgentPatch.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentPatch.to_json())

# convert the object into a dict
generic_collection_agent_patch_dict = generic_collection_agent_patch_instance.to_dict()
# create an instance of GenericCollectionAgentPatch from a dict
generic_collection_agent_patch_from_dict = GenericCollectionAgentPatch.from_dict(generic_collection_agent_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


