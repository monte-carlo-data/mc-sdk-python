# MetricsQueryOut

The answer to one metrics query over your account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** | The &#x60;group_by&#x60; names, then the &#x60;metrics&#x60; names, in request order. | 
**rows** | **List[List[object]]** | One list of values per row, in &#x60;columns&#x60; order. Metric values are numbers or null. | 
**data_as_of** | **datetime** | The time the data in this answer reflects. The data is refreshed periodically, not in real time, so later changes are not in it. Null when there is no data to answer from. | 
**truncated** | **bool** | True when more rows matched than &#x60;limit&#x60;. Add filters, narrow the time range or group by fewer dimensions. Raise &#x60;limit&#x60; only up to 10,000. | 
**limit** | **int** | The most rows this answer could hold, as asked for. | 
**rows_returned** | **int** | The number of rows in &#x60;rows&#x60;. | 
**total_rows** | **int** | The number of rows the query matched, which is more than &#x60;rows_returned&#x60; when &#x60;truncated&#x60;. Null when it is not known. Use it instead of counting &#x60;rows&#x60;. | 
**warnings** | **List[str]** | Short notes on how to read the answer, such as how to narrow a truncated one. Empty when there is nothing to note. | 

## Example

```python
from pycarlo2.models.metrics_query_out import MetricsQueryOut

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsQueryOut from a JSON string
metrics_query_out_instance = MetricsQueryOut.from_json(json)
# print the JSON string representation of the object
print(MetricsQueryOut.to_json())

# convert the object into a dict
metrics_query_out_dict = metrics_query_out_instance.to_dict()
# create an instance of MetricsQueryOut from a dict
metrics_query_out_from_dict = MetricsQueryOut.from_dict(metrics_query_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


