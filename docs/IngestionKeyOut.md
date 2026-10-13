# IngestionKeyOut

A key that pushes data to the one warehouse or container it is scoped to.  Exactly one of `warehouse_id`, `bi_container_id` and `etl_container_id` is set for a key created through this API. None is set when the key names no warehouse or container, several of them, or one you cannot see. A key created outside this API with no scope at all is accepted for any of your account's resources, so replace it with a scoped one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key. | 
**description** | **str** | What this key is for. | 
**created_time** | **datetime** | When the key was created. | 
**warehouse_id** | **UUID** | The warehouse the key pushes metadata, lineage and query logs to. Null when the key is scoped to a container. | [optional] 
**bi_container_id** | **UUID** | The BI container the key pushes BI assets to. Null when the key is scoped to something else. | [optional] 
**etl_container_id** | **UUID** | The ETL container the key pushes ETL jobs and runs to. Null when the key is scoped to something else. | [optional] 
**mcd_id** | **str** | Key id to present, as the &#x60;x-mcd-id&#x60; header or a client&#39;s &#x60;mcd_id&#x60; setting. The same value as &#x60;id&#x60;. | 

## Example

```python
from pycarlo2.models.ingestion_key_out import IngestionKeyOut

# TODO update the JSON string below
json = "{}"
# create an instance of IngestionKeyOut from a JSON string
ingestion_key_out_instance = IngestionKeyOut.from_json(json)
# print the JSON string representation of the object
print(IngestionKeyOut.to_json())

# convert the object into a dict
ingestion_key_out_dict = ingestion_key_out_instance.to_dict()
# create an instance of IngestionKeyOut from a dict
ingestion_key_out_from_dict = IngestionKeyOut.from_dict(ingestion_key_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


