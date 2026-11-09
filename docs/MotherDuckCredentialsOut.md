# MotherDuckCredentialsOut

MotherDuck credentials Monte Carlo stores. The token is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**db_name** | **str** | MotherDuck database to connect to. | 

## Example

```python
from pycarlo2.models.mother_duck_credentials_out import MotherDuckCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of MotherDuckCredentialsOut from a JSON string
mother_duck_credentials_out_instance = MotherDuckCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(MotherDuckCredentialsOut.to_json())

# convert the object into a dict
mother_duck_credentials_out_dict = mother_duck_credentials_out_instance.to_dict()
# create an instance of MotherDuckCredentialsOut from a dict
mother_duck_credentials_out_from_dict = MotherDuckCredentialsOut.from_dict(mother_duck_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


