# AwsSecretsManagerCredentialsOut

Where in AWS Secrets Manager a connection's credentials live.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**bq_project_id** | **str** | BigQuery project the connection reads from. Null unless set. | 
**sql_warehouse_id** | **str** | Databricks SQL warehouse the connection runs queries on. Null unless set. | 
**aws_secret** | **str** | Name or ARN of the AWS Secrets Manager secret holding the connection&#39;s credentials. | 
**aws_region** | **str** | AWS region of the secret. Null when unset. | 
**assumable_role** | **str** | ARN of the role the deployment assumes to read the secret. Null when unset. | 
**external_id** | **str** | External id presented when assuming the role. Null when unset. | 

## Example

```python
from pycarlo2.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSecretsManagerCredentialsOut from a JSON string
aws_secrets_manager_credentials_out_instance = AwsSecretsManagerCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(AwsSecretsManagerCredentialsOut.to_json())

# convert the object into a dict
aws_secrets_manager_credentials_out_dict = aws_secrets_manager_credentials_out_instance.to_dict()
# create an instance of AwsSecretsManagerCredentialsOut from a dict
aws_secrets_manager_credentials_out_from_dict = AwsSecretsManagerCredentialsOut.from_dict(aws_secrets_manager_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


