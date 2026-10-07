# TeradataCredentialsValidateIn

Candidate Teradata credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Used for this check and not kept. | 
**db_name** | **str** | Database to connect to. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Do not check the server against &#x60;ssl_ca_data&#x60;. &#x60;td_sslmode&#x60; decides whether the connection uses TLS. | [optional] 
**td_sslmode** | [**TeradataSslMode**](TeradataSslMode.md) | How the connection to Teradata uses TLS. | [optional] 
**td_logmech** | [**TeradataLogonMechanism**](TeradataLogonMechanism.md) | How Teradata authenticates the user. | [optional] 

## Example

```python
from pycarlo2.models.teradata_credentials_validate_in import TeradataCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of TeradataCredentialsValidateIn from a JSON string
teradata_credentials_validate_in_instance = TeradataCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(TeradataCredentialsValidateIn.to_json())

# convert the object into a dict
teradata_credentials_validate_in_dict = teradata_credentials_validate_in_instance.to_dict()
# create an instance of TeradataCredentialsValidateIn from a dict
teradata_credentials_validate_in_from_dict = TeradataCredentialsValidateIn.from_dict(teradata_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


