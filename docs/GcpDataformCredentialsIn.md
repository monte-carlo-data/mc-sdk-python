# GcpDataformCredentialsIn

What to create GCP Dataform credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Google Cloud project that holds the Dataform repositories. | 
**locations** | **List[str]** | Google Cloud regions to read Dataform repositories in, such as us-central1. | 
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. It needs Dataform API access. Stored by Monte Carlo and never returned. | 

## Example

```python
from pycarlo2.models.gcp_dataform_credentials_in import GcpDataformCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDataformCredentialsIn from a JSON string
gcp_dataform_credentials_in_instance = GcpDataformCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(GcpDataformCredentialsIn.to_json())

# convert the object into a dict
gcp_dataform_credentials_in_dict = gcp_dataform_credentials_in_instance.to_dict()
# create an instance of GcpDataformCredentialsIn from a dict
gcp_dataform_credentials_in_from_dict = GcpDataformCredentialsIn.from_dict(gcp_dataform_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


