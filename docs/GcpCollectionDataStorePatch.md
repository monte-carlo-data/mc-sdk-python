# GcpCollectionDataStorePatch

Details to change on a Cloud Storage data store. Only what you send is changed.  The service account key is the exception: it replaces the stored key instead of merging into it. Sending only `name` skips the checks against your storage, since a name is not validated against it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Name of the Cloud Storage bucket Monte Carlo should use. | [optional] 
**service_account_key** | **str** | Service account key Monte Carlo reaches the bucket with, as the contents of the JSON key file Google issued for it. It replaces the stored key rather than merging into it. | [optional] 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 

## Example

```python
from pycarlo2.models.gcp_collection_data_store_patch import GcpCollectionDataStorePatch

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionDataStorePatch from a JSON string
gcp_collection_data_store_patch_instance = GcpCollectionDataStorePatch.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionDataStorePatch.to_json())

# convert the object into a dict
gcp_collection_data_store_patch_dict = gcp_collection_data_store_patch_instance.to_dict()
# create an instance of GcpCollectionDataStorePatch from a dict
gcp_collection_data_store_patch_from_dict = GcpCollectionDataStorePatch.from_dict(gcp_collection_data_store_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


