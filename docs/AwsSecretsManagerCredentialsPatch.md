# AwsSecretsManagerCredentialsPatch

A change to AWS Secrets Manager credentials.  A field left out is unchanged. An optional field set to null is cleared. `aws_secret` cannot be cleared.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**databricks_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**aws_secret** | **str** | Name or ARN of the AWS Secrets Manager secret holding the connection&#39;s credentials. | [optional] 
**aws_region** | **str** | AWS region of the secret. Omit it to use the deployment&#39;s own region. | [optional] 
**assumable_role** | **str** | ARN of a role the deployment assumes to read the secret. Omit it to read as itself. | [optional] 
**external_id** | **str** | External id the assumed role&#39;s trust policy requires, if it requires one. | [optional] 

## Example

```python
from montecarlo.models.aws_secrets_manager_credentials_patch import AwsSecretsManagerCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSecretsManagerCredentialsPatch from a JSON string
aws_secrets_manager_credentials_patch_instance = AwsSecretsManagerCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AwsSecretsManagerCredentialsPatch.to_json())

# convert the object into a dict
aws_secrets_manager_credentials_patch_dict = aws_secrets_manager_credentials_patch_instance.to_dict()
# create an instance of AwsSecretsManagerCredentialsPatch from a dict
aws_secrets_manager_credentials_patch_from_dict = AwsSecretsManagerCredentialsPatch.from_dict(aws_secrets_manager_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


