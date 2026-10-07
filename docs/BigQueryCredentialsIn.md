# BigQueryCredentialsIn

What to create BigQuery service account credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. Stored by Monte Carlo and never returned. | 

## Example

```python
from pycarlo2.models.big_query_credentials_in import BigQueryCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryCredentialsIn from a JSON string
big_query_credentials_in_instance = BigQueryCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(BigQueryCredentialsIn.to_json())

# convert the object into a dict
big_query_credentials_in_dict = big_query_credentials_in_instance.to_dict()
# create an instance of BigQueryCredentialsIn from a dict
big_query_credentials_in_from_dict = BigQueryCredentialsIn.from_dict(big_query_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


