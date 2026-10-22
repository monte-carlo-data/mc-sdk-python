# SalesforceCrmCredentialsOut

Salesforce CRM credentials Monte Carlo stores. The password, the security token and the consumer secret are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**auth_mode** | [**SalesforceCrmAuthMode**](SalesforceCrmAuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60;, &#x60;password&#x60; and &#x60;security_token&#x60;. &#x60;oauth_client_credentials&#x60; takes &#x60;consumer_key&#x60;, &#x60;consumer_secret&#x60; and &#x60;domain&#x60;. | 
**username** | **str** | Salesforce user Monte Carlo signs in as, for &#x60;password&#x60;. | 
**consumer_key** | **str** | Consumer key of the connected app Monte Carlo signs in as, for &#x60;oauth_client_credentials&#x60;. | 
**domain** | **str** | My Domain of your org, such as &#x60;acme.my.salesforce.com&#x60;, for &#x60;oauth_client_credentials&#x60;. The &#x60;.salesforce.com&#x60; suffix is optional. | 

## Example

```python
from pycarlo2.models.salesforce_crm_credentials_out import SalesforceCrmCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceCrmCredentialsOut from a JSON string
salesforce_crm_credentials_out_instance = SalesforceCrmCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SalesforceCrmCredentialsOut.to_json())

# convert the object into a dict
salesforce_crm_credentials_out_dict = salesforce_crm_credentials_out_instance.to_dict()
# create an instance of SalesforceCrmCredentialsOut from a dict
salesforce_crm_credentials_out_from_dict = SalesforceCrmCredentialsOut.from_dict(salesforce_crm_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


