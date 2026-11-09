# MotherDuckCredentialsPatch

A change to existing MotherDuck credentials.  A field left out is unchanged. `token` set to null is unchanged. `db_name` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** | MotherDuck database to connect to. | [optional] 
**token** | **str** | New access token. | [optional] 

## Example

```python
from pycarlo2.models.mother_duck_credentials_patch import MotherDuckCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of MotherDuckCredentialsPatch from a JSON string
mother_duck_credentials_patch_instance = MotherDuckCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(MotherDuckCredentialsPatch.to_json())

# convert the object into a dict
mother_duck_credentials_patch_dict = mother_duck_credentials_patch_instance.to_dict()
# create an instance of MotherDuckCredentialsPatch from a dict
mother_duck_credentials_patch_from_dict = MotherDuckCredentialsPatch.from_dict(mother_duck_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


