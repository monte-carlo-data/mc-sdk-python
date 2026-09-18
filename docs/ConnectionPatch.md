# ConnectionPatch

A change to an existing connection. Sent when renaming one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the connection. Omit it to leave the name unchanged. An explicit null is ignored, the same as omitting the field. | [optional] 

## Example

```python
from montecarlo.models.connection_patch import ConnectionPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPatch from a JSON string
connection_patch_instance = ConnectionPatch.from_json(json)
# print the JSON string representation of the object
print(ConnectionPatch.to_json())

# convert the object into a dict
connection_patch_dict = connection_patch_instance.to_dict()
# create an instance of ConnectionPatch from a dict
connection_patch_from_dict = ConnectionPatch.from_dict(connection_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


