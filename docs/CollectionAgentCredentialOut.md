# CollectionAgentCredentialOut

A credential of either kind, as the list returns it.  `type` says which kind, and which of the kind-specific fields are set. A kind-specific read returns the same credential with only its own fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the credential. For a token this is also its key id; for an OAuth client, its client id. | 
**deployment_id** | **UUID** | Identifier of the deployment whose agent presents this credential. | 
**type** | [**CredentialType**](CredentialType.md) | Which kind of credential this is. | 
**description** | **str** | What this credential is for. | 
**created_time** | **datetime** | When the credential was created. | 
**mcd_id** | **str** | Key id the agent presents. Set for a &#x60;TOKEN&#x60;, null otherwise. | [optional] 
**client_id** | **str** | Client id the agent presents. Set for an &#x60;OAUTH_CLIENT&#x60;, null otherwise. | [optional] 
**scopes** | **List[str]** | OAuth scopes the client is granted. Set for an &#x60;OAUTH_CLIENT&#x60;, null otherwise. | [optional] 
**expiration_time** | **datetime** | When an &#x60;OAUTH_CLIENT&#x60; stops being accepted. Null for one that does not expire, and for a &#x60;TOKEN&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.collection_agent_credential_out import CollectionAgentCredentialOut

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionAgentCredentialOut from a JSON string
collection_agent_credential_out_instance = CollectionAgentCredentialOut.from_json(json)
# print the JSON string representation of the object
print(CollectionAgentCredentialOut.to_json())

# convert the object into a dict
collection_agent_credential_out_dict = collection_agent_credential_out_instance.to_dict()
# create an instance of CollectionAgentCredentialOut from a dict
collection_agent_credential_out_from_dict = CollectionAgentCredentialOut.from_dict(collection_agent_credential_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


