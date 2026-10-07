# FileCredentialsPatch

A change to file credentials.  A field left out is unchanged. An optional field set to null is cleared. `file_path` cannot be cleared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**file_path** | **str** | Path of the file on the deployment that holds the connection&#39;s credentials. | [optional] 

## Example

```python
from pycarlo2.models.file_credentials_patch import FileCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of FileCredentialsPatch from a JSON string
file_credentials_patch_instance = FileCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(FileCredentialsPatch.to_json())

# convert the object into a dict
file_credentials_patch_dict = file_credentials_patch_instance.to_dict()
# create an instance of FileCredentialsPatch from a dict
file_credentials_patch_from_dict = FileCredentialsPatch.from_dict(file_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


