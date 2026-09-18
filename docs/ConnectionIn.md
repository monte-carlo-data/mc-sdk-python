# ConnectionIn

What to create a connection with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the connection. Unique among the warehouse&#39;s connections. | 
**warehouse_id** | **UUID** | The warehouse to add the connection to. Its type has to match what the credentials are for. | 
**credentials_id** | **UUID** | The credentials the connection reads with. They also decide the connection&#39;s type. Create them first, through one of the credentials endpoints. | 
**job_types** | **List[str]** | The jobs to run on this connection. Omit it to run what the connection type runs by default, which is what the app does. Which values are accepted depends on the connection type. An empty list is not accepted; omit the field to take the defaults. | [optional] 

## Example

```python
from montecarlo.models.connection_in import ConnectionIn

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


