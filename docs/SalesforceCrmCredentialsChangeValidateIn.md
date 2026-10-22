# SalesforceCrmCredentialsChangeValidateIn

A change to existing Salesforce CRM credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**auth_mode** | [**SalesforceCrmAuthMode**](SalesforceCrmAuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60;, &#x60;password&#x60; and &#x60;security_token&#x60;. &#x60;oauth_client_credentials&#x60; takes &#x60;consumer_key&#x60;, &#x60;consumer_secret&#x60; and &#x60;domain&#x60;. | [optional] 
**username** | **str** | Salesforce user Monte Carlo signs in as, for &#x60;password&#x60;. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;password&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**security_token** | **str** | Security token of &#x60;username&#x60;, for &#x60;password&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**consumer_key** | **str** | Consumer key of the connected app Monte Carlo signs in as, for &#x60;oauth_client_credentials&#x60;. | [optional] 
**consumer_secret** | **str** | Consumer secret of the connected app, for &#x60;oauth_client_credentials&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**domain** | **str** | My Domain of your org, such as &#x60;acme.my.salesforce.com&#x60;, for &#x60;oauth_client_credentials&#x60;. The &#x60;.salesforce.com&#x60; suffix is optional. Changing it requires sending the credentials&#39; secrets again. | [optional] 

## Example

```python
from pycarlo2.models.salesforce_crm_credentials_change_validate_in import SalesforceCrmCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceCrmCredentialsChangeValidateIn from a JSON string
salesforce_crm_credentials_change_validate_in_instance = SalesforceCrmCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(SalesforceCrmCredentialsChangeValidateIn.to_json())

# convert the object into a dict
salesforce_crm_credentials_change_validate_in_dict = salesforce_crm_credentials_change_validate_in_instance.to_dict()
# create an instance of SalesforceCrmCredentialsChangeValidateIn from a dict
salesforce_crm_credentials_change_validate_in_from_dict = SalesforceCrmCredentialsChangeValidateIn.from_dict(salesforce_crm_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


