# AthenaCredentialsIn

What to create Athena credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assumable_role** | **str** | ARN of the IAM role in your AWS account that the deployment assumes. | 
**external_id** | **str** | External id your role&#39;s trust policy requires, if it requires one. It is not the deployment&#39;s &#x60;aws_external_id&#x60;. | [optional] 
**aws_region** | **str** | AWS region to call. Omit it to use the deployment&#39;s own region. | [optional] 
**catalog** | **str** | Athena data catalog to query. Omit it to use &#x60;AwsDataCatalog&#x60;. | [optional] 
**workgroup** | **str** | Athena workgroup to run queries in. Omit it to use the &#x60;primary&#x60; workgroup. The role needs permission to start queries in it. | [optional] 

## Example

```python
from pycarlo2.models.athena_credentials_in import AthenaCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of AthenaCredentialsIn from a JSON string
athena_credentials_in_instance = AthenaCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(AthenaCredentialsIn.to_json())

# convert the object into a dict
athena_credentials_in_dict = athena_credentials_in_instance.to_dict()
# create an instance of AthenaCredentialsIn from a dict
athena_credentials_in_from_dict = AthenaCredentialsIn.from_dict(athena_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


