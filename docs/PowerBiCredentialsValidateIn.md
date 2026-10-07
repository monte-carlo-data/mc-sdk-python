# PowerBiCredentialsValidateIn

Candidate Power BI credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**username** | **str** | User Monte Carlo signs in as, for &#x60;primary_user&#x60;. | [optional] 
**app_client_secret** | **str** | Secret of the app registration, for &#x60;service_principal&#x60;. Used for this check and not kept. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;primary_user&#x60;. Used for this check and not kept. | [optional] 
**tenant_id** | **str** | Microsoft Entra ID tenant the Power BI service belongs to. | 
**app_client_id** | **str** | Client ID of the Entra ID app registration Monte Carlo signs in with. | 
**auth_mode** | [**PowerBiAuthMode**](PowerBiAuthMode.md) | How Monte Carlo signs in. &#x60;service_principal&#x60; takes &#x60;app_client_secret&#x60;. &#x60;primary_user&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. | 

## Example

```python
from pycarlo2.models.power_bi_credentials_validate_in import PowerBiCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PowerBiCredentialsValidateIn from a JSON string
power_bi_credentials_validate_in_instance = PowerBiCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(PowerBiCredentialsValidateIn.to_json())

# convert the object into a dict
power_bi_credentials_validate_in_dict = power_bi_credentials_validate_in_instance.to_dict()
# create an instance of PowerBiCredentialsValidateIn from a dict
power_bi_credentials_validate_in_from_dict = PowerBiCredentialsValidateIn.from_dict(power_bi_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


