# EtlContainerIn

What to create an ETL container with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NewEtlContainerType**](NewEtlContainerType.md) | The ETL tool the container represents. Its connection has to be for this tool. Cannot be changed after the container is created. | 
**name** | **str** | Display name for the ETL container. No two containers of the same type can share a name. | 
**deployment_id** | **UUID** | The deployment the container&#39;s connection will run through. Pick one from the deployments list. Only a deployment on Monte Carlo&#39;s current collection platform is accepted. &#x60;airflow&#x60; takes none. &#x60;custom-etl-connector&#x60; takes the deployment of the agent that registered the connector, or none for a push-only connector. Every other type requires one. | [optional] 

## Example

```python
from pycarlo2.models.etl_container_in import EtlContainerIn

# TODO update the JSON string below
json = "{}"
# create an instance of EtlContainerIn from a JSON string
etl_container_in_instance = EtlContainerIn.from_json(json)
# print the JSON string representation of the object
print(EtlContainerIn.to_json())

# convert the object into a dict
etl_container_in_dict = etl_container_in_instance.to_dict()
# create an instance of EtlContainerIn from a dict
etl_container_in_from_dict = EtlContainerIn.from_dict(etl_container_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


