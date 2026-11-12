# HiveCredentialsIn

What to create HiveServer2 credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the HiveServer2. | 
**port** | **int** | Port the HiveServer2 listens on in binary mode. | [optional] 
**user** | **str** | User Monte Carlo signs in as. Hive takes no password. | 
**db_name** | **str** | Database Monte Carlo connects to. | [optional] 
**auth_mode** | [**HiveAuthMode**](HiveAuthMode.md) | How Monte Carlo signs in. Omit it for &#x60;SASL&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.hive_credentials_in import HiveCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of HiveCredentialsIn from a JSON string
hive_credentials_in_instance = HiveCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(HiveCredentialsIn.to_json())

# convert the object into a dict
hive_credentials_in_dict = hive_credentials_in_instance.to_dict()
# create an instance of HiveCredentialsIn from a dict
hive_credentials_in_from_dict = HiveCredentialsIn.from_dict(hive_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


