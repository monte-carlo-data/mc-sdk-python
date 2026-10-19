# StarburstEnterpriseCredentialsPatch

A change to existing Starburst Enterprise credentials.  A field left out is unchanged. An `ssl_*` field set to null is cleared. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Skip the check of the server&#39;s certificate. The connection always uses TLS. | [optional] 

## Example

```python
from pycarlo2.models.starburst_enterprise_credentials_patch import StarburstEnterpriseCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstEnterpriseCredentialsPatch from a JSON string
starburst_enterprise_credentials_patch_instance = StarburstEnterpriseCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(StarburstEnterpriseCredentialsPatch.to_json())

# convert the object into a dict
starburst_enterprise_credentials_patch_dict = starburst_enterprise_credentials_patch_instance.to_dict()
# create an instance of StarburstEnterpriseCredentialsPatch from a dict
starburst_enterprise_credentials_patch_from_dict = StarburstEnterpriseCredentialsPatch.from_dict(starburst_enterprise_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


