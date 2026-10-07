# BiContainerIn

What to create a BI container with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NewBiContainerType**](NewBiContainerType.md) | The BI tool the container represents. Every connection added to it has to be for this tool. Cannot be changed after the container is created. | 
**name** | **str** | Display name for the BI container. | 
**deployment_id** | **UUID** | The deployment the container&#39;s connections will run through. Pick one from the deployments list. Only a deployment on Monte Carlo&#39;s current collection platform is accepted. | 

## Example

```python
from pycarlo2.models.bi_container_in import BiContainerIn

# TODO update the JSON string below
json = "{}"
# create an instance of BiContainerIn from a JSON string
bi_container_in_instance = BiContainerIn.from_json(json)
# print the JSON string representation of the object
print(BiContainerIn.to_json())

# convert the object into a dict
bi_container_in_dict = bi_container_in_instance.to_dict()
# create an instance of BiContainerIn from a dict
bi_container_in_from_dict = BiContainerIn.from_dict(bi_container_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


