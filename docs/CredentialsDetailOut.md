# CredentialsDetailOut

Credentials of any kind, with the non-secret fields of that kind.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**details** | **Dict[str, object]** | The fields the typed read of this kind returns beyond the ones above, such as &#x60;account&#x60; and &#x60;user&#x60; for Snowflake. Never a secret. | 

## Example

```python
from pycarlo2.models.credentials_detail_out import CredentialsDetailOut

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsDetailOut from a JSON string
credentials_detail_out_instance = CredentialsDetailOut.from_json(json)
# print the JSON string representation of the object
print(CredentialsDetailOut.to_json())

# convert the object into a dict
credentials_detail_out_dict = credentials_detail_out_instance.to_dict()
# create an instance of CredentialsDetailOut from a dict
credentials_detail_out_from_dict = CredentialsDetailOut.from_dict(credentials_detail_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


