# AirflowCallbacksKeyIn

The Airflow ETL container a callbacks key reports to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What this key is for. Monte Carlo generates one naming the warehouse or container if you leave it out. | [optional] 
**etl_container_id** | **UUID** | The &#x60;airflow&#x60; ETL container the Airflow environment reports to. | 

## Example

```python
from pycarlo2.models.airflow_callbacks_key_in import AirflowCallbacksKeyIn

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowCallbacksKeyIn from a JSON string
airflow_callbacks_key_in_instance = AirflowCallbacksKeyIn.from_json(json)
# print the JSON string representation of the object
print(AirflowCallbacksKeyIn.to_json())

# convert the object into a dict
airflow_callbacks_key_in_dict = airflow_callbacks_key_in_instance.to_dict()
# create an instance of AirflowCallbacksKeyIn from a dict
airflow_callbacks_key_in_from_dict = AirflowCallbacksKeyIn.from_dict(airflow_callbacks_key_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


