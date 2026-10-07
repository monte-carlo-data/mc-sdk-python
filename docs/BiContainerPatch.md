# BiContainerPatch

A change to an existing BI container. Sent when renaming one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the BI container. Omit it to leave the name unchanged. An explicit null is ignored, the same as omitting the field. | [optional] 

## Example

```python
from pycarlo2.models.bi_container_patch import BiContainerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of BiContainerPatch from a JSON string
bi_container_patch_instance = BiContainerPatch.from_json(json)
# print the JSON string representation of the object
print(BiContainerPatch.to_json())

# convert the object into a dict
bi_container_patch_dict = bi_container_patch_instance.to_dict()
# create an instance of BiContainerPatch from a dict
bi_container_patch_from_dict = BiContainerPatch.from_dict(bi_container_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


