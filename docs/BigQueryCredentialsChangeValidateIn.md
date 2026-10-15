# BigQueryCredentialsChangeValidateIn

A change to existing BigQuery credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**service_account_key** | **str** | New JSON key file, as its text. Replaces the stored key whole. | [optional] 

## Example

```python
from pycarlo2.models.big_query_credentials_change_validate_in import BigQueryCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryCredentialsChangeValidateIn from a JSON string
big_query_credentials_change_validate_in_instance = BigQueryCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(BigQueryCredentialsChangeValidateIn.to_json())

# convert the object into a dict
big_query_credentials_change_validate_in_dict = big_query_credentials_change_validate_in_instance.to_dict()
# create an instance of BigQueryCredentialsChangeValidateIn from a dict
big_query_credentials_change_validate_in_from_dict = BigQueryCredentialsChangeValidateIn.from_dict(big_query_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


