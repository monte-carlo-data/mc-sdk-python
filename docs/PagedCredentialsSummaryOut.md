# PagedCredentialsSummaryOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[CredentialsSummaryOut]**](CredentialsSummaryOut.md) | The items on this page, in the list&#39;s sort order. | 
**next_cursor** | **str** | Pass this as &#x60;cursor&#x60; to fetch the next page. Null when this is the last page. | 
**has_more** | **bool** | Whether there are more items after this page. | 
**count** | **int** | Total number of items across every page. Only returned when the request set &#x60;with_count&#x3D;true&#x60;; null otherwise. | 

## Example

```python
from montecarlo.models.paged_credentials_summary_out import PagedCredentialsSummaryOut

# TODO update the JSON string below
json = "{}"
# create an instance of PagedCredentialsSummaryOut from a JSON string
paged_credentials_summary_out_instance = PagedCredentialsSummaryOut.from_json(json)
# print the JSON string representation of the object
print(PagedCredentialsSummaryOut.to_json())

# convert the object into a dict
paged_credentials_summary_out_dict = paged_credentials_summary_out_instance.to_dict()
# create an instance of PagedCredentialsSummaryOut from a dict
paged_credentials_summary_out_from_dict = PagedCredentialsSummaryOut.from_dict(paged_credentials_summary_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


