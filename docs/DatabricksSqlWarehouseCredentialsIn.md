# DatabricksSqlWarehouseCredentialsIn

What to create Databricks credentials for running queries with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_url** | **str** | URL of the Databricks workspace, or its host name. | 
**sql_warehouse_id** | **str** | ID of the Databricks SQL warehouse the connection runs on. | 
**workspace_id** | **str** | ID of the Databricks workspace. | [optional] 
**token** | **str** | Personal access token or service principal token. Send this, or &#x60;oauth_client_id&#x60; and &#x60;oauth_client_secret&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**oauth_client_id** | **str** | Client ID of the service principal Monte Carlo signs in as with OAuth. Send it with &#x60;oauth_client_secret&#x60;, instead of &#x60;token&#x60;. | [optional] 
**oauth_client_secret** | **str** | OAuth secret of the service principal in &#x60;oauth_client_id&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**azure_tenant_id** | **str** | Microsoft Entra ID tenant, for a service principal Azure manages. Send it with &#x60;azure_workspace_resource_id&#x60; and the OAuth client. | [optional] 
**azure_workspace_resource_id** | **str** | Azure resource ID of the workspace, for a service principal Azure manages. Send it with &#x60;azure_tenant_id&#x60; and the OAuth client. | [optional] 

## Example

```python
from pycarlo2.models.databricks_sql_warehouse_credentials_in import DatabricksSqlWarehouseCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksSqlWarehouseCredentialsIn from a JSON string
databricks_sql_warehouse_credentials_in_instance = DatabricksSqlWarehouseCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(DatabricksSqlWarehouseCredentialsIn.to_json())

# convert the object into a dict
databricks_sql_warehouse_credentials_in_dict = databricks_sql_warehouse_credentials_in_instance.to_dict()
# create an instance of DatabricksSqlWarehouseCredentialsIn from a dict
databricks_sql_warehouse_credentials_in_from_dict = DatabricksSqlWarehouseCredentialsIn.from_dict(databricks_sql_warehouse_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


