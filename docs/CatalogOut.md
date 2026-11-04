# CatalogOut

The metrics you can query, or the dimensions every one of the chosen metrics shares.  Exactly one of the two lists is present. Fields without a value are left out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[CatalogItemOut]**](CatalogItemOut.md) | Every metric you can query. Left out when metrics were chosen. | [optional] 
**dimensions** | [**List[CatalogItemOut]**](CatalogItemOut.md) | The dimensions you can group and filter all of the chosen metrics by. Left out when no metrics were chosen. | [optional] 

## Example

```python
from pycarlo2.models.catalog_out import CatalogOut

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogOut from a JSON string
catalog_out_instance = CatalogOut.from_json(json)
# print the JSON string representation of the object
print(CatalogOut.to_json())

# convert the object into a dict
catalog_out_dict = catalog_out_instance.to_dict()
# create an instance of CatalogOut from a dict
catalog_out_from_dict = CatalogOut.from_dict(catalog_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


