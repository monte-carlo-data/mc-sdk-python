# LookerCredentialsOut

Looker API credentials Monte Carlo stores. The client secret is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**base_url** | **str** | URL of the Looker API, such as https://acme.cloud.looker.com. | 
**api_client_id** | **str** | Client ID of the Looker API key. | 
**verify_ssl** | **bool** | Whether to verify Looker&#39;s TLS certificate. Verified when left out. Null unless set. | 

## Example

```python
from montecarlo.models.looker_credentials_out import LookerCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of LookerCredentialsOut from a JSON string
looker_credentials_out_instance = LookerCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(LookerCredentialsOut.to_json())

# convert the object into a dict
looker_credentials_out_dict = looker_credentials_out_instance.to_dict()
# create an instance of LookerCredentialsOut from a dict
looker_credentials_out_from_dict = LookerCredentialsOut.from_dict(looker_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


