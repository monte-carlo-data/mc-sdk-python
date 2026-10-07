# GenericCollectionAgentTokenOut

A key and secret a generic collection agent sends as headers on every request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the credential. For a token this is also its key id; for an OAuth client, its client id. | 
**deployment_id** | **UUID** | Identifier of the deployment whose agent presents this credential. | 
**type** | [**CredentialType**](CredentialType.md) | Which kind of credential this is. | 
**description** | **str** | What this credential is for. | 
**created_time** | **datetime** | When the credential was created. | 
**mcd_id** | **str** | Key id the agent presents, as &#x60;mcd_id&#x60; in its configuration. The same value as &#x60;id&#x60;. | 

## Example

```python
from pycarlo2.models.generic_collection_agent_token_out import GenericCollectionAgentTokenOut

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentTokenOut from a JSON string
generic_collection_agent_token_out_instance = GenericCollectionAgentTokenOut.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentTokenOut.to_json())

# convert the object into a dict
generic_collection_agent_token_out_dict = generic_collection_agent_token_out_instance.to_dict()
# create an instance of GenericCollectionAgentTokenOut from a dict
generic_collection_agent_token_out_from_dict = GenericCollectionAgentTokenOut.from_dict(generic_collection_agent_token_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


