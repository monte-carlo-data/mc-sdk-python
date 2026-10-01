# MySqlCredentialsPatch

A change to existing MySQL credentials.  A field left out is unchanged. An `ssl_*` field set to null is cleared. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Connect without TLS. | [optional] 
**ssl_verify_cert** | **bool** | Check the server&#39;s certificate against the CA. | [optional] 
**ssl_verify_identity** | **bool** | Check the certificate and that it names the host. | [optional] 
**ssl_skip_cert_verification** | **bool** | Encrypt the connection without checking the server&#39;s certificate. | [optional] 

## Example

```python
from montecarlo.models.my_sql_credentials_patch import MySqlCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of MySqlCredentialsPatch from a JSON string
my_sql_credentials_patch_instance = MySqlCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(MySqlCredentialsPatch.to_json())

# convert the object into a dict
my_sql_credentials_patch_dict = my_sql_credentials_patch_instance.to_dict()
# create an instance of MySqlCredentialsPatch from a dict
my_sql_credentials_patch_from_dict = MySqlCredentialsPatch.from_dict(my_sql_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


