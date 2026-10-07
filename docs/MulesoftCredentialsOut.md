# MulesoftCredentialsOut

MuleSoft Anypoint credentials Monte Carlo stores. The client secret is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**app_client_id** | **str** | Client ID of the Anypoint connected app. The app needs the View Environment, Read Deployments and Exchange Viewer scopes. | 
**region** | [**MulesoftRegion**](MulesoftRegion.md) | Anypoint Platform instance the organization lives on. | 
**org_id** | **str** | Anypoint organization or business group to collect from. Set it when your Mule applications are deployed in a business group. Leave it out to collect the organization that owns the connected app. Null unless set. | 

## Example

```python
from pycarlo2.models.mulesoft_credentials_out import MulesoftCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of MulesoftCredentialsOut from a JSON string
mulesoft_credentials_out_instance = MulesoftCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(MulesoftCredentialsOut.to_json())

# convert the object into a dict
mulesoft_credentials_out_dict = mulesoft_credentials_out_instance.to_dict()
# create an instance of MulesoftCredentialsOut from a dict
mulesoft_credentials_out_from_dict = MulesoftCredentialsOut.from_dict(mulesoft_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


