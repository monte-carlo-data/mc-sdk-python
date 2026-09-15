# StorageServicePrincipalCredentialsIn

The service principal Monte Carlo authenticates to the storage account as.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Directory (tenant) id the service principal lives in. | 
**client_id** | **str** | Application (client) id of the service principal. | 
**client_secret** | **str** | Client secret of the service principal. | 
**account_url** | **str** | URL of the storage account Monte Carlo sends requests to. A private endpoint or a custom host works, so this is not required to be under &#x60;blob.core.windows.net&#x60;. | 
**account_name** | **str** | Name of the storage account, needed only when &#x60;account_url&#x60; does not start with it. Monte Carlo takes the first label of the host otherwise, which is right for a standard or private-link URL but not for a custom ingress host. | [optional] 

## Example

```python
from montecarlo.models.storage_service_principal_credentials_in import StorageServicePrincipalCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of StorageServicePrincipalCredentialsIn from a JSON string
storage_service_principal_credentials_in_instance = StorageServicePrincipalCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(StorageServicePrincipalCredentialsIn.to_json())

# convert the object into a dict
storage_service_principal_credentials_in_dict = storage_service_principal_credentials_in_instance.to_dict()
# create an instance of StorageServicePrincipalCredentialsIn from a dict
storage_service_principal_credentials_in_from_dict = StorageServicePrincipalCredentialsIn.from_dict(storage_service_principal_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


