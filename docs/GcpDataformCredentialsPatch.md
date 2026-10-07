# GcpDataformCredentialsPatch

A change to existing GCP Dataform credentials.  A field left out is unchanged. `service_account_key` set to null is unchanged. `project_id` and `locations` cannot be cleared. A new `locations` replaces the stored list, and a new `service_account_key` replaces the stored key whole. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Google Cloud project that holds the Dataform repositories. | [optional] 
**locations** | **List[str]** | Google Cloud regions to read Dataform repositories in, such as us-central1. | [optional] 
**service_account_key** | **str** | The service account&#39;s JSON key file, as its text. It needs Dataform API access. Stored by Monte Carlo and never returned. | [optional] 

## Example

```python
from pycarlo2.models.gcp_dataform_credentials_patch import GcpDataformCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDataformCredentialsPatch from a JSON string
gcp_dataform_credentials_patch_instance = GcpDataformCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(GcpDataformCredentialsPatch.to_json())

# convert the object into a dict
gcp_dataform_credentials_patch_dict = gcp_dataform_credentials_patch_instance.to_dict()
# create an instance of GcpDataformCredentialsPatch from a dict
gcp_dataform_credentials_patch_from_dict = GcpDataformCredentialsPatch.from_dict(gcp_dataform_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


