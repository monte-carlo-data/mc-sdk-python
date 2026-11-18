# OpenTelemetryKeyOut

A key your agents send OpenTelemetry traces with, to one Agent Observability deployment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key. | 
**description** | **str** | What this key is for. | 
**created_time** | **datetime** | When the key was created. | 
**deployment_id** | **UUID** | The &#x60;AGENT_OBSERVABILITY&#x60; deployment the key sends traces to. | 
**mcd_id** | **str** | Key id to present, as the &#x60;x-mcd-id&#x60; header or a client&#39;s &#x60;mcd_id&#x60; setting. The same value as &#x60;id&#x60;. | 

## Example

```python
from pycarlo2.models.open_telemetry_key_out import OpenTelemetryKeyOut

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTelemetryKeyOut from a JSON string
open_telemetry_key_out_instance = OpenTelemetryKeyOut.from_json(json)
# print the JSON string representation of the object
print(OpenTelemetryKeyOut.to_json())

# convert the object into a dict
open_telemetry_key_out_dict = open_telemetry_key_out_instance.to_dict()
# create an instance of OpenTelemetryKeyOut from a dict
open_telemetry_key_out_from_dict = OpenTelemetryKeyOut.from_dict(open_telemetry_key_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


