# AirflowCredentialsIn

What to create Airflow connection details with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Host name of the Airflow web server, as Airflow reports it to Monte Carlo. | 

## Example

```python
from pycarlo2.models.airflow_credentials_in import AirflowCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowCredentialsIn from a JSON string
airflow_credentials_in_instance = AirflowCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AirflowCredentialsIn.to_json())

# convert the object into a dict
airflow_credentials_in_dict = airflow_credentials_in_instance.to_dict()
# create an instance of AirflowCredentialsIn from a dict
airflow_credentials_in_from_dict = AirflowCredentialsIn.from_dict(airflow_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


