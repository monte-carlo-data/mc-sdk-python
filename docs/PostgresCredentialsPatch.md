# PostgresCredentialsPatch

A change to existing PostgreSQL credentials.  A field left out is unchanged. A setting or an `ssl_*` field set to null is cleared. `password` set to null is unchanged. `host`, `port`, `db_name` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from pycarlo2.models.postgres_credentials_patch import PostgresCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of PostgresCredentialsPatch from a JSON string
postgres_credentials_patch_instance = PostgresCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(PostgresCredentialsPatch.to_json())

# convert the object into a dict
postgres_credentials_patch_dict = postgres_credentials_patch_instance.to_dict()
# create an instance of PostgresCredentialsPatch from a dict
postgres_credentials_patch_from_dict = PostgresCredentialsPatch.from_dict(postgres_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


