# CredentialsSummaryOut

Credentials a connection reads with, as the list shows them.  The typed read of each credentials kind returns these fields plus the non-secret ones of that kind. No read returns secret material.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 

## Example

```python
from montecarlo.models.credentials_summary_out import CredentialsSummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsSummaryOut from a JSON string
credentials_summary_out_instance = CredentialsSummaryOut.from_json(json)
# print the JSON string representation of the object
print(CredentialsSummaryOut.to_json())

# convert the object into a dict
credentials_summary_out_dict = credentials_summary_out_instance.to_dict()
# create an instance of CredentialsSummaryOut from a dict
credentials_summary_out_from_dict = CredentialsSummaryOut.from_dict(credentials_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


