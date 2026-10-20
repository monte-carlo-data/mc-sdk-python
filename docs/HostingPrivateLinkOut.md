# HostingPrivateLinkOut

The private connectivity details of one region of your Monte Carlo instance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**AwsPrivateLinkOut**](AwsPrivateLinkOut.md) | AWS private connectivity. Null when the region has none. | 

## Example

```python
from pycarlo2.models.hosting_private_link_out import HostingPrivateLinkOut

# TODO update the JSON string below
json = "{}"
# create an instance of HostingPrivateLinkOut from a JSON string
hosting_private_link_out_instance = HostingPrivateLinkOut.from_json(json)
# print the JSON string representation of the object
print(HostingPrivateLinkOut.to_json())

# convert the object into a dict
hosting_private_link_out_dict = hosting_private_link_out_instance.to_dict()
# create an instance of HostingPrivateLinkOut from a dict
hosting_private_link_out_from_dict = HostingPrivateLinkOut.from_dict(hosting_private_link_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


