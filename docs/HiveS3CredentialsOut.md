# HiveS3CredentialsOut

The S3 location Monte Carlo reads Hive query logs from, and the role it assumes to read it. Hive (S3) needs no secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. Null unless set. | 
**bucket** | **str** | S3 bucket Monte Carlo reads from. | 
**prefix** | **str** | Key prefix the objects sit under, such as &#x60;emr/prod&#x60;. Leave out the bucket, a leading &#x60;/&#x60; and any &#x60;s3://&#x60; scheme. | 

## Example

```python
from pycarlo2.models.hive_s3_credentials_out import HiveS3CredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of HiveS3CredentialsOut from a JSON string
hive_s3_credentials_out_instance = HiveS3CredentialsOut.from_json(json)
# print the JSON string representation of the object
print(HiveS3CredentialsOut.to_json())

# convert the object into a dict
hive_s3_credentials_out_dict = hive_s3_credentials_out_instance.to_dict()
# create an instance of HiveS3CredentialsOut from a dict
hive_s3_credentials_out_from_dict = HiveS3CredentialsOut.from_dict(hive_s3_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


