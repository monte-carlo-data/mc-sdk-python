# EtlContainerOut

An ETL container: one ETL tool Monte Carlo observes, and the home of its connection.  Create the container first, then add a connection to it. Deleting a container never deletes its connection; remove that first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the ETL container. | 
**type** | [**EtlContainerType**](EtlContainerType.md) | The ETL tool the container represents. Fixed once created. | 
**name** | **str** | Display name of the ETL container. | 
**is_synthetic** | **bool** | True for a container this API does not create or delete. Most belong to another connection, such as a warehouse or BI connection, and go away with it. | 
**deployment_id** | **UUID** | The deployment the container&#39;s connection runs through. Null for a type that runs on none, such as &#x60;airflow&#x60;. The id may name a deployment on Monte Carlo&#39;s older collection platform. The deployments endpoints do not list those. | 
**deployment_name** | **str** | Display name of the deployment. Null exactly when &#x60;deployment_id&#x60; is. | 
**created_time** | **datetime** | When the ETL container was created. | 

## Example

```python
from pycarlo2.models.etl_container_out import EtlContainerOut

# TODO update the JSON string below
json = "{}"
# create an instance of EtlContainerOut from a JSON string
etl_container_out_instance = EtlContainerOut.from_json(json)
# print the JSON string representation of the object
print(EtlContainerOut.to_json())

# convert the object into a dict
etl_container_out_dict = etl_container_out_instance.to_dict()
# create an instance of EtlContainerOut from a dict
etl_container_out_from_dict = EtlContainerOut.from_dict(etl_container_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


