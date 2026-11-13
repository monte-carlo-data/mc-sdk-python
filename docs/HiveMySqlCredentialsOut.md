# HiveMySqlCredentialsOut

Credentials for a Hive metastore on MySQL that Monte Carlo stores. The password is never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the database endpoint. | 
**port** | **int** | Port the database listens on. | 
**db_name** | **str** | MySQL database that holds the Hive metastore. | 
**user** | **str** | Database user Monte Carlo logs in as. | 
**ssl_ca_url** | **str** | https URL of the PEM bundle of certificate authorities the MySQL server&#39;s certificate is checked against. Monte Carlo downloads it at each connection and connects over TLS. For Amazon RDS, use https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem. Null when none is set, or when the stored CA is not fetched from a URL and checked, as when it was set up to read from Monte Carlo storage or to skip the check. Setting &#x60;ssl_ca_url&#x60; replaces such a setup. | 

## Example

```python
from pycarlo2.models.hive_my_sql_credentials_out import HiveMySqlCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of HiveMySqlCredentialsOut from a JSON string
hive_my_sql_credentials_out_instance = HiveMySqlCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(HiveMySqlCredentialsOut.to_json())

# convert the object into a dict
hive_my_sql_credentials_out_dict = hive_my_sql_credentials_out_instance.to_dict()
# create an instance of HiveMySqlCredentialsOut from a dict
hive_my_sql_credentials_out_from_dict = HiveMySqlCredentialsOut.from_dict(hive_my_sql_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


