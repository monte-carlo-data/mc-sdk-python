# GcpSecretManagerCredentialsOut

Where in GCP Secret Manager a connection's credentials live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Null unless set. | 
**databricks_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Null unless set. | 
**gcp_secret** | **str** | Name of the GCP Secret Manager secret holding the connection&#39;s credentials. | 

## Example

```python
from montecarlo.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSecretManagerCredentialsOut from a JSON string
gcp_secret_manager_credentials_out_instance = GcpSecretManagerCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(GcpSecretManagerCredentialsOut.to_json())

# convert the object into a dict
gcp_secret_manager_credentials_out_dict = gcp_secret_manager_credentials_out_instance.to_dict()
# create an instance of GcpSecretManagerCredentialsOut from a dict
gcp_secret_manager_credentials_out_from_dict = GcpSecretManagerCredentialsOut.from_dict(gcp_secret_manager_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


