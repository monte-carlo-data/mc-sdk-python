# WarehousePatch

A change to an existing warehouse. Sent when renaming one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the warehouse. Omit it to leave the name unchanged. An explicit null is ignored, the same as omitting the field. | [optional] 

## Example

```python
from montecarlo.models.warehouse_patch import WarehousePatch

# TODO update the JSON string below
json = "{}"
# create an instance of WarehousePatch from a JSON string
warehouse_patch_instance = WarehousePatch.from_json(json)
# print the JSON string representation of the object
print(WarehousePatch.to_json())

# convert the object into a dict
warehouse_patch_dict = warehouse_patch_instance.to_dict()
# create an instance of WarehousePatch from a dict
warehouse_patch_from_dict = WarehousePatch.from_dict(warehouse_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


