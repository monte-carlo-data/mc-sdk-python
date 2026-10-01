# Db2CredentialsIn

What to create Db2 credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Connect without TLS. | [optional] 

## Example

```python
from montecarlo.models.db2_credentials_in import Db2CredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of Db2CredentialsIn from a JSON string
db2_credentials_in_instance = Db2CredentialsIn.from_json(json)
# print the JSON string representation of the object
print(Db2CredentialsIn.to_json())

# convert the object into a dict
db2_credentials_in_dict = db2_credentials_in_instance.to_dict()
# create an instance of Db2CredentialsIn from a dict
db2_credentials_in_from_dict = Db2CredentialsIn.from_dict(db2_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


