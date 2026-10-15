# GcpDataformCredentialsChangeValidateIn

A change to existing GCP Dataform credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**project_id** | **str** | Google Cloud project that holds the Dataform repositories. | [optional] 
**locations** | **List[str]** | Google Cloud regions to read Dataform repositories in, such as us-central1. | [optional] 
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. It needs Dataform API access. Stored by Monte Carlo and never returned. | [optional] 

## Example

```python
from pycarlo2.models.gcp_dataform_credentials_change_validate_in import GcpDataformCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDataformCredentialsChangeValidateIn from a JSON string
gcp_dataform_credentials_change_validate_in_instance = GcpDataformCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(GcpDataformCredentialsChangeValidateIn.to_json())

# convert the object into a dict
gcp_dataform_credentials_change_validate_in_dict = gcp_dataform_credentials_change_validate_in_instance.to_dict()
# create an instance of GcpDataformCredentialsChangeValidateIn from a dict
gcp_dataform_credentials_change_validate_in_from_dict = GcpDataformCredentialsChangeValidateIn.from_dict(gcp_dataform_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


