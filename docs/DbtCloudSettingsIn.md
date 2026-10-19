# DbtCloudSettingsIn

Which dbt Cloud runs a dbt Cloud webhook connection processes. Every field is required, because the settings are replaced whole. Send an empty list for none.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_match** | [**ConnectionMatch**](ConnectionMatch.md) | How a run is matched to the connection&#39;s warehouse. &#x60;off&#x60;, the default, drops no run for its dbt connection. | 
**allowed_connections** | **List[str]** | The dbt connections, by id or name, whose runs are kept. At least one for &#x60;allow_list&#x60;. Empty otherwise. | 
**allowed_environments** | **List[str]** | The dbt environments, by name and ignoring case, whose runs are kept. Empty keeps runs from every environment. | 

## Example

```python
from pycarlo2.models.dbt_cloud_settings_in import DbtCloudSettingsIn

# TODO update the JSON string below
json = "{}"
# create an instance of DbtCloudSettingsIn from a JSON string
dbt_cloud_settings_in_instance = DbtCloudSettingsIn.from_json(json)
# print the JSON string representation of the object
print(DbtCloudSettingsIn.to_json())

# convert the object into a dict
dbt_cloud_settings_in_dict = dbt_cloud_settings_in_instance.to_dict()
# create an instance of DbtCloudSettingsIn from a dict
dbt_cloud_settings_in_from_dict = DbtCloudSettingsIn.from_dict(dbt_cloud_settings_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


