# StarburstEnterpriseCredentialsIn

What to create Starburst Enterprise credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Stored by Monte Carlo and never returned. | 
**db_name** | **str** | Database to connect to. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Skip the check of the server&#39;s certificate. The connection always uses TLS. | [optional] 

## Example

```python
from pycarlo2.models.starburst_enterprise_credentials_in import StarburstEnterpriseCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstEnterpriseCredentialsIn from a JSON string
starburst_enterprise_credentials_in_instance = StarburstEnterpriseCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(StarburstEnterpriseCredentialsIn.to_json())

# convert the object into a dict
starburst_enterprise_credentials_in_dict = starburst_enterprise_credentials_in_instance.to_dict()
# create an instance of StarburstEnterpriseCredentialsIn from a dict
starburst_enterprise_credentials_in_from_dict = StarburstEnterpriseCredentialsIn.from_dict(starburst_enterprise_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


