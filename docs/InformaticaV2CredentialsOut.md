# InformaticaV2CredentialsOut

Informatica credentials Monte Carlo stores. The passwords and the client secret are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**auth_mode** | [**InformaticaV2AuthMode**](InformaticaV2AuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60; and &#x60;password&#x60;. &#x60;oauth&#x60; takes &#x60;org_id&#x60; and the &#x60;oauth_*&#x60; fields. | 
**base_url** | **str** | Informatica login URL for your POD. Leave it out for https://dm-us.informaticacloud.com. Null unless set. | 
**username** | **str** | Informatica user. Null unless &#x60;auth_mode&#x60; is password. | 
**org_id** | **str** | Informatica organization ID. Null unless &#x60;auth_mode&#x60; is oauth. | 
**oauth_client_id** | **str** | Client ID of the identity provider app. Null unless &#x60;auth_mode&#x60; is oauth. | 
**oauth_grant_type** | [**OAuthGrantType**](OAuthGrantType.md) | Grant Monte Carlo requests the token with. Null unless &#x60;auth_mode&#x60; is oauth. | 
**oauth_access_token_endpoint** | **str** | Identity provider URL Monte Carlo requests tokens from. Null unless &#x60;auth_mode&#x60; is oauth. | 
**oauth_scope** | **str** | Scope the token is requested with. Null unless set. | 
**oauth_username** | **str** | Identity provider user. Null unless the grant is password. | 

## Example

```python
from pycarlo2.models.informatica_v2_credentials_out import InformaticaV2CredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of InformaticaV2CredentialsOut from a JSON string
informatica_v2_credentials_out_instance = InformaticaV2CredentialsOut.from_json(json)
# print the JSON string representation of the object
print(InformaticaV2CredentialsOut.to_json())

# convert the object into a dict
informatica_v2_credentials_out_dict = informatica_v2_credentials_out_instance.to_dict()
# create an instance of InformaticaV2CredentialsOut from a dict
informatica_v2_credentials_out_from_dict = InformaticaV2CredentialsOut.from_dict(informatica_v2_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


