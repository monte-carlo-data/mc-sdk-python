# FivetranCredentialsOut

Fivetran API credentials Monte Carlo stores. The key and its secret are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**base_url** | **str** | URL of the Fivetran REST API. Leave it out for https://api.fivetran.com/v1/. Null unless set. | 

## Example

```python
from pycarlo2.models.fivetran_credentials_out import FivetranCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of FivetranCredentialsOut from a JSON string
fivetran_credentials_out_instance = FivetranCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(FivetranCredentialsOut.to_json())

# convert the object into a dict
fivetran_credentials_out_dict = fivetran_credentials_out_instance.to_dict()
# create an instance of FivetranCredentialsOut from a dict
fivetran_credentials_out_from_dict = FivetranCredentialsOut.from_dict(fivetran_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


