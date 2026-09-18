# PagedConnectionOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ConnectionOut]**](ConnectionOut.md) | The items on this page, in the list&#39;s sort order. | 
**next_cursor** | **str** | Pass this as &#x60;cursor&#x60; to fetch the next page. Null when this is the last page. | 
**has_more** | **bool** | Whether there are more items after this page. | 
**count** | **int** | Total number of items across every page. Only returned when the request set &#x60;with_count&#x3D;true&#x60;; null otherwise. | 

## Example

```python
from montecarlo.models.paged_connection_out import PagedConnectionOut

# TODO update the JSON string below
json = "{}"
# create an instance of PagedConnectionOut from a JSON string
paged_connection_out_instance = PagedConnectionOut.from_json(json)
# print the JSON string representation of the object
print(PagedConnectionOut.to_json())

# convert the object into a dict
paged_connection_out_dict = paged_connection_out_instance.to_dict()
# create an instance of PagedConnectionOut from a dict
paged_connection_out_from_dict = PagedConnectionOut.from_dict(paged_connection_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


