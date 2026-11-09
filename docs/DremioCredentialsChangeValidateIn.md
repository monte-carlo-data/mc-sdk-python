# DremioCredentialsChangeValidateIn

A change to existing Dremio credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**db_name** | **str** | Dremio project or space to connect to. | [optional] 
**tls** | **bool** | Connect over TLS. Dremio Cloud requires it. | [optional] 
**host** | **str** | Hostname of the Dremio Arrow Flight endpoint, such as &#x60;data.dremio.cloud&#x60; for Dremio Cloud (&#x60;data.eu.dremio.cloud&#x60; in the EU). Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port Dremio serves Arrow Flight on. | [optional] 
**token** | **str** | New personal access token. | [optional] 

## Example

```python
from pycarlo2.models.dremio_credentials_change_validate_in import DremioCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DremioCredentialsChangeValidateIn from a JSON string
dremio_credentials_change_validate_in_instance = DremioCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(DremioCredentialsChangeValidateIn.to_json())

# convert the object into a dict
dremio_credentials_change_validate_in_dict = dremio_credentials_change_validate_in_instance.to_dict()
# create an instance of DremioCredentialsChangeValidateIn from a dict
dremio_credentials_change_validate_in_from_dict = DremioCredentialsChangeValidateIn.from_dict(dremio_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


