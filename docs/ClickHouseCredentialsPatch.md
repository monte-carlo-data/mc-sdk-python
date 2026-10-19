# ClickHouseCredentialsPatch

A change to existing ClickHouse credentials.  A field left out is unchanged. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 

## Example

```python
from pycarlo2.models.click_house_credentials_patch import ClickHouseCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ClickHouseCredentialsPatch from a JSON string
click_house_credentials_patch_instance = ClickHouseCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(ClickHouseCredentialsPatch.to_json())

# convert the object into a dict
click_house_credentials_patch_dict = click_house_credentials_patch_instance.to_dict()
# create an instance of ClickHouseCredentialsPatch from a dict
click_house_credentials_patch_from_dict = ClickHouseCredentialsPatch.from_dict(click_house_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


