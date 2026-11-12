# MicrosoftFabricCredentialsIn

What to create Microsoft Fabric credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the Fabric warehouse or lakehouse SQL analytics endpoint, as Fabric shows it under SQL connection string, such as &#x60;abc123.datawarehouse.fabric.microsoft.com&#x60;. It goes unquoted into the connection string Monte Carlo builds, so it cannot contain whitespace or any of &#x60;;&#x60;, &#x60;{&#x60;, &#x60;}&#x60; and &#x60;&#x3D;&#x60;. | 
**port** | **int** | Port of the SQL endpoint. Fabric serves it on 1433. | 
**db_name** | **str** | Warehouse or lakehouse to connect to. It goes unquoted into the connection string Monte Carlo builds, so it cannot contain whitespace or any of &#x60;;&#x60;, &#x60;{&#x60;, &#x60;}&#x60; and &#x60;&#x3D;&#x60;. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the Fabric workspace belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**app_client_secret** | **str** | Secret of the app registration. Stored by Monte Carlo and never returned. | 

## Example

```python
from pycarlo2.models.microsoft_fabric_credentials_in import MicrosoftFabricCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftFabricCredentialsIn from a JSON string
microsoft_fabric_credentials_in_instance = MicrosoftFabricCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(MicrosoftFabricCredentialsIn.to_json())

# convert the object into a dict
microsoft_fabric_credentials_in_dict = microsoft_fabric_credentials_in_instance.to_dict()
# create an instance of MicrosoftFabricCredentialsIn from a dict
microsoft_fabric_credentials_in_from_dict = MicrosoftFabricCredentialsIn.from_dict(microsoft_fabric_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


