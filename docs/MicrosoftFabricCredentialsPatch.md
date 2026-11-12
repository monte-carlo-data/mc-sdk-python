# MicrosoftFabricCredentialsPatch

A change to existing Microsoft Fabric credentials.  A field left out is unchanged. `app_client_secret` set to null is unchanged. No other field can be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the Fabric warehouse or lakehouse SQL analytics endpoint, as Fabric shows it under SQL connection string, such as &#x60;abc123.datawarehouse.fabric.microsoft.com&#x60;. It goes unquoted into the connection string Monte Carlo builds, so it cannot contain whitespace or any of &#x60;;&#x60;, &#x60;{&#x60;, &#x60;}&#x60; and &#x60;&#x3D;&#x60;. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port of the SQL endpoint. Fabric serves it on 1433. | [optional] 
**db_name** | **str** | Warehouse or lakehouse to connect to. It goes unquoted into the connection string Monte Carlo builds, so it cannot contain whitespace or any of &#x60;;&#x60;, &#x60;{&#x60;, &#x60;}&#x60; and &#x60;&#x3D;&#x60;. | [optional] 
**tenant_id** | **str** | Microsoft Entra ID tenant the Fabric workspace belongs to. | [optional] 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | [optional] 
**app_client_secret** | **str** | Secret of the app registration. Stored by Monte Carlo and never returned. | [optional] 

## Example

```python
from pycarlo2.models.microsoft_fabric_credentials_patch import MicrosoftFabricCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftFabricCredentialsPatch from a JSON string
microsoft_fabric_credentials_patch_instance = MicrosoftFabricCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(MicrosoftFabricCredentialsPatch.to_json())

# convert the object into a dict
microsoft_fabric_credentials_patch_dict = microsoft_fabric_credentials_patch_instance.to_dict()
# create an instance of MicrosoftFabricCredentialsPatch from a dict
microsoft_fabric_credentials_patch_from_dict = MicrosoftFabricCredentialsPatch.from_dict(microsoft_fabric_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


