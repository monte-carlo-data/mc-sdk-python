# GenericCollectionAgentTokenCreatedOut

A token as it comes back from its create, the only time the secret is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the credential. For a token this is also its key id; for an OAuth client, its client id. | 
**deployment_id** | **UUID** | Identifier of the deployment whose agent presents this credential. | 
**type** | [**CredentialType**](CredentialType.md) | Which kind of credential this is. | 
**description** | **str** | What this credential is for. | 
**created_time** | **datetime** | When the credential was created. | 
**mcd_id** | **str** | Key id the agent presents, as &#x60;mcd_id&#x60; in its configuration. The same value as &#x60;id&#x60;. | 
**mcd_token** | **str** | Secret the agent presents, as &#x60;mcd_token&#x60; in its configuration. Returned once, by this call. It is not retrievable afterwards, and Terraform holds it in state like any generated credential. To rotate, create a new credential and delete this one. | [readonly] 

## Example

```python
from pycarlo2.models.generic_collection_agent_token_created_out import GenericCollectionAgentTokenCreatedOut

# TODO update the JSON string below
json = "{}"
# create an instance of GenericCollectionAgentTokenCreatedOut from a JSON string
generic_collection_agent_token_created_out_instance = GenericCollectionAgentTokenCreatedOut.from_json(json)
# print the JSON string representation of the object
print(GenericCollectionAgentTokenCreatedOut.to_json())

# convert the object into a dict
generic_collection_agent_token_created_out_dict = generic_collection_agent_token_created_out_instance.to_dict()
# create an instance of GenericCollectionAgentTokenCreatedOut from a dict
generic_collection_agent_token_created_out_from_dict = GenericCollectionAgentTokenCreatedOut.from_dict(generic_collection_agent_token_created_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


