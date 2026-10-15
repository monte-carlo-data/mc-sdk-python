# GcpSecretManagerCredentialsChangeValidateIn

A change to existing GCP Secret Manager credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**gcp_secret** | **str** | Name of the GCP Secret Manager secret holding the connection&#39;s credentials. | [optional] 

## Example

```python
from pycarlo2.models.gcp_secret_manager_credentials_change_validate_in import GcpSecretManagerCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSecretManagerCredentialsChangeValidateIn from a JSON string
gcp_secret_manager_credentials_change_validate_in_instance = GcpSecretManagerCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(GcpSecretManagerCredentialsChangeValidateIn.to_json())

# convert the object into a dict
gcp_secret_manager_credentials_change_validate_in_dict = gcp_secret_manager_credentials_change_validate_in_instance.to_dict()
# create an instance of GcpSecretManagerCredentialsChangeValidateIn from a dict
gcp_secret_manager_credentials_change_validate_in_from_dict = GcpSecretManagerCredentialsChangeValidateIn.from_dict(gcp_secret_manager_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


