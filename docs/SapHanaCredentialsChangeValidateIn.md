# SapHanaCredentialsChangeValidateIn

A change to existing SAP HANA credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 

## Example

```python
from pycarlo2.models.sap_hana_credentials_change_validate_in import SapHanaCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaCredentialsChangeValidateIn from a JSON string
sap_hana_credentials_change_validate_in_instance = SapHanaCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(SapHanaCredentialsChangeValidateIn.to_json())

# convert the object into a dict
sap_hana_credentials_change_validate_in_dict = sap_hana_credentials_change_validate_in_instance.to_dict()
# create an instance of SapHanaCredentialsChangeValidateIn from a dict
sap_hana_credentials_change_validate_in_from_dict = SapHanaCredentialsChangeValidateIn.from_dict(sap_hana_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


