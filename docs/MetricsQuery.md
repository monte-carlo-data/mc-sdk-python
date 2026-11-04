# MetricsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | **List[str]** | Metric names from the catalog. | 
**group_by** | **List[str]** | Dimension names from the catalog, such as &#x60;metric_time__week&#x60;. | [optional] 
**filters** | [**List[MetricsFilter]**](MetricsFilter.md) | Conditions every counted row must meet, all of them. | [optional] 
**order_by** | [**List[MetricsOrderBy]**](MetricsOrderBy.md) | How to sort the rows, by requested names. | [optional] 
**limit** | **int** | The most rows to return. The default is 1,000 and the most is 10,000. | [optional] [default to 1000]

## Example

```python
from pycarlo2.models.metrics_query import MetricsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsQuery from a JSON string
metrics_query_instance = MetricsQuery.from_json(json)
# print the JSON string representation of the object
print(MetricsQuery.to_json())

# convert the object into a dict
metrics_query_dict = metrics_query_instance.to_dict()
# create an instance of MetricsQuery from a dict
metrics_query_from_dict = MetricsQuery.from_dict(metrics_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


