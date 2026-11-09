# MotherDuckCredentialsValidateIn

Candidate MotherDuck credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**db_name** | **str** | MotherDuck database to connect to. | 
**token** | **str** | Access token Monte Carlo signs in to MotherDuck with. Used for this check and not kept. | 

## Example

```python
from pycarlo2.models.mother_duck_credentials_validate_in import MotherDuckCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of MotherDuckCredentialsValidateIn from a JSON string
mother_duck_credentials_validate_in_instance = MotherDuckCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(MotherDuckCredentialsValidateIn.to_json())

# convert the object into a dict
mother_duck_credentials_validate_in_dict = mother_duck_credentials_validate_in_instance.to_dict()
# create an instance of MotherDuckCredentialsValidateIn from a dict
mother_duck_credentials_validate_in_from_dict = MotherDuckCredentialsValidateIn.from_dict(mother_duck_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


