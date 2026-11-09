# DocPageOut

A page of the Analytics API docs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** | The page&#39;s id. Ask for it with &#x60;slug&#x60; to get its body. | 
**title** | **str** | The page title. | 
**summary** | **str** | One line on what the page covers. | [optional] 
**parent** | **str** | The slug of the page it sits under. | [optional] 
**body** | **str** | The page as Markdown. Set only when one page was asked for. &#x60;doc:&lt;slug&gt;&#x60; links name other pages. | [optional] 
**prompt** | **str** | A dashboard example&#39;s prompt: send it to an agent to build that dashboard. | [optional] 

## Example

```python
from pycarlo2.models.doc_page_out import DocPageOut

# TODO update the JSON string below
json = "{}"
# create an instance of DocPageOut from a JSON string
doc_page_out_instance = DocPageOut.from_json(json)
# print the JSON string representation of the object
print(DocPageOut.to_json())

# convert the object into a dict
doc_page_out_dict = doc_page_out_instance.to_dict()
# create an instance of DocPageOut from a dict
doc_page_out_from_dict = DocPageOut.from_dict(doc_page_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


