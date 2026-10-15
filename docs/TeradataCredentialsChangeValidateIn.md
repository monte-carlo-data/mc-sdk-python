# TeradataCredentialsChangeValidateIn

A change to existing Teradata credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Do not check the server against &#x60;ssl_ca_data&#x60;. &#x60;td_sslmode&#x60; decides whether the connection uses TLS. | [optional] 
**td_sslmode** | [**TeradataSslMode**](TeradataSslMode.md) | How the connection to Teradata uses TLS. | [optional] 
**td_logmech** | [**TeradataLogonMechanism**](TeradataLogonMechanism.md) | How Teradata authenticates the user. | [optional] 

## Example

```python
from pycarlo2.models.teradata_credentials_change_validate_in import TeradataCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of TeradataCredentialsChangeValidateIn from a JSON string
teradata_credentials_change_validate_in_instance = TeradataCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(TeradataCredentialsChangeValidateIn.to_json())

# convert the object into a dict
teradata_credentials_change_validate_in_dict = teradata_credentials_change_validate_in_instance.to_dict()
# create an instance of TeradataCredentialsChangeValidateIn from a dict
teradata_credentials_change_validate_in_from_dict = TeradataCredentialsChangeValidateIn.from_dict(teradata_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


