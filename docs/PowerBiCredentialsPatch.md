# PowerBiCredentialsPatch

A change to existing Power BI credentials.  A field left out is unchanged. A secret set to null is unchanged. `tenant_id`, `app_client_id` and `auth_mode` cannot be cleared. A new `auth_mode` drops the fields of the old one, so send the new mode's fields with it. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | User Monte Carlo signs in as, for &#x60;primary_user&#x60;. | [optional] 
**app_client_secret** | **str** | Secret of the app registration, for &#x60;service_principal&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;primary_user&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**tenant_id** | **str** | Microsoft Entra ID tenant the Power BI service belongs to. | [optional] 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | [optional] 
**auth_mode** | [**PowerBiAuthMode**](PowerBiAuthMode.md) | How Monte Carlo signs in. &#x60;service_principal&#x60; takes &#x60;app_client_secret&#x60;. &#x60;primary_user&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.power_bi_credentials_patch import PowerBiCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiCredentialsPatch from a JSON string
power_bi_credentials_patch_instance = PowerBiCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(PowerBiCredentialsPatch.to_json())

# convert the object into a dict
power_bi_credentials_patch_dict = power_bi_credentials_patch_instance.to_dict()
# create an instance of PowerBiCredentialsPatch from a dict
power_bi_credentials_patch_from_dict = PowerBiCredentialsPatch.from_dict(power_bi_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


