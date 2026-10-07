# InformaticaV2CredentialsValidateIn

Candidate Informatica credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**base_url** | **str** | Informatica login URL for your POD. Leave it out for https://dm-us.informaticacloud.com. | [optional] 
**username** | **str** | Informatica user, for &#x60;password&#x60;. | [optional] 
**org_id** | **str** | Informatica organization ID, for &#x60;oauth&#x60;. | [optional] 
**oauth_client_id** | **str** | Client ID of the app registered with your identity provider, for &#x60;oauth&#x60;. | [optional] 
**oauth_grant_type** | [**OAuthGrantType**](OAuthGrantType.md) | Grant Monte Carlo requests the token with, for &#x60;oauth&#x60;. &#x60;password&#x60; also takes &#x60;oauth_username&#x60; and &#x60;oauth_password&#x60;. | [optional] 
**oauth_access_token_endpoint** | **str** | Identity provider URL Monte Carlo requests tokens from. | [optional] 
**oauth_scope** | **str** | Scope to request the token with. Leave it out to request none. | [optional] 
**oauth_username** | **str** | Identity provider user, for the &#x60;password&#x60; grant. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;password&#x60;. Used for this check and not kept. | [optional] 
**oauth_client_secret** | **str** | Secret of the identity provider app, for &#x60;oauth&#x60;. Used for this check and not kept. | [optional] 
**oauth_password** | **str** | Password of &#x60;oauth_username&#x60;, for the &#x60;password&#x60; grant. Used for this check and not kept. | [optional] 
**auth_mode** | [**InformaticaV2AuthMode**](InformaticaV2AuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. &#x60;oauth&#x60; takes &#x60;org_id&#x60; and the &#x60;oauth_*&#x60; fields. | 

## Example

```python
from pycarlo2.models.informatica_v2_credentials_validate_in import InformaticaV2CredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of InformaticaV2CredentialsValidateIn from a JSON string
informatica_v2_credentials_validate_in_instance = InformaticaV2CredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(InformaticaV2CredentialsValidateIn.to_json())

# convert the object into a dict
informatica_v2_credentials_validate_in_dict = informatica_v2_credentials_validate_in_instance.to_dict()
# create an instance of InformaticaV2CredentialsValidateIn from a dict
informatica_v2_credentials_validate_in_from_dict = InformaticaV2CredentialsValidateIn.from_dict(informatica_v2_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


