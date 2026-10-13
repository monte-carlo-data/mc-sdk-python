# IntegrationKeyScope

What an integration key lets its holder do.  `INGESTION` pushes metadata, lineage, query logs, ETL jobs and runs, or BI assets to the warehouse or container the key is scoped to. `AIRFLOW_CALLBACKS` reports an Airflow environment's DAG and task runs to the Airflow ETL container the key is scoped to.

## Enum

* `INGESTION` (value: `'INGESTION'`)

* `AIRFLOW_CALLBACKS` (value: `'AIRFLOW_CALLBACKS'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


