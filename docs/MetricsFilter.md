# MetricsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | A dimension name from the catalog. | 
**op** | [**MetricsFilterOperator**](MetricsFilterOperator.md) | &#x60;in&#x60;, &#x60;not_in&#x60;: any of the values. &#x60;not_in&#x60; also keeps rows where the dimension is empty. &#x60;gte&#x60;, &#x60;lte&#x60;, &#x60;gt&#x60;, &#x60;lt&#x60;: compare with one value and never match an empty dimension. &#x60;contains&#x60;: one text, matched anywhere in the value, ignoring case. &#x60;is_null&#x60;: one boolean, &#x60;true&#x60; for rows where the dimension is empty and &#x60;false&#x60; for rows where it is not. The text &#x60;true&#x60; or &#x60;false&#x60; works too. | 
**values** | **List[object]** | The values to compare with. A date is an ISO string, such as &#x60;2026-10-01&#x60;. | 

## Example

```python
from pycarlo2.models.metrics_filter import MetricsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsFilter from a JSON string
metrics_filter_instance = MetricsFilter.from_json(json)
# print the JSON string representation of the object
print(MetricsFilter.to_json())

# convert the object into a dict
metrics_filter_dict = metrics_filter_instance.to_dict()
# create an instance of MetricsFilter from a dict
metrics_filter_from_dict = MetricsFilter.from_dict(metrics_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


