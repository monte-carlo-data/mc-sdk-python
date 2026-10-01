# SapHanaCredentialsIn

What to create SAP HANA credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | 

## Example

```python
from montecarlo.models.sap_hana_credentials_in import SapHanaCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaCredentialsIn from a JSON string
sap_hana_credentials_in_instance = SapHanaCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(SapHanaCredentialsIn.to_json())

# convert the object into a dict
sap_hana_credentials_in_dict = sap_hana_credentials_in_instance.to_dict()
# create an instance of SapHanaCredentialsIn from a dict
sap_hana_credentials_in_from_dict = SapHanaCredentialsIn.from_dict(sap_hana_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


