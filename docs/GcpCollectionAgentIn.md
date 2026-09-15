# GcpCollectionAgentIn

Details Monte Carlo needs to reach a collection agent you have deployed on GCP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_key** | **str** | Credentials for &#x60;GCP_JSON_SERVICE_ACCOUNT_KEY&#x60;, as the contents of the JSON key file Google issued for the service account. Send this or &#x60;auth_headers&#x60;, never both. It replaces the stored credentials rather than merging into them. | [optional] 
**auth_headers** | [**AuthHeadersCredentialsIn**](AuthHeadersCredentialsIn.md) | Credentials for &#x60;CUSTOM_AUTH_HEADERS&#x60;. Send this or &#x60;service_account_key&#x60;, never both. It replaces the stored credentials rather than merging into them. | [optional] 
**authentication_type** | [**GcpAgentAuthenticationType**](GcpAgentAuthenticationType.md) | How Monte Carlo authenticates when it calls the agent. Send it together with the matching credentials. | 
**deployment_id** | **UUID** | Deployment to register the collection agent on. It must already hold an unregistered GCP collection agent. | 
**cloud_run_url** | **str** | URL of the Cloud Run service Monte Carlo should call. | 
**name** | **str** | Display name for the collection agent. Replaces the name it currently has. | [optional] 

## Example

```python
from montecarlo.models.gcp_collection_agent_in import GcpCollectionAgentIn

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCollectionAgentIn from a JSON string
gcp_collection_agent_in_instance = GcpCollectionAgentIn.from_json(json)
# print the JSON string representation of the object
print(GcpCollectionAgentIn.to_json())

# convert the object into a dict
gcp_collection_agent_in_dict = gcp_collection_agent_in_instance.to_dict()
# create an instance of GcpCollectionAgentIn from a dict
gcp_collection_agent_in_from_dict = GcpCollectionAgentIn.from_dict(gcp_collection_agent_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


