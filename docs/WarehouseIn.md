# WarehouseIn

What to create a warehouse with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the warehouse. Unique among your warehouses of the same type. | 
**type** | [**WarehouseType**](WarehouseType.md) | The kind of data platform the warehouse represents. Every connection added to it has to fit. Cannot be changed after the warehouse is created. Send this or &#x60;connection_type&#x60;, not both. | [optional] 
**connection_type** | **str** | The type of the first connection you plan to add. The warehouse type is taken from it and returned as &#x60;type&#x60;. Send this or &#x60;type&#x60;, not both. A connection type no warehouse type can be taken from is refused, custom connectors included. So is one this account does not have. | [optional] 
**deployment_id** | **UUID** | The deployment the warehouse&#39;s connections will run through. Pick one from the deployments list. Only a deployment on Monte Carlo&#39;s current collection platform is accepted. | 

## Example

```python
from montecarlo.models.warehouse_in import WarehouseIn

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseIn from a JSON string
warehouse_in_instance = WarehouseIn.from_json(json)
# print the JSON string representation of the object
print(WarehouseIn.to_json())

# convert the object into a dict
warehouse_in_dict = warehouse_in_instance.to_dict()
# create an instance of WarehouseIn from a dict
warehouse_in_from_dict = WarehouseIn.from_dict(warehouse_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


