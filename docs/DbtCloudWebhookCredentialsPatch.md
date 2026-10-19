# DbtCloudWebhookCredentialsPatch

A change to existing dbt Cloud webhook credentials.  A field left out is unchanged. `base_url` set to null is cleared. `service_token` and `hmac_secret` set to null are unchanged. Sending an empty body returns the credentials as they are. A new `account_id`, `webhook_id` or `hmac_secret` takes effect on the connection using the credentials at once. Update the webhook in dbt Cloud first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_token** | **str** | A dbt Cloud service token that can read the account. Stored by Monte Carlo and never returned. | [optional] 
**hmac_secret** | **str** | The webhook&#39;s HMAC secret, shown by dbt Cloud when the webhook is created. Monte Carlo checks each event&#39;s signature with it. Stored by Monte Carlo and never returned. | [optional] 
**account_id** | **str** | Your dbt Cloud account id, the number in the account&#39;s URLs. | [optional] 
**webhook_id** | **str** | Id of the dbt Cloud webhook that sends job.run.completed events to Monte Carlo. | [optional] 
**base_url** | **str** | Your dbt Cloud access URL followed by /api/v2, such as https://emea.dbt.com/api/v2. Leave it out for https://cloud.getdbt.com/api/v2. Setting it to a new URL requires sending service_token again. | [optional] 

## Example

```python
from pycarlo2.models.dbt_cloud_webhook_credentials_patch import DbtCloudWebhookCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudWebhookCredentialsPatch from a JSON string
dbt_cloud_webhook_credentials_patch_instance = DbtCloudWebhookCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(DbtCloudWebhookCredentialsPatch.to_json())

# convert the object into a dict
dbt_cloud_webhook_credentials_patch_dict = dbt_cloud_webhook_credentials_patch_instance.to_dict()
# create an instance of DbtCloudWebhookCredentialsPatch from a dict
dbt_cloud_webhook_credentials_patch_from_dict = DbtCloudWebhookCredentialsPatch.from_dict(dbt_cloud_webhook_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


