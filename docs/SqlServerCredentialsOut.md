# SqlServerCredentialsOut

SQL Server credentials Monte Carlo stores. The password and the keytab are never returned.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the credentials. | 
**connection_type** | **str** | The connection type the credentials are for, such as &#x60;snowflake&#x60;. Fixed once created. | 
**storage_type** | [**CredentialsStorageType**](CredentialsStorageType.md) | Where the secret lives. Fixed once created. | 
**created_time** | **datetime** | When the credentials were created. | 
**host** | **str** | Hostname of the database endpoint. For &#x60;kerberos&#x60;, the fully qualified name the server&#39;s service principal is registered under. | 
**port** | **int** | Port the database listens on. | 
**db_name** | **str** | Database to connect to. Null when none is set. | 
**auth_mode** | [**SqlServerAuthMode**](SqlServerAuthMode.md) | How Monte Carlo signs in. &#x60;sql&#x60; takes &#x60;user&#x60; and &#x60;password&#x60;. &#x60;kerberos&#x60; takes &#x60;realm&#x60;, &#x60;kdc&#x60;, &#x60;principal&#x60;, and one of &#x60;keytab_base64&#x60; or &#x60;password&#x60;. | 
**user** | **str** | SQL login Monte Carlo signs in as, for &#x60;sql&#x60;. Null for &#x60;kerberos&#x60;. | 
**realm** | **str** | Kerberos realm, normally the Active Directory domain in capitals, for &#x60;kerberos&#x60;. Null for &#x60;sql&#x60;. | 
**kdc** | **str** | Hostname of the key distribution center, optionally with &#x60;:port&#x60;, for &#x60;kerberos&#x60;. Null for &#x60;sql&#x60;. | 
**principal** | **str** | Active Directory principal Monte Carlo signs in as, for &#x60;kerberos&#x60;. Null for &#x60;sql&#x60;. | 

## Example

```python
from pycarlo2.models.sql_server_credentials_out import SqlServerCredentialsOut

# TODO update the JSON string below
json = "{}"
# create an instance of SqlServerCredentialsOut from a JSON string
sql_server_credentials_out_instance = SqlServerCredentialsOut.from_json(json)
# print the JSON string representation of the object
print(SqlServerCredentialsOut.to_json())

# convert the object into a dict
sql_server_credentials_out_dict = sql_server_credentials_out_instance.to_dict()
# create an instance of SqlServerCredentialsOut from a dict
sql_server_credentials_out_from_dict = SqlServerCredentialsOut.from_dict(sql_server_credentials_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


