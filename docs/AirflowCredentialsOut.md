# AirflowCredentialsOut

The Airflow environment's connection details. Airflow needs no secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host_name** | **str** | Host name of the Airflow web server, as Airflow reports it to Monte Carlo. | 

## Example

```python
from pycarlo2.models.airflow_credentials_out import AirflowCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowCredentialsOut from a JSON string
airflow_credentials_out_instance = AirflowCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(AirflowCredentialsOut.to_json())

# convert the object into a dict
airflow_credentials_out_dict = airflow_credentials_out_instance.to_dict()
# create an instance of AirflowCredentialsOut from a dict
airflow_credentials_out_from_dict = AirflowCredentialsOut.from_dict(airflow_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


