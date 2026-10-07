# GenericCollectionAgentOAuthClientCreatedOut

An OAuth client as it comes back from its create, the only time the secret is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the credential. For a token this is also its key id; for an OAuth client, its client id. | 
**deployment_id** | **UUID** | Identifier of the deployment whose agent presents this credential. | 
**type** | [**CredentialType**](CredentialType.md) | Which kind of credential this is. | 
**description** | **str** | What this credential is for. | 
**created_time** | **datetime** | When the credential was created. | 
**client_id** | **str** | Client id the agent presents, as &#x60;client_id&#x60; in its configuration. The same value as &#x60;id&#x60;. | 
**scopes** | **List[str]** | OAuth scopes the client is granted. | 
**expiration_time** | **datetime** | When the client stops being accepted. Null for a client that does not expire. | [optional] 
**client_secret** | **str** | Secret the agent presents, as &#x60;client_secret&#x60; in its configuration. Returned once, by this call. It is not retrievable afterwards, and Terraform holds it in state like any generated credential. To rotate, create a new credential and delete this one. | [readonly] 
**secret_id** | **str** | Identifier of the secret this call created, as the client&#39;s secrets are listed. Keep it with the secret. | 

## Example

```python
from pycarlo2.models.generic_collection_agent_o_auth_client_created_out import GenericCollectionAgentOAuthClientCreatedOut

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentOAuthClientCreatedOut from a JSON string
generic_collection_agent_o_auth_client_created_out_instance = GenericCollectionAgentOAuthClientCreatedOut.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentOAuthClientCreatedOut.to_json())

# convert the object into a dict
generic_collection_agent_o_auth_client_created_out_dict = generic_collection_agent_o_auth_client_created_out_instance.to_dict()
# create an instance of GenericCollectionAgentOAuthClientCreatedOut from a dict
generic_collection_agent_o_auth_client_created_out_from_dict = GenericCollectionAgentOAuthClientCreatedOut.from_dict(generic_collection_agent_o_auth_client_created_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


