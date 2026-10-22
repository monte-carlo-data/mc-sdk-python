# SalesforceDataCloudCredentialsIn

What to create Salesforce Data Cloud credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_mode** | [**SalesforceDataCloudAuthMode**](SalesforceDataCloudAuthMode.md) | How Monte Carlo signs in. &#x60;oauth_client_credentials&#x60; takes &#x60;consumer_secret&#x60;. &#x60;jwt_bearer&#x60; takes &#x60;username&#x60; and &#x60;private_key&#x60;. Both take &#x60;domain&#x60; and &#x60;consumer_key&#x60;. | 
**domain** | **str** | My Domain host of your org, such as &#x60;acme.my.salesforce.com&#x60;. | 
**consumer_key** | **str** | Consumer key of the connected app Monte Carlo signs in as. | 
**username** | **str** | Salesforce user the JWT signs in as, for &#x60;jwt_bearer&#x60;. | [optional] 
**consumer_secret** | **str** | Consumer secret of the connected app, for &#x60;oauth_client_credentials&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**private_key** | **str** | PEM private key whose certificate is on the connected app, for &#x60;jwt_bearer&#x60;. It must be an unencrypted RSA key. Stored by Monte Carlo and never returned. | [optional] 
**dataspaces** | **List[str]** | Data spaces Monte Carlo collects metadata from. | [optional] 
**dataspace** | **str** | The one data space a query connection runs in. Once set, it can be changed but not cleared. Sending it in an update, even unchanged, moves row count collection for that data space&#39;s tables to the query connections using these credentials. | [optional] 

## Example

```python
from pycarlo2.models.salesforce_data_cloud_credentials_in import SalesforceDataCloudCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceDataCloudCredentialsIn from a JSON string
salesforce_data_cloud_credentials_in_instance = SalesforceDataCloudCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(SalesforceDataCloudCredentialsIn.to_json())

# convert the object into a dict
salesforce_data_cloud_credentials_in_dict = salesforce_data_cloud_credentials_in_instance.to_dict()
# create an instance of SalesforceDataCloudCredentialsIn from a dict
salesforce_data_cloud_credentials_in_from_dict = SalesforceDataCloudCredentialsIn.from_dict(salesforce_data_cloud_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


