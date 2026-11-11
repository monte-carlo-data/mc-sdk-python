# SparkCredentialsIn

What to create Spark Thrift server credentials with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host name of the Thrift server, for &#x60;binary&#x60;. | [optional] 
**port** | **int** | Port of the Thrift server, such as &#x60;10000&#x60;, for &#x60;binary&#x60;. | [optional] 
**db_name** | **str** | Database Monte Carlo connects to, such as &#x60;default&#x60;, for &#x60;binary&#x60;. | [optional] 
**url** | **str** | URL of the Thrift server&#39;s HTTP endpoint, for &#x60;http&#x60;, such as &#x60;https://thrift.example.com:10001/cliservice&#x60;. Its path is the HTTP path. For a Databricks cluster, use &#x60;https://&lt;workspace-host&gt;:443/sql/protocolv1/o/&lt;org-id&gt;/&lt;cluster-id&gt;&#x60;, not the &#x60;jdbc:&#x60; URL. It cannot hold a user, a password, a query or a fragment. | [optional] 
**mode** | [**SparkMode**](SparkMode.md) | How Monte Carlo reaches the Spark Thrift server. &#x60;binary&#x60; takes &#x60;host&#x60;, &#x60;port&#x60; and &#x60;db_name&#x60;. &#x60;http&#x60; takes &#x60;url&#x60; and &#x60;password&#x60;. | 
**user** | **str** | User Monte Carlo signs in as. | 
**password** | **str** | Password of &#x60;user&#x60;. &#x60;http&#x60; needs one. &#x60;binary&#x60; does not send it to the server, so it is optional there. Stored by Monte Carlo and never returned. | [optional] 

## Example

```python
from pycarlo2.models.spark_credentials_in import SparkCredentialsIn

# TODO update the JSON string below
json = "{}"
# create an instance of SparkCredentialsIn from a JSON string
spark_credentials_in_instance = SparkCredentialsIn.from_json(json)
# print the JSON string representation of the object
print(SparkCredentialsIn.to_json())

# convert the object into a dict
spark_credentials_in_dict = spark_credentials_in_instance.to_dict()
# create an instance of SparkCredentialsIn from a dict
spark_credentials_in_from_dict = SparkCredentialsIn.from_dict(spark_credentials_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


