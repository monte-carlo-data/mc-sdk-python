# CustomConnectorTerminology

The nouns an ETL connector uses for its own job, task and group tiers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | **str** | Noun for the job tier. | 
**task** | **str** | Noun for the task tier. Null if the tool has none. | 
**group** | **str** | Noun for the group tier above jobs. Null if the tool has none. | 

## Example

```python
from pycarlo2.models.custom_connector_terminology import CustomConnectorTerminology

# TODO update the JSON string below
json = "{}"
# create an instance of CustomConnectorTerminology from a JSON string
custom_connector_terminology_instance = CustomConnectorTerminology.from_json(json)
# print the JSON string representation of the object
print(CustomConnectorTerminology.to_json())

# convert the object into a dict
custom_connector_terminology_dict = custom_connector_terminology_instance.to_dict()
# create an instance of CustomConnectorTerminology from a dict
custom_connector_terminology_from_dict = CustomConnectorTerminology.from_dict(custom_connector_terminology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


