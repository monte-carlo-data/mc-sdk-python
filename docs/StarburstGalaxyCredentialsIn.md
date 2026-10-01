# StarburstGalaxyCredentialsIn

What to create Starburst Galaxy credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | [optional] 

## Example

```python
from montecarlo.models.starburst_galaxy_credentials_in import StarburstGalaxyCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstGalaxyCredentialsIn from a JSON string
starburst_galaxy_credentials_in_instance = StarburstGalaxyCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(StarburstGalaxyCredentialsIn.to_json())

# convert the object into a dict
starburst_galaxy_credentials_in_dict = starburst_galaxy_credentials_in_instance.to_dict()
# create an instance of StarburstGalaxyCredentialsIn from a dict
starburst_galaxy_credentials_in_from_dict = StarburstGalaxyCredentialsIn.from_dict(starburst_galaxy_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


