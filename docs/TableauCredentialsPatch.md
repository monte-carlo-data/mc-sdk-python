# TableauCredentialsPatch

A change to existing Tableau credentials.  A field left out is unchanged. `site_name` and `verify_ssl` set to null are cleared. A secret set to null is unchanged. `server_name` cannot be cleared, and neither can `username` while the credentials sign in with a password or a connected app, which need one. Sending a field of another way to sign in drops the stored one: a personal access token drops the username too. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_name** | **str** | Tableau site to connect to. Leave it out for the default site. | [optional] 
**verify_ssl** | **bool** | Whether to verify the server&#39;s TLS certificate. Verified when left out. | [optional] 
**username** | **str** | Tableau user. Send it with &#x60;password&#x60;, or with a connected app. Not used with a personal access token. | [optional] 
**token_name** | **str** | Name of a personal access token. Send it with &#x60;token_value&#x60;. | [optional] 
**connected_app_client_id** | **str** | Client ID of a Tableau connected app. Send it with &#x60;connected_app_secret_id&#x60;, &#x60;connected_app_secret_value&#x60; and &#x60;username&#x60;. | [optional] 
**connected_app_secret_id** | **str** | ID of the connected app&#39;s secret. An identifier, not the secret itself. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;. Send this, a personal access token, or a connected app. Stored by Monte Carlo and never returned. | [optional] 
**token_value** | **str** | Secret of the personal access token in &#x60;token_name&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**connected_app_secret_value** | **str** | Value of the connected app&#39;s secret in &#x60;connected_app_secret_id&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**server_name** | **str** | URL of the Tableau server, starting with https:// or http://. | [optional] 

## Example

```python
from pycarlo2.models.tableau_credentials_patch import TableauCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCredentialsPatch from a JSON string
tableau_credentials_patch_instance = TableauCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(TableauCredentialsPatch.to_json())

# convert the object into a dict
tableau_credentials_patch_dict = tableau_credentials_patch_instance.to_dict()
# create an instance of TableauCredentialsPatch from a dict
tableau_credentials_patch_from_dict = TableauCredentialsPatch.from_dict(tableau_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


