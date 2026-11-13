# HiveMySqlCredentialsPatch

A change to existing credentials for a Hive metastore on MySQL.  A field left out is unchanged. `password` set to null is unchanged. `host`, `port`, `db_name` and `user` cannot be cleared. `ssl_ca_url` set to null removes the CA and needs `password` sent again. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. Changing it requires sending the credentials&#39; secrets again. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**user** | **str** | Database user Monte Carlo logs in as. | [optional] 
**password** | **str** | New password of the database user. | [optional] 
**ssl_ca_url** | **str** | https URL of the PEM bundle of certificate authorities the MySQL server&#39;s certificate is checked against. Monte Carlo downloads it at each connection and connects over TLS. For Amazon RDS, use https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem. A value replaces any setup that read the CA from Monte Carlo storage or skipped the check. Null removes it. Changing it requires sending the credentials&#39; secrets again. | [optional] 

## Example

```python
from pycarlo2.models.hive_my_sql_credentials_patch import HiveMySqlCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of HiveMySqlCredentialsPatch from a JSON string
hive_my_sql_credentials_patch_instance = HiveMySqlCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(HiveMySqlCredentialsPatch.to_json())

# convert the object into a dict
hive_my_sql_credentials_patch_dict = hive_my_sql_credentials_patch_instance.to_dict()
# create an instance of HiveMySqlCredentialsPatch from a dict
hive_my_sql_credentials_patch_from_dict = HiveMySqlCredentialsPatch.from_dict(hive_my_sql_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


