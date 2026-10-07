# AzureDataFactoryCredentialsOut

Azure Data Factory credentials Monte Carlo stores. The client secret is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the data factory belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**subscription_id** | **str** | Azure subscription that holds the data factory. | 
**resource_group_name** | **str** | Resource group that holds the data factory. | 
**factory_name** | **str** | Name of the data factory. | 

## Example

```python
from pycarlo2.models.azure_data_factory_credentials_out import AzureDataFactoryCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDataFactoryCredentialsOut from a JSON string
azure_data_factory_credentials_out_instance = AzureDataFactoryCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(AzureDataFactoryCredentialsOut.to_json())

# convert the object into a dict
azure_data_factory_credentials_out_dict = azure_data_factory_credentials_out_instance.to_dict()
# create an instance of AzureDataFactoryCredentialsOut from a dict
azure_data_factory_credentials_out_from_dict = AzureDataFactoryCredentialsOut.from_dict(azure_data_factory_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


