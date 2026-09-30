# GcpSecretManagerCredentialsIn

Credentials kept in your GCP Secret Manager. Monte Carlo stores where to find them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;, or one of your custom connector types. Fixed once created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**gcp_secret** | **str** | Name of the GCP Secret Manager secret holding the connection&#39;s credentials. | 

## Example

```python
from montecarlo.models.gcp_secret_manager_credentials_in import GcpSecretManagerCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSecretManagerCredentialsIn from a JSON string
gcp_secret_manager_credentials_in_instance = GcpSecretManagerCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(GcpSecretManagerCredentialsIn.to_json())

# convert the object into a dict
gcp_secret_manager_credentials_in_dict = gcp_secret_manager_credentials_in_instance.to_dict()
# create an instance of GcpSecretManagerCredentialsIn from a dict
gcp_secret_manager_credentials_in_from_dict = GcpSecretManagerCredentialsIn.from_dict(gcp_secret_manager_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


