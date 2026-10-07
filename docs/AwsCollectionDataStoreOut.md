# AwsCollectionDataStoreOut

A data store held in an S3 bucket.

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
**bucket_name** | **str** | Name of the S3 bucket Monte Carlo uses. Empty until it has been registered. | 
**external_id** | **str** | Value to put in the trust policy of the role Monte Carlo assumes to access the bucket. Null before Monte Carlo has generated one, and for a caller who cannot register a data store. Also null if the value could not be read just now, so retry once before treating it as absent. | [optional] 

## Example

```python
from pycarlo2.models.aws_collection_data_store_out import AwsCollectionDataStoreOut

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionDataStoreOut from a JSON string
aws_collection_data_store_out_instance = AwsCollectionDataStoreOut.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionDataStoreOut.to_json())

# convert the object into a dict
aws_collection_data_store_out_dict = aws_collection_data_store_out_instance.to_dict()
# create an instance of AwsCollectionDataStoreOut from a dict
aws_collection_data_store_out_from_dict = AwsCollectionDataStoreOut.from_dict(aws_collection_data_store_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


