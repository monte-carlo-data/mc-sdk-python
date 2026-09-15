# PagedWarehouseOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[WarehouseOut]**](WarehouseOut.md) | The items on this page, in the list&#39;s sort order. | 
**next_cursor** | **str** | Pass this as &#x60;cursor&#x60; to fetch the next page. Null when this is the last page. | 
**has_more** | **bool** | Whether there are more items after this page. | 
**count** | **int** | Total number of items across every page. Only returned when the request set &#x60;with_count&#x3D;true&#x60;; null otherwise. | 

## Example

```python
from montecarlo.models.paged_warehouse_out import PagedWarehouseOut

# TODO update the JSON string below
json = "{}"
# create an instance of PagedWarehouseOut from a JSON string
paged_warehouse_out_instance = PagedWarehouseOut.from_json(json)
# print the JSON string representation of the object
print(PagedWarehouseOut.to_json())

# convert the object into a dict
paged_warehouse_out_dict = paged_warehouse_out_instance.to_dict()
# create an instance of PagedWarehouseOut from a dict
paged_warehouse_out_from_dict = PagedWarehouseOut.from_dict(paged_warehouse_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


