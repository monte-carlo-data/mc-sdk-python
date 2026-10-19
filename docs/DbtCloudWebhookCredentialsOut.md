# DbtCloudWebhookCredentialsOut

dbt Cloud webhook credentials Monte Carlo stores. The service token and the HMAC secret are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**account_id** | **str** | Your dbt Cloud account id, the number in the account&#39;s URLs. | 
**webhook_id** | **str** | Id of the dbt Cloud webhook that sends job.run.completed events to Monte Carlo. | 
**base_url** | **str** | Your dbt Cloud access URL followed by /api/v2. Null means https://cloud.getdbt.com/api/v2. | 

## Example

```python
from pycarlo2.models.dbt_cloud_webhook_credentials_out import DbtCloudWebhookCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudWebhookCredentialsOut from a JSON string
dbt_cloud_webhook_credentials_out_instance = DbtCloudWebhookCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(DbtCloudWebhookCredentialsOut.to_json())

# convert the object into a dict
dbt_cloud_webhook_credentials_out_dict = dbt_cloud_webhook_credentials_out_instance.to_dict()
# create an instance of DbtCloudWebhookCredentialsOut from a dict
dbt_cloud_webhook_credentials_out_from_dict = DbtCloudWebhookCredentialsOut.from_dict(dbt_cloud_webhook_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


