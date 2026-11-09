# MotherDuckCredentialsChangeValidateIn

A change to existing MotherDuck credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**db_name** | **str** | MotherDuck database to connect to. | [optional] 
**token** | **str** | New access token. | [optional] 

## Example

```python
from pycarlo2.models.mother_duck_credentials_change_validate_in import MotherDuckCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of MotherDuckCredentialsChangeValidateIn from a JSON string
mother_duck_credentials_change_validate_in_instance = MotherDuckCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(MotherDuckCredentialsChangeValidateIn.to_json())

# convert the object into a dict
mother_duck_credentials_change_validate_in_dict = mother_duck_credentials_change_validate_in_instance.to_dict()
# create an instance of MotherDuckCredentialsChangeValidateIn from a dict
mother_duck_credentials_change_validate_in_from_dict = MotherDuckCredentialsChangeValidateIn.from_dict(mother_duck_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


