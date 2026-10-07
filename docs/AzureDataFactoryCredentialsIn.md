# AzureDataFactoryCredentialsIn

What to create Azure Data Factory credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Microsoft Entra ID tenant the data factory belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**app_client_secret** | **str** | Secret of the app registration. Stored by Monte Carlo and never returned. | 
**subscription_id** | **str** | Azure subscription that holds the data factory. | 
**resource_group_name** | **str** | Resource group that holds the data factory. | 
**factory_name** | **str** | Name of the data factory. | 

## Example

```python
from pycarlo2.models.azure_data_factory_credentials_in import AzureDataFactoryCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDataFactoryCredentialsIn from a JSON string
azure_data_factory_credentials_in_instance = AzureDataFactoryCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AzureDataFactoryCredentialsIn.to_json())

# convert the object into a dict
azure_data_factory_credentials_in_dict = azure_data_factory_credentials_in_instance.to_dict()
# create an instance of AzureDataFactoryCredentialsIn from a dict
azure_data_factory_credentials_in_from_dict = AzureDataFactoryCredentialsIn.from_dict(azure_data_factory_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


