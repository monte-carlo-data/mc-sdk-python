# Db2CredentialsPatch

A change to existing Db2 credentials.  A field left out is unchanged. An `ssl_*` field set to null is cleared. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

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

## Example

```python
from montecarlo.models.db2_credentials_patch import Db2CredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of Db2CredentialsPatch from a JSON string
db2_credentials_patch_instance = Db2CredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(Db2CredentialsPatch.to_json())

# convert the object into a dict
db2_credentials_patch_dict = db2_credentials_patch_instance.to_dict()
# create an instance of Db2CredentialsPatch from a dict
db2_credentials_patch_from_dict = Db2CredentialsPatch.from_dict(db2_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


