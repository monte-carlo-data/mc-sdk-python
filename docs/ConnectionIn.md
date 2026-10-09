# ConnectionIn

What to create a connection with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the connection. Unique among the connections of its warehouse or BI container. An ETL container holds one connection. | 
**warehouse_id** | **UUID** | The warehouse to add the connection to. Its type has to match what the credentials are for. Send exactly one of this, &#x60;bi_container_id&#x60; and &#x60;etl_container_id&#x60;. | [optional] 
**bi_container_id** | **UUID** | The BI container to add the connection to, for Tableau, Looker or Power BI credentials. Its type has to match what the credentials are for: a &#x60;looker&#x60; container takes both &#x60;looker&#x60; and &#x60;looker-git-clone&#x60; credentials. Send exactly one of this, &#x60;warehouse_id&#x60; and &#x60;etl_container_id&#x60;. | [optional] 
**etl_container_id** | **UUID** | The ETL container to add the connection to, for ETL tool credentials such as Fivetran or Airflow. The container&#39;s type has to equal the credentials&#39; type, and the container must not have a connection yet. A &#x60;custom-etl-connector&#x60; container takes a custom ETL connector&#39;s credentials, or none when it has no deployment. Send exactly one of this, &#x60;warehouse_id&#x60; and &#x60;bi_container_id&#x60;. | [optional] 
**credentials_id** | **UUID** | The credentials the connection reads with. They also decide the connection&#39;s type. Create them first, through one of the credentials endpoints. Required, except on a push-only ETL container: a &#x60;custom-etl-connector&#x60; container with no deployment. Its connection takes no credentials, and has the container&#39;s type. | [optional] 
**job_types** | **List[str]** | The jobs to run on this connection. Omit it to run what the connection type runs by default, which is what the app does. Which values are accepted depends on the connection type. &#x60;etl&#x60; on a Snowflake, Power BI or Salesforce Data Cloud connection also creates its ETL container. An empty list is not accepted; omit the field to take the defaults. | [optional] 

## Example

```python
from pycarlo2.models.connection_in import ConnectionIn

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionIn from a JSON string
connection_in_instance = ConnectionIn.from_json(json)
# print the JSON string representation of the object
print(ConnectionIn.to_json())

# convert the object into a dict
connection_in_dict = connection_in_instance.to_dict()
# create an instance of ConnectionIn from a dict
connection_in_from_dict = ConnectionIn.from_dict(connection_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


