# TeradataCredentialsPatch

A change to existing Teradata credentials.  A field left out is unchanged. A setting or an `ssl_*` field set to null is cleared. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. Changing it requires sending the credentials&#39; secrets again. | [optional] 
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
from pycarlo2.models.teradata_credentials_patch import TeradataCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TeradataCredentialsPatch from a JSON string
teradata_credentials_patch_instance = TeradataCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(TeradataCredentialsPatch.to_json())

# convert the object into a dict
teradata_credentials_patch_dict = teradata_credentials_patch_instance.to_dict()
# create an instance of TeradataCredentialsPatch from a dict
teradata_credentials_patch_from_dict = TeradataCredentialsPatch.from_dict(teradata_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


