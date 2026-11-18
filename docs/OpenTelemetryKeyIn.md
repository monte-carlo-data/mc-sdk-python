# OpenTelemetryKeyIn

The Agent Observability deployment an OpenTelemetry key sends traces to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What this key is for. Monte Carlo generates one naming the deployment if you leave it out. | [optional] 
**deployment_id** | **UUID** | The &#x60;AGENT_OBSERVABILITY&#x60; deployment to send traces to. It may still be &#x60;PROVISIONING&#x60;. | 

## Example

```python
from pycarlo2.models.open_telemetry_key_in import OpenTelemetryKeyIn

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTelemetryKeyIn from a JSON string
open_telemetry_key_in_instance = OpenTelemetryKeyIn.from_json(json)
# print the JSON string representation of the object
print(OpenTelemetryKeyIn.to_json())

# convert the object into a dict
open_telemetry_key_in_dict = open_telemetry_key_in_instance.to_dict()
# create an instance of OpenTelemetryKeyIn from a dict
open_telemetry_key_in_from_dict = OpenTelemetryKeyIn.from_dict(open_telemetry_key_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


