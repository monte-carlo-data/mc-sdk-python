# BiContainerOut

A BI container: one BI tool Monte Carlo observes, and the home of its connections.  Create the container first, then add connections to it. Deleting a container never deletes a connection; remove those first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the BI container. | 
**type** | [**BiContainerType**](BiContainerType.md) | The BI tool the container represents. Fixed once created. | 
**name** | **str** | Display name of the BI container. Null for a container that was never named. | 
**deployment_id** | **UUID** | The deployment the container&#39;s connections run through. Null for a custom BI connector&#39;s container, which has none. The id may name a deployment on Monte Carlo&#39;s older collection platform. The deployments endpoints do not list those. | 
**deployment_name** | **str** | Display name of the deployment. Null exactly when &#x60;deployment_id&#x60; is. | 
**created_time** | **datetime** | When the BI container was created. | 

## Example

```python
from montecarlo.models.bi_container_out import BiContainerOut

# TODO update the JSON string below
json = "{}"
# create an instance of BiContainerOut from a JSON string
bi_container_out_instance = BiContainerOut.from_json(json)
# print the JSON string representation of the object
print(BiContainerOut.to_json())

# convert the object into a dict
bi_container_out_dict = bi_container_out_instance.to_dict()
# create an instance of BiContainerOut from a dict
bi_container_out_from_dict = BiContainerOut.from_dict(bi_container_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


