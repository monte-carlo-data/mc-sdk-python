# PowerBiCredentialsOut

Power BI credentials Monte Carlo stores. The secret and the password are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**tenant_id** | **str** | Microsoft Entra ID tenant the Power BI service belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**auth_mode** | [**PowerBiAuthMode**](PowerBiAuthMode.md) | How Monte Carlo signs in. &#x60;service_principal&#x60; takes &#x60;app_client_secret&#x60;. &#x60;primary_user&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. | 
**username** | **str** | User Monte Carlo signs in as. Null unless set. | 

## Example

```python
from montecarlo.models.power_bi_credentials_out import PowerBiCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiCredentialsOut from a JSON string
power_bi_credentials_out_instance = PowerBiCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(PowerBiCredentialsOut.to_json())

# convert the object into a dict
power_bi_credentials_out_dict = power_bi_credentials_out_instance.to_dict()
# create an instance of PowerBiCredentialsOut from a dict
power_bi_credentials_out_from_dict = PowerBiCredentialsOut.from_dict(power_bi_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


