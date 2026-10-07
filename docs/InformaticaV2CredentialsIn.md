# InformaticaV2CredentialsIn

What to create Informatica credentials with.  `auth_mode` decides what else to send. `password` takes `username` and `password`. `oauth` takes `org_id`, `oauth_client_id`, `oauth_client_secret`, `oauth_grant_type` and `oauth_access_token_endpoint`, and with the `password` grant also `oauth_username` and `oauth_password`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Informatica login URL for your POD. Leave it out for https://dm-us.informaticacloud.com. | [optional] 
**username** | **str** | Informatica user, for &#x60;password&#x60;. | [optional] 
**org_id** | **str** | Informatica organization ID, for &#x60;oauth&#x60;. | [optional] 
**oauth_client_id** | **str** | Client ID of the app registered with your identity provider, for &#x60;oauth&#x60;. | [optional] 
**oauth_grant_type** | [**OAuthGrantType**](OAuthGrantType.md) | Grant Monte Carlo requests the token with, for &#x60;oauth&#x60;. &#x60;password&#x60; also takes &#x60;oauth_username&#x60; and &#x60;oauth_password&#x60;. | [optional] 
**oauth_access_token_endpoint** | **str** | Identity provider URL Monte Carlo requests tokens from. | [optional] 
**oauth_scope** | **str** | Scope to request the token with. Leave it out to request none. | [optional] 
**oauth_username** | **str** | Identity provider user, for the &#x60;password&#x60; grant. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;password&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**oauth_client_secret** | **str** | Secret of the identity provider app, for &#x60;oauth&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**oauth_password** | **str** | Password of &#x60;oauth_username&#x60;, for the &#x60;password&#x60; grant. Stored by Monte Carlo and never returned. | [optional] 
**auth_mode** | [**InformaticaV2AuthMode**](InformaticaV2AuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. &#x60;oauth&#x60; takes &#x60;org_id&#x60; and the &#x60;oauth_*&#x60; fields. | 

## Example

```python
from pycarlo2.models.informatica_v2_credentials_in import InformaticaV2CredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of InformaticaV2CredentialsIn from a JSON string
informatica_v2_credentials_in_instance = InformaticaV2CredentialsIn.from_json(json)
# print the JSON string representation of the object
print(InformaticaV2CredentialsIn.to_json())

# convert the object into a dict
informatica_v2_credentials_in_dict = informatica_v2_credentials_in_instance.to_dict()
# create an instance of InformaticaV2CredentialsIn from a dict
informatica_v2_credentials_in_from_dict = InformaticaV2CredentialsIn.from_dict(informatica_v2_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


