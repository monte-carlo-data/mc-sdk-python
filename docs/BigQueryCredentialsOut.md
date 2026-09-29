# BigQueryCredentialsOut

BigQuery service account credentials Monte Carlo stores. The key is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**project_id** | **str** | Google Cloud project the service account belongs to. | 
**client_email** | **str** | Email address of the service account. | 

## Example

```python
from montecarlo.models.big_query_credentials_out import BigQueryCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryCredentialsOut from a JSON string
big_query_credentials_out_instance = BigQueryCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(BigQueryCredentialsOut.to_json())

# convert the object into a dict
big_query_credentials_out_dict = big_query_credentials_out_instance.to_dict()
# create an instance of BigQueryCredentialsOut from a dict
big_query_credentials_out_from_dict = BigQueryCredentialsOut.from_dict(big_query_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


