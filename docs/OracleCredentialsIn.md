# OracleCredentialsIn

What to create Oracle credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Connect without TLS. | [optional] 
**ssl_verify_cert** | **bool** | Check the server&#39;s certificate against the CA. | [optional] 
**ssl_verify_identity** | **bool** | Check the certificate and that it names the host. | [optional] 
**ssl_skip_cert_verification** | **bool** | Encrypt the connection without checking the server&#39;s certificate. | [optional] 

## Example

```python
from montecarlo.models.oracle_credentials_in import OracleCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of OracleCredentialsIn from a JSON string
oracle_credentials_in_instance = OracleCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(OracleCredentialsIn.to_json())

# convert the object into a dict
oracle_credentials_in_dict = oracle_credentials_in_instance.to_dict()
# create an instance of OracleCredentialsIn from a dict
oracle_credentials_in_from_dict = OracleCredentialsIn.from_dict(oracle_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


