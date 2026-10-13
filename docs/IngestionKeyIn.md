# IngestionKeyIn

The warehouse or container an ingestion key pushes to. Send exactly one of the three.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What this key is for. Monte Carlo generates one naming the warehouse or container if you leave it out. | [optional] 
**warehouse_id** | **UUID** | The warehouse to push metadata, lineage and query logs to. Send exactly one of this, &#x60;bi_container_id&#x60; and &#x60;etl_container_id&#x60;. | [optional] 
**bi_container_id** | **UUID** | The BI container to push BI assets to, such as a &#x60;custom-bi-connector&#x60; container. Send exactly one of this, &#x60;warehouse_id&#x60; and &#x60;etl_container_id&#x60;. | [optional] 
**etl_container_id** | **UUID** | The ETL container to push ETL jobs and runs to, such as a &#x60;custom-etl-connector&#x60; container. Send exactly one of this, &#x60;warehouse_id&#x60; and &#x60;bi_container_id&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.ingestion_key_in import IngestionKeyIn

# TODO update the JSON string below
json = "{}"
# create an instance of IngestionKeyIn from a JSON string
ingestion_key_in_instance = IngestionKeyIn.from_json(json)
# print the JSON string representation of the object
print(IngestionKeyIn.to_json())

# convert the object into a dict
ingestion_key_in_dict = ingestion_key_in_instance.to_dict()
# create an instance of IngestionKeyIn from a dict
ingestion_key_in_from_dict = IngestionKeyIn.from_dict(ingestion_key_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


