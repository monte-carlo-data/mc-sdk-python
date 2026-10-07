# GenericCollectionAgentOAuthClientIn

Which deployment to mint an OAuth client for, and how long it should live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment whose generic collection agent will present this credential. It must have been provisioned for a generic collection agent. | 
**description** | **str** | What this credential is for. Monte Carlo generates one naming the agent if you leave it out. | [optional] 
**expiration_days** | **int** | Days until the client stops being accepted. Leave it out for a client that does not expire. | [optional] 

## Example

```python
from pycarlo2.models.generic_collection_agent_o_auth_client_in import GenericCollectionAgentOAuthClientIn

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentOAuthClientIn from a JSON string
generic_collection_agent_o_auth_client_in_instance = GenericCollectionAgentOAuthClientIn.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentOAuthClientIn.to_json())

# convert the object into a dict
generic_collection_agent_o_auth_client_in_dict = generic_collection_agent_o_auth_client_in_instance.to_dict()
# create an instance of GenericCollectionAgentOAuthClientIn from a dict
generic_collection_agent_o_auth_client_in_from_dict = GenericCollectionAgentOAuthClientIn.from_dict(generic_collection_agent_o_auth_client_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


