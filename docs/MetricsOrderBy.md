# MetricsOrderBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | A requested metric or dimension. | 
**descending** | **bool** | Sort from the largest value down. | [optional] [default to False]

## Example

```python
from pycarlo2.models.metrics_order_by import MetricsOrderBy

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsOrderBy from a JSON string
metrics_order_by_instance = MetricsOrderBy.from_json(json)
# print the JSON string representation of the object
print(MetricsOrderBy.to_json())

# convert the object into a dict
metrics_order_by_dict = metrics_order_by_instance.to_dict()
# create an instance of MetricsOrderBy from a dict
metrics_order_by_from_dict = MetricsOrderBy.from_dict(metrics_order_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


