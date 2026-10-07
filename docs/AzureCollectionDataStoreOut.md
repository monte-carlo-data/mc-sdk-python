# AzureCollectionDataStoreOut

A data store held in an Azure Blob Storage container.  There is no external id: Monte Carlo assumes no role to reach Azure storage.

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
**container_name** | **str** | Name of the blob container Monte Carlo uses. Empty until it has been registered. The storage account holding it is part of the credentials, so it is not returned. | 

## Example

```python
from pycarlo2.models.azure_collection_data_store_out import AzureCollectionDataStoreOut

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCollectionDataStoreOut from a JSON string
azure_collection_data_store_out_instance = AzureCollectionDataStoreOut.from_json(json)
# print the JSON string representation of the object
print(AzureCollectionDataStoreOut.to_json())

# convert the object into a dict
azure_collection_data_store_out_dict = azure_collection_data_store_out_instance.to_dict()
# create an instance of AzureCollectionDataStoreOut from a dict
azure_collection_data_store_out_from_dict = AzureCollectionDataStoreOut.from_dict(azure_collection_data_store_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


