# DatabricksSqlWarehouseCredentialsValidateIn

Candidate Databricks query credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**workspace_url** | **str** | URL of the Databricks workspace, or its host name. | 
**sql_warehouse_id** | **str** | ID of the Databricks SQL warehouse the connection runs on. | 
**workspace_id** | **str** | ID of the Databricks workspace. | [optional] 
**token** | **str** | Personal access token or service principal token. Send this, or &#x60;oauth_client_id&#x60; and &#x60;oauth_client_secret&#x60;. Used for this check and not kept. | [optional] 
**oauth_client_id** | **str** | Client ID of the service principal Monte Carlo signs in as with OAuth. Send it with &#x60;oauth_client_secret&#x60;, instead of &#x60;token&#x60;. | [optional] 
**oauth_client_secret** | **str** | OAuth secret of the service principal in &#x60;oauth_client_id&#x60;. Used for this check and not kept. | [optional] 
**azure_tenant_id** | **str** | Microsoft Entra ID tenant, for a service principal Azure manages. Send it with &#x60;azure_workspace_resource_id&#x60; and the OAuth client. | [optional] 
**azure_workspace_resource_id** | **str** | Azure resource ID of the workspace, for a service principal Azure manages. Send it with &#x60;azure_tenant_id&#x60; and the OAuth client. | [optional] 

## Example

```python
from pycarlo2.models.databricks_sql_warehouse_credentials_validate_in import DatabricksSqlWarehouseCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksSqlWarehouseCredentialsValidateIn from a JSON string
databricks_sql_warehouse_credentials_validate_in_instance = DatabricksSqlWarehouseCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(DatabricksSqlWarehouseCredentialsValidateIn.to_json())

# convert the object into a dict
databricks_sql_warehouse_credentials_validate_in_dict = databricks_sql_warehouse_credentials_validate_in_instance.to_dict()
# create an instance of DatabricksSqlWarehouseCredentialsValidateIn from a dict
databricks_sql_warehouse_credentials_validate_in_from_dict = DatabricksSqlWarehouseCredentialsValidateIn.from_dict(databricks_sql_warehouse_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


