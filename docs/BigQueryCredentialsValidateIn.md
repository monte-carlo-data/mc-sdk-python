# BigQueryCredentialsValidateIn

Candidate BigQuery service account credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. Used for this check and not kept. | 

## Example

```python
from pycarlo2.models.big_query_credentials_validate_in import BigQueryCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of BigQueryCredentialsValidateIn from a JSON string
big_query_credentials_validate_in_instance = BigQueryCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(BigQueryCredentialsValidateIn.to_json())

# convert the object into a dict
big_query_credentials_validate_in_dict = big_query_credentials_validate_in_instance.to_dict()
# create an instance of BigQueryCredentialsValidateIn from a dict
big_query_credentials_validate_in_from_dict = BigQueryCredentialsValidateIn.from_dict(big_query_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


