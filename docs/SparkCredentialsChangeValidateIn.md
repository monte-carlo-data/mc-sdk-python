# SparkCredentialsChangeValidateIn

A change to existing Spark Thrift server credentials to validate before it is made.  Takes the same fields as an update, with the same rules. The stored credentials are not changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_id** | **UUID** | Deployment that runs the validations. It has to be one &#x60;GET /deployments&#x60; lists, and it has to be able to reach the system the credentials are for. | 
**host** | **str** | Host name of the Thrift server, for &#x60;binary&#x60;. Changing it requires sending &#x60;password&#x60; again when the credentials hold one. | [optional] 
**port** | **int** | Port of the Thrift server, such as &#x60;10000&#x60;, for &#x60;binary&#x60;. | [optional] 
**db_name** | **str** | Database Monte Carlo connects to, such as &#x60;default&#x60;, for &#x60;binary&#x60;. | [optional] 
**url** | **str** | URL of the Thrift server&#39;s HTTP endpoint, for &#x60;http&#x60;, such as &#x60;https://thrift.example.com:10001/cliservice&#x60;. Its path is the HTTP path. For a Databricks cluster, use &#x60;https://&lt;workspace-host&gt;:443/sql/protocolv1/o/&lt;org-id&gt;/&lt;cluster-id&gt;&#x60;, not the &#x60;jdbc:&#x60; URL. It cannot hold a user, a password, a query or a fragment. Changing it requires sending &#x60;password&#x60; again when the credentials hold one. | [optional] 
**mode** | [**SparkMode**](SparkMode.md) | How Monte Carlo reaches the Spark Thrift server. &#x60;binary&#x60; takes &#x60;host&#x60;, &#x60;port&#x60; and &#x60;db_name&#x60;. &#x60;http&#x60; takes &#x60;url&#x60; and &#x60;password&#x60;. | [optional] 
**user** | **str** | User Monte Carlo signs in as. | [optional] 
**password** | **str** | New password of &#x60;user&#x60;. | [optional] 

## Example

```python
from pycarlo2.models.spark_credentials_change_validate_in import SparkCredentialsChangeValidateIn

# TODO update the JSON string below
json = "{}"
# create an instance of SparkCredentialsChangeValidateIn from a JSON string
spark_credentials_change_validate_in_instance = SparkCredentialsChangeValidateIn.from_json(json)
# print the JSON string representation of the object
print(SparkCredentialsChangeValidateIn.to_json())

# convert the object into a dict
spark_credentials_change_validate_in_dict = spark_credentials_change_validate_in_instance.to_dict()
# create an instance of SparkCredentialsChangeValidateIn from a dict
spark_credentials_change_validate_in_from_dict = SparkCredentialsChangeValidateIn.from_dict(spark_credentials_change_validate_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


