# AirflowCallbacksKeyOut

A key an Airflow environment reports its DAG and task runs with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key. | 
**description** | **str** | What this key is for. | 
**created_time** | **datetime** | When the key was created. | 
**etl_container_id** | **UUID** | The Airflow ETL container the key reports to. Null when the key names no warehouse or container, several of them, or one you cannot see. A key created outside this API with no scope at all is accepted for any of your account&#39;s resources, so replace it with a scoped one. | [optional] 
**mcd_id** | **str** | Key id to present, as the &#x60;x-mcd-id&#x60; header or a client&#39;s &#x60;mcd_id&#x60; setting. The same value as &#x60;id&#x60;. | 

## Example

```python
from pycarlo2.models.airflow_callbacks_key_out import AirflowCallbacksKeyOut

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowCallbacksKeyOut from a JSON string
airflow_callbacks_key_out_instance = AirflowCallbacksKeyOut.from_json(json)
# print the JSON string representation of the object
print(AirflowCallbacksKeyOut.to_json())

# convert the object into a dict
airflow_callbacks_key_out_dict = airflow_callbacks_key_out_instance.to_dict()
# create an instance of AirflowCallbacksKeyOut from a dict
airflow_callbacks_key_out_from_dict = AirflowCallbacksKeyOut.from_dict(airflow_callbacks_key_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


