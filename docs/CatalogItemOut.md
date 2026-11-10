# CatalogItemOut

A metric, or a dimension metrics can be grouped and filtered by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to use in a query. | 
**label** | **str** | A short display name. | [optional] 
**description** | **str** | What it counts or describes. | [optional] 
**requires_metric_time** | **bool** | Metrics only. True when the metric answers only grouped by &#x60;metric_time&#x60;, for example a month-to-date total. Left out for a dimension. | [optional] 
**history_start** | **date** | Metrics only. The first date the metric keeps. A query that filters &#x60;metric_time&#x60; before it is refused, so start a window on or after it. Left out for a metric that keeps all its history. | [optional] 
**longer_history** | **str** | Metrics only. A metric that keeps dates before &#x60;history_start&#x60;. Left out when there is none. | [optional] 
**format** | [**CatalogMetricFormat**](CatalogMetricFormat.md) | Metrics only. How to show the value: &#x60;percent&#x60; for a share from 0 to 1 (0.16 is 16%), &#x60;credits&#x60; or &#x60;hours&#x60;. Left out for a plain number. | [optional] 
**type** | [**CatalogDimensionType**](CatalogDimensionType.md) | Dimensions only. Left out for a metric. | [optional] 
**time_grains** | **List[str]** | Time dimensions only. The grains a query can append to the name, such as &#x60;metric_time__week&#x60; for &#x60;week&#x60;. Left out otherwise. | [optional] 

## Example

```python
from pycarlo2.models.catalog_item_out import CatalogItemOut

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogItemOut from a JSON string
catalog_item_out_instance = CatalogItemOut.from_json(json)
# print the JSON string representation of the object
print(CatalogItemOut.to_json())

# convert the object into a dict
catalog_item_out_dict = catalog_item_out_instance.to_dict()
# create an instance of CatalogItemOut from a dict
catalog_item_out_from_dict = CatalogItemOut.from_dict(catalog_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


