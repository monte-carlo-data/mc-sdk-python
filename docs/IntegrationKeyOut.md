# IntegrationKeyOut

An integration key of any scope, as the list returns it.  `scope` says what the key does. At most one of the parent ids is set. All three are null when the key names no warehouse or container, several of them, or one you cannot see. A key created outside this API with no scope at all is accepted for any of your account's resources, so replace it with a scoped one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key. | 
**description** | **str** | What this key is for. | 
**created_time** | **datetime** | When the key was created. | 
**scope** | [**IntegrationKeyScope**](IntegrationKeyScope.md) | What the key lets its holder do. | 
**warehouse_id** | **UUID** | The warehouse the key is scoped to, if it is scoped to one. | [optional] 
**bi_container_id** | **UUID** | The BI container the key is scoped to, if it is scoped to one. | [optional] 
**etl_container_id** | **UUID** | The ETL container the key is scoped to, if it is scoped to one. | [optional] 

## Example

```python
from pycarlo2.models.integration_key_out import IntegrationKeyOut

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationKeyOut from a JSON string
integration_key_out_instance = IntegrationKeyOut.from_json(json)
# print the JSON string representation of the object
print(IntegrationKeyOut.to_json())

# convert the object into a dict
integration_key_out_dict = integration_key_out_instance.to_dict()
# create an instance of IntegrationKeyOut from a dict
integration_key_out_from_dict = IntegrationKeyOut.from_dict(integration_key_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


