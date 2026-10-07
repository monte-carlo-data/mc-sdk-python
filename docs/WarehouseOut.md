# WarehouseOut

A warehouse: a data platform Monte Carlo observes, and the home of its connections.  Create the warehouse first, then add connections to it. Deleting a warehouse never deletes a connection; remove those first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the warehouse. | 
**name** | **str** | Display name of the warehouse. Null for a warehouse that was never named. | 
**type** | [**WarehouseType**](WarehouseType.md) | The kind of data platform the warehouse represents. Fixed once created. | 
**deployment_id** | **UUID** | The deployment the warehouse&#39;s connections run through. Null for a warehouse that has no deployment. The id may name a deployment on Monte Carlo&#39;s older collection platform. The deployments endpoints do not list those. | 
**created_time** | **datetime** | When the warehouse was created. | 

## Example

```python
from pycarlo2.models.warehouse_out import WarehouseOut

# TODO update the JSON string below
json = "{}"
# create an instance of WarehouseOut from a JSON string
warehouse_out_instance = WarehouseOut.from_json(json)
# print the JSON string representation of the object
print(WarehouseOut.to_json())

# convert the object into a dict
warehouse_out_dict = warehouse_out_instance.to_dict()
# create an instance of WarehouseOut from a dict
warehouse_out_from_dict = WarehouseOut.from_dict(warehouse_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


