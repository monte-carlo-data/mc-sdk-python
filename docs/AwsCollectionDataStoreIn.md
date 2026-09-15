# AwsCollectionDataStoreIn

Details Monte Carlo needs to access a data store you keep in an S3 bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment to register the data store on. It must already hold an unregistered S3 data store. | 
**bucket_name** | **str** | Name of the S3 bucket Monte Carlo should use. | 
**role_arn** | **str** | ARN of the role Monte Carlo assumes to access the bucket. Its trust policy must already carry the deployment&#39;s external id. | 
**name** | **str** | Display name for the data store. Replaces the name its deployment gave it. | [optional] 

## Example

```python
from montecarlo.models.aws_collection_data_store_in import AwsCollectionDataStoreIn

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCollectionDataStoreIn from a JSON string
aws_collection_data_store_in_instance = AwsCollectionDataStoreIn.from_json(json)
# print the JSON string representation of the object
print(AwsCollectionDataStoreIn.to_json())

# convert the object into a dict
aws_collection_data_store_in_dict = aws_collection_data_store_in_instance.to_dict()
# create an instance of AwsCollectionDataStoreIn from a dict
aws_collection_data_store_in_from_dict = AwsCollectionDataStoreIn.from_dict(aws_collection_data_store_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


