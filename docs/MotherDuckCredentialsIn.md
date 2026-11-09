# MotherDuckCredentialsIn

What to create MotherDuck credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** | MotherDuck database to connect to. | 
**token** | **str** | Access token Monte Carlo signs in to MotherDuck with. Stored by Monte Carlo and never returned. | 

## Example

```python
from pycarlo2.models.mother_duck_credentials_in import MotherDuckCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of MotherDuckCredentialsIn from a JSON string
mother_duck_credentials_in_instance = MotherDuckCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(MotherDuckCredentialsIn.to_json())

# convert the object into a dict
mother_duck_credentials_in_dict = mother_duck_credentials_in_instance.to_dict()
# create an instance of MotherDuckCredentialsIn from a dict
mother_duck_credentials_in_from_dict = MotherDuckCredentialsIn.from_dict(mother_duck_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


