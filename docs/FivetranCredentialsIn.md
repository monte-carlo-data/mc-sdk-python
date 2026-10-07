# FivetranCredentialsIn

What to create Fivetran API credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Key of the Fivetran API key. Stored by Monte Carlo and never returned. | 
**api_password** | **str** | Secret of the Fivetran API key. Stored by Monte Carlo and never returned. | 
**base_url** | **str** | URL of the Fivetran REST API. Leave it out for https://api.fivetran.com/v1/. | [optional] 

## Example

```python
from pycarlo2.models.fivetran_credentials_in import FivetranCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of FivetranCredentialsIn from a JSON string
fivetran_credentials_in_instance = FivetranCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(FivetranCredentialsIn.to_json())

# convert the object into a dict
fivetran_credentials_in_dict = fivetran_credentials_in_instance.to_dict()
# create an instance of FivetranCredentialsIn from a dict
fivetran_credentials_in_from_dict = FivetranCredentialsIn.from_dict(fivetran_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


