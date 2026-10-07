# GcpSecretManagerCredentialsPatch

A change to GCP Secret Manager credentials.  A field left out is unchanged. An optional field set to null is cleared. `gcp_secret` cannot be cleared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**gcp_secret** | **str** | Name of the GCP Secret Manager secret holding the connection&#39;s credentials. | [optional] 

## Example

```python
from pycarlo2.models.gcp_secret_manager_credentials_patch import GcpSecretManagerCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of GcpSecretManagerCredentialsPatch from a JSON string
gcp_secret_manager_credentials_patch_instance = GcpSecretManagerCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(GcpSecretManagerCredentialsPatch.to_json())

# convert the object into a dict
gcp_secret_manager_credentials_patch_dict = gcp_secret_manager_credentials_patch_instance.to_dict()
# create an instance of GcpSecretManagerCredentialsPatch from a dict
gcp_secret_manager_credentials_patch_from_dict = GcpSecretManagerCredentialsPatch.from_dict(gcp_secret_manager_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


