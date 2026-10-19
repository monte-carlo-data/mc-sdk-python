# DatabricksSqlWarehouseCredentialsPatch

A change to existing Databricks query credentials.  A field left out is unchanged. `workspace_id` and the Azure fields set to null are cleared. `token` and `oauth_client_secret` set to null are unchanged. `workspace_url` and `sql_warehouse_id` cannot be cleared. Sending `token` drops a stored OAuth client and its Azure fields. Sending the OAuth client drops a stored token. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_url** | **str** | URL of the Databricks workspace, or its host name. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**sql_warehouse_id** | **str** | ID of the Databricks SQL warehouse the connection runs on. | [optional] 
**workspace_id** | **str** | ID of the Databricks workspace. | [optional] 
**token** | **str** | Personal access token or service principal token. Send this, or &#x60;oauth_client_id&#x60; and &#x60;oauth_client_secret&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**oauth_client_id** | **str** | Client ID of the service principal Monte Carlo signs in as with OAuth. Send it with &#x60;oauth_client_secret&#x60;, instead of &#x60;token&#x60;. | [optional] 
**oauth_client_secret** | **str** | OAuth secret of the service principal in &#x60;oauth_client_id&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**azure_tenant_id** | **str** | Microsoft Entra ID tenant, for a service principal Azure manages. Send it with &#x60;azure_workspace_resource_id&#x60; and the OAuth client. | [optional] 
**azure_workspace_resource_id** | **str** | Azure resource ID of the workspace, for a service principal Azure manages. Send it with &#x60;azure_tenant_id&#x60; and the OAuth client. | [optional] 

## Example

```python
from pycarlo2.models.databricks_sql_warehouse_credentials_patch import DatabricksSqlWarehouseCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksSqlWarehouseCredentialsPatch from a JSON string
databricks_sql_warehouse_credentials_patch_instance = DatabricksSqlWarehouseCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(DatabricksSqlWarehouseCredentialsPatch.to_json())

# convert the object into a dict
databricks_sql_warehouse_credentials_patch_dict = databricks_sql_warehouse_credentials_patch_instance.to_dict()
# create an instance of DatabricksSqlWarehouseCredentialsPatch from a dict
databricks_sql_warehouse_credentials_patch_from_dict = DatabricksSqlWarehouseCredentialsPatch.from_dict(databricks_sql_warehouse_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


