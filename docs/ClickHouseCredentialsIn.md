# ClickHouseCredentialsIn

What to create ClickHouse credentials with.

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
from montecarlo.models.click_house_credentials_in import ClickHouseCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of ClickHouseCredentialsIn from a JSON string
click_house_credentials_in_instance = ClickHouseCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(ClickHouseCredentialsIn.to_json())

# convert the object into a dict
click_house_credentials_in_dict = click_house_credentials_in_instance.to_dict()
# create an instance of ClickHouseCredentialsIn from a dict
click_house_credentials_in_from_dict = ClickHouseCredentialsIn.from_dict(click_house_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


