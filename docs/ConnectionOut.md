# ConnectionOut

A connection: what Monte Carlo reaches one of a warehouse's, a BI container's or an ETL container's systems with.  A connection belongs to a warehouse, a BI container or an ETL container, and reads its secret from a credentials row. Deleting it leaves both in place.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the connection. | 
**connection_type** | **str** | What the connection reaches, such as &#x60;snowflake&#x60;. Taken from the credentials the connection was created with, and fixed once created. | 
**name** | **str** | Display name of the connection. Null for a connection that was never named. | 
**warehouse_id** | **UUID** | The warehouse the connection belongs to. Null for a connection on a BI or ETL container. Fixed once created. | 
**warehouse_name** | **str** | Display name of that warehouse. Null for a warehouse that was never named, and for a connection on a BI or ETL container. | 
**bi_container_id** | **UUID** | The BI container the connection belongs to. Null for a connection on a warehouse or an ETL container. Fixed once created. | 
**bi_container_name** | **str** | Display name of that BI container. Null for a container that was never named, and for a connection on a warehouse or an ETL container. | 
**etl_container_id** | **UUID** | The ETL container the connection belongs to. Fixed once created for a connection on an ETL container. A warehouse or BI connection has one while it collects ETL jobs through a container of its own, such as Snowflake Tasks, a Databricks metastore or Power BI dataflows, and it changes when that is turned on or off. Null otherwise. | 
**etl_container_name** | **str** | Display name of that ETL container. Null when there is no ETL container. | 
**deployment_id** | **UUID** | The deployment the connection runs through, taken from its warehouse, BI container or ETL container. Null when that has no deployment, as an Airflow ETL container has none. The id may name a deployment on Monte Carlo&#39;s older collection platform, which the deployments endpoints do not list. | 
**deployment_name** | **str** | Display name of that deployment. Null when there is no deployment to name. | 
**credentials_id** | **UUID** | The credentials the connection reads with. Null for a connection created before credentials became their own resource, and for one created outside this API. | 
**credentials_storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where that secret lives. Null when there are no credentials to describe. | 
**job_types** | **List[str]** | The jobs Monte Carlo runs on this connection, such as &#x60;metadata&#x60;. | 
**created_time** | **datetime** | When the connection was created. | 

## Example

```python
from pycarlo2.models.connection_out import ConnectionOut

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionOut from a JSON string
connection_out_instance = ConnectionOut.from_json(json)
# print the JSON string representation of the object
print(ConnectionOut.to_json())

# convert the object into a dict
connection_out_dict = connection_out_instance.to_dict()
# create an instance of ConnectionOut from a dict
connection_out_from_dict = ConnectionOut.from_dict(connection_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


