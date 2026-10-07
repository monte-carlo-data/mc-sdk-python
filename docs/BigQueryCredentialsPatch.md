# BigQueryCredentialsPatch

A change to existing BigQuery credentials.  A new `service_account_key` replaces the stored key whole. Left out or null, the key is unchanged. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_key** | **str** | New JSON key file, as its text. Replaces the stored key whole. | [optional] 

## Example

```python
from pycarlo2.models.big_query_credentials_patch import BigQueryCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryCredentialsPatch from a JSON string
big_query_credentials_patch_instance = BigQueryCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(BigQueryCredentialsPatch.to_json())

# convert the object into a dict
big_query_credentials_patch_dict = big_query_credentials_patch_instance.to_dict()
# create an instance of BigQueryCredentialsPatch from a dict
big_query_credentials_patch_from_dict = BigQueryCredentialsPatch.from_dict(big_query_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


