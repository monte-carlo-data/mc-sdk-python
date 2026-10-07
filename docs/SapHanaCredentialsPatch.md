# SapHanaCredentialsPatch

A change to existing SAP HANA credentials.  A field left out is unchanged. `password` set to null is unchanged. `host`, `port`, `db_name` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 

## Example

```python
from pycarlo2.models.sap_hana_credentials_patch import SapHanaCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaCredentialsPatch from a JSON string
sap_hana_credentials_patch_instance = SapHanaCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(SapHanaCredentialsPatch.to_json())

# convert the object into a dict
sap_hana_credentials_patch_dict = sap_hana_credentials_patch_instance.to_dict()
# create an instance of SapHanaCredentialsPatch from a dict
sap_hana_credentials_patch_from_dict = SapHanaCredentialsPatch.from_dict(sap_hana_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


