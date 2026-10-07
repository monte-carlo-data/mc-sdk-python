# DatabricksSqlWarehouseCredentialsOut

Databricks credentials Monte Carlo stores for running queries on a SQL warehouse. The token and the OAuth secret are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**workspace_url** | **str** | URL of the Databricks workspace, or its host name. | 
**sql_warehouse_id** | **str** | ID of the Databricks SQL warehouse the connection runs on. | 
**workspace_id** | **str** | ID of the Databricks workspace. Null unless set. | 
**oauth_client_id** | **str** | Client ID of the OAuth service principal. Null for token credentials. | 
**azure_tenant_id** | **str** | Microsoft Entra ID tenant of the service principal. Null unless set. | 
**azure_workspace_resource_id** | **str** | Azure resource ID of the workspace. Null unless set. | 

## Example

```python
from pycarlo2.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksSqlWarehouseCredentialsOut from a JSON string
databricks_sql_warehouse_credentials_out_instance = DatabricksSqlWarehouseCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(DatabricksSqlWarehouseCredentialsOut.to_json())

# convert the object into a dict
databricks_sql_warehouse_credentials_out_dict = databricks_sql_warehouse_credentials_out_instance.to_dict()
# create an instance of DatabricksSqlWarehouseCredentialsOut from a dict
databricks_sql_warehouse_credentials_out_from_dict = DatabricksSqlWarehouseCredentialsOut.from_dict(databricks_sql_warehouse_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


