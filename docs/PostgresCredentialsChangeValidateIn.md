# PostgresCredentialsChangeValidateIn

A change to existing PostgreSQL credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Connect without TLS. | [optional] 
**ssl_verify_cert** | **bool** | Check the server&#39;s certificate against the CA. | [optional] 
**ssl_verify_identity** | **bool** | Check the certificate and that it names the host. | [optional] 
**ssl_skip_cert_verification** | **bool** | Encrypt the connection without checking the server&#39;s certificate. | [optional] 
**rds_proxy** | **bool** | Whether &#x60;host&#x60; is an Amazon RDS Proxy endpoint. | [optional] 

## Example

```python
from pycarlo2.models.postgres_credentials_change_validate_in import PostgresCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresCredentialsChangeValidateIn from a JSON string
postgres_credentials_change_validate_in_instance = PostgresCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(PostgresCredentialsChangeValidateIn.to_json())

# convert the object into a dict
postgres_credentials_change_validate_in_dict = postgres_credentials_change_validate_in_instance.to_dict()
# create an instance of PostgresCredentialsChangeValidateIn from a dict
postgres_credentials_change_validate_in_from_dict = PostgresCredentialsChangeValidateIn.from_dict(postgres_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


