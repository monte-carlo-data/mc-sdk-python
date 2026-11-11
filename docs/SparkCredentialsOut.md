# SparkCredentialsOut

Spark Thrift server credentials Monte Carlo stores. The password is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**mode** | [**SparkMode**](SparkMode.md) | How Monte Carlo reaches the Spark Thrift server. &#x60;binary&#x60; takes &#x60;host&#x60;, &#x60;port&#x60; and &#x60;db_name&#x60;. &#x60;http&#x60; takes &#x60;url&#x60; and &#x60;password&#x60;. | 
**host** | **str** | Host name of the Thrift server, for &#x60;binary&#x60;. Null for &#x60;http&#x60;. | 
**port** | **int** | Port of the Thrift server, such as &#x60;10000&#x60;, for &#x60;binary&#x60;. Null for &#x60;http&#x60;. | 
**db_name** | **str** | Database Monte Carlo connects to, such as &#x60;default&#x60;, for &#x60;binary&#x60;. Null for &#x60;http&#x60;. | 
**url** | **str** | URL of the Thrift server&#39;s HTTP endpoint, for &#x60;http&#x60;, such as &#x60;https://thrift.example.com:10001/cliservice&#x60;. Its path is the HTTP path. For a Databricks cluster, use &#x60;https://&lt;workspace-host&gt;:443/sql/protocolv1/o/&lt;org-id&gt;/&lt;cluster-id&gt;&#x60;, not the &#x60;jdbc:&#x60; URL. It cannot hold a user, a password, a query or a fragment. Null for &#x60;binary&#x60;. | 
**user** | **str** | User Monte Carlo signs in as. | 

## Example

```python
from pycarlo2.models.spark_credentials_out import SparkCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SparkCredentialsOut from a JSON string
spark_credentials_out_instance = SparkCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SparkCredentialsOut.to_json())

# convert the object into a dict
spark_credentials_out_dict = spark_credentials_out_instance.to_dict()
# create an instance of SparkCredentialsOut from a dict
spark_credentials_out_from_dict = SparkCredentialsOut.from_dict(spark_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


