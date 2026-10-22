# DbtCloudSettingsOut

Which dbt Cloud runs a dbt Cloud webhook connection processes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_match** | [**ConnectionMatch**](ConnectionMatch.md) | How a run is matched to the connection&#39;s warehouse. &#x60;off&#x60;, the default, drops no run for its dbt connection. | 
**allowed_connection_fields** | **List[str]** | The dbt connection fields to compare, such as &#x60;account&#x60; for Snowflake. &#x60;name&#x60; and &#x60;id&#x60; match a dbt connection by its own name or id. At least one for &#x60;allow_list&#x60;. Empty otherwise. | 
**allowed_connection_values** | **List[str]** | The values to match, exactly as they appear in dbt Cloud. A run is kept when one of &#x60;allowed_connection_fields&#x60; on its dbt connection equals one of them. At least one for &#x60;allow_list&#x60;. Empty otherwise. | 
**allowed_environments** | **List[str]** | The dbt environments, by name and ignoring case, whose runs are kept. Empty keeps runs from every environment. | 

## Example

```python
from pycarlo2.models.dbt_cloud_settings_out import DbtCloudSettingsOut

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudSettingsOut from a JSON string
dbt_cloud_settings_out_instance = DbtCloudSettingsOut.from_json(json)
# print the JSON string representation of the object
print(DbtCloudSettingsOut.to_json())

# convert the object into a dict
dbt_cloud_settings_out_dict = dbt_cloud_settings_out_instance.to_dict()
# create an instance of DbtCloudSettingsOut from a dict
dbt_cloud_settings_out_from_dict = DbtCloudSettingsOut.from_dict(dbt_cloud_settings_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


