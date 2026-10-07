# ConnectionIn

What to create a connection with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the connection. Unique among the connections of its warehouse or BI container. | 
**warehouse_id** | **UUID** | The warehouse to add the connection to. Its type has to match what the credentials are for. Send this or &#x60;bi_container_id&#x60;, not both. | [optional] 
**bi_container_id** | **UUID** | The BI container to add the connection to, for Tableau, Looker or Power BI credentials. Its type has to match what the credentials are for: a &#x60;looker&#x60; container takes both &#x60;looker&#x60; and &#x60;looker-git-clone&#x60; credentials. Send this or &#x60;warehouse_id&#x60;, not both. | [optional] 
**credentials_id** | **UUID** | The credentials the connection reads with. They also decide the connection&#39;s type. Create them first, through one of the credentials endpoints. | 
**job_types** | **List[str]** | The jobs to run on this connection. Omit it to run what the connection type runs by default, which is what the app does. Which values are accepted depends on the connection type. An empty list is not accepted; omit the field to take the defaults. | [optional] 

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


