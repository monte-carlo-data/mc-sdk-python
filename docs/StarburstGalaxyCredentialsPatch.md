# StarburstGalaxyCredentialsPatch

A change to existing Starburst Galaxy credentials.  A field left out is unchanged. `password` set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `user` cannot be cleared. Sending an empty body returns the credentials as they are.

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
from montecarlo.models.starburst_galaxy_credentials_patch import StarburstGalaxyCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstGalaxyCredentialsPatch from a JSON string
starburst_galaxy_credentials_patch_instance = StarburstGalaxyCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(StarburstGalaxyCredentialsPatch.to_json())

# convert the object into a dict
starburst_galaxy_credentials_patch_dict = starburst_galaxy_credentials_patch_instance.to_dict()
# create an instance of StarburstGalaxyCredentialsPatch from a dict
starburst_galaxy_credentials_patch_from_dict = StarburstGalaxyCredentialsPatch.from_dict(starburst_galaxy_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


