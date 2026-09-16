# SnowflakeCredentialsIn

What to create Snowflake key pair credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Snowflake account identifier, such as &#x60;xy12345.us-east-1&#x60;. Without the &#x60;.snowflakecomputing.com&#x60; suffix. | 
**user** | **str** | Snowflake user the key pair belongs to. | 
**private_key** | **str** | The private key of the pair, as PEM text including its BEGIN and END lines. Stored by Monte Carlo and never returned. | 
**private_key_passphrase** | **str** | Passphrase the private key is encrypted with. Omit it for an unencrypted key. Never returned. | [optional] 
**warehouse** | **str** | Snowflake virtual warehouse to run queries in. Omit it to use the user&#39;s default. | [optional] 

## Example

```python
from montecarlo.models.snowflake_credentials_in import SnowflakeCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeCredentialsIn from a JSON string
snowflake_credentials_in_instance = SnowflakeCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(SnowflakeCredentialsIn.to_json())

# convert the object into a dict
snowflake_credentials_in_dict = snowflake_credentials_in_instance.to_dict()
# create an instance of SnowflakeCredentialsIn from a dict
snowflake_credentials_in_from_dict = SnowflakeCredentialsIn.from_dict(snowflake_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


