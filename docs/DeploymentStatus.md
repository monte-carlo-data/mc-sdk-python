# DeploymentStatus

How far Monte Carlo has got with setting a deployment up.  Only an `AGENT_OBSERVABILITY` deployment is ever `PROVISIONING` or `FAILED`. It starts in `PROVISIONING` and moves to `READY` or `FAILED` once Monte Carlo has finished setting it up. Every other deployment is always `READY`. A deployment's `enabled` says whether it can serve connections.

## Enum

* `PROVISIONING` (value: `'PROVISIONING'`)

* `READY` (value: `'READY'`)

* `FAILED` (value: `'FAILED'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


