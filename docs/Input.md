# Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Position to continue from, as returned in &#x60;next_cursor&#x60; by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. | [optional] 
**limit** | **int** | Maximum number of items to return, between 1 and 100. | [optional] [default to 50]
**with_count** | **bool** | Whether to also return the total number of items across every page, in &#x60;count&#x60;. Off by default: counting costs an extra query. | [optional] [default to False]

## Example

```python
from pycarlo2.models.input import Input

# TODO update the JSON string below
json = "{}"
# create an instance of Input from a JSON string
input_instance = Input.from_json(json)
# print the JSON string representation of the object
print(Input.to_json())

# convert the object into a dict
input_dict = input_instance.to_dict()
# create an instance of Input from a dict
input_from_dict = Input.from_dict(input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


