# SnowflakeCredentialsOut

Snowflake key pair credentials Monte Carlo stores. The key itself is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**account** | **str** | Snowflake account identifier, without the host suffix. | 
**user** | **str** | Snowflake user the key pair belongs to. | 
**warehouse** | **str** | Snowflake virtual warehouse queries run in. Null when none is set. | 

## Example

```python
from montecarlo.models.snowflake_credentials_out import SnowflakeCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeCredentialsOut from a JSON string
snowflake_credentials_out_instance = SnowflakeCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SnowflakeCredentialsOut.to_json())

# convert the object into a dict
snowflake_credentials_out_dict = snowflake_credentials_out_instance.to_dict()
# create an instance of SnowflakeCredentialsOut from a dict
snowflake_credentials_out_from_dict = SnowflakeCredentialsOut.from_dict(snowflake_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


