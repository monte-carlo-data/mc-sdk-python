# FieldErrorOut

One field of a request that failed validation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **List[str]** | Where the invalid field sits, as the path to it from the top of the request body. For example &#x60;[&#39;port&#39;]&#x60;, or &#x60;[&#39;settings&#39;, &#39;timeout&#39;]&#x60; for a field nested inside an object. | 
**code** | **str** | Machine-readable code identifying the kind of validation failure. | 
**message** | **str** | Human-readable explanation of why this field failed validation. | 
**extra** | **Dict[str, str]** | Values that parameterize &#x60;message&#x60;, for a client that renders its own text instead of showing &#x60;message&#x60; directly. Absent when there is nothing to report. | [optional] 

## Example

```python
from pycarlo2.models.field_error_out import FieldErrorOut

# TODO update the JSON string below
json = "{}"
# create an instance of FieldErrorOut from a JSON string
field_error_out_instance = FieldErrorOut.from_json(json)
# print the JSON string representation of the object
print(FieldErrorOut.to_json())

# convert the object into a dict
field_error_out_dict = field_error_out_instance.to_dict()
# create an instance of FieldErrorOut from a dict
field_error_out_from_dict = FieldErrorOut.from_dict(field_error_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


