# SapHanaCredentialsOut

SAP HANA credentials Monte Carlo stores. The password is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**db_name** | **str** | Database to connect to. | 
**user** | **str** | Database user Monte Carlo logs in as. | 

## Example

```python
from pycarlo2.models.sap_hana_credentials_out import SapHanaCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SapHanaCredentialsOut from a JSON string
sap_hana_credentials_out_instance = SapHanaCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SapHanaCredentialsOut.to_json())

# convert the object into a dict
sap_hana_credentials_out_dict = sap_hana_credentials_out_instance.to_dict()
# create an instance of SapHanaCredentialsOut from a dict
sap_hana_credentials_out_from_dict = SapHanaCredentialsOut.from_dict(sap_hana_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


