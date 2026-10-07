# EtlContainerPatch

A change to an existing ETL container. Sent when renaming one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the ETL container. Omit it to leave the name unchanged. An explicit null is ignored, the same as omitting the field. | [optional] 

## Example

```python
from pycarlo2.models.etl_container_patch import EtlContainerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EtlContainerPatch from a JSON string
etl_container_patch_instance = EtlContainerPatch.from_json(json)
# print the JSON string representation of the object
print(EtlContainerPatch.to_json())

# convert the object into a dict
etl_container_patch_dict = etl_container_patch_instance.to_dict()
# create an instance of EtlContainerPatch from a dict
etl_container_patch_from_dict = EtlContainerPatch.from_dict(etl_container_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


