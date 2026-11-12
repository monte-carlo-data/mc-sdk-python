# MicrosoftFabricCredentialsOut

Microsoft Fabric credentials Monte Carlo stores. The client secret is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the Fabric warehouse or lakehouse SQL analytics endpoint, as Fabric shows it under SQL connection string, such as &#x60;abc123.datawarehouse.fabric.microsoft.com&#x60;. | 
**port** | **int** | Port of the SQL endpoint. Fabric serves it on 1433. | 
**db_name** | **str** | Warehouse or lakehouse to connect to. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the Fabric workspace belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 

## Example

```python
from pycarlo2.models.microsoft_fabric_credentials_out import MicrosoftFabricCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftFabricCredentialsOut from a JSON string
microsoft_fabric_credentials_out_instance = MicrosoftFabricCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(MicrosoftFabricCredentialsOut.to_json())

# convert the object into a dict
microsoft_fabric_credentials_out_dict = microsoft_fabric_credentials_out_instance.to_dict()
# create an instance of MicrosoftFabricCredentialsOut from a dict
microsoft_fabric_credentials_out_from_dict = MicrosoftFabricCredentialsOut.from_dict(microsoft_fabric_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


