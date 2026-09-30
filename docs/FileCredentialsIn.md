# FileCredentialsIn

Credentials kept in a file on your deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;, or one of your custom connector types. Fixed once created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**file_path** | **str** | Path of the file on the deployment that holds the connection&#39;s credentials. | 

## Example

```python
from montecarlo.models.file_credentials_in import FileCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of FileCredentialsIn from a JSON string
file_credentials_in_instance = FileCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(FileCredentialsIn.to_json())

# convert the object into a dict
file_credentials_in_dict = file_credentials_in_instance.to_dict()
# create an instance of FileCredentialsIn from a dict
file_credentials_in_from_dict = FileCredentialsIn.from_dict(file_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


