# FileCredentialsOut

Which file on the deployment holds a connection's credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Null unless set. | 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Null unless set. | 
**file_path** | **str** | Path of the file on the deployment that holds the connection&#39;s credentials. | 

## Example

```python
from pycarlo2.models.file_credentials_out import FileCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of FileCredentialsOut from a JSON string
file_credentials_out_instance = FileCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(FileCredentialsOut.to_json())

# convert the object into a dict
file_credentials_out_dict = file_credentials_out_instance.to_dict()
# create an instance of FileCredentialsOut from a dict
file_credentials_out_from_dict = FileCredentialsOut.from_dict(file_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


