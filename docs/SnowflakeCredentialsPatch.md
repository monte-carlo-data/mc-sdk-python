# SnowflakeCredentialsPatch

A change to existing Snowflake credentials.  A field left out is unchanged. `warehouse` set to null is cleared. `private_key` replaces the whole key pair: the passphrase is kept only when the same request sends one, and a passphrase is only accepted alongside `private_key`, null included. `private_key` set to null is unchanged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | New Snowflake account identifier, without the &#x60;.snowflakecomputing.com&#x60; suffix. | [optional] 
**user** | **str** | New Snowflake user. | [optional] 
**private_key** | **str** | New private key, as PEM text. Replaces the stored key and its passphrase; send &#x60;private_key_passphrase&#x60; in the same request if the new key has one. | [optional] 
**private_key_passphrase** | **str** | Passphrase of the new private key. Only accepted together with &#x60;private_key&#x60;. | [optional] 
**warehouse** | **str** | New Snowflake virtual warehouse. An explicit null clears it; queries then run in the user&#39;s default. | [optional] 

## Example

```python
from montecarlo.models.snowflake_credentials_patch import SnowflakeCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeCredentialsPatch from a JSON string
snowflake_credentials_patch_instance = SnowflakeCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(SnowflakeCredentialsPatch.to_json())

# convert the object into a dict
snowflake_credentials_patch_dict = snowflake_credentials_patch_instance.to_dict()
# create an instance of SnowflakeCredentialsPatch from a dict
snowflake_credentials_patch_from_dict = SnowflakeCredentialsPatch.from_dict(snowflake_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


