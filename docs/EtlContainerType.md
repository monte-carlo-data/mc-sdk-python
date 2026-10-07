# EtlContainerType

The ETL tool an ETL container represents.  Only the types a create accepts can be created through this API. Containers of every other type read with `is_synthetic` true and cannot be deleted through this API. Most belong to another connection, such as a warehouse or BI connection, and go away with it.

## Enum

* `AIRFLOW` (value: `'airflow'`)

* `AZURE_MINUS_DATA_MINUS_FACTORY` (value: `'azure-data-factory'`)

* `CUSTOM_MINUS_ETL_MINUS_CONNECTOR` (value: `'custom-etl-connector'`)

* `DATABRICKS` (value: `'databricks'`)

* `FIVETRAN` (value: `'fivetran'`)

* `GCP_MINUS_DATAFORM` (value: `'gcp-dataform'`)

* `INFORMATICA` (value: `'informatica'`)

* `INFORMATICA_MINUS_V2` (value: `'informatica-v2'`)

* `MULESOFT` (value: `'mulesoft'`)

* `POWER_BI_DATAFLOW` (value: `'power_bi_dataflow'`)

* `SALESFORCE_MINUS_DATA_MINUS_CLOUD` (value: `'salesforce-data-cloud'`)

* `SNOWFLAKE` (value: `'snowflake'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


