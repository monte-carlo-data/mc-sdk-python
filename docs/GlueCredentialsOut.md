# GlueCredentialsOut

The role Monte Carlo assumes to read your Glue catalog. Glue needs no secret.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. Null unless set. | 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. Null unless set. | 
**aws_region** | **str** | AWS region to call. Null means the deployment&#39;s own region. | 
**ssl_ca_data** | **str** | PEM text of a CA certificate to check the AWS endpoint&#39;s certificate against. Null unless set. | 

## Example

```python
from pycarlo2.models.glue_credentials_out import GlueCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of GlueCredentialsOut from a JSON string
glue_credentials_out_instance = GlueCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(GlueCredentialsOut.to_json())

# convert the object into a dict
glue_credentials_out_dict = glue_credentials_out_instance.to_dict()
# create an instance of GlueCredentialsOut from a dict
glue_credentials_out_from_dict = GlueCredentialsOut.from_dict(glue_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


