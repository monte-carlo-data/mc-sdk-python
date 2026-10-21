# AthenaCredentialsOut

The role Monte Carlo assumes to run Athena queries. Athena needs no secret.

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
**catalog** | **str** | Athena data catalog to query. Null means &#x60;AwsDataCatalog&#x60;. | 
**workgroup** | **str** | Athena workgroup to run queries in. Null means the &#x60;primary&#x60; workgroup. | 

## Example

```python
from pycarlo2.models.athena_credentials_out import AthenaCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of AthenaCredentialsOut from a JSON string
athena_credentials_out_instance = AthenaCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(AthenaCredentialsOut.to_json())

# convert the object into a dict
athena_credentials_out_dict = athena_credentials_out_instance.to_dict()
# create an instance of AthenaCredentialsOut from a dict
athena_credentials_out_from_dict = AthenaCredentialsOut.from_dict(athena_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


