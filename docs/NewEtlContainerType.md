# NewEtlContainerType

The ETL tool to create an ETL container for.  An `airflow` container takes no deployment. A `custom-etl-connector` container takes the deployment of the agent that registered its connector type, or none for a push-only connector. Every other type runs through one.

## Enum

* `AIRFLOW` (value: `'airflow'`)

* `AZURE_MINUS_DATA_MINUS_FACTORY` (value: `'azure-data-factory'`)

* `CUSTOM_MINUS_ETL_MINUS_CONNECTOR` (value: `'custom-etl-connector'`)

* `FIVETRAN` (value: `'fivetran'`)

* `GCP_MINUS_DATAFORM` (value: `'gcp-dataform'`)

* `INFORMATICA_MINUS_V2` (value: `'informatica-v2'`)

* `MULESOFT` (value: `'mulesoft'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


