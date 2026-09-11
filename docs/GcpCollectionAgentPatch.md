# GcpCollectionAgentPatch

Details to change on a GCP collection agent. Only what you send is changed.  Credentials are the exception: they replace the stored credentials instead of merging into them, so send them in full along with the matching `authentication_type`. Sending only `name` skips the checks against your Cloud Run service, since a name is not validated against it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_headers** | [**AuthHeadersCredentialsIn**](AuthHeadersCredentialsIn.md) | Credentials for &#x60;CUSTOM_AUTH_HEADERS&#x60;. Send this or &#x60;service_account_key&#x60;, never both. It replaces the stored credentials rather than merging into them. | [optional] 
**authentication_type** | [**GcpAgentAuthenticationType**](GcpAgentAuthenticationType.md) | How Monte Carlo authenticates when it calls the agent. Send it together with the matching credentials. | [optional] 
**cloud_run_url** | **str** | URL of the Cloud Run service Monte Carlo should call. | [optional] 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 
**service_account_key** | **str** | Credentials for &#x60;GCP_JSON_SERVICE_ACCOUNT_KEY&#x60;, as the contents of the JSON key file Google issued for the service account. Send this or &#x60;auth_headers&#x60;, never both. It replaces the stored credentials rather than merging into them. | [optional] 

## Example

```python
from montecarlo.models.gcp_collection_agent_patch import GcpCollectionAgentPatch

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionAgentPatch from a JSON string
gcp_collection_agent_patch_instance = GcpCollectionAgentPatch.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionAgentPatch.to_json())

# convert the object into a dict
gcp_collection_agent_patch_dict = gcp_collection_agent_patch_instance.to_dict()
# create an instance of GcpCollectionAgentPatch from a dict
gcp_collection_agent_patch_from_dict = GcpCollectionAgentPatch.from_dict(gcp_collection_agent_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


