# NewBiContainerType

The BI tool to create a BI container for.  A `looker` container holds both the Looker API connection and the LookML git connection. A `custom-bi-connector` container takes the deployment of the agent that registered its connector type, or none for a push-only connector. Every other type runs through one.

## Enum

* `LOOKER` (value: `'looker'`)

* `TABLEAU` (value: `'tableau'`)

* `POWER_MINUS_BI` (value: `'power-bi'`)

* `CUSTOM_MINUS_BI_MINUS_CONNECTOR` (value: `'custom-bi-connector'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


