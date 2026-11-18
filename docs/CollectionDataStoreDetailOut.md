# CollectionDataStoreDetailOut

A data store on any platform, with the fields its platform-specific read returns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the data store. | 
**name** | **str** | Display name of the data store. Null when it has no name. | [optional] 
**deployment_id** | **UUID** | Identifier of the deployment this data store belongs to. | 
**storage_type** | [**StorageType**](StorageType.md) | Which kind of storage the data store keeps its data in. | 
**authentication_type** | [**AuthenticationType**](AuthenticationType.md) | How Monte Carlo authenticates when it reaches the data store. | 
**enabled** | **bool** | Whether Monte Carlo is using this data store. One that is unregistered, or whose validation failed, is not enabled. | 
**created_time** | **datetime** | When the data store was created, which is when its deployment was provisioned. | [optional] 
**last_updated_time** | **datetime** | When the data store was last registered, renamed, or given different storage or credentials. Null until one of those has happened. | [optional] 
**platform** | [**RuntimePlatform**](RuntimePlatform.md) | Where the data store runs. | 
**endpoint** | **str** | Address of the data store, in the form its platform uses. On AWS that is an S3 bucket name, on Azure the name of a blob container, and on GCP a Cloud Storage bucket name. Empty until it has been registered. | 
**details** | **Dict[str, object]** | The fields the platform-specific read of this data store returns beyond the ones above, such as &#x60;bucket_name&#x60; and &#x60;external_id&#x60; on AWS. Never a secret. | 

## Example

```python
from pycarlo2.models.collection_data_store_detail_out import CollectionDataStoreDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionDataStoreDetailOut from a JSON string
collection_data_store_detail_out_instance = CollectionDataStoreDetailOut.from_json(json)
# print the JSON string representation of the object
print(CollectionDataStoreDetailOut.to_json())

# convert the object into a dict
collection_data_store_detail_out_dict = collection_data_store_detail_out_instance.to_dict()
# create an instance of CollectionDataStoreDetailOut from a dict
collection_data_store_detail_out_from_dict = CollectionDataStoreDetailOut.from_dict(collection_data_store_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


