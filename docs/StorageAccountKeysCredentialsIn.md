# StorageAccountKeysCredentialsIn

The connection string Monte Carlo uses to reach the storage account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_string** | **str** | Connection string for the storage account holding the container. It carries the account key, so treat it as a secret. | 

## Example

```python
from montecarlo.models.storage_account_keys_credentials_in import StorageAccountKeysCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of StorageAccountKeysCredentialsIn from a JSON string
storage_account_keys_credentials_in_instance = StorageAccountKeysCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(StorageAccountKeysCredentialsIn.to_json())

# convert the object into a dict
storage_account_keys_credentials_in_dict = storage_account_keys_credentials_in_instance.to_dict()
# create an instance of StorageAccountKeysCredentialsIn from a dict
storage_account_keys_credentials_in_from_dict = StorageAccountKeysCredentialsIn.from_dict(storage_account_keys_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


