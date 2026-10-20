# HostingNetworkOut

The public IP addresses one region of your Monte Carlo instance connects from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ip_addresses** | **List[str]** | Addresses Monte Carlo collects from, such as when it reaches your warehouse, collection agent or data store over the internet. | 
**saas_ip_addresses** | **List[str]** | Addresses the rest of the Monte Carlo platform connects from. | 
**webhook_ip_addresses** | **List[str]** | Addresses Monte Carlo sends webhook notifications from. | 
**data_platform_ip_addresses** | **List[str]** | Addresses Monte Carlo&#39;s data processing services connect from. | 

## Example

```python
from pycarlo2.models.hosting_network_out import HostingNetworkOut

# TODO update the JSON string below
json = "{}"
# create an instance of HostingNetworkOut from a JSON string
hosting_network_out_instance = HostingNetworkOut.from_json(json)
# print the JSON string representation of the object
print(HostingNetworkOut.to_json())

# convert the object into a dict
hosting_network_out_dict = hosting_network_out_instance.to_dict()
# create an instance of HostingNetworkOut from a dict
hosting_network_out_from_dict = HostingNetworkOut.from_dict(hosting_network_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


