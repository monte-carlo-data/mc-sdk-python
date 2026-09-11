# GcpCollectionDataStoreOut

A data store held in a Google Cloud Storage bucket.  There is no external id: Monte Carlo assumes no role to reach Cloud Storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | [**AuthenticationType**](AuthenticationType.md) | How Monte Carlo authenticates when it reaches the data store. | 
**bucket_name** | **str** | Name of the Cloud Storage bucket Monte Carlo uses. Empty until it has been registered. | 
**created_time** | **datetime** | When the data store was created, which is when its deployment was provisioned. | [optional] 
**deployment_id** | **UUID** | Identifier of the deployment this data store belongs to. | 
**enabled** | **bool** | Whether Monte Carlo is using this data store. One that is unregistered, or whose validation failed, is not enabled. | 
**id** | **UUID** | Unique identifier of the data store. | 
**last_updated_time** | **datetime** | When the data store was last registered, renamed, or given different storage or credentials. Null until one of those has happened. | [optional] 
**name** | **str** | Display name of the data store. Null when it has no name. | [optional] 
**storage_type** | [**StorageType**](StorageType.md) | Which kind of storage the data store keeps its data in. | 

## Example

```python
from montecarlo.models.gcp_collection_data_store_out import GcpCollectionDataStoreOut

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionDataStoreOut from a JSON string
gcp_collection_data_store_out_instance = GcpCollectionDataStoreOut.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionDataStoreOut.to_json())

# convert the object into a dict
gcp_collection_data_store_out_dict = gcp_collection_data_store_out_instance.to_dict()
# create an instance of GcpCollectionDataStoreOut from a dict
gcp_collection_data_store_out_from_dict = GcpCollectionDataStoreOut.from_dict(gcp_collection_data_store_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


