# PineconeCredentialsIn

What to create Pinecone credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Pinecone environment the project runs in, such as &#x60;us-east-1-aws&#x60;. | 
**project_id** | **str** | Id of the Pinecone project. | 
**api_key** | **str** | API key of the Pinecone project. Stored by Monte Carlo and never returned. | 

## Example

```python
from pycarlo2.models.pinecone_credentials_in import PineconeCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeCredentialsIn from a JSON string
pinecone_credentials_in_instance = PineconeCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(PineconeCredentialsIn.to_json())

# convert the object into a dict
pinecone_credentials_in_dict = pinecone_credentials_in_instance.to_dict()
# create an instance of PineconeCredentialsIn from a dict
pinecone_credentials_in_from_dict = PineconeCredentialsIn.from_dict(pinecone_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


