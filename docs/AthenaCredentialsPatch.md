# AthenaCredentialsPatch

A change to existing Athena credentials.  A field left out is unchanged. A field set to null is cleared. `assumable_role` cannot be cleared. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | [optional] 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**aws_region** | **str** | AWS region to call. Omit it to use the deployment&#39;s own region. | [optional] 
**catalog** | **str** | Athena data catalog to query. Omit it to use &#x60;AwsDataCatalog&#x60;. | [optional] 
**workgroup** | **str** | Athena workgroup to run queries in. Omit it to use the &#x60;primary&#x60; workgroup. The role needs permission to start queries in it. | [optional] 

## Example

```python
from pycarlo2.models.athena_credentials_patch import AthenaCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of AthenaCredentialsPatch from a JSON string
athena_credentials_patch_instance = AthenaCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(AthenaCredentialsPatch.to_json())

# convert the object into a dict
athena_credentials_patch_dict = athena_credentials_patch_instance.to_dict()
# create an instance of AthenaCredentialsPatch from a dict
athena_credentials_patch_from_dict = AthenaCredentialsPatch.from_dict(athena_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


