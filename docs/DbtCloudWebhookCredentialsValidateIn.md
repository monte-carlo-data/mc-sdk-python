# DbtCloudWebhookCredentialsValidateIn

Candidate dbt Cloud webhook credentials to validate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**service_token** | **str** | A dbt Cloud service token that can read the account. Used for this check and not kept. | 
**hmac_secret** | **str** | The webhook&#39;s HMAC secret, shown by dbt Cloud when the webhook is created. Monte Carlo checks each event&#39;s signature with it. Used for this check and not kept. | 
**account_id** | **str** | Your dbt Cloud account id, the number in the account&#39;s URLs. | 
**webhook_id** | **str** | Id of the dbt Cloud webhook that sends job.run.completed events to Monte Carlo. | 
**base_url** | **str** | Your dbt Cloud access URL followed by /api/v2, such as https://emea.dbt.com/api/v2. Leave it out for https://cloud.getdbt.com/api/v2. | [optional] 

## Example

```python
from pycarlo2.models.dbt_cloud_webhook_credentials_validate_in import DbtCloudWebhookCredentialsValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudWebhookCredentialsValidateIn from a JSON string
dbt_cloud_webhook_credentials_validate_in_instance = DbtCloudWebhookCredentialsValidateIn.from_json(json)
# print the JSON string representation of the object
print(DbtCloudWebhookCredentialsValidateIn.to_json())

# convert the object into a dict
dbt_cloud_webhook_credentials_validate_in_dict = dbt_cloud_webhook_credentials_validate_in_instance.to_dict()
# create an instance of DbtCloudWebhookCredentialsValidateIn from a dict
dbt_cloud_webhook_credentials_validate_in_from_dict = DbtCloudWebhookCredentialsValidateIn.from_dict(dbt_cloud_webhook_credentials_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


