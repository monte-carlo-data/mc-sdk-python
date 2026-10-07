# GcpDataformCredentialsValidateIn

Candidate GCP Dataform credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**project_id** | **str** | Google Cloud project that holds the Dataform repositories. | 
**locations** | **List[str]** | Google Cloud regions to read Dataform repositories in, such as us-central1. | 
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. It needs Dataform API access. Used for this check and not kept. | 

## Example

```python
from pycarlo2.models.gcp_dataform_credentials_validate_in import GcpDataformCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDataformCredentialsValidateIn from a JSON string
gcp_dataform_credentials_validate_in_instance = GcpDataformCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(GcpDataformCredentialsValidateIn.to_json())

# convert the object into a dict
gcp_dataform_credentials_validate_in_dict = gcp_dataform_credentials_validate_in_instance.to_dict()
# create an instance of GcpDataformCredentialsValidateIn from a dict
gcp_dataform_credentials_validate_in_from_dict = GcpDataformCredentialsValidateIn.from_dict(gcp_dataform_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


