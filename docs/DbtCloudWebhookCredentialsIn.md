# DbtCloudWebhookCredentialsIn

What to create dbt Cloud webhook credentials with.  Create the webhook in dbt Cloud first, pointing at `dbt_cloud_webhook_url` from `GET /hosting/domains`. dbt Cloud then shows its id and HMAC secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** | A dbt Cloud service token that can read the account. Stored by Monte Carlo and never returned. | 
**hmac_secret** | **str** | The webhook&#39;s HMAC secret, shown by dbt Cloud when the webhook is created. Monte Carlo checks each event&#39;s signature with it. Stored by Monte Carlo and never returned. | 
**account_id** | **str** | Your dbt Cloud account id, the number in the account&#39;s URLs. | 
**webhook_id** | **str** | Id of the dbt Cloud webhook that sends job.run.completed events to Monte Carlo. | 
**base_url** | **str** | Your dbt Cloud access URL followed by /api/v2, such as https://emea.dbt.com/api/v2. Leave it out for https://cloud.getdbt.com/api/v2. | [optional] 

## Example

```python
from pycarlo2.models.dbt_cloud_webhook_credentials_in import DbtCloudWebhookCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudWebhookCredentialsIn from a JSON string
dbt_cloud_webhook_credentials_in_instance = DbtCloudWebhookCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(DbtCloudWebhookCredentialsIn.to_json())

# convert the object into a dict
dbt_cloud_webhook_credentials_in_dict = dbt_cloud_webhook_credentials_in_instance.to_dict()
# create an instance of DbtCloudWebhookCredentialsIn from a dict
dbt_cloud_webhook_credentials_in_from_dict = DbtCloudWebhookCredentialsIn.from_dict(dbt_cloud_webhook_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


