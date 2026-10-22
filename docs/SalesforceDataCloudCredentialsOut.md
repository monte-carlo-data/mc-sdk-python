# SalesforceDataCloudCredentialsOut

Salesforce Data Cloud credentials Monte Carlo stores. The consumer secret and the private key are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**auth_mode** | [**SalesforceDataCloudAuthMode**](SalesforceDataCloudAuthMode.md) | How Monte Carlo signs in. &#x60;oauth_client_credentials&#x60; takes &#x60;consumer_secret&#x60;. &#x60;jwt_bearer&#x60; takes &#x60;username&#x60; and &#x60;private_key&#x60;. Both take &#x60;domain&#x60; and &#x60;consumer_key&#x60;. | 
**domain** | **str** | My Domain host of your org, such as &#x60;acme.my.salesforce.com&#x60;. | 
**consumer_key** | **str** | Consumer key of the connected app Monte Carlo signs in as. | 
**username** | **str** | Salesforce user the JWT signs in as, for &#x60;jwt_bearer&#x60;. | 
**dataspaces** | **List[str]** | Data spaces Monte Carlo collects metadata from. | 
**dataspace** | **str** | The one data space a query connection runs in. Once set, it can be changed but not cleared. Sending it in an update, even unchanged, moves row count collection for that data space&#39;s tables to the query connections using these credentials. | 

## Example

```python
from pycarlo2.models.salesforce_data_cloud_credentials_out import SalesforceDataCloudCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceDataCloudCredentialsOut from a JSON string
salesforce_data_cloud_credentials_out_instance = SalesforceDataCloudCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SalesforceDataCloudCredentialsOut.to_json())

# convert the object into a dict
salesforce_data_cloud_credentials_out_dict = salesforce_data_cloud_credentials_out_instance.to_dict()
# create an instance of SalesforceDataCloudCredentialsOut from a dict
salesforce_data_cloud_credentials_out_from_dict = SalesforceDataCloudCredentialsOut.from_dict(salesforce_data_cloud_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


