# StarburstEnterpriseCredentialsValidateIn

Candidate Starburst Enterprise credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Used for this check and not kept. | 
**db_name** | **str** | Database to connect to. | [optional] 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Skip the check of the server&#39;s certificate. The connection always uses TLS. | [optional] 

## Example

```python
from pycarlo2.models.starburst_enterprise_credentials_validate_in import StarburstEnterpriseCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of StarburstEnterpriseCredentialsValidateIn from a JSON string
starburst_enterprise_credentials_validate_in_instance = StarburstEnterpriseCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(StarburstEnterpriseCredentialsValidateIn.to_json())

# convert the object into a dict
starburst_enterprise_credentials_validate_in_dict = starburst_enterprise_credentials_validate_in_instance.to_dict()
# create an instance of StarburstEnterpriseCredentialsValidateIn from a dict
starburst_enterprise_credentials_validate_in_from_dict = StarburstEnterpriseCredentialsValidateIn.from_dict(starburst_enterprise_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


