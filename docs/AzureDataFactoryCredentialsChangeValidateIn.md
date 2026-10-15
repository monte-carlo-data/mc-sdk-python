# AzureDataFactoryCredentialsChangeValidateIn

A change to existing Azure Data Factory credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the data factory belongs to. | [optional] 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | [optional] 
**app_client_secret** | **str** | Secret of the app registration. Stored by Monte Carlo and never returned. | [optional] 
**subscription_id** | **str** | Azure subscription that holds the data factory. | [optional] 
**resource_group_name** | **str** | Resource group that holds the data factory. | [optional] 
**factory_name** | **str** | Name of the data factory. | [optional] 

## Example

```python
from pycarlo2.models.azure_data_factory_credentials_change_validate_in import AzureDataFactoryCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDataFactoryCredentialsChangeValidateIn from a JSON string
azure_data_factory_credentials_change_validate_in_instance = AzureDataFactoryCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureDataFactoryCredentialsChangeValidateIn.to_json())

# convert the object into a dict
azure_data_factory_credentials_change_validate_in_dict = azure_data_factory_credentials_change_validate_in_instance.to_dict()
# create an instance of AzureDataFactoryCredentialsChangeValidateIn from a dict
azure_data_factory_credentials_change_validate_in_from_dict = AzureDataFactoryCredentialsChangeValidateIn.from_dict(azure_data_factory_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


