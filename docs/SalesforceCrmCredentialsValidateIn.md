# SalesforceCrmCredentialsValidateIn

Candidate Salesforce CRM credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**auth_mode** | [**SalesforceCrmAuthMode**](SalesforceCrmAuthMode.md) | How Monte Carlo signs in. &#x60;password&#x60; takes &#x60;username&#x60;, &#x60;password&#x60; and &#x60;security_token&#x60;. &#x60;oauth_client_credentials&#x60; takes &#x60;consumer_key&#x60;, &#x60;consumer_secret&#x60; and &#x60;domain&#x60;. | 
**username** | **str** | Salesforce user Monte Carlo signs in as, for &#x60;password&#x60;. | [optional] 
**password** | **str** | Password of &#x60;username&#x60;, for &#x60;password&#x60;. Used for this check and not kept. | [optional] 
**security_token** | **str** | Security token of &#x60;username&#x60;, for &#x60;password&#x60;. Used for this check and not kept. | [optional] 
**consumer_key** | **str** | Consumer key of the connected app Monte Carlo signs in as, for &#x60;oauth_client_credentials&#x60;. | [optional] 
**consumer_secret** | **str** | Consumer secret of the connected app, for &#x60;oauth_client_credentials&#x60;. Used for this check and not kept. | [optional] 
**domain** | **str** | My Domain of your org, such as &#x60;acme.my.salesforce.com&#x60;, for &#x60;oauth_client_credentials&#x60;. The &#x60;.salesforce.com&#x60; suffix is optional. | [optional] 

## Example

```python
from pycarlo2.models.salesforce_crm_credentials_validate_in import SalesforceCrmCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceCrmCredentialsValidateIn from a JSON string
salesforce_crm_credentials_validate_in_instance = SalesforceCrmCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(SalesforceCrmCredentialsValidateIn.to_json())

# convert the object into a dict
salesforce_crm_credentials_validate_in_dict = salesforce_crm_credentials_validate_in_instance.to_dict()
# create an instance of SalesforceCrmCredentialsValidateIn from a dict
salesforce_crm_credentials_validate_in_from_dict = SalesforceCrmCredentialsValidateIn.from_dict(salesforce_crm_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


