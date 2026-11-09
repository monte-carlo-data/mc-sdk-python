# PineconeCredentialsValidateIn

Candidate Pinecone credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**environment** | **str** | Pinecone environment the project runs in, such as &#x60;us-east-1-aws&#x60;. | 
**project_id** | **str** | Id of the Pinecone project. | 
**api_key** | **str** | API key of the Pinecone project. Used for this check and not kept. | 

## Example

```python
from pycarlo2.models.pinecone_credentials_validate_in import PineconeCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeCredentialsValidateIn from a JSON string
pinecone_credentials_validate_in_instance = PineconeCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(PineconeCredentialsValidateIn.to_json())

# convert the object into a dict
pinecone_credentials_validate_in_dict = pinecone_credentials_validate_in_instance.to_dict()
# create an instance of PineconeCredentialsValidateIn from a dict
pinecone_credentials_validate_in_from_dict = PineconeCredentialsValidateIn.from_dict(pinecone_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


