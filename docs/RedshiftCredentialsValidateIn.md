# RedshiftCredentialsValidateIn

Candidate Redshift credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**password** | **str** | Password of the database user. Used for this check and not kept. | 
**ssl_ca_data** | **str** | PEM text of the CA certificate the server&#39;s certificate is checked against. | [optional] 
**ssl_disabled** | **bool** | Connect without TLS. | [optional] 
**ssl_verify_cert** | **bool** | Check the server&#39;s certificate against the CA. | [optional] 
**ssl_verify_identity** | **bool** | Check the certificate and that it names the host. | [optional] 
**ssl_skip_cert_verification** | **bool** | Encrypt the connection without checking the server&#39;s certificate. | [optional] 
**db_name** | **str** | Redshift database to connect to. | 

## Example

```python
from montecarlo.models.redshift_credentials_validate_in import RedshiftCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftCredentialsValidateIn from a JSON string
redshift_credentials_validate_in_instance = RedshiftCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(RedshiftCredentialsValidateIn.to_json())

# convert the object into a dict
redshift_credentials_validate_in_dict = redshift_credentials_validate_in_instance.to_dict()
# create an instance of RedshiftCredentialsValidateIn from a dict
redshift_credentials_validate_in_from_dict = RedshiftCredentialsValidateIn.from_dict(redshift_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


