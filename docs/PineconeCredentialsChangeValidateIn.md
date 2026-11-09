# PineconeCredentialsChangeValidateIn

A change to existing Pinecone credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**environment** | **str** | Pinecone environment the project runs in, such as &#x60;us-east-1-aws&#x60;. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**project_id** | **str** | Id of the Pinecone project. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**api_key** | **str** | New API key of the Pinecone project. | [optional] 

## Example

```python
from pycarlo2.models.pinecone_credentials_change_validate_in import PineconeCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeCredentialsChangeValidateIn from a JSON string
pinecone_credentials_change_validate_in_instance = PineconeCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(PineconeCredentialsChangeValidateIn.to_json())

# convert the object into a dict
pinecone_credentials_change_validate_in_dict = pinecone_credentials_change_validate_in_instance.to_dict()
# create an instance of PineconeCredentialsChangeValidateIn from a dict
pinecone_credentials_change_validate_in_from_dict = PineconeCredentialsChangeValidateIn.from_dict(pinecone_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


