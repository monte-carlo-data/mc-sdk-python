# PostgresCredentialsIn

What to create PostgreSQL credentials with.

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
**rds_proxy** | **bool** | Whether &#x60;host&#x60; is an Amazon RDS Proxy endpoint. | [optional] 

## Example

```python
from pycarlo2.models.postgres_credentials_in import PostgresCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresCredentialsIn from a JSON string
postgres_credentials_in_instance = PostgresCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(PostgresCredentialsIn.to_json())

# convert the object into a dict
postgres_credentials_in_dict = postgres_credentials_in_instance.to_dict()
# create an instance of PostgresCredentialsIn from a dict
postgres_credentials_in_from_dict = PostgresCredentialsIn.from_dict(postgres_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


