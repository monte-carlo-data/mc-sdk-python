# AzureCollectionDataStorePatch

Details to change on an Azure data store. Only what you send is changed.  A credentials object is the exception: it replaces the stored credentials instead of merging into them, so send every field of the object you send, along with the matching `authentication_type`. Sending only `name` skips the checks against your storage, since a name is not validated against it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_account_keys** | [**StorageAccountKeysCredentialsIn**](StorageAccountKeysCredentialsIn.md) | Credentials for &#x60;AZURE_STORAGE_ACCOUNT_KEYS&#x60;. Send this or &#x60;service_principal&#x60;, never both. | [optional] 
**service_principal** | [**StorageServicePrincipalCredentialsIn**](StorageServicePrincipalCredentialsIn.md) | Credentials for &#x60;AZURE_STORAGE_SERVICE_PRINCIPAL&#x60;. Send this or &#x60;storage_account_keys&#x60;, never both. | [optional] 
**container_name** | **str** | Name of the blob container Monte Carlo should use. | [optional] 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 
**authentication_type** | [**AzureDataStoreAuthenticationType**](AzureDataStoreAuthenticationType.md) | How Monte Carlo authenticates to the storage account. Send it together with the matching credentials object. | [optional] 

## Example

```python
from montecarlo.models.azure_collection_data_store_patch import AzureCollectionDataStorePatch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCollectionDataStorePatch from a JSON string
azure_collection_data_store_patch_instance = AzureCollectionDataStorePatch.from_json(json)
# print the JSON string representation of the object
print(AzureCollectionDataStorePatch.to_json())

# convert the object into a dict
azure_collection_data_store_patch_dict = azure_collection_data_store_patch_instance.to_dict()
# create an instance of AzureCollectionDataStorePatch from a dict
azure_collection_data_store_patch_from_dict = AzureCollectionDataStorePatch.from_dict(azure_collection_data_store_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


