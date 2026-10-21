# GlueCredentialsChangeValidateIn

A change to existing Glue credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | [optional] 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**aws_region** | **str** | AWS region to call. Omit it to use the deployment&#39;s own region. | [optional] 
**ssl_ca_data** | **str** | PEM text of a CA certificate to check the AWS endpoint&#39;s certificate against. | [optional] 

## Example

```python
from pycarlo2.models.glue_credentials_change_validate_in import GlueCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of GlueCredentialsChangeValidateIn from a JSON string
glue_credentials_change_validate_in_instance = GlueCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(GlueCredentialsChangeValidateIn.to_json())

# convert the object into a dict
glue_credentials_change_validate_in_dict = glue_credentials_change_validate_in_instance.to_dict()
# create an instance of GlueCredentialsChangeValidateIn from a dict
glue_credentials_change_validate_in_from_dict = GlueCredentialsChangeValidateIn.from_dict(glue_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


