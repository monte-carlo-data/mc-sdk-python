# PineconeCredentialsOut

Pinecone credentials Monte Carlo stores. The API key is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**environment** | **str** | Pinecone environment the project runs in, such as &#x60;us-east-1-aws&#x60;. | 
**project_id** | **str** | Id of the Pinecone project. | 

## Example

```python
from pycarlo2.models.pinecone_credentials_out import PineconeCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of PineconeCredentialsOut from a JSON string
pinecone_credentials_out_instance = PineconeCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(PineconeCredentialsOut.to_json())

# convert the object into a dict
pinecone_credentials_out_dict = pinecone_credentials_out_instance.to_dict()
# create an instance of PineconeCredentialsOut from a dict
pinecone_credentials_out_from_dict = PineconeCredentialsOut.from_dict(pinecone_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


