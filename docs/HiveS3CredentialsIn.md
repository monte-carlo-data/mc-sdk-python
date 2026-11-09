# HiveS3CredentialsIn

What to create Hive (S3) credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**bucket** | **str** | S3 bucket Monte Carlo reads from. | 
**prefix** | **str** | Key prefix of the EMR log root, such as &#x60;emr/prod&#x60;. Leave out the bucket, a leading &#x60;/&#x60; and any &#x60;s3://&#x60; scheme. Send an empty string when the cluster&#39;s EMR log URI is the bucket root. Monte Carlo reads each cluster&#39;s Hive logs under &#x60;&lt;prefix&gt;/&lt;cluster-id&gt;/node/&lt;instance-id&gt;/applications/hive/&#x60;. | 

## Example

```python
from pycarlo2.models.hive_s3_credentials_in import HiveS3CredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of HiveS3CredentialsIn from a JSON string
hive_s3_credentials_in_instance = HiveS3CredentialsIn.from_json(json)
# print the JSON string representation of the object
print(HiveS3CredentialsIn.to_json())

# convert the object into a dict
hive_s3_credentials_in_dict = hive_s3_credentials_in_instance.to_dict()
# create an instance of HiveS3CredentialsIn from a dict
hive_s3_credentials_in_from_dict = HiveS3CredentialsIn.from_dict(hive_s3_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


