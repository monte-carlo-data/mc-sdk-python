# GlueCredentialsPatch

A change to existing Glue credentials.  A field left out is unchanged. A field set to null is cleared. `assumable_role` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | [optional] 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**aws_region** | **str** | AWS region to call. Omit it to use the deployment&#39;s own region. | [optional] 
**ssl_ca_data** | **str** | PEM text of a CA certificate to check the AWS endpoint&#39;s certificate against. | [optional] 

## Example

```python
from pycarlo2.models.glue_credentials_patch import GlueCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of GlueCredentialsPatch from a JSON string
glue_credentials_patch_instance = GlueCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(GlueCredentialsPatch.to_json())

# convert the object into a dict
glue_credentials_patch_dict = glue_credentials_patch_instance.to_dict()
# create an instance of GlueCredentialsPatch from a dict
glue_credentials_patch_from_dict = GlueCredentialsPatch.from_dict(glue_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


