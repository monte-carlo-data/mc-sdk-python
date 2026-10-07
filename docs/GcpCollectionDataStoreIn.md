# GcpCollectionDataStoreIn

Details Monte Carlo needs to access a data store you keep in a Google Cloud Storage bucket.  Registering through this API always authenticates with a service account key. There is no authentication type to choose.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment to register the data store on. It must already hold an unregistered Cloud Storage data store. | 
**bucket_name** | **str** | Name of the Cloud Storage bucket Monte Carlo should use. | 
**service_account_key** | **str** | Service account key Monte Carlo reaches the bucket with, as the contents of the JSON key file Google issued for it. It replaces the stored key rather than merging into it. | 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 

## Example

```python
from pycarlo2.models.gcp_collection_data_store_in import GcpCollectionDataStoreIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionDataStoreIn from a JSON string
gcp_collection_data_store_in_instance = GcpCollectionDataStoreIn.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionDataStoreIn.to_json())

# convert the object into a dict
gcp_collection_data_store_in_dict = gcp_collection_data_store_in_instance.to_dict()
# create an instance of GcpCollectionDataStoreIn from a dict
gcp_collection_data_store_in_from_dict = GcpCollectionDataStoreIn.from_dict(gcp_collection_data_store_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


