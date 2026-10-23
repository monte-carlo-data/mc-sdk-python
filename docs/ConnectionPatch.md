# ConnectionPatch

A change to an existing connection: a new name, ETL turned on or off, new dbt Cloud settings, or other credentials.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New display name for the connection. Omit it to leave the name unchanged. An explicit null is ignored, the same as omitting the field. | [optional] 
**job_types** | **List[str]** | The connection&#39;s job types with &#x60;etl&#x60; added or removed. Adding &#x60;etl&#x60; turns on ETL collection for a Snowflake (Snowflake Tasks), Power BI (dataflows) or Salesforce Data Cloud connection, and creates the ETL container that &#x60;etl_container_id&#x60; then names. Removing it deletes that container. No other job can be added or removed. Omit it to leave the job types unchanged. | [optional] 
**dbt_cloud** | [**DbtCloudSettingsIn**](DbtCloudSettingsIn.md) | Which dbt Cloud runs a dbt Cloud webhook connection processes. A dbt Cloud webhook reports runs from every environment in the dbt account. These settings decide which of them Monte Carlo processes for the connection&#39;s warehouse. Only a dbt Cloud webhook connection takes it. An object replaces the settings whole. Null resets them to the defaults. Omit it to leave them unchanged. | [optional] 
**credentials_id** | **UUID** | Credentials for the connection to read with from now on. They must be for the connection&#39;s own type, and may be stored by Monte Carlo or self-hosted. The previous credentials are kept, and can be deleted once nothing uses them. Omit it to keep the current credentials. An explicit null is ignored, the same as omitting the field. | [optional] 

## Example

```python
from pycarlo2.models.connection_patch import ConnectionPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionPatch from a JSON string
connection_patch_instance = ConnectionPatch.from_json(json)
# print the JSON string representation of the object
print(ConnectionPatch.to_json())

# convert the object into a dict
connection_patch_dict = connection_patch_instance.to_dict()
# create an instance of ConnectionPatch from a dict
connection_patch_from_dict = ConnectionPatch.from_dict(connection_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


