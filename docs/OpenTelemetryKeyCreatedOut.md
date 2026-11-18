# OpenTelemetryKeyCreatedOut

An OpenTelemetry key as it comes back from its create, the only time the secret is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the key. | 
**description** | **str** | What this key is for. | 
**created_time** | **datetime** | When the key was created. | 
**deployment_id** | **UUID** | The &#x60;AGENT_OBSERVABILITY&#x60; deployment the key sends traces to. | 
**mcd_id** | **str** | Key id to present, as the &#x60;x-mcd-id&#x60; header or a client&#39;s &#x60;mcd_id&#x60; setting. The same value as &#x60;id&#x60;. | 
**mcd_token** | **str** | Secret to present, as the &#x60;x-mcd-token&#x60; header or a client&#39;s &#x60;mcd_token&#x60; setting. Returned once, by this call, and not retrievable afterwards. Terraform keeps it in state, so anyone who can read the state can read the secret: &#x60;sensitive&#x60; only hides it from CLI output. Keep state in a backend that encrypts it and limits who can read it. Hand the secret on through a write-only argument, such as &#x60;aws_secretsmanager_secret_version.secret_string_wo&#x60;, not through an output, because a &#x60;sensitive&#x60; output is stored in state too. To rotate, create a new key and delete this one. | [readonly] 

## Example

```python
from pycarlo2.models.open_telemetry_key_created_out import OpenTelemetryKeyCreatedOut

# TODO update the JSON string below
json = "{}"
# create an instance of OpenTelemetryKeyCreatedOut from a JSON string
open_telemetry_key_created_out_instance = OpenTelemetryKeyCreatedOut.from_json(json)
# print the JSON string representation of the object
print(OpenTelemetryKeyCreatedOut.to_json())

# convert the object into a dict
open_telemetry_key_created_out_dict = open_telemetry_key_created_out_instance.to_dict()
# create an instance of OpenTelemetryKeyCreatedOut from a dict
open_telemetry_key_created_out_from_dict = OpenTelemetryKeyCreatedOut.from_dict(open_telemetry_key_created_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


