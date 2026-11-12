# HiveCredentialsPatch

A change to existing HiveServer2 credentials.  A field left out is unchanged. `port` and `db_name` set to null are cleared, and `auth_mode` set to null goes back to `SASL`. `host` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the HiveServer2. | [optional] 
**port** | **int** | Port the HiveServer2 listens on in binary mode. | [optional] 
**user** | **str** | User Monte Carlo signs in as. Hive takes no password. | [optional] 
**db_name** | **str** | Database Monte Carlo connects to. | [optional] 
**auth_mode** | [**HiveAuthMode**](HiveAuthMode.md) | How Monte Carlo signs in. Omit it for &#x60;SASL&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.hive_credentials_patch import HiveCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of HiveCredentialsPatch from a JSON string
hive_credentials_patch_instance = HiveCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(HiveCredentialsPatch.to_json())

# convert the object into a dict
hive_credentials_patch_dict = hive_credentials_patch_instance.to_dict()
# create an instance of HiveCredentialsPatch from a dict
hive_credentials_patch_from_dict = HiveCredentialsPatch.from_dict(hive_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


