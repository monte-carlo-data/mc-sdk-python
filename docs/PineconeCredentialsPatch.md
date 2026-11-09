# PineconeCredentialsPatch

A change to existing Pinecone credentials.  A field left out is unchanged. `api_key` set to null is unchanged. `environment` and `project_id` cannot be cleared. Changing `environment` or `project_id` requires sending `api_key` again. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Pinecone environment the project runs in, such as &#x60;us-east-1-aws&#x60;. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**project_id** | **str** | Id of the Pinecone project. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**api_key** | **str** | New API key of the Pinecone project. | [optional] 

## Example

```python
from pycarlo2.models.pinecone_credentials_patch import PineconeCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeCredentialsPatch from a JSON string
pinecone_credentials_patch_instance = PineconeCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(PineconeCredentialsPatch.to_json())

# convert the object into a dict
pinecone_credentials_patch_dict = pinecone_credentials_patch_instance.to_dict()
# create an instance of PineconeCredentialsPatch from a dict
pinecone_credentials_patch_from_dict = PineconeCredentialsPatch.from_dict(pinecone_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


