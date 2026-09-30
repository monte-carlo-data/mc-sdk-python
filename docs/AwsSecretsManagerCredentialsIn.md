# AwsSecretsManagerCredentialsIn

Credentials kept in your AWS Secrets Manager. Monte Carlo stores where to find them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60; or &#x60;bigquery&#x60;, or one of your custom connector types. Fixed once created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Only for a BigQuery connection. | [optional] 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Required for a &#x60;databricks-sql-warehouse&#x60; or &#x60;databricks-metastore-sql-warehouse&#x60; connection. | [optional] 
**aws_secret** | **str** | Name or ARN of the AWS Secrets Manager secret holding the connection&#39;s credentials. | 
**aws_region** | **str** | AWS region of the secret. Omit it to use the deployment&#39;s own region. | [optional] 
**assumable_role** | **str** | ARN of a role the deployment assumes to read the secret. Omit it to read as itself. | [optional] 
**external_id** | **str** | External id the assumed role&#39;s trust policy requires, if it requires one. | [optional] 

## Example

```python
from montecarlo.models.aws_secrets_manager_credentials_in import AwsSecretsManagerCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSecretsManagerCredentialsIn from a JSON string
aws_secrets_manager_credentials_in_instance = AwsSecretsManagerCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AwsSecretsManagerCredentialsIn.to_json())

# convert the object into a dict
aws_secrets_manager_credentials_in_dict = aws_secrets_manager_credentials_in_instance.to_dict()
# create an instance of AwsSecretsManagerCredentialsIn from a dict
aws_secrets_manager_credentials_in_from_dict = AwsSecretsManagerCredentialsIn.from_dict(aws_secrets_manager_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


