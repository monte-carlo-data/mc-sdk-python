# ClickHouseCredentialsValidateIn

Candidate ClickHouse credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Used for this check and not kept. | 
**db_name** | **str** | Database to connect to. | [optional] 

## Example

```python
from montecarlo.models.click_house_credentials_validate_in import ClickHouseCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of ClickHouseCredentialsValidateIn from a JSON string
click_house_credentials_validate_in_instance = ClickHouseCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(ClickHouseCredentialsValidateIn.to_json())

# convert the object into a dict
click_house_credentials_validate_in_dict = click_house_credentials_validate_in_instance.to_dict()
# create an instance of ClickHouseCredentialsValidateIn from a dict
click_house_credentials_validate_in_from_dict = ClickHouseCredentialsValidateIn.from_dict(click_house_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


