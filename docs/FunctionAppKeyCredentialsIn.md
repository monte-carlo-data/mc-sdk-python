# FunctionAppKeyCredentialsIn

Credentials Monte Carlo uses when it authenticates with a function app key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** | Function app key Monte Carlo presents when it calls the agent. | 

## Example

```python
from pycarlo2.models.function_app_key_credentials_in import FunctionAppKeyCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionAppKeyCredentialsIn from a JSON string
function_app_key_credentials_in_instance = FunctionAppKeyCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(FunctionAppKeyCredentialsIn.to_json())

# convert the object into a dict
function_app_key_credentials_in_dict = function_app_key_credentials_in_instance.to_dict()
# create an instance of FunctionAppKeyCredentialsIn from a dict
function_app_key_credentials_in_from_dict = FunctionAppKeyCredentialsIn.from_dict(function_app_key_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


