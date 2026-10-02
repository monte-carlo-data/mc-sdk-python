# TableauCredentialsValidateIn

Candidate Tableau credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**site_name** | **str** | Tableau site to connect to. Leave it out for the default site. | [optional] 
**verify_ssl** | **bool** | Whether to verify the server&#39;s TLS certificate. Verified when left out. | [optional] 
**username** | **str** | Tableau user. Send it with &#x60;password&#x60;, or with a connected app. Not used with a personal access token. | [optional] 
**token_name** | **str** | Name of a personal access token. Send it with &#x60;token_value&#x60;. | [optional] 
**connected_app_client_id** | **str** | Client ID of a Tableau connected app. Send it with &#x60;connected_app_secret_id&#x60;, &#x60;connected_app_secret_value&#x60; and &#x60;username&#x60;. | [optional] 
**connected_app_secret_id** | **str** | ID of the connected app&#39;s secret. An identifier, not the secret itself. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;. Send this, a personal access token, or a connected app. Used for this check and not kept. | [optional] 
**token_value** | **str** | Secret of the personal access token in &#x60;token_name&#x60;. Used for this check and not kept. | [optional] 
**connected_app_secret_value** | **str** | Value of the connected app&#39;s secret in &#x60;connected_app_secret_id&#x60;. Used for this check and not kept. | [optional] 
**server_name** | **str** | URL of the Tableau server, starting with https:// or http://. | 

## Example

```python
from montecarlo.models.tableau_credentials_validate_in import TableauCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of TableauCredentialsValidateIn from a JSON string
tableau_credentials_validate_in_instance = TableauCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(TableauCredentialsValidateIn.to_json())

# convert the object into a dict
tableau_credentials_validate_in_dict = tableau_credentials_validate_in_instance.to_dict()
# create an instance of TableauCredentialsValidateIn from a dict
tableau_credentials_validate_in_from_dict = TableauCredentialsValidateIn.from_dict(tableau_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


