# SqlServerCredentialsPatch

A change to existing SQL Server credentials.  A field left out is unchanged. A secret set to null is unchanged. `db_name` set to null is cleared. `host`, `port` and `auth_mode` cannot be cleared. A new `auth_mode` drops the fields and the secret of the old one, so send the new mode's fields with it. A new `keytab_base64` drops a stored `password`, and a new `password` drops a stored keytab. Sending an empty body returns the credentials as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Hostname of the database endpoint. For &#x60;kerberos&#x60;, the fully qualified name the server&#39;s service principal is registered under. | [optional] 
**port** | **int** | Port the database listens on. | [optional] 
**db_name** | **str** | Database to connect to. | [optional] 
**auth_mode** | [**SqlServerAuthMode**](SqlServerAuthMode.md) | How Monte Carlo signs in. &#x60;sql&#x60; takes &#x60;user&#x60; and &#x60;password&#x60;. &#x60;kerberos&#x60; takes &#x60;realm&#x60;, &#x60;kdc&#x60;, &#x60;principal&#x60;, and one of &#x60;keytab_base64&#x60; or &#x60;password&#x60;. | [optional] 
**user** | **str** | SQL login Monte Carlo signs in as, for &#x60;sql&#x60;. | [optional] 
**realm** | **str** | Kerberos realm, normally the Active Directory domain in capitals, for &#x60;kerberos&#x60;. | [optional] 
**kdc** | **str** | Hostname of the key distribution center, optionally with &#x60;:port&#x60;, for &#x60;kerberos&#x60;. | [optional] 
**principal** | **str** | Active Directory principal Monte Carlo signs in as, for &#x60;kerberos&#x60;. | [optional] 
**password** | **str** | Password of &#x60;user&#x60; for &#x60;sql&#x60;, or of the Active Directory account behind &#x60;principal&#x60; for &#x60;kerberos&#x60;. Stored by Monte Carlo and never returned. | [optional] 
**keytab_base64** | **str** | Base64-encoded keytab for &#x60;principal&#x60;, for &#x60;kerberos&#x60;. Send this or &#x60;password&#x60;. Stored by Monte Carlo and never returned. | [optional] 

## Example

```python
from pycarlo2.models.sql_server_credentials_patch import SqlServerCredentialsPatch

# TODO update the JSON string below
json = "{}"
# create an instance of SqlServerCredentialsPatch from a JSON string
sql_server_credentials_patch_instance = SqlServerCredentialsPatch.from_json(json)
# print the JSON string representation of the object
print(SqlServerCredentialsPatch.to_json())

# convert the object into a dict
sql_server_credentials_patch_dict = sql_server_credentials_patch_instance.to_dict()
# create an instance of SqlServerCredentialsPatch from a dict
sql_server_credentials_patch_from_dict = SqlServerCredentialsPatch.from_dict(sql_server_credentials_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


