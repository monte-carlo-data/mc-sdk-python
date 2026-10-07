# AzureCollectionDataStoreIn

Details Monte Carlo needs to access a data store you keep in Azure Blob Storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_account_keys** | [**StorageAccountKeysCredentialsIn**](StorageAccountKeysCredentialsIn.md) | Credentials for &#x60;AZURE_STORAGE_ACCOUNT_KEYS&#x60;. Send this or &#x60;service_principal&#x60;, never both. | [optional] 
**service_principal** | [**StorageServicePrincipalCredentialsIn**](StorageServicePrincipalCredentialsIn.md) | Credentials for &#x60;AZURE_STORAGE_SERVICE_PRINCIPAL&#x60;. Send this or &#x60;storage_account_keys&#x60;, never both. | [optional] 
**authentication_type** | [**AzureDataStoreAuthenticationType**](AzureDataStoreAuthenticationType.md) | How Monte Carlo authenticates to the storage account. Send it together with the matching credentials object. | 
**deployment_id** | **UUID** | Deployment to register the data store on. It must already hold an unregistered Azure data store. | 
**container_name** | **str** | Name of the blob container Monte Carlo should use. | 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 

## Example

```python
from pycarlo2.models.azure_collection_data_store_in import AzureCollectionDataStoreIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCollectionDataStoreIn from a JSON string
azure_collection_data_store_in_instance = AzureCollectionDataStoreIn.from_json(json)
# print the JSON string representation of the object
print(AzureCollectionDataStoreIn.to_json())

# convert the object into a dict
azure_collection_data_store_in_dict = azure_collection_data_store_in_instance.to_dict()
# create an instance of AzureCollectionDataStoreIn from a dict
azure_collection_data_store_in_from_dict = AzureCollectionDataStoreIn.from_dict(azure_collection_data_store_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


