# AirflowCredentialsPatch

A change to existing Airflow connection details.  `host_name` cannot be cleared. Sending an empty body returns the details as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | Host name of the Airflow web server, as Airflow reports it to Monte Carlo. | [optional] 

## Example

```python
from pycarlo2.models.airflow_credentials_patch import AirflowCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AirflowCredentialsPatch from a JSON string
airflow_credentials_patch_instance = AirflowCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AirflowCredentialsPatch.to_json())

# convert the object into a dict
airflow_credentials_patch_dict = airflow_credentials_patch_instance.to_dict()
# create an instance of AirflowCredentialsPatch from a dict
airflow_credentials_patch_from_dict = AirflowCredentialsPatch.from_dict(airflow_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


