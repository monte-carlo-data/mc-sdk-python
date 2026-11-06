# DocsOut

Pages of the Analytics API docs: every page without its body, or the one page asked for with it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pages** | [**List[DocPageOut]**](DocPageOut.md) | The pages. | 

## Example

```python
from pycarlo2.models.docs_out import DocsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DocsOut from a JSON string
docs_out_instance = DocsOut.from_json(json)
# print the JSON string representation of the object
print(DocsOut.to_json())

# convert the object into a dict
docs_out_dict = docs_out_instance.to_dict()
# create an instance of DocsOut from a dict
docs_out_from_dict = DocsOut.from_dict(docs_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


