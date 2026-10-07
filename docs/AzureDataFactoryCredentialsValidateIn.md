# AzureDataFactoryCredentialsValidateIn

Candidate Azure Data Factory credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the data factory belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**app_client_secret** | **str** | Secret of the app registration. Used for this check and not kept. | 
**subscription_id** | **str** | Azure subscription that holds the data factory. | 
**resource_group_name** | **str** | Resource group that holds the data factory. | 
**factory_name** | **str** | Name of the data factory. | 

## Example

```python
from pycarlo2.models.azure_data_factory_credentials_validate_in import AzureDataFactoryCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of AzureDataFactoryCredentialsValidateIn from a JSON string
azure_data_factory_credentials_validate_in_instance = AzureDataFactoryCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(AzureDataFactoryCredentialsValidateIn.to_json())

# convert the object into a dict
azure_data_factory_credentials_validate_in_dict = azure_data_factory_credentials_validate_in_instance.to_dict()
# create an instance of AzureDataFactoryCredentialsValidateIn from a dict
azure_data_factory_credentials_validate_in_from_dict = AzureDataFactoryCredentialsValidateIn.from_dict(azure_data_factory_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


