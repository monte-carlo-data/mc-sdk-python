# DbtCloudWebhookCredentialsChangeValidateIn

A change to existing dbt Cloud webhook credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**service_token** | **str** | A dbt Cloud service token that can read the account. Stored by Monte Carlo and never returned. | [optional] 
**hmac_secret** | **str** | The webhook&#39;s HMAC secret, shown by dbt Cloud when the webhook is created. Monte Carlo checks each event&#39;s signature with it. Stored by Monte Carlo and never returned. | [optional] 
**account_id** | **str** | Your dbt Cloud account id, the number in the account&#39;s URLs. | [optional] 
**webhook_id** | **str** | Id of the dbt Cloud webhook that sends job.run.completed events to Monte Carlo. | [optional] 
**base_url** | **str** | Your dbt Cloud access URL followed by /api/v2, such as https://emea.dbt.com/api/v2. Leave it out for https://cloud.getdbt.com/api/v2. Setting it to a new URL requires sending service_token again. | [optional] 

## Example

```python
from pycarlo2.models.dbt_cloud_webhook_credentials_change_validate_in import DbtCloudWebhookCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudWebhookCredentialsChangeValidateIn from a JSON string
dbt_cloud_webhook_credentials_change_validate_in_instance = DbtCloudWebhookCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(DbtCloudWebhookCredentialsChangeValidateIn.to_json())

# convert the object into a dict
dbt_cloud_webhook_credentials_change_validate_in_dict = dbt_cloud_webhook_credentials_change_validate_in_instance.to_dict()
# create an instance of DbtCloudWebhookCredentialsChangeValidateIn from a dict
dbt_cloud_webhook_credentials_change_validate_in_from_dict = DbtCloudWebhookCredentialsChangeValidateIn.from_dict(dbt_cloud_webhook_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


