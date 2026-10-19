# SnowflakeCredentialsChangeValidateIn

A change to existing Snowflake credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**account** | **str** | New Snowflake account identifier, without the &#x60;.snowflakecomputing.com&#x60; suffix. Letters, digits, &#x60;_&#x60;, &#x60;.&#x60; and &#x60;-&#x60; only. | [optional] 
**user** | **str** | New Snowflake user. | [optional] 
**private_key** | **str** | New private key, as PEM text. Replaces the stored key and its passphrase; send &#x60;private_key_passphrase&#x60; in the same request if the new key has one. | [optional] 
**private_key_passphrase** | **str** | Passphrase of the new private key. Only accepted together with &#x60;private_key&#x60;. | [optional] 
**warehouse** | **str** | New Snowflake virtual warehouse. An explicit null clears it; queries then run in the user&#39;s default. | [optional] 

## Example

```python
from pycarlo2.models.snowflake_credentials_change_validate_in import SnowflakeCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeCredentialsChangeValidateIn from a JSON string
snowflake_credentials_change_validate_in_instance = SnowflakeCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(SnowflakeCredentialsChangeValidateIn.to_json())

# convert the object into a dict
snowflake_credentials_change_validate_in_dict = snowflake_credentials_change_validate_in_instance.to_dict()
# create an instance of SnowflakeCredentialsChangeValidateIn from a dict
snowflake_credentials_change_validate_in_from_dict = SnowflakeCredentialsChangeValidateIn.from_dict(snowflake_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


