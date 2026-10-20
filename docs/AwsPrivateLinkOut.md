# AwsPrivateLinkOut

How Monte Carlo reaches your AWS collection agent and data store privately.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account Monte Carlo collects from. | 
**principal_arn** | **str** | ARN of the IAM role Monte Carlo reaches your collection agent and data store with. | 
**private_subnet_cidrs** | **List[str]** | CIDR blocks of the private subnets Monte Carlo collects from. Allow these rather than individual private IP addresses, which AWS can change. | 
**regions** | [**List[AwsPrivateLinkRegionOut]**](AwsPrivateLinkRegionOut.md) | The regions where Monte Carlo has a VPC for collection. | 

## Example

```python
from pycarlo2.models.aws_private_link_out import AwsPrivateLinkOut

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPrivateLinkOut from a JSON string
aws_private_link_out_instance = AwsPrivateLinkOut.from_json(json)
# print the JSON string representation of the object
print(AwsPrivateLinkOut.to_json())

# convert the object into a dict
aws_private_link_out_dict = aws_private_link_out_instance.to_dict()
# create an instance of AwsPrivateLinkOut from a dict
aws_private_link_out_from_dict = AwsPrivateLinkOut.from_dict(aws_private_link_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


