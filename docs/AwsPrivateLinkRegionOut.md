# AwsPrivateLinkRegionOut

An AWS region where Monte Carlo has a VPC for collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** | The AWS region. | 
**vpc_id** | **str** | ID of Monte Carlo&#39;s VPC in the region. | 
**data_store_vpc_endpoint_id** | **str** | ID of the S3 VPC endpoint Monte Carlo reaches a data store&#39;s bucket through. Use it in an &#x60;aws:SourceVpce&#x60; condition on the bucket policy. Null when the region has none. | 
**agent_vpc_endpoint_id** | **str** | ID of the Lambda VPC endpoint Monte Carlo invokes a collection agent through. Use it in an &#x60;aws:SourceVpce&#x60; condition on the function&#39;s policy. Null when the region has none. | 

## Example

```python
from pycarlo2.models.aws_private_link_region_out import AwsPrivateLinkRegionOut

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPrivateLinkRegionOut from a JSON string
aws_private_link_region_out_instance = AwsPrivateLinkRegionOut.from_json(json)
# print the JSON string representation of the object
print(AwsPrivateLinkRegionOut.to_json())

# convert the object into a dict
aws_private_link_region_out_dict = aws_private_link_region_out_instance.to_dict()
# create an instance of AwsPrivateLinkRegionOut from a dict
aws_private_link_region_out_from_dict = AwsPrivateLinkRegionOut.from_dict(aws_private_link_region_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


