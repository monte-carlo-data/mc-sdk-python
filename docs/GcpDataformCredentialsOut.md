# GcpDataformCredentialsOut

GCP Dataform credentials Monte Carlo stores. The key is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**project_id** | **str** | Google Cloud project that holds the Dataform repositories. | 
**locations** | **List[str]** | Google Cloud regions to read Dataform repositories in, such as us-central1. | 
**client_email** | **str** | Email address of the service account. | 

## Example

```python
from pycarlo2.models.gcp_dataform_credentials_out import GcpDataformCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of GcpDataformCredentialsOut from a JSON string
gcp_dataform_credentials_out_instance = GcpDataformCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(GcpDataformCredentialsOut.to_json())

# convert the object into a dict
gcp_dataform_credentials_out_dict = gcp_dataform_credentials_out_instance.to_dict()
# create an instance of GcpDataformCredentialsOut from a dict
gcp_dataform_credentials_out_from_dict = GcpDataformCredentialsOut.from_dict(gcp_dataform_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


