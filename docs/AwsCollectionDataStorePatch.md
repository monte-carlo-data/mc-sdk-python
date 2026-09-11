# AwsCollectionDataStorePatch

Details to change on an S3 data store. Only what you send is changed.  Sending only `name` skips the bucket checks, since a name is not validated against your storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_name** | **str** | Name of the S3 bucket Monte Carlo should use. | [optional] 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 
**role_arn** | **str** | ARN of the role Monte Carlo assumes to access the bucket. Its trust policy must already carry the deployment&#39;s external id. | [optional] 

## Example

```python
from montecarlo.models.aws_collection_data_store_patch import AwsCollectionDataStorePatch

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionDataStorePatch from a JSON string
aws_collection_data_store_patch_instance = AwsCollectionDataStorePatch.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionDataStorePatch.to_json())

# convert the object into a dict
aws_collection_data_store_patch_dict = aws_collection_data_store_patch_instance.to_dict()
# create an instance of AwsCollectionDataStorePatch from a dict
aws_collection_data_store_patch_from_dict = AwsCollectionDataStorePatch.from_dict(aws_collection_data_store_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


