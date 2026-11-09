# HiveS3CredentialsPatch

A change to existing Hive (S3) credentials.  A field left out is unchanged. `external_id` set to null is cleared. `bucket`, `prefix` and `assumable_role` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | [optional] 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**bucket** | **str** | S3 bucket Monte Carlo reads from. | [optional] 
**prefix** | **str** | Key prefix of the EMR log root, such as &#x60;emr/prod&#x60;. Leave out the bucket, a leading &#x60;/&#x60; and any &#x60;s3://&#x60; scheme. Send an empty string when the cluster&#39;s EMR log URI is the bucket root. Monte Carlo reads each cluster&#39;s Hive logs under &#x60;&lt;prefix&gt;/&lt;cluster-id&gt;/node/&lt;instance-id&gt;/applications/hive/&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.hive_s3_credentials_patch import HiveS3CredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of HiveS3CredentialsPatch from a JSON string
hive_s3_credentials_patch_instance = HiveS3CredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(HiveS3CredentialsPatch.to_json())

# convert the object into a dict
hive_s3_credentials_patch_dict = hive_s3_credentials_patch_instance.to_dict()
# create an instance of HiveS3CredentialsPatch from a dict
hive_s3_credentials_patch_from_dict = HiveS3CredentialsPatch.from_dict(hive_s3_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


