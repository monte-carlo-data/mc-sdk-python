# HostingDomainsOut

The URLs your Monte Carlo deployment serves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ui_url** | **str** | URL of the Monte Carlo web app. | 
**integrations_url** | **str** | Base URL of the integrations gateway, which receives webhooks and other inbound requests from the tools you connect. | 
**graphql_api_url** | **str** | URL of the GraphQL API, for API keys. | 
**graphql_oauth_api_url** | **str** | URL of the GraphQL API, for OAuth clients. | 
**m2m_token_url** | **str** | URL an OAuth client requests an access token from, with the client-credentials grant. Null when the deployment does not support OAuth clients. | 
**m2m_instance_scope** | **str** | Scope an OAuth client requests for its token to reach this deployment. Null when the deployment does not support OAuth clients. | 
**dbt_cloud_webhook_url** | **str** | URL to give dbt Cloud when you create the webhook that reports job runs to Monte Carlo. | 

## Example

```python
from pycarlo2.models.hosting_domains_out import HostingDomainsOut

# TODO update the JSON string below
json = "{}"
# create an instance of HostingDomainsOut from a JSON string
hosting_domains_out_instance = HostingDomainsOut.from_json(json)
# print the JSON string representation of the object
print(HostingDomainsOut.to_json())

# convert the object into a dict
hosting_domains_out_dict = hosting_domains_out_instance.to_dict()
# create an instance of HostingDomainsOut from a dict
hosting_domains_out_from_dict = HostingDomainsOut.from_dict(hosting_domains_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


