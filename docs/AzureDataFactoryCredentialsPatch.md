# AzureDataFactoryCredentialsPatch

A change to existing Azure Data Factory credentials.  A field left out is unchanged. `app_client_secret` set to null is unchanged. No other field can be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Microsoft Entra ID tenant the data factory belongs to. | [optional] 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | [optional] 
**app_client_secret** | **str** | Secret of the app registration. Stored by Monte Carlo and never returned. | [optional] 
**subscription_id** | **str** | Azure subscription that holds the data factory. | [optional] 
**resource_group_name** | **str** | Resource group that holds the data factory. | [optional] 
**factory_name** | **str** | Name of the data factory. | [optional] 

## Example

```python
from pycarlo2.models.azure_data_factory_credentials_patch import AzureDataFactoryCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDataFactoryCredentialsPatch from a JSON string
azure_data_factory_credentials_patch_instance = AzureDataFactoryCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AzureDataFactoryCredentialsPatch.to_json())

# convert the object into a dict
azure_data_factory_credentials_patch_dict = azure_data_factory_credentials_patch_instance.to_dict()
# create an instance of AzureDataFactoryCredentialsPatch from a dict
azure_data_factory_credentials_patch_from_dict = AzureDataFactoryCredentialsPatch.from_dict(azure_data_factory_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


