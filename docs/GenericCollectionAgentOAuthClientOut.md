# GenericCollectionAgentOAuthClientOut

An OAuth 2.0 client a generic collection agent exchanges for short-lived access tokens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | Client id the agent presents, as &#x60;client_id&#x60; in its configuration. The same value as &#x60;id&#x60;. | 
**created_time** | **datetime** | When the credential was created. | 
**deployment_id** | **UUID** | Identifier of the deployment whose agent presents this credential. | 
**description** | **str** | What this credential is for. | 
**expiration_time** | **datetime** | When the client stops being accepted. Null for a client that does not expire. | [optional] 
**id** | **str** | Unique identifier of the credential. For a token this is also its key id; for an OAuth client, its client id. | 
**scopes** | **List[str]** | OAuth scopes the client is granted. | 
**type** | [**CredentialType**](CredentialType.md) | Which kind of credential this is. | 

## Example

```python
from montecarlo.models.generic_collection_agent_o_auth_client_out import GenericCollectionAgentOAuthClientOut

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentOAuthClientOut from a JSON string
generic_collection_agent_o_auth_client_out_instance = GenericCollectionAgentOAuthClientOut.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentOAuthClientOut.to_json())

# convert the object into a dict
generic_collection_agent_o_auth_client_out_dict = generic_collection_agent_o_auth_client_out_instance.to_dict()
# create an instance of GenericCollectionAgentOAuthClientOut from a dict
generic_collection_agent_o_auth_client_out_from_dict = GenericCollectionAgentOAuthClientOut.from_dict(generic_collection_agent_o_auth_client_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


