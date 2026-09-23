# SnowflakeCredentialsValidateIn

Candidate Snowflake key pair credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**account** | **str** | Snowflake account identifier, such as &#x60;xy12345.us-east-1&#x60;. Without the &#x60;.snowflakecomputing.com&#x60; suffix. | 
**user** | **str** | Snowflake user the key pair belongs to. | 
**private_key** | **str** | The private key of the pair, as PEM text including its BEGIN and END lines. Used for this check and not kept. | 
**private_key_passphrase** | **str** | Passphrase the private key is encrypted with. Omit it for an unencrypted key. Never returned. | [optional] 
**warehouse** | **str** | Snowflake virtual warehouse to run queries in. Omit it to use the user&#39;s default. | [optional] 

## Example

```python
from montecarlo.models.snowflake_credentials_validate_in import SnowflakeCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeCredentialsValidateIn from a JSON string
snowflake_credentials_validate_in_instance = SnowflakeCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(SnowflakeCredentialsValidateIn.to_json())

# convert the object into a dict
snowflake_credentials_validate_in_dict = snowflake_credentials_validate_in_instance.to_dict()
# create an instance of SnowflakeCredentialsValidateIn from a dict
snowflake_credentials_validate_in_from_dict = SnowflakeCredentialsValidateIn.from_dict(snowflake_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


