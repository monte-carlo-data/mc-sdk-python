# TableauCredentialsOut

Tableau credentials Monte Carlo stores. The password and the secrets are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**server_name** | **str** | URL of the Tableau server, starting with https:// or http://. | 
**site_name** | **str** | Tableau site. Null for the default site. | 
**verify_ssl** | **bool** | Whether to verify the server&#39;s TLS certificate. Verified when left out. Null unless set. | 
**username** | **str** | Tableau user. Null for a personal access token. | 
**token_name** | **str** | Name of the personal access token. Null unless the credentials use one. | 
**connected_app_client_id** | **str** | Client ID of the connected app. Null unless the credentials use one. | 
**connected_app_secret_id** | **str** | ID of the connected app&#39;s secret. Null unless the credentials use one. | 

## Example

```python
from pycarlo2.models.tableau_credentials_out import TableauCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCredentialsOut from a JSON string
tableau_credentials_out_instance = TableauCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(TableauCredentialsOut.to_json())

# convert the object into a dict
tableau_credentials_out_dict = tableau_credentials_out_instance.to_dict()
# create an instance of TableauCredentialsOut from a dict
tableau_credentials_out_from_dict = TableauCredentialsOut.from_dict(tableau_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


