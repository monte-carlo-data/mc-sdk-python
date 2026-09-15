# ServicePrincipalCredentialsIn

The service principal Monte Carlo authenticates as.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Directory (tenant) id the service principal lives in. | 
**client_id** | **str** | Application (client) id of the service principal. | 
**client_secret** | **str** | Client secret of the service principal. | 
**audience** | **str** | Audience the issued token is for, usually the function app&#39;s application id. | 

## Example

```python
from montecarlo.models.service_principal_credentials_in import ServicePrincipalCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePrincipalCredentialsIn from a JSON string
service_principal_credentials_in_instance = ServicePrincipalCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(ServicePrincipalCredentialsIn.to_json())

# convert the object into a dict
service_principal_credentials_in_dict = service_principal_credentials_in_instance.to_dict()
# create an instance of ServicePrincipalCredentialsIn from a dict
service_principal_credentials_in_from_dict = ServicePrincipalCredentialsIn.from_dict(service_principal_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


