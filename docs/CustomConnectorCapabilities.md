# CustomConnectorCapabilities

What a custom warehouse connector supports, as its collection agent declared it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supports_metadata** | **bool** | Whether the connector supports metadata collection. | 
**supports_query_logs** | **bool** | Whether the connector supports query log collection. | 
**supports_lineage** | **bool** | Whether the connector supports lineage extraction. | 
**supports_field_lineage** | **bool** | Whether the connector supports field-level lineage. | 
**supports_schema** | **bool** | Whether the connector supports schema collection. | 
**supports_freshness** | **bool** | Whether the connector supports freshness monitoring. | 
**supports_volume_rows** | **bool** | Whether the connector supports row-count volume monitoring. | 
**supports_volume_bytes** | **bool** | Whether the connector supports byte-size volume monitoring. | 
**supports_custom_sql_monitor** | **bool** | Whether the connector supports custom SQL monitors. | 
**supports_full_query_language** | **bool** | Whether the connector supports the full query language. | 
**supports_stats_monitor** | **bool** | Whether the connector supports stats monitors. | 
**supports_comparison_monitor** | **bool** | Whether the connector supports comparison monitors. | 
**supports_validation_monitor** | **bool** | Whether the connector supports validation monitors. | 
**supports_json_schema_monitor** | **bool** | Whether the connector supports JSON schema monitors. | 
**supports_transform** | **bool** | Whether the connector supports transforms. | 
**supports_agent_monitor** | **bool** | Whether the connector supports agent monitors. | 
**supports_agent_trajectory_monitor** | **bool** | Whether the connector supports agent trajectory monitors. | 
**supports_non_metadata_size_collection** | **bool** | Whether the connector supports size collection without metadata. | 
**supports_metric_monitors_on_unknown_types** | **bool** | Whether the connector supports metric monitors on unknown field types. | 

## Example

```python
from pycarlo2.models.custom_connector_capabilities import CustomConnectorCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of CustomConnectorCapabilities from a JSON string
custom_connector_capabilities_instance = CustomConnectorCapabilities.from_json(json)
# print the JSON string representation of the object
print(CustomConnectorCapabilities.to_json())

# convert the object into a dict
custom_connector_capabilities_dict = custom_connector_capabilities_instance.to_dict()
# create an instance of CustomConnectorCapabilities from a dict
custom_connector_capabilities_from_dict = CustomConnectorCapabilities.from_dict(custom_connector_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


