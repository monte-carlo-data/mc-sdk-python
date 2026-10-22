# pycarlo2.CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_airflow_credentials**](CredentialsApi.md#create_airflow_credentials) | **POST** /api/v2/credentials/airflow | Create Airflow credentials
[**create_athena_credentials**](CredentialsApi.md#create_athena_credentials) | **POST** /api/v2/credentials/athena | Create Athena credentials
[**create_aws_secrets_manager_credentials**](CredentialsApi.md#create_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws | Create AWS Secrets Manager credentials
[**create_azure_data_factory_credentials**](CredentialsApi.md#create_azure_data_factory_credentials) | **POST** /api/v2/credentials/azure-data-factory | Create Azure Data Factory credentials
[**create_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#create_azure_dedicated_sql_pool_credentials) | **POST** /api/v2/credentials/azure-dedicated-sql-pool | Create Azure Dedicated SQL Pool credentials
[**create_azure_key_vault_credentials**](CredentialsApi.md#create_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure | Create Azure Key Vault credentials
[**create_azure_sql_database_credentials**](CredentialsApi.md#create_azure_sql_database_credentials) | **POST** /api/v2/credentials/azure-sql-database | Create Azure SQL Database credentials
[**create_bigquery_credentials**](CredentialsApi.md#create_bigquery_credentials) | **POST** /api/v2/credentials/bigquery | Create BigQuery credentials
[**create_clickhouse_credentials**](CredentialsApi.md#create_clickhouse_credentials) | **POST** /api/v2/credentials/clickhouse | Create ClickHouse credentials
[**create_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse | Create Databricks metadata collection credentials
[**create_databricks_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse | Create Databricks query credentials
[**create_db2_credentials**](CredentialsApi.md#create_db2_credentials) | **POST** /api/v2/credentials/db2 | Create Db2 credentials
[**create_dbt_cloud_webhook_credentials**](CredentialsApi.md#create_dbt_cloud_webhook_credentials) | **POST** /api/v2/credentials/dbt-cloud-webhook | Create dbt Cloud webhook credentials
[**create_env_var_credentials**](CredentialsApi.md#create_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var | Create environment variable credentials
[**create_file_credentials**](CredentialsApi.md#create_file_credentials) | **POST** /api/v2/credentials/self-hosted/file | Create file credentials
[**create_fivetran_credentials**](CredentialsApi.md#create_fivetran_credentials) | **POST** /api/v2/credentials/fivetran | Create Fivetran credentials
[**create_gcp_dataform_credentials**](CredentialsApi.md#create_gcp_dataform_credentials) | **POST** /api/v2/credentials/gcp-dataform | Create GCP Dataform credentials
[**create_gcp_secret_manager_credentials**](CredentialsApi.md#create_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp | Create GCP Secret Manager credentials
[**create_glue_credentials**](CredentialsApi.md#create_glue_credentials) | **POST** /api/v2/credentials/glue | Create Glue credentials
[**create_informatica_v2_credentials**](CredentialsApi.md#create_informatica_v2_credentials) | **POST** /api/v2/credentials/informatica-v2 | Create Informatica credentials
[**create_looker_credentials**](CredentialsApi.md#create_looker_credentials) | **POST** /api/v2/credentials/looker | Create Looker credentials
[**create_looker_git_clone_credentials**](CredentialsApi.md#create_looker_git_clone_credentials) | **POST** /api/v2/credentials/looker-git-clone | Create LookML repository credentials
[**create_mariadb_credentials**](CredentialsApi.md#create_mariadb_credentials) | **POST** /api/v2/credentials/mariadb | Create MariaDB credentials
[**create_mulesoft_credentials**](CredentialsApi.md#create_mulesoft_credentials) | **POST** /api/v2/credentials/mulesoft | Create MuleSoft credentials
[**create_mysql_credentials**](CredentialsApi.md#create_mysql_credentials) | **POST** /api/v2/credentials/mysql | Create MySQL credentials
[**create_oracle_credentials**](CredentialsApi.md#create_oracle_credentials) | **POST** /api/v2/credentials/oracle | Create Oracle credentials
[**create_postgres_credentials**](CredentialsApi.md#create_postgres_credentials) | **POST** /api/v2/credentials/postgres | Create PostgreSQL credentials
[**create_power_bi_credentials**](CredentialsApi.md#create_power_bi_credentials) | **POST** /api/v2/credentials/power-bi | Create Power BI credentials
[**create_redshift_credentials**](CredentialsApi.md#create_redshift_credentials) | **POST** /api/v2/credentials/redshift | Create Redshift credentials
[**create_salesforce_crm_credentials**](CredentialsApi.md#create_salesforce_crm_credentials) | **POST** /api/v2/credentials/salesforce-crm | Create Salesforce CRM credentials
[**create_sap_hana_credentials**](CredentialsApi.md#create_sap_hana_credentials) | **POST** /api/v2/credentials/sap-hana | Create SAP HANA credentials
[**create_snowflake_credentials**](CredentialsApi.md#create_snowflake_credentials) | **POST** /api/v2/credentials/snowflake | Create Snowflake credentials
[**create_sql_server_credentials**](CredentialsApi.md#create_sql_server_credentials) | **POST** /api/v2/credentials/sql-server | Create SQL Server credentials
[**create_starburst_enterprise_credentials**](CredentialsApi.md#create_starburst_enterprise_credentials) | **POST** /api/v2/credentials/starburst-enterprise | Create Starburst Enterprise credentials
[**create_starburst_galaxy_credentials**](CredentialsApi.md#create_starburst_galaxy_credentials) | **POST** /api/v2/credentials/starburst-galaxy | Create Starburst Galaxy credentials
[**create_tableau_credentials**](CredentialsApi.md#create_tableau_credentials) | **POST** /api/v2/credentials/tableau | Create Tableau credentials
[**create_teradata_credentials**](CredentialsApi.md#create_teradata_credentials) | **POST** /api/v2/credentials/teradata | Create Teradata credentials
[**delete_airflow_credentials**](CredentialsApi.md#delete_airflow_credentials) | **DELETE** /api/v2/credentials/airflow/{credentials_id} | Delete Airflow credentials
[**delete_athena_credentials**](CredentialsApi.md#delete_athena_credentials) | **DELETE** /api/v2/credentials/athena/{credentials_id} | Delete Athena credentials
[**delete_aws_secrets_manager_credentials**](CredentialsApi.md#delete_aws_secrets_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/aws/{credentials_id} | Delete AWS Secrets Manager credentials
[**delete_azure_data_factory_credentials**](CredentialsApi.md#delete_azure_data_factory_credentials) | **DELETE** /api/v2/credentials/azure-data-factory/{credentials_id} | Delete Azure Data Factory credentials
[**delete_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#delete_azure_dedicated_sql_pool_credentials) | **DELETE** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Delete Azure Dedicated SQL Pool credentials
[**delete_azure_key_vault_credentials**](CredentialsApi.md#delete_azure_key_vault_credentials) | **DELETE** /api/v2/credentials/self-hosted/azure/{credentials_id} | Delete Azure Key Vault credentials
[**delete_azure_sql_database_credentials**](CredentialsApi.md#delete_azure_sql_database_credentials) | **DELETE** /api/v2/credentials/azure-sql-database/{credentials_id} | Delete Azure SQL Database credentials
[**delete_bigquery_credentials**](CredentialsApi.md#delete_bigquery_credentials) | **DELETE** /api/v2/credentials/bigquery/{credentials_id} | Delete BigQuery credentials
[**delete_clickhouse_credentials**](CredentialsApi.md#delete_clickhouse_credentials) | **DELETE** /api/v2/credentials/clickhouse/{credentials_id} | Delete ClickHouse credentials
[**delete_credentials**](CredentialsApi.md#delete_credentials) | **DELETE** /api/v2/credentials/{credentials_id} | Delete credentials
[**delete_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_metastore_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Delete Databricks metadata collection credentials
[**delete_databricks_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Delete Databricks query credentials
[**delete_db2_credentials**](CredentialsApi.md#delete_db2_credentials) | **DELETE** /api/v2/credentials/db2/{credentials_id} | Delete Db2 credentials
[**delete_dbt_cloud_webhook_credentials**](CredentialsApi.md#delete_dbt_cloud_webhook_credentials) | **DELETE** /api/v2/credentials/dbt-cloud-webhook/{credentials_id} | Delete dbt Cloud webhook credentials
[**delete_env_var_credentials**](CredentialsApi.md#delete_env_var_credentials) | **DELETE** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Delete environment variable credentials
[**delete_file_credentials**](CredentialsApi.md#delete_file_credentials) | **DELETE** /api/v2/credentials/self-hosted/file/{credentials_id} | Delete file credentials
[**delete_fivetran_credentials**](CredentialsApi.md#delete_fivetran_credentials) | **DELETE** /api/v2/credentials/fivetran/{credentials_id} | Delete Fivetran credentials
[**delete_gcp_dataform_credentials**](CredentialsApi.md#delete_gcp_dataform_credentials) | **DELETE** /api/v2/credentials/gcp-dataform/{credentials_id} | Delete GCP Dataform credentials
[**delete_gcp_secret_manager_credentials**](CredentialsApi.md#delete_gcp_secret_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Delete GCP Secret Manager credentials
[**delete_glue_credentials**](CredentialsApi.md#delete_glue_credentials) | **DELETE** /api/v2/credentials/glue/{credentials_id} | Delete Glue credentials
[**delete_informatica_v2_credentials**](CredentialsApi.md#delete_informatica_v2_credentials) | **DELETE** /api/v2/credentials/informatica-v2/{credentials_id} | Delete Informatica credentials
[**delete_looker_credentials**](CredentialsApi.md#delete_looker_credentials) | **DELETE** /api/v2/credentials/looker/{credentials_id} | Delete Looker credentials
[**delete_looker_git_clone_credentials**](CredentialsApi.md#delete_looker_git_clone_credentials) | **DELETE** /api/v2/credentials/looker-git-clone/{credentials_id} | Delete LookML repository credentials
[**delete_mariadb_credentials**](CredentialsApi.md#delete_mariadb_credentials) | **DELETE** /api/v2/credentials/mariadb/{credentials_id} | Delete MariaDB credentials
[**delete_mulesoft_credentials**](CredentialsApi.md#delete_mulesoft_credentials) | **DELETE** /api/v2/credentials/mulesoft/{credentials_id} | Delete MuleSoft credentials
[**delete_mysql_credentials**](CredentialsApi.md#delete_mysql_credentials) | **DELETE** /api/v2/credentials/mysql/{credentials_id} | Delete MySQL credentials
[**delete_oracle_credentials**](CredentialsApi.md#delete_oracle_credentials) | **DELETE** /api/v2/credentials/oracle/{credentials_id} | Delete Oracle credentials
[**delete_postgres_credentials**](CredentialsApi.md#delete_postgres_credentials) | **DELETE** /api/v2/credentials/postgres/{credentials_id} | Delete PostgreSQL credentials
[**delete_power_bi_credentials**](CredentialsApi.md#delete_power_bi_credentials) | **DELETE** /api/v2/credentials/power-bi/{credentials_id} | Delete Power BI credentials
[**delete_redshift_credentials**](CredentialsApi.md#delete_redshift_credentials) | **DELETE** /api/v2/credentials/redshift/{credentials_id} | Delete Redshift credentials
[**delete_salesforce_crm_credentials**](CredentialsApi.md#delete_salesforce_crm_credentials) | **DELETE** /api/v2/credentials/salesforce-crm/{credentials_id} | Delete Salesforce CRM credentials
[**delete_sap_hana_credentials**](CredentialsApi.md#delete_sap_hana_credentials) | **DELETE** /api/v2/credentials/sap-hana/{credentials_id} | Delete SAP HANA credentials
[**delete_snowflake_credentials**](CredentialsApi.md#delete_snowflake_credentials) | **DELETE** /api/v2/credentials/snowflake/{credentials_id} | Delete Snowflake credentials
[**delete_sql_server_credentials**](CredentialsApi.md#delete_sql_server_credentials) | **DELETE** /api/v2/credentials/sql-server/{credentials_id} | Delete SQL Server credentials
[**delete_starburst_enterprise_credentials**](CredentialsApi.md#delete_starburst_enterprise_credentials) | **DELETE** /api/v2/credentials/starburst-enterprise/{credentials_id} | Delete Starburst Enterprise credentials
[**delete_starburst_galaxy_credentials**](CredentialsApi.md#delete_starburst_galaxy_credentials) | **DELETE** /api/v2/credentials/starburst-galaxy/{credentials_id} | Delete Starburst Galaxy credentials
[**delete_tableau_credentials**](CredentialsApi.md#delete_tableau_credentials) | **DELETE** /api/v2/credentials/tableau/{credentials_id} | Delete Tableau credentials
[**delete_teradata_credentials**](CredentialsApi.md#delete_teradata_credentials) | **DELETE** /api/v2/credentials/teradata/{credentials_id} | Delete Teradata credentials
[**get_airflow_credentials**](CredentialsApi.md#get_airflow_credentials) | **GET** /api/v2/credentials/airflow/{credentials_id} | Get Airflow credentials
[**get_athena_credentials**](CredentialsApi.md#get_athena_credentials) | **GET** /api/v2/credentials/athena/{credentials_id} | Get Athena credentials
[**get_aws_secrets_manager_credentials**](CredentialsApi.md#get_aws_secrets_manager_credentials) | **GET** /api/v2/credentials/self-hosted/aws/{credentials_id} | Get AWS Secrets Manager credentials
[**get_azure_data_factory_credentials**](CredentialsApi.md#get_azure_data_factory_credentials) | **GET** /api/v2/credentials/azure-data-factory/{credentials_id} | Get Azure Data Factory credentials
[**get_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#get_azure_dedicated_sql_pool_credentials) | **GET** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Get Azure Dedicated SQL Pool credentials
[**get_azure_key_vault_credentials**](CredentialsApi.md#get_azure_key_vault_credentials) | **GET** /api/v2/credentials/self-hosted/azure/{credentials_id} | Get Azure Key Vault credentials
[**get_azure_sql_database_credentials**](CredentialsApi.md#get_azure_sql_database_credentials) | **GET** /api/v2/credentials/azure-sql-database/{credentials_id} | Get Azure SQL Database credentials
[**get_bigquery_credentials**](CredentialsApi.md#get_bigquery_credentials) | **GET** /api/v2/credentials/bigquery/{credentials_id} | Get BigQuery credentials
[**get_clickhouse_credentials**](CredentialsApi.md#get_clickhouse_credentials) | **GET** /api/v2/credentials/clickhouse/{credentials_id} | Get ClickHouse credentials
[**get_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_metastore_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Get Databricks metadata collection credentials
[**get_databricks_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Get Databricks query credentials
[**get_db2_credentials**](CredentialsApi.md#get_db2_credentials) | **GET** /api/v2/credentials/db2/{credentials_id} | Get Db2 credentials
[**get_dbt_cloud_webhook_credentials**](CredentialsApi.md#get_dbt_cloud_webhook_credentials) | **GET** /api/v2/credentials/dbt-cloud-webhook/{credentials_id} | Get dbt Cloud webhook credentials
[**get_env_var_credentials**](CredentialsApi.md#get_env_var_credentials) | **GET** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Get environment variable credentials
[**get_file_credentials**](CredentialsApi.md#get_file_credentials) | **GET** /api/v2/credentials/self-hosted/file/{credentials_id} | Get file credentials
[**get_fivetran_credentials**](CredentialsApi.md#get_fivetran_credentials) | **GET** /api/v2/credentials/fivetran/{credentials_id} | Get Fivetran credentials
[**get_gcp_dataform_credentials**](CredentialsApi.md#get_gcp_dataform_credentials) | **GET** /api/v2/credentials/gcp-dataform/{credentials_id} | Get GCP Dataform credentials
[**get_gcp_secret_manager_credentials**](CredentialsApi.md#get_gcp_secret_manager_credentials) | **GET** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Get GCP Secret Manager credentials
[**get_glue_credentials**](CredentialsApi.md#get_glue_credentials) | **GET** /api/v2/credentials/glue/{credentials_id} | Get Glue credentials
[**get_informatica_v2_credentials**](CredentialsApi.md#get_informatica_v2_credentials) | **GET** /api/v2/credentials/informatica-v2/{credentials_id} | Get Informatica credentials
[**get_looker_credentials**](CredentialsApi.md#get_looker_credentials) | **GET** /api/v2/credentials/looker/{credentials_id} | Get Looker credentials
[**get_looker_git_clone_credentials**](CredentialsApi.md#get_looker_git_clone_credentials) | **GET** /api/v2/credentials/looker-git-clone/{credentials_id} | Get LookML repository credentials
[**get_mariadb_credentials**](CredentialsApi.md#get_mariadb_credentials) | **GET** /api/v2/credentials/mariadb/{credentials_id} | Get MariaDB credentials
[**get_mulesoft_credentials**](CredentialsApi.md#get_mulesoft_credentials) | **GET** /api/v2/credentials/mulesoft/{credentials_id} | Get MuleSoft credentials
[**get_mysql_credentials**](CredentialsApi.md#get_mysql_credentials) | **GET** /api/v2/credentials/mysql/{credentials_id} | Get MySQL credentials
[**get_oracle_credentials**](CredentialsApi.md#get_oracle_credentials) | **GET** /api/v2/credentials/oracle/{credentials_id} | Get Oracle credentials
[**get_postgres_credentials**](CredentialsApi.md#get_postgres_credentials) | **GET** /api/v2/credentials/postgres/{credentials_id} | Get PostgreSQL credentials
[**get_power_bi_credentials**](CredentialsApi.md#get_power_bi_credentials) | **GET** /api/v2/credentials/power-bi/{credentials_id} | Get Power BI credentials
[**get_redshift_credentials**](CredentialsApi.md#get_redshift_credentials) | **GET** /api/v2/credentials/redshift/{credentials_id} | Get Redshift credentials
[**get_salesforce_crm_credentials**](CredentialsApi.md#get_salesforce_crm_credentials) | **GET** /api/v2/credentials/salesforce-crm/{credentials_id} | Get Salesforce CRM credentials
[**get_sap_hana_credentials**](CredentialsApi.md#get_sap_hana_credentials) | **GET** /api/v2/credentials/sap-hana/{credentials_id} | Get SAP HANA credentials
[**get_snowflake_credentials**](CredentialsApi.md#get_snowflake_credentials) | **GET** /api/v2/credentials/snowflake/{credentials_id} | Get Snowflake credentials
[**get_sql_server_credentials**](CredentialsApi.md#get_sql_server_credentials) | **GET** /api/v2/credentials/sql-server/{credentials_id} | Get SQL Server credentials
[**get_starburst_enterprise_credentials**](CredentialsApi.md#get_starburst_enterprise_credentials) | **GET** /api/v2/credentials/starburst-enterprise/{credentials_id} | Get Starburst Enterprise credentials
[**get_starburst_galaxy_credentials**](CredentialsApi.md#get_starburst_galaxy_credentials) | **GET** /api/v2/credentials/starburst-galaxy/{credentials_id} | Get Starburst Galaxy credentials
[**get_tableau_credentials**](CredentialsApi.md#get_tableau_credentials) | **GET** /api/v2/credentials/tableau/{credentials_id} | Get Tableau credentials
[**get_teradata_credentials**](CredentialsApi.md#get_teradata_credentials) | **GET** /api/v2/credentials/teradata/{credentials_id} | Get Teradata credentials
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /api/v2/credentials | List credentials
[**update_airflow_credentials**](CredentialsApi.md#update_airflow_credentials) | **PATCH** /api/v2/credentials/airflow/{credentials_id} | Update Airflow credentials
[**update_athena_credentials**](CredentialsApi.md#update_athena_credentials) | **PATCH** /api/v2/credentials/athena/{credentials_id} | Update Athena credentials
[**update_aws_secrets_manager_credentials**](CredentialsApi.md#update_aws_secrets_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/aws/{credentials_id} | Update AWS Secrets Manager credentials
[**update_azure_data_factory_credentials**](CredentialsApi.md#update_azure_data_factory_credentials) | **PATCH** /api/v2/credentials/azure-data-factory/{credentials_id} | Update Azure Data Factory credentials
[**update_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#update_azure_dedicated_sql_pool_credentials) | **PATCH** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Update Azure Dedicated SQL Pool credentials
[**update_azure_key_vault_credentials**](CredentialsApi.md#update_azure_key_vault_credentials) | **PATCH** /api/v2/credentials/self-hosted/azure/{credentials_id} | Update Azure Key Vault credentials
[**update_azure_sql_database_credentials**](CredentialsApi.md#update_azure_sql_database_credentials) | **PATCH** /api/v2/credentials/azure-sql-database/{credentials_id} | Update Azure SQL Database credentials
[**update_bigquery_credentials**](CredentialsApi.md#update_bigquery_credentials) | **PATCH** /api/v2/credentials/bigquery/{credentials_id} | Update BigQuery credentials
[**update_clickhouse_credentials**](CredentialsApi.md#update_clickhouse_credentials) | **PATCH** /api/v2/credentials/clickhouse/{credentials_id} | Update ClickHouse credentials
[**update_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_metastore_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Update Databricks metadata collection credentials
[**update_databricks_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Update Databricks query credentials
[**update_db2_credentials**](CredentialsApi.md#update_db2_credentials) | **PATCH** /api/v2/credentials/db2/{credentials_id} | Update Db2 credentials
[**update_dbt_cloud_webhook_credentials**](CredentialsApi.md#update_dbt_cloud_webhook_credentials) | **PATCH** /api/v2/credentials/dbt-cloud-webhook/{credentials_id} | Update dbt Cloud webhook credentials
[**update_env_var_credentials**](CredentialsApi.md#update_env_var_credentials) | **PATCH** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Update environment variable credentials
[**update_file_credentials**](CredentialsApi.md#update_file_credentials) | **PATCH** /api/v2/credentials/self-hosted/file/{credentials_id} | Update file credentials
[**update_fivetran_credentials**](CredentialsApi.md#update_fivetran_credentials) | **PATCH** /api/v2/credentials/fivetran/{credentials_id} | Update Fivetran credentials
[**update_gcp_dataform_credentials**](CredentialsApi.md#update_gcp_dataform_credentials) | **PATCH** /api/v2/credentials/gcp-dataform/{credentials_id} | Update GCP Dataform credentials
[**update_gcp_secret_manager_credentials**](CredentialsApi.md#update_gcp_secret_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Update GCP Secret Manager credentials
[**update_glue_credentials**](CredentialsApi.md#update_glue_credentials) | **PATCH** /api/v2/credentials/glue/{credentials_id} | Update Glue credentials
[**update_informatica_v2_credentials**](CredentialsApi.md#update_informatica_v2_credentials) | **PATCH** /api/v2/credentials/informatica-v2/{credentials_id} | Update Informatica credentials
[**update_looker_credentials**](CredentialsApi.md#update_looker_credentials) | **PATCH** /api/v2/credentials/looker/{credentials_id} | Update Looker credentials
[**update_looker_git_clone_credentials**](CredentialsApi.md#update_looker_git_clone_credentials) | **PATCH** /api/v2/credentials/looker-git-clone/{credentials_id} | Update LookML repository credentials
[**update_mariadb_credentials**](CredentialsApi.md#update_mariadb_credentials) | **PATCH** /api/v2/credentials/mariadb/{credentials_id} | Update MariaDB credentials
[**update_mulesoft_credentials**](CredentialsApi.md#update_mulesoft_credentials) | **PATCH** /api/v2/credentials/mulesoft/{credentials_id} | Update MuleSoft credentials
[**update_mysql_credentials**](CredentialsApi.md#update_mysql_credentials) | **PATCH** /api/v2/credentials/mysql/{credentials_id} | Update MySQL credentials
[**update_oracle_credentials**](CredentialsApi.md#update_oracle_credentials) | **PATCH** /api/v2/credentials/oracle/{credentials_id} | Update Oracle credentials
[**update_postgres_credentials**](CredentialsApi.md#update_postgres_credentials) | **PATCH** /api/v2/credentials/postgres/{credentials_id} | Update PostgreSQL credentials
[**update_power_bi_credentials**](CredentialsApi.md#update_power_bi_credentials) | **PATCH** /api/v2/credentials/power-bi/{credentials_id} | Update Power BI credentials
[**update_redshift_credentials**](CredentialsApi.md#update_redshift_credentials) | **PATCH** /api/v2/credentials/redshift/{credentials_id} | Update Redshift credentials
[**update_salesforce_crm_credentials**](CredentialsApi.md#update_salesforce_crm_credentials) | **PATCH** /api/v2/credentials/salesforce-crm/{credentials_id} | Update Salesforce CRM credentials
[**update_sap_hana_credentials**](CredentialsApi.md#update_sap_hana_credentials) | **PATCH** /api/v2/credentials/sap-hana/{credentials_id} | Update SAP HANA credentials
[**update_snowflake_credentials**](CredentialsApi.md#update_snowflake_credentials) | **PATCH** /api/v2/credentials/snowflake/{credentials_id} | Update Snowflake credentials
[**update_sql_server_credentials**](CredentialsApi.md#update_sql_server_credentials) | **PATCH** /api/v2/credentials/sql-server/{credentials_id} | Update SQL Server credentials
[**update_starburst_enterprise_credentials**](CredentialsApi.md#update_starburst_enterprise_credentials) | **PATCH** /api/v2/credentials/starburst-enterprise/{credentials_id} | Update Starburst Enterprise credentials
[**update_starburst_galaxy_credentials**](CredentialsApi.md#update_starburst_galaxy_credentials) | **PATCH** /api/v2/credentials/starburst-galaxy/{credentials_id} | Update Starburst Galaxy credentials
[**update_tableau_credentials**](CredentialsApi.md#update_tableau_credentials) | **PATCH** /api/v2/credentials/tableau/{credentials_id} | Update Tableau credentials
[**update_teradata_credentials**](CredentialsApi.md#update_teradata_credentials) | **PATCH** /api/v2/credentials/teradata/{credentials_id} | Update Teradata credentials
[**validate_athena_credentials**](CredentialsApi.md#validate_athena_credentials) | **POST** /api/v2/credentials/athena/validate | Validate Athena credentials
[**validate_athena_credentials_change**](CredentialsApi.md#validate_athena_credentials_change) | **POST** /api/v2/credentials/athena/{credentials_id}/validate | Validate a change to Athena credentials
[**validate_aws_secrets_manager_credentials**](CredentialsApi.md#validate_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws/validate | Validate AWS Secrets Manager credentials
[**validate_aws_secrets_manager_credentials_change**](CredentialsApi.md#validate_aws_secrets_manager_credentials_change) | **POST** /api/v2/credentials/self-hosted/aws/{credentials_id}/validate | Validate a change to AWS Secrets Manager credentials
[**validate_azure_data_factory_credentials**](CredentialsApi.md#validate_azure_data_factory_credentials) | **POST** /api/v2/credentials/azure-data-factory/validate | Validate Azure Data Factory credentials
[**validate_azure_data_factory_credentials_change**](CredentialsApi.md#validate_azure_data_factory_credentials_change) | **POST** /api/v2/credentials/azure-data-factory/{credentials_id}/validate | Validate a change to Azure Data Factory credentials
[**validate_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#validate_azure_dedicated_sql_pool_credentials) | **POST** /api/v2/credentials/azure-dedicated-sql-pool/validate | Validate Azure Dedicated SQL Pool credentials
[**validate_azure_dedicated_sql_pool_credentials_change**](CredentialsApi.md#validate_azure_dedicated_sql_pool_credentials_change) | **POST** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id}/validate | Validate a change to Azure Dedicated SQL Pool credentials
[**validate_azure_key_vault_credentials**](CredentialsApi.md#validate_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure/validate | Validate Azure Key Vault credentials
[**validate_azure_key_vault_credentials_change**](CredentialsApi.md#validate_azure_key_vault_credentials_change) | **POST** /api/v2/credentials/self-hosted/azure/{credentials_id}/validate | Validate a change to Azure Key Vault credentials
[**validate_azure_sql_database_credentials**](CredentialsApi.md#validate_azure_sql_database_credentials) | **POST** /api/v2/credentials/azure-sql-database/validate | Validate Azure SQL Database credentials
[**validate_azure_sql_database_credentials_change**](CredentialsApi.md#validate_azure_sql_database_credentials_change) | **POST** /api/v2/credentials/azure-sql-database/{credentials_id}/validate | Validate a change to Azure SQL Database credentials
[**validate_bigquery_credentials**](CredentialsApi.md#validate_bigquery_credentials) | **POST** /api/v2/credentials/bigquery/validate | Validate BigQuery credentials
[**validate_bigquery_credentials_change**](CredentialsApi.md#validate_bigquery_credentials_change) | **POST** /api/v2/credentials/bigquery/{credentials_id}/validate | Validate a change to BigQuery credentials
[**validate_clickhouse_credentials**](CredentialsApi.md#validate_clickhouse_credentials) | **POST** /api/v2/credentials/clickhouse/validate | Validate ClickHouse credentials
[**validate_clickhouse_credentials_change**](CredentialsApi.md#validate_clickhouse_credentials_change) | **POST** /api/v2/credentials/clickhouse/{credentials_id}/validate | Validate a change to ClickHouse credentials
[**validate_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse/validate | Validate Databricks metadata collection credentials
[**validate_databricks_metastore_sql_warehouse_credentials_change**](CredentialsApi.md#validate_databricks_metastore_sql_warehouse_credentials_change) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id}/validate | Validate a change to Databricks metadata collection credentials
[**validate_databricks_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse/validate | Validate Databricks query credentials
[**validate_databricks_sql_warehouse_credentials_change**](CredentialsApi.md#validate_databricks_sql_warehouse_credentials_change) | **POST** /api/v2/credentials/databricks-sql-warehouse/{credentials_id}/validate | Validate a change to Databricks query credentials
[**validate_db2_credentials**](CredentialsApi.md#validate_db2_credentials) | **POST** /api/v2/credentials/db2/validate | Validate Db2 credentials
[**validate_db2_credentials_change**](CredentialsApi.md#validate_db2_credentials_change) | **POST** /api/v2/credentials/db2/{credentials_id}/validate | Validate a change to Db2 credentials
[**validate_dbt_cloud_webhook_credentials**](CredentialsApi.md#validate_dbt_cloud_webhook_credentials) | **POST** /api/v2/credentials/dbt-cloud-webhook/validate | Validate dbt Cloud webhook credentials
[**validate_dbt_cloud_webhook_credentials_change**](CredentialsApi.md#validate_dbt_cloud_webhook_credentials_change) | **POST** /api/v2/credentials/dbt-cloud-webhook/{credentials_id}/validate | Validate a change to dbt Cloud webhook credentials
[**validate_env_var_credentials**](CredentialsApi.md#validate_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var/validate | Validate environment variable credentials
[**validate_env_var_credentials_change**](CredentialsApi.md#validate_env_var_credentials_change) | **POST** /api/v2/credentials/self-hosted/env-var/{credentials_id}/validate | Validate a change to environment variable credentials
[**validate_file_credentials**](CredentialsApi.md#validate_file_credentials) | **POST** /api/v2/credentials/self-hosted/file/validate | Validate file credentials
[**validate_file_credentials_change**](CredentialsApi.md#validate_file_credentials_change) | **POST** /api/v2/credentials/self-hosted/file/{credentials_id}/validate | Validate a change to file credentials
[**validate_fivetran_credentials**](CredentialsApi.md#validate_fivetran_credentials) | **POST** /api/v2/credentials/fivetran/validate | Validate Fivetran credentials
[**validate_fivetran_credentials_change**](CredentialsApi.md#validate_fivetran_credentials_change) | **POST** /api/v2/credentials/fivetran/{credentials_id}/validate | Validate a change to Fivetran credentials
[**validate_gcp_dataform_credentials**](CredentialsApi.md#validate_gcp_dataform_credentials) | **POST** /api/v2/credentials/gcp-dataform/validate | Validate GCP Dataform credentials
[**validate_gcp_dataform_credentials_change**](CredentialsApi.md#validate_gcp_dataform_credentials_change) | **POST** /api/v2/credentials/gcp-dataform/{credentials_id}/validate | Validate a change to GCP Dataform credentials
[**validate_gcp_secret_manager_credentials**](CredentialsApi.md#validate_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp/validate | Validate GCP Secret Manager credentials
[**validate_gcp_secret_manager_credentials_change**](CredentialsApi.md#validate_gcp_secret_manager_credentials_change) | **POST** /api/v2/credentials/self-hosted/gcp/{credentials_id}/validate | Validate a change to GCP Secret Manager credentials
[**validate_glue_credentials**](CredentialsApi.md#validate_glue_credentials) | **POST** /api/v2/credentials/glue/validate | Validate Glue credentials
[**validate_glue_credentials_change**](CredentialsApi.md#validate_glue_credentials_change) | **POST** /api/v2/credentials/glue/{credentials_id}/validate | Validate a change to Glue credentials
[**validate_informatica_v2_credentials**](CredentialsApi.md#validate_informatica_v2_credentials) | **POST** /api/v2/credentials/informatica-v2/validate | Validate Informatica credentials
[**validate_informatica_v2_credentials_change**](CredentialsApi.md#validate_informatica_v2_credentials_change) | **POST** /api/v2/credentials/informatica-v2/{credentials_id}/validate | Validate a change to Informatica credentials
[**validate_looker_credentials**](CredentialsApi.md#validate_looker_credentials) | **POST** /api/v2/credentials/looker/validate | Validate Looker credentials
[**validate_looker_credentials_change**](CredentialsApi.md#validate_looker_credentials_change) | **POST** /api/v2/credentials/looker/{credentials_id}/validate | Validate a change to Looker credentials
[**validate_looker_git_clone_credentials**](CredentialsApi.md#validate_looker_git_clone_credentials) | **POST** /api/v2/credentials/looker-git-clone/validate | Validate LookML repository credentials
[**validate_looker_git_clone_credentials_change**](CredentialsApi.md#validate_looker_git_clone_credentials_change) | **POST** /api/v2/credentials/looker-git-clone/{credentials_id}/validate | Validate a change to LookML repository credentials
[**validate_mariadb_credentials**](CredentialsApi.md#validate_mariadb_credentials) | **POST** /api/v2/credentials/mariadb/validate | Validate MariaDB credentials
[**validate_mariadb_credentials_change**](CredentialsApi.md#validate_mariadb_credentials_change) | **POST** /api/v2/credentials/mariadb/{credentials_id}/validate | Validate a change to MariaDB credentials
[**validate_mulesoft_credentials**](CredentialsApi.md#validate_mulesoft_credentials) | **POST** /api/v2/credentials/mulesoft/validate | Validate MuleSoft credentials
[**validate_mulesoft_credentials_change**](CredentialsApi.md#validate_mulesoft_credentials_change) | **POST** /api/v2/credentials/mulesoft/{credentials_id}/validate | Validate a change to MuleSoft credentials
[**validate_mysql_credentials**](CredentialsApi.md#validate_mysql_credentials) | **POST** /api/v2/credentials/mysql/validate | Validate MySQL credentials
[**validate_mysql_credentials_change**](CredentialsApi.md#validate_mysql_credentials_change) | **POST** /api/v2/credentials/mysql/{credentials_id}/validate | Validate a change to MySQL credentials
[**validate_oracle_credentials**](CredentialsApi.md#validate_oracle_credentials) | **POST** /api/v2/credentials/oracle/validate | Validate Oracle credentials
[**validate_oracle_credentials_change**](CredentialsApi.md#validate_oracle_credentials_change) | **POST** /api/v2/credentials/oracle/{credentials_id}/validate | Validate a change to Oracle credentials
[**validate_postgres_credentials**](CredentialsApi.md#validate_postgres_credentials) | **POST** /api/v2/credentials/postgres/validate | Validate PostgreSQL credentials
[**validate_postgres_credentials_change**](CredentialsApi.md#validate_postgres_credentials_change) | **POST** /api/v2/credentials/postgres/{credentials_id}/validate | Validate a change to PostgreSQL credentials
[**validate_power_bi_credentials**](CredentialsApi.md#validate_power_bi_credentials) | **POST** /api/v2/credentials/power-bi/validate | Validate Power BI credentials
[**validate_power_bi_credentials_change**](CredentialsApi.md#validate_power_bi_credentials_change) | **POST** /api/v2/credentials/power-bi/{credentials_id}/validate | Validate a change to Power BI credentials
[**validate_redshift_credentials**](CredentialsApi.md#validate_redshift_credentials) | **POST** /api/v2/credentials/redshift/validate | Validate Redshift credentials
[**validate_redshift_credentials_change**](CredentialsApi.md#validate_redshift_credentials_change) | **POST** /api/v2/credentials/redshift/{credentials_id}/validate | Validate a change to Redshift credentials
[**validate_salesforce_crm_credentials**](CredentialsApi.md#validate_salesforce_crm_credentials) | **POST** /api/v2/credentials/salesforce-crm/validate | Validate Salesforce CRM credentials
[**validate_salesforce_crm_credentials_change**](CredentialsApi.md#validate_salesforce_crm_credentials_change) | **POST** /api/v2/credentials/salesforce-crm/{credentials_id}/validate | Validate a change to Salesforce CRM credentials
[**validate_sap_hana_credentials**](CredentialsApi.md#validate_sap_hana_credentials) | **POST** /api/v2/credentials/sap-hana/validate | Validate SAP HANA credentials
[**validate_sap_hana_credentials_change**](CredentialsApi.md#validate_sap_hana_credentials_change) | **POST** /api/v2/credentials/sap-hana/{credentials_id}/validate | Validate a change to SAP HANA credentials
[**validate_snowflake_credentials**](CredentialsApi.md#validate_snowflake_credentials) | **POST** /api/v2/credentials/snowflake/validate | Validate Snowflake credentials
[**validate_snowflake_credentials_change**](CredentialsApi.md#validate_snowflake_credentials_change) | **POST** /api/v2/credentials/snowflake/{credentials_id}/validate | Validate a change to Snowflake credentials
[**validate_sql_server_credentials**](CredentialsApi.md#validate_sql_server_credentials) | **POST** /api/v2/credentials/sql-server/validate | Validate SQL Server credentials
[**validate_sql_server_credentials_change**](CredentialsApi.md#validate_sql_server_credentials_change) | **POST** /api/v2/credentials/sql-server/{credentials_id}/validate | Validate a change to SQL Server credentials
[**validate_starburst_enterprise_credentials**](CredentialsApi.md#validate_starburst_enterprise_credentials) | **POST** /api/v2/credentials/starburst-enterprise/validate | Validate Starburst Enterprise credentials
[**validate_starburst_enterprise_credentials_change**](CredentialsApi.md#validate_starburst_enterprise_credentials_change) | **POST** /api/v2/credentials/starburst-enterprise/{credentials_id}/validate | Validate a change to Starburst Enterprise credentials
[**validate_starburst_galaxy_credentials**](CredentialsApi.md#validate_starburst_galaxy_credentials) | **POST** /api/v2/credentials/starburst-galaxy/validate | Validate Starburst Galaxy credentials
[**validate_starburst_galaxy_credentials_change**](CredentialsApi.md#validate_starburst_galaxy_credentials_change) | **POST** /api/v2/credentials/starburst-galaxy/{credentials_id}/validate | Validate a change to Starburst Galaxy credentials
[**validate_tableau_credentials**](CredentialsApi.md#validate_tableau_credentials) | **POST** /api/v2/credentials/tableau/validate | Validate Tableau credentials
[**validate_tableau_credentials_change**](CredentialsApi.md#validate_tableau_credentials_change) | **POST** /api/v2/credentials/tableau/{credentials_id}/validate | Validate a change to Tableau credentials
[**validate_teradata_credentials**](CredentialsApi.md#validate_teradata_credentials) | **POST** /api/v2/credentials/teradata/validate | Validate Teradata credentials
[**validate_teradata_credentials_change**](CredentialsApi.md#validate_teradata_credentials_change) | **POST** /api/v2/credentials/teradata/{credentials_id}/validate | Validate a change to Teradata credentials


# **create_airflow_credentials**
> AirflowCredentialsOut create_airflow_credentials(airflow_credentials_in)

Create Airflow credentials

Store the connection details of an Airflow environment.

Airflow reports its runs to Monte Carlo, so there is no secret to keep. An account
holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.airflow_credentials_in import AirflowCredentialsIn
from pycarlo2.models.airflow_credentials_out import AirflowCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    airflow_credentials_in = pycarlo2.AirflowCredentialsIn() # AirflowCredentialsIn | 

    try:
        # Create Airflow credentials
        api_response = api_instance.create_airflow_credentials(airflow_credentials_in)
        print("The response of CredentialsApi->create_airflow_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_airflow_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **airflow_credentials_in** | [**AirflowCredentialsIn**](AirflowCredentialsIn.md)|  | 

### Return type

[**AirflowCredentialsOut**](AirflowCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_athena_credentials**
> AthenaCredentialsOut create_athena_credentials(athena_credentials_in)

Create Athena credentials

Store the IAM role Monte Carlo assumes to run Athena queries.

Athena needs no secret. Create the credentials first, then create a connection that
references them on a `data-lake` warehouse. Nothing is checked against AWS here.

An account holds a limited number of credentials. Past that, the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.athena_credentials_in import AthenaCredentialsIn
from pycarlo2.models.athena_credentials_out import AthenaCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    athena_credentials_in = pycarlo2.AthenaCredentialsIn() # AthenaCredentialsIn | 

    try:
        # Create Athena credentials
        api_response = api_instance.create_athena_credentials(athena_credentials_in)
        print("The response of CredentialsApi->create_athena_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_athena_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athena_credentials_in** | [**AthenaCredentialsIn**](AthenaCredentialsIn.md)|  | 

### Return type

[**AthenaCredentialsOut**](AthenaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_aws_secrets_manager_credentials**
> AwsSecretsManagerCredentialsOut create_aws_secrets_manager_credentials(aws_secrets_manager_credentials_in)

Create AWS Secrets Manager credentials

Store where a connection's credentials live in your AWS Secrets Manager.

Monte Carlo keeps the reference, not the secret, and reads the secret from your store each
time the connection is used. Create the credentials first, then create a connection that
references them. Nothing is checked against AWS here.

`connection_type` names what the secret holds credentials for, and is fixed once created.
An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.aws_secrets_manager_credentials_in import AwsSecretsManagerCredentialsIn
from pycarlo2.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    aws_secrets_manager_credentials_in = pycarlo2.AwsSecretsManagerCredentialsIn() # AwsSecretsManagerCredentialsIn | 

    try:
        # Create AWS Secrets Manager credentials
        api_response = api_instance.create_aws_secrets_manager_credentials(aws_secrets_manager_credentials_in)
        print("The response of CredentialsApi->create_aws_secrets_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_aws_secrets_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_secrets_manager_credentials_in** | [**AwsSecretsManagerCredentialsIn**](AwsSecretsManagerCredentialsIn.md)|  | 

### Return type

[**AwsSecretsManagerCredentialsOut**](AwsSecretsManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_data_factory_credentials**
> AzureDataFactoryCredentialsOut create_azure_data_factory_credentials(azure_data_factory_credentials_in)

Create Azure Data Factory credentials

Store Azure Data Factory credentials.

Monte Carlo keeps the client secret and returns everything else. Nothing
is checked against Azure Data Factory here. An account holds a limited number of credentials;
past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_data_factory_credentials_in import AzureDataFactoryCredentialsIn
from pycarlo2.models.azure_data_factory_credentials_out import AzureDataFactoryCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_data_factory_credentials_in = pycarlo2.AzureDataFactoryCredentialsIn() # AzureDataFactoryCredentialsIn | 

    try:
        # Create Azure Data Factory credentials
        api_response = api_instance.create_azure_data_factory_credentials(azure_data_factory_credentials_in)
        print("The response of CredentialsApi->create_azure_data_factory_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_azure_data_factory_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_data_factory_credentials_in** | [**AzureDataFactoryCredentialsIn**](AzureDataFactoryCredentialsIn.md)|  | 

### Return type

[**AzureDataFactoryCredentialsOut**](AzureDataFactoryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_dedicated_sql_pool_credentials**
> AzureDedicatedSqlPoolCredentialsOut create_azure_dedicated_sql_pool_credentials(azure_dedicated_sql_pool_credentials_in)

Create Azure Dedicated SQL Pool credentials

Store an Azure Dedicated SQL Pool login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Azure Dedicated SQL Pool
here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_dedicated_sql_pool_credentials_in import AzureDedicatedSqlPoolCredentialsIn
from pycarlo2.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_dedicated_sql_pool_credentials_in = pycarlo2.AzureDedicatedSqlPoolCredentialsIn() # AzureDedicatedSqlPoolCredentialsIn | 

    try:
        # Create Azure Dedicated SQL Pool credentials
        api_response = api_instance.create_azure_dedicated_sql_pool_credentials(azure_dedicated_sql_pool_credentials_in)
        print("The response of CredentialsApi->create_azure_dedicated_sql_pool_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_azure_dedicated_sql_pool_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_dedicated_sql_pool_credentials_in** | [**AzureDedicatedSqlPoolCredentialsIn**](AzureDedicatedSqlPoolCredentialsIn.md)|  | 

### Return type

[**AzureDedicatedSqlPoolCredentialsOut**](AzureDedicatedSqlPoolCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_key_vault_credentials**
> AzureKeyVaultCredentialsOut create_azure_key_vault_credentials(azure_key_vault_credentials_in)

Create Azure Key Vault credentials

Store where a connection's credentials live in your Azure Key Vault.

Monte Carlo keeps the reference, not the secret, and reads the secret from your store each
time the connection is used. Name the vault by `akv_vault_name`, `akv_vault_url`, or both.
Create the credentials first, then create a connection that references them. Nothing is
checked against Azure here.

`connection_type` names what the secret holds credentials for, and is fixed once created.
An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_key_vault_credentials_in import AzureKeyVaultCredentialsIn
from pycarlo2.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_key_vault_credentials_in = pycarlo2.AzureKeyVaultCredentialsIn() # AzureKeyVaultCredentialsIn | 

    try:
        # Create Azure Key Vault credentials
        api_response = api_instance.create_azure_key_vault_credentials(azure_key_vault_credentials_in)
        print("The response of CredentialsApi->create_azure_key_vault_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_azure_key_vault_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_key_vault_credentials_in** | [**AzureKeyVaultCredentialsIn**](AzureKeyVaultCredentialsIn.md)|  | 

### Return type

[**AzureKeyVaultCredentialsOut**](AzureKeyVaultCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_azure_sql_database_credentials**
> AzureSqlDatabaseCredentialsOut create_azure_sql_database_credentials(azure_sql_database_credentials_in)

Create Azure SQL Database credentials

Store an Azure SQL Database login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Azure SQL Database here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_sql_database_credentials_in import AzureSqlDatabaseCredentialsIn
from pycarlo2.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_sql_database_credentials_in = pycarlo2.AzureSqlDatabaseCredentialsIn() # AzureSqlDatabaseCredentialsIn | 

    try:
        # Create Azure SQL Database credentials
        api_response = api_instance.create_azure_sql_database_credentials(azure_sql_database_credentials_in)
        print("The response of CredentialsApi->create_azure_sql_database_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_azure_sql_database_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_sql_database_credentials_in** | [**AzureSqlDatabaseCredentialsIn**](AzureSqlDatabaseCredentialsIn.md)|  | 

### Return type

[**AzureSqlDatabaseCredentialsOut**](AzureSqlDatabaseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_bigquery_credentials**
> BigQueryCredentialsOut create_bigquery_credentials(big_query_credentials_in)

Create BigQuery credentials

Store a BigQuery service account key for connections to use.

Monte Carlo keeps the key and returns only its project and service account email. Create
the credentials first, then create a connection that references them. Nothing is checked
against BigQuery here.

The key must be a service account key issued by Google. An account holds a limited number
of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.big_query_credentials_in import BigQueryCredentialsIn
from pycarlo2.models.big_query_credentials_out import BigQueryCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    big_query_credentials_in = pycarlo2.BigQueryCredentialsIn() # BigQueryCredentialsIn | 

    try:
        # Create BigQuery credentials
        api_response = api_instance.create_bigquery_credentials(big_query_credentials_in)
        print("The response of CredentialsApi->create_bigquery_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_bigquery_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **big_query_credentials_in** | [**BigQueryCredentialsIn**](BigQueryCredentialsIn.md)|  | 

### Return type

[**BigQueryCredentialsOut**](BigQueryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clickhouse_credentials**
> ClickHouseCredentialsOut create_clickhouse_credentials(click_house_credentials_in)

Create ClickHouse credentials

Store a ClickHouse login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against ClickHouse here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.click_house_credentials_in import ClickHouseCredentialsIn
from pycarlo2.models.click_house_credentials_out import ClickHouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    click_house_credentials_in = pycarlo2.ClickHouseCredentialsIn() # ClickHouseCredentialsIn | 

    try:
        # Create ClickHouse credentials
        api_response = api_instance.create_clickhouse_credentials(click_house_credentials_in)
        print("The response of CredentialsApi->create_clickhouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_clickhouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_house_credentials_in** | [**ClickHouseCredentialsIn**](ClickHouseCredentialsIn.md)|  | 

### Return type

[**ClickHouseCredentialsOut**](ClickHouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_databricks_metastore_sql_warehouse_credentials**
> DatabricksMetastoreSqlWarehouseCredentialsOut create_databricks_metastore_sql_warehouse_credentials(databricks_metastore_sql_warehouse_credentials_in)

Create Databricks metadata collection credentials

Store Databricks credentials for collecting metadata through a SQL warehouse.

Monte Carlo keeps the token or the OAuth secret and returns everything else. Create the
credentials first, then create a connection that references them, on a data lake
warehouse. Nothing is checked against Databricks here.

Send `token`, or `oauth_client_id` and `oauth_client_secret`. For a service principal
Azure manages, add `azure_tenant_id` and `azure_workspace_resource_id` to the OAuth
client. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_in import DatabricksMetastoreSqlWarehouseCredentialsIn
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    databricks_metastore_sql_warehouse_credentials_in = pycarlo2.DatabricksMetastoreSqlWarehouseCredentialsIn() # DatabricksMetastoreSqlWarehouseCredentialsIn | 

    try:
        # Create Databricks metadata collection credentials
        api_response = api_instance.create_databricks_metastore_sql_warehouse_credentials(databricks_metastore_sql_warehouse_credentials_in)
        print("The response of CredentialsApi->create_databricks_metastore_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databricks_metastore_sql_warehouse_credentials_in** | [**DatabricksMetastoreSqlWarehouseCredentialsIn**](DatabricksMetastoreSqlWarehouseCredentialsIn.md)|  | 

### Return type

[**DatabricksMetastoreSqlWarehouseCredentialsOut**](DatabricksMetastoreSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_databricks_sql_warehouse_credentials**
> DatabricksSqlWarehouseCredentialsOut create_databricks_sql_warehouse_credentials(databricks_sql_warehouse_credentials_in)

Create Databricks query credentials

Store Databricks credentials for running queries on a SQL warehouse.

Monte Carlo keeps the token or the OAuth secret and returns everything else. Create the
credentials first, then create a connection that references them. Nothing is checked
against Databricks here.

The connection goes on a data lake warehouse that already has a metastore connection, such
as a Databricks metadata collection one. Name that warehouse when creating the connection.

Send `token`, or `oauth_client_id` and `oauth_client_secret`. For a service principal
Azure manages, add `azure_tenant_id` and `azure_workspace_resource_id` to the OAuth
client. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_sql_warehouse_credentials_in import DatabricksSqlWarehouseCredentialsIn
from pycarlo2.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    databricks_sql_warehouse_credentials_in = pycarlo2.DatabricksSqlWarehouseCredentialsIn() # DatabricksSqlWarehouseCredentialsIn | 

    try:
        # Create Databricks query credentials
        api_response = api_instance.create_databricks_sql_warehouse_credentials(databricks_sql_warehouse_credentials_in)
        print("The response of CredentialsApi->create_databricks_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_databricks_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databricks_sql_warehouse_credentials_in** | [**DatabricksSqlWarehouseCredentialsIn**](DatabricksSqlWarehouseCredentialsIn.md)|  | 

### Return type

[**DatabricksSqlWarehouseCredentialsOut**](DatabricksSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_db2_credentials**
> Db2CredentialsOut create_db2_credentials(db2_credentials_in)

Create Db2 credentials

Store a Db2 login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Db2 here.

Send `ssl_ca_data` to check the server against your own CA, or `ssl_disabled` to connect without
TLS. The two cannot be combined. An account holds a limited number of credentials; past that the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.db2_credentials_in import Db2CredentialsIn
from pycarlo2.models.db2_credentials_out import Db2CredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    db2_credentials_in = pycarlo2.Db2CredentialsIn() # Db2CredentialsIn | 

    try:
        # Create Db2 credentials
        api_response = api_instance.create_db2_credentials(db2_credentials_in)
        print("The response of CredentialsApi->create_db2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_db2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db2_credentials_in** | [**Db2CredentialsIn**](Db2CredentialsIn.md)|  | 

### Return type

[**Db2CredentialsOut**](Db2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dbt_cloud_webhook_credentials**
> DbtCloudWebhookCredentialsOut create_dbt_cloud_webhook_credentials(dbt_cloud_webhook_credentials_in)

Create dbt Cloud webhook credentials

Store dbt Cloud webhook credentials.

Monte Carlo keeps the service token and the HMAC secret and returns everything else.
Nothing is checked against dbt Cloud here. An account holds a limited number of
credentials. Past that, the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.dbt_cloud_webhook_credentials_in import DbtCloudWebhookCredentialsIn
from pycarlo2.models.dbt_cloud_webhook_credentials_out import DbtCloudWebhookCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    dbt_cloud_webhook_credentials_in = pycarlo2.DbtCloudWebhookCredentialsIn() # DbtCloudWebhookCredentialsIn | 

    try:
        # Create dbt Cloud webhook credentials
        api_response = api_instance.create_dbt_cloud_webhook_credentials(dbt_cloud_webhook_credentials_in)
        print("The response of CredentialsApi->create_dbt_cloud_webhook_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_dbt_cloud_webhook_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbt_cloud_webhook_credentials_in** | [**DbtCloudWebhookCredentialsIn**](DbtCloudWebhookCredentialsIn.md)|  | 

### Return type

[**DbtCloudWebhookCredentialsOut**](DbtCloudWebhookCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_env_var_credentials**
> EnvVarCredentialsOut create_env_var_credentials(env_var_credentials_in)

Create environment variable credentials

Store which environment variable of your deployment holds a connection's credentials.

Monte Carlo keeps the variable's name, not its value, and reads the value on the deployment
each time the connection is used. The name has to start with `MCD_`. A value encrypted with
AWS KMS is decrypted with the key `kms_key_id` names. Create the credentials first, then
create a connection that references them. Nothing is checked on the deployment here.

`connection_type` names what the variable holds credentials for, and is fixed once created.
An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.env_var_credentials_in import EnvVarCredentialsIn
from pycarlo2.models.env_var_credentials_out import EnvVarCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    env_var_credentials_in = pycarlo2.EnvVarCredentialsIn() # EnvVarCredentialsIn | 

    try:
        # Create environment variable credentials
        api_response = api_instance.create_env_var_credentials(env_var_credentials_in)
        print("The response of CredentialsApi->create_env_var_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_env_var_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_credentials_in** | [**EnvVarCredentialsIn**](EnvVarCredentialsIn.md)|  | 

### Return type

[**EnvVarCredentialsOut**](EnvVarCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_credentials**
> FileCredentialsOut create_file_credentials(file_credentials_in)

Create file credentials

Store which file on your deployment holds a connection's credentials.

Monte Carlo keeps the path, not the contents, and reads the file on the deployment each
time the connection is used. Create the credentials first, then create a connection that
references them. Nothing is checked on the deployment here.

`connection_type` names what the file holds credentials for, and is fixed once created. An
account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.file_credentials_in import FileCredentialsIn
from pycarlo2.models.file_credentials_out import FileCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    file_credentials_in = pycarlo2.FileCredentialsIn() # FileCredentialsIn | 

    try:
        # Create file credentials
        api_response = api_instance.create_file_credentials(file_credentials_in)
        print("The response of CredentialsApi->create_file_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_file_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_credentials_in** | [**FileCredentialsIn**](FileCredentialsIn.md)|  | 

### Return type

[**FileCredentialsOut**](FileCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fivetran_credentials**
> FivetranCredentialsOut create_fivetran_credentials(fivetran_credentials_in)

Create Fivetran credentials

Store Fivetran credentials.

Monte Carlo keeps the API key and its secret and returns everything else. Nothing is
checked against Fivetran here. An account holds a limited number of credentials; past that the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.fivetran_credentials_in import FivetranCredentialsIn
from pycarlo2.models.fivetran_credentials_out import FivetranCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    fivetran_credentials_in = pycarlo2.FivetranCredentialsIn() # FivetranCredentialsIn | 

    try:
        # Create Fivetran credentials
        api_response = api_instance.create_fivetran_credentials(fivetran_credentials_in)
        print("The response of CredentialsApi->create_fivetran_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_fivetran_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fivetran_credentials_in** | [**FivetranCredentialsIn**](FivetranCredentialsIn.md)|  | 

### Return type

[**FivetranCredentialsOut**](FivetranCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_dataform_credentials**
> GcpDataformCredentialsOut create_gcp_dataform_credentials(gcp_dataform_credentials_in)

Create GCP Dataform credentials

Store GCP Dataform credentials.

Monte Carlo keeps the key and returns everything else. Nothing is checked against
GCP Dataform here. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_dataform_credentials_in import GcpDataformCredentialsIn
from pycarlo2.models.gcp_dataform_credentials_out import GcpDataformCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    gcp_dataform_credentials_in = pycarlo2.GcpDataformCredentialsIn() # GcpDataformCredentialsIn | 

    try:
        # Create GCP Dataform credentials
        api_response = api_instance.create_gcp_dataform_credentials(gcp_dataform_credentials_in)
        print("The response of CredentialsApi->create_gcp_dataform_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_gcp_dataform_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_dataform_credentials_in** | [**GcpDataformCredentialsIn**](GcpDataformCredentialsIn.md)|  | 

### Return type

[**GcpDataformCredentialsOut**](GcpDataformCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_gcp_secret_manager_credentials**
> GcpSecretManagerCredentialsOut create_gcp_secret_manager_credentials(gcp_secret_manager_credentials_in)

Create GCP Secret Manager credentials

Store where a connection's credentials live in your GCP Secret Manager.

Monte Carlo keeps the reference, not the secret, and reads the secret from your store each
time the connection is used. Create the credentials first, then create a connection that
references them. Nothing is checked against GCP here.

`connection_type` names what the secret holds credentials for, and is fixed once created.
An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_secret_manager_credentials_in import GcpSecretManagerCredentialsIn
from pycarlo2.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    gcp_secret_manager_credentials_in = pycarlo2.GcpSecretManagerCredentialsIn() # GcpSecretManagerCredentialsIn | 

    try:
        # Create GCP Secret Manager credentials
        api_response = api_instance.create_gcp_secret_manager_credentials(gcp_secret_manager_credentials_in)
        print("The response of CredentialsApi->create_gcp_secret_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_gcp_secret_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_secret_manager_credentials_in** | [**GcpSecretManagerCredentialsIn**](GcpSecretManagerCredentialsIn.md)|  | 

### Return type

[**GcpSecretManagerCredentialsOut**](GcpSecretManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_glue_credentials**
> GlueCredentialsOut create_glue_credentials(glue_credentials_in)

Create Glue credentials

Store the IAM role Monte Carlo assumes to read your Glue catalog.

Glue needs no secret. Create the credentials first, then create a connection that
references them on a `data-lake` warehouse. Nothing is checked against AWS here.

An account holds a limited number of credentials. Past that, the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.glue_credentials_in import GlueCredentialsIn
from pycarlo2.models.glue_credentials_out import GlueCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    glue_credentials_in = pycarlo2.GlueCredentialsIn() # GlueCredentialsIn | 

    try:
        # Create Glue credentials
        api_response = api_instance.create_glue_credentials(glue_credentials_in)
        print("The response of CredentialsApi->create_glue_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_glue_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glue_credentials_in** | [**GlueCredentialsIn**](GlueCredentialsIn.md)|  | 

### Return type

[**GlueCredentialsOut**](GlueCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_informatica_v2_credentials**
> InformaticaV2CredentialsOut create_informatica_v2_credentials(informatica_v2_credentials_in)

Create Informatica credentials

Store Informatica credentials.

Monte Carlo keeps the passwords and the client secret and returns everything else. Nothing is
checked against Informatica here.

`auth_mode` decides what else to send: `username` and `password` for `password`, or `org_id` and
the `oauth_*` fields for `oauth`. An account holds a limited number of credentials; past that
the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.informatica_v2_credentials_in import InformaticaV2CredentialsIn
from pycarlo2.models.informatica_v2_credentials_out import InformaticaV2CredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    informatica_v2_credentials_in = pycarlo2.InformaticaV2CredentialsIn() # InformaticaV2CredentialsIn | 

    try:
        # Create Informatica credentials
        api_response = api_instance.create_informatica_v2_credentials(informatica_v2_credentials_in)
        print("The response of CredentialsApi->create_informatica_v2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_informatica_v2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **informatica_v2_credentials_in** | [**InformaticaV2CredentialsIn**](InformaticaV2CredentialsIn.md)|  | 

### Return type

[**InformaticaV2CredentialsOut**](InformaticaV2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_looker_credentials**
> LookerCredentialsOut create_looker_credentials(looker_credentials_in)

Create Looker credentials

Store Looker API credentials.

Monte Carlo keeps the client secret and returns everything else. Create the credentials
first, then create a connection that references them, on a Looker BI container. Nothing is
checked against Looker here. An account holds a limited number of credentials; past that
the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_credentials_in import LookerCredentialsIn
from pycarlo2.models.looker_credentials_out import LookerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    looker_credentials_in = pycarlo2.LookerCredentialsIn() # LookerCredentialsIn | 

    try:
        # Create Looker credentials
        api_response = api_instance.create_looker_credentials(looker_credentials_in)
        print("The response of CredentialsApi->create_looker_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_looker_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **looker_credentials_in** | [**LookerCredentialsIn**](LookerCredentialsIn.md)|  | 

### Return type

[**LookerCredentialsOut**](LookerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_looker_git_clone_credentials**
> LookerGitCloneCredentialsOut create_looker_git_clone_credentials(looker_git_clone_credentials_in)

Create LookML repository credentials

Store credentials for cloning a LookML repository.

Monte Carlo keeps the token or the SSH key and returns everything else. Create the
credentials first, then create a connection that references them, on the Looker BI
container that holds the Looker API connection. Nothing is checked against the
repository here.

Send `username` and `token` for an HTTPS clone, or `ssh_key` for an SSH clone. An account
holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_git_clone_credentials_in import LookerGitCloneCredentialsIn
from pycarlo2.models.looker_git_clone_credentials_out import LookerGitCloneCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    looker_git_clone_credentials_in = pycarlo2.LookerGitCloneCredentialsIn() # LookerGitCloneCredentialsIn | 

    try:
        # Create LookML repository credentials
        api_response = api_instance.create_looker_git_clone_credentials(looker_git_clone_credentials_in)
        print("The response of CredentialsApi->create_looker_git_clone_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_looker_git_clone_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **looker_git_clone_credentials_in** | [**LookerGitCloneCredentialsIn**](LookerGitCloneCredentialsIn.md)|  | 

### Return type

[**LookerGitCloneCredentialsOut**](LookerGitCloneCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mariadb_credentials**
> MariaDbCredentialsOut create_mariadb_credentials(maria_db_credentials_in)

Create MariaDB credentials

Store a MariaDB login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against MariaDB here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.maria_db_credentials_in import MariaDbCredentialsIn
from pycarlo2.models.maria_db_credentials_out import MariaDbCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    maria_db_credentials_in = pycarlo2.MariaDbCredentialsIn() # MariaDbCredentialsIn | 

    try:
        # Create MariaDB credentials
        api_response = api_instance.create_mariadb_credentials(maria_db_credentials_in)
        print("The response of CredentialsApi->create_mariadb_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_mariadb_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maria_db_credentials_in** | [**MariaDbCredentialsIn**](MariaDbCredentialsIn.md)|  | 

### Return type

[**MariaDbCredentialsOut**](MariaDbCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mulesoft_credentials**
> MulesoftCredentialsOut create_mulesoft_credentials(mulesoft_credentials_in)

Create MuleSoft credentials

Store MuleSoft credentials.

Monte Carlo keeps the client secret and returns everything else. Nothing is checked
against MuleSoft here. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.mulesoft_credentials_in import MulesoftCredentialsIn
from pycarlo2.models.mulesoft_credentials_out import MulesoftCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    mulesoft_credentials_in = pycarlo2.MulesoftCredentialsIn() # MulesoftCredentialsIn | 

    try:
        # Create MuleSoft credentials
        api_response = api_instance.create_mulesoft_credentials(mulesoft_credentials_in)
        print("The response of CredentialsApi->create_mulesoft_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_mulesoft_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mulesoft_credentials_in** | [**MulesoftCredentialsIn**](MulesoftCredentialsIn.md)|  | 

### Return type

[**MulesoftCredentialsOut**](MulesoftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mysql_credentials**
> MySqlCredentialsOut create_mysql_credentials(my_sql_credentials_in)

Create MySQL credentials

Store a MySQL login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against MySQL here.

Send `ssl_ca_data` to check the server against your own CA, or `ssl_disabled` to connect without
TLS. The two cannot be combined. An account holds a limited number of credentials; past that the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.my_sql_credentials_in import MySqlCredentialsIn
from pycarlo2.models.my_sql_credentials_out import MySqlCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    my_sql_credentials_in = pycarlo2.MySqlCredentialsIn() # MySqlCredentialsIn | 

    try:
        # Create MySQL credentials
        api_response = api_instance.create_mysql_credentials(my_sql_credentials_in)
        print("The response of CredentialsApi->create_mysql_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_mysql_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **my_sql_credentials_in** | [**MySqlCredentialsIn**](MySqlCredentialsIn.md)|  | 

### Return type

[**MySqlCredentialsOut**](MySqlCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_oracle_credentials**
> OracleCredentialsOut create_oracle_credentials(oracle_credentials_in)

Create Oracle credentials

Store an Oracle login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Oracle here.

Send `ssl_ca_data` to check the server against your own CA, or `ssl_disabled` to connect without
TLS. The two cannot be combined. An account holds a limited number of credentials; past that the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.oracle_credentials_in import OracleCredentialsIn
from pycarlo2.models.oracle_credentials_out import OracleCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    oracle_credentials_in = pycarlo2.OracleCredentialsIn() # OracleCredentialsIn | 

    try:
        # Create Oracle credentials
        api_response = api_instance.create_oracle_credentials(oracle_credentials_in)
        print("The response of CredentialsApi->create_oracle_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_oracle_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oracle_credentials_in** | [**OracleCredentialsIn**](OracleCredentialsIn.md)|  | 

### Return type

[**OracleCredentialsOut**](OracleCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_postgres_credentials**
> PostgresCredentialsOut create_postgres_credentials(postgres_credentials_in)

Create PostgreSQL credentials

Store a PostgreSQL login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against PostgreSQL here.

Send `ssl_ca_data` to check the server against your own CA, or `ssl_disabled` to connect without
TLS. The two cannot be combined. An account holds a limited number of credentials; past that the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.postgres_credentials_in import PostgresCredentialsIn
from pycarlo2.models.postgres_credentials_out import PostgresCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    postgres_credentials_in = pycarlo2.PostgresCredentialsIn() # PostgresCredentialsIn | 

    try:
        # Create PostgreSQL credentials
        api_response = api_instance.create_postgres_credentials(postgres_credentials_in)
        print("The response of CredentialsApi->create_postgres_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_postgres_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postgres_credentials_in** | [**PostgresCredentialsIn**](PostgresCredentialsIn.md)|  | 

### Return type

[**PostgresCredentialsOut**](PostgresCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_power_bi_credentials**
> PowerBiCredentialsOut create_power_bi_credentials(power_bi_credentials_in)

Create Power BI credentials

Store Power BI credentials.

Monte Carlo keeps the client secret or the password and returns everything else. Create
the credentials first, then create a connection that references them, on a Power BI
container. Nothing is checked against Power BI here.

`auth_mode` decides what else to send: `app_client_secret` for `service_principal`, or
`username` and `password` for `primary_user`. An account holds a limited number of
credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.power_bi_credentials_in import PowerBiCredentialsIn
from pycarlo2.models.power_bi_credentials_out import PowerBiCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    power_bi_credentials_in = pycarlo2.PowerBiCredentialsIn() # PowerBiCredentialsIn | 

    try:
        # Create Power BI credentials
        api_response = api_instance.create_power_bi_credentials(power_bi_credentials_in)
        print("The response of CredentialsApi->create_power_bi_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_power_bi_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_bi_credentials_in** | [**PowerBiCredentialsIn**](PowerBiCredentialsIn.md)|  | 

### Return type

[**PowerBiCredentialsOut**](PowerBiCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_redshift_credentials**
> RedshiftCredentialsOut create_redshift_credentials(redshift_credentials_in)

Create Redshift credentials

Store a Redshift login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first,
then create a connection that references them. Nothing is checked against Redshift here.

Send `ssl_ca_data` to check the server against your own CA, or `ssl_disabled` to connect
without TLS. The two cannot be combined. An account holds a limited number of credentials;
past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.redshift_credentials_in import RedshiftCredentialsIn
from pycarlo2.models.redshift_credentials_out import RedshiftCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    redshift_credentials_in = pycarlo2.RedshiftCredentialsIn() # RedshiftCredentialsIn | 

    try:
        # Create Redshift credentials
        api_response = api_instance.create_redshift_credentials(redshift_credentials_in)
        print("The response of CredentialsApi->create_redshift_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_redshift_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redshift_credentials_in** | [**RedshiftCredentialsIn**](RedshiftCredentialsIn.md)|  | 

### Return type

[**RedshiftCredentialsOut**](RedshiftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_salesforce_crm_credentials**
> SalesforceCrmCredentialsOut create_salesforce_crm_credentials(salesforce_crm_credentials_in)

Create Salesforce CRM credentials

Store a Salesforce sign-in for connections to use.

Monte Carlo keeps the password, the security token or the consumer secret and returns
everything else. Create the credentials first, then create a connection that references
them. Nothing is checked against Salesforce here.

`auth_mode` decides what else to send: `username`, `password` and `security_token` for
`password`, or `consumer_key`, `consumer_secret` and `domain` for
`oauth_client_credentials`. An account holds a limited number of credentials. Past that, the
create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.salesforce_crm_credentials_in import SalesforceCrmCredentialsIn
from pycarlo2.models.salesforce_crm_credentials_out import SalesforceCrmCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    salesforce_crm_credentials_in = pycarlo2.SalesforceCrmCredentialsIn() # SalesforceCrmCredentialsIn | 

    try:
        # Create Salesforce CRM credentials
        api_response = api_instance.create_salesforce_crm_credentials(salesforce_crm_credentials_in)
        print("The response of CredentialsApi->create_salesforce_crm_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_salesforce_crm_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_crm_credentials_in** | [**SalesforceCrmCredentialsIn**](SalesforceCrmCredentialsIn.md)|  | 

### Return type

[**SalesforceCrmCredentialsOut**](SalesforceCrmCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sap_hana_credentials**
> SapHanaCredentialsOut create_sap_hana_credentials(sap_hana_credentials_in)

Create SAP HANA credentials

Store a SAP HANA login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against SAP HANA here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sap_hana_credentials_in import SapHanaCredentialsIn
from pycarlo2.models.sap_hana_credentials_out import SapHanaCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    sap_hana_credentials_in = pycarlo2.SapHanaCredentialsIn() # SapHanaCredentialsIn | 

    try:
        # Create SAP HANA credentials
        api_response = api_instance.create_sap_hana_credentials(sap_hana_credentials_in)
        print("The response of CredentialsApi->create_sap_hana_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_sap_hana_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sap_hana_credentials_in** | [**SapHanaCredentialsIn**](SapHanaCredentialsIn.md)|  | 

### Return type

[**SapHanaCredentialsOut**](SapHanaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snowflake_credentials**
> SnowflakeCredentialsOut create_snowflake_credentials(snowflake_credentials_in)

Create Snowflake credentials

Store a Snowflake key pair for connections to use.

Monte Carlo keeps the private key and returns only the account, user and warehouse. Create
the credentials first, then create a connection that references them. Nothing is checked
against Snowflake here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.snowflake_credentials_in import SnowflakeCredentialsIn
from pycarlo2.models.snowflake_credentials_out import SnowflakeCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    snowflake_credentials_in = pycarlo2.SnowflakeCredentialsIn() # SnowflakeCredentialsIn | 

    try:
        # Create Snowflake credentials
        api_response = api_instance.create_snowflake_credentials(snowflake_credentials_in)
        print("The response of CredentialsApi->create_snowflake_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_snowflake_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snowflake_credentials_in** | [**SnowflakeCredentialsIn**](SnowflakeCredentialsIn.md)|  | 

### Return type

[**SnowflakeCredentialsOut**](SnowflakeCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sql_server_credentials**
> SqlServerCredentialsOut create_sql_server_credentials(sql_server_credentials_in)

Create SQL Server credentials

Store a SQL Server login for connections to use.

Monte Carlo keeps the password or the keytab and returns everything else. Create the
credentials first, then create a connection that references them. Nothing is checked
against SQL Server here.

`auth_mode` decides what else to send: `user` and `password` for `sql`, or `realm`, `kdc`,
`principal` and one of `keytab_base64` or `password` for `kerberos`. An account holds a
limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sql_server_credentials_in import SqlServerCredentialsIn
from pycarlo2.models.sql_server_credentials_out import SqlServerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    sql_server_credentials_in = pycarlo2.SqlServerCredentialsIn() # SqlServerCredentialsIn | 

    try:
        # Create SQL Server credentials
        api_response = api_instance.create_sql_server_credentials(sql_server_credentials_in)
        print("The response of CredentialsApi->create_sql_server_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_sql_server_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_server_credentials_in** | [**SqlServerCredentialsIn**](SqlServerCredentialsIn.md)|  | 

### Return type

[**SqlServerCredentialsOut**](SqlServerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_starburst_enterprise_credentials**
> StarburstEnterpriseCredentialsOut create_starburst_enterprise_credentials(starburst_enterprise_credentials_in)

Create Starburst Enterprise credentials

Store a Starburst Enterprise login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Starburst Enterprise here.

The connection always uses TLS. Send `ssl_ca_data` to check the server against your own CA, or
`ssl_disabled` to skip the certificate check. The two cannot be combined. An account holds a
limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_enterprise_credentials_in import StarburstEnterpriseCredentialsIn
from pycarlo2.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    starburst_enterprise_credentials_in = pycarlo2.StarburstEnterpriseCredentialsIn() # StarburstEnterpriseCredentialsIn | 

    try:
        # Create Starburst Enterprise credentials
        api_response = api_instance.create_starburst_enterprise_credentials(starburst_enterprise_credentials_in)
        print("The response of CredentialsApi->create_starburst_enterprise_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_starburst_enterprise_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starburst_enterprise_credentials_in** | [**StarburstEnterpriseCredentialsIn**](StarburstEnterpriseCredentialsIn.md)|  | 

### Return type

[**StarburstEnterpriseCredentialsOut**](StarburstEnterpriseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_starburst_galaxy_credentials**
> StarburstGalaxyCredentialsOut create_starburst_galaxy_credentials(starburst_galaxy_credentials_in)

Create Starburst Galaxy credentials

Store a Starburst Galaxy login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Starburst Galaxy here.

An account holds a limited number of credentials; past that the create is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_galaxy_credentials_in import StarburstGalaxyCredentialsIn
from pycarlo2.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    starburst_galaxy_credentials_in = pycarlo2.StarburstGalaxyCredentialsIn() # StarburstGalaxyCredentialsIn | 

    try:
        # Create Starburst Galaxy credentials
        api_response = api_instance.create_starburst_galaxy_credentials(starburst_galaxy_credentials_in)
        print("The response of CredentialsApi->create_starburst_galaxy_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_starburst_galaxy_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starburst_galaxy_credentials_in** | [**StarburstGalaxyCredentialsIn**](StarburstGalaxyCredentialsIn.md)|  | 

### Return type

[**StarburstGalaxyCredentialsOut**](StarburstGalaxyCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tableau_credentials**
> TableauCredentialsOut create_tableau_credentials(tableau_credentials_in)

Create Tableau credentials

Store Tableau credentials.

Monte Carlo keeps the password or the secret and returns everything else. Create the
credentials first, then create a connection that references them, on a Tableau BI
container. Nothing is checked against Tableau here.

Send one way to sign in: `username` and `password`, `token_name` and `token_value` for a
personal access token, or `username` with the three `connected_app_*` fields for a
connected app. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.tableau_credentials_in import TableauCredentialsIn
from pycarlo2.models.tableau_credentials_out import TableauCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    tableau_credentials_in = pycarlo2.TableauCredentialsIn() # TableauCredentialsIn | 

    try:
        # Create Tableau credentials
        api_response = api_instance.create_tableau_credentials(tableau_credentials_in)
        print("The response of CredentialsApi->create_tableau_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_tableau_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tableau_credentials_in** | [**TableauCredentialsIn**](TableauCredentialsIn.md)|  | 

### Return type

[**TableauCredentialsOut**](TableauCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_teradata_credentials**
> TeradataCredentialsOut create_teradata_credentials(teradata_credentials_in)

Create Teradata credentials

Store a Teradata login for connections to use.

Monte Carlo keeps the password and returns everything else. Create the credentials first, then
create a connection that references them. Nothing is checked against Teradata here.

Send `ssl_ca_data` to check the server against your own CA. `td_sslmode` decides whether the
connection uses TLS. An account holds a limited number of credentials; past that the create is
refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.teradata_credentials_in import TeradataCredentialsIn
from pycarlo2.models.teradata_credentials_out import TeradataCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    teradata_credentials_in = pycarlo2.TeradataCredentialsIn() # TeradataCredentialsIn | 

    try:
        # Create Teradata credentials
        api_response = api_instance.create_teradata_credentials(teradata_credentials_in)
        print("The response of CredentialsApi->create_teradata_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_teradata_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teradata_credentials_in** | [**TeradataCredentialsIn**](TeradataCredentialsIn.md)|  | 

### Return type

[**TeradataCredentialsOut**](TeradataCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_airflow_credentials**
> delete_airflow_credentials(credentials_id)

Delete Airflow credentials

Delete Airflow connection details.

Refused while a connection still uses them. Delete the connection first.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Airflow credentials
        api_instance.delete_airflow_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_airflow_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_athena_credentials**
> delete_athena_credentials(credentials_id)

Delete Athena credentials

Delete Athena credentials.

Refused while a connection still uses them. Delete the connection first. The role in your
AWS account is left as it is.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Athena credentials
        api_instance.delete_athena_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_athena_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_secrets_manager_credentials**
> delete_aws_secrets_manager_credentials(credentials_id)

Delete AWS Secrets Manager credentials

Delete AWS Secrets Manager credentials.

Refused while a connection still uses them. Delete the connection first. The secret in AWS
is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete AWS Secrets Manager credentials
        api_instance.delete_aws_secrets_manager_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_aws_secrets_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_data_factory_credentials**
> delete_azure_data_factory_credentials(credentials_id)

Delete Azure Data Factory credentials

Delete Azure Data Factory credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored client secret. Rotate it in Microsoft Entra ID if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Azure Data Factory credentials
        api_instance.delete_azure_data_factory_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_data_factory_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_dedicated_sql_pool_credentials**
> delete_azure_dedicated_sql_pool_credentials(credentials_id)

Delete Azure Dedicated SQL Pool credentials

Delete Azure Dedicated SQL Pool credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Azure Dedicated SQL Pool if the password itself must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Azure Dedicated SQL Pool credentials
        api_instance.delete_azure_dedicated_sql_pool_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_dedicated_sql_pool_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_key_vault_credentials**
> delete_azure_key_vault_credentials(credentials_id)

Delete Azure Key Vault credentials

Delete Azure Key Vault credentials.

Refused while a connection still uses them. Delete the connection first. The secret in Azure
is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Azure Key Vault credentials
        api_instance.delete_azure_key_vault_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_key_vault_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_azure_sql_database_credentials**
> delete_azure_sql_database_credentials(credentials_id)

Delete Azure SQL Database credentials

Delete Azure SQL Database credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Azure SQL Database if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Azure SQL Database credentials
        api_instance.delete_azure_sql_database_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_sql_database_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bigquery_credentials**
> delete_bigquery_credentials(credentials_id)

Delete BigQuery credentials

Delete BigQuery credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored key. Revoke the key in Google Cloud if the key itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete BigQuery credentials
        api_instance.delete_bigquery_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_bigquery_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_clickhouse_credentials**
> delete_clickhouse_credentials(credentials_id)

Delete ClickHouse credentials

Delete ClickHouse credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in ClickHouse if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete ClickHouse credentials
        api_instance.delete_clickhouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_clickhouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credentials**
> delete_credentials(credentials_id)

Delete credentials

Delete credentials of any connection type and storage.

Takes the id the list or a connection returns. Refused while a connection still uses them.
Delete the connection first. Monte Carlo stops using them. Whatever they point at is
untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete credentials
        api_instance.delete_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_databricks_metastore_sql_warehouse_credentials**
> delete_databricks_metastore_sql_warehouse_credentials(credentials_id)

Delete Databricks metadata collection credentials

Delete Databricks metadata collection credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored token or OAuth secret. Revoke it in Databricks, or in Microsoft Entra ID
for a service principal Azure manages, if the secret itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Databricks metadata collection credentials
        api_instance.delete_databricks_metastore_sql_warehouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_databricks_sql_warehouse_credentials**
> delete_databricks_sql_warehouse_credentials(credentials_id)

Delete Databricks query credentials

Delete Databricks query credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored token or OAuth secret. Revoke it in Databricks, or in Microsoft Entra ID
for a service principal Azure manages, if the secret itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Databricks query credentials
        api_instance.delete_databricks_sql_warehouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_databricks_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_db2_credentials**
> delete_db2_credentials(credentials_id)

Delete Db2 credentials

Delete Db2 credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Db2 if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Db2 credentials
        api_instance.delete_db2_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_db2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dbt_cloud_webhook_credentials**
> delete_dbt_cloud_webhook_credentials(credentials_id)

Delete dbt Cloud webhook credentials

Delete dbt Cloud webhook credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored service token and HMAC secret. Delete the token and the webhook in dbt
Cloud if they must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete dbt Cloud webhook credentials
        api_instance.delete_dbt_cloud_webhook_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_dbt_cloud_webhook_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_env_var_credentials**
> delete_env_var_credentials(credentials_id)

Delete environment variable credentials

Delete environment variable credentials.

Refused while a connection still uses them. Delete the connection first. The variable on the
deployment is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete environment variable credentials
        api_instance.delete_env_var_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_env_var_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_credentials**
> delete_file_credentials(credentials_id)

Delete file credentials

Delete file credentials.

Refused while a connection still uses them. Delete the connection first. The file on the
deployment is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete file credentials
        api_instance.delete_file_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_file_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fivetran_credentials**
> delete_fivetran_credentials(credentials_id)

Delete Fivetran credentials

Delete Fivetran credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored API key and secret. Delete the API key in Fivetran if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Fivetran credentials
        api_instance.delete_fivetran_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_fivetran_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gcp_dataform_credentials**
> delete_gcp_dataform_credentials(credentials_id)

Delete GCP Dataform credentials

Delete GCP Dataform credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored service account key. Delete the key in Google Cloud if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete GCP Dataform credentials
        api_instance.delete_gcp_dataform_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_gcp_dataform_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gcp_secret_manager_credentials**
> delete_gcp_secret_manager_credentials(credentials_id)

Delete GCP Secret Manager credentials

Delete GCP Secret Manager credentials.

Refused while a connection still uses them. Delete the connection first. The secret in GCP
is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete GCP Secret Manager credentials
        api_instance.delete_gcp_secret_manager_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_gcp_secret_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_glue_credentials**
> delete_glue_credentials(credentials_id)

Delete Glue credentials

Delete Glue credentials.

Refused while a connection still uses them. Delete the connection first. The role in your
AWS account is left as it is.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Glue credentials
        api_instance.delete_glue_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_glue_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_informatica_v2_credentials**
> delete_informatica_v2_credentials(credentials_id)

Delete Informatica credentials

Delete Informatica credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password or client secret. Rotate it in Informatica or your identity provider if it
must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Informatica credentials
        api_instance.delete_informatica_v2_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_informatica_v2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_looker_credentials**
> delete_looker_credentials(credentials_id)

Delete Looker credentials

Delete Looker API credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored client secret. Delete the API key in Looker if the secret itself must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Looker credentials
        api_instance.delete_looker_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_looker_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_looker_git_clone_credentials**
> delete_looker_git_clone_credentials(credentials_id)

Delete LookML repository credentials

Delete LookML repository credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored token or SSH key. Revoke it on the git server if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete LookML repository credentials
        api_instance.delete_looker_git_clone_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_looker_git_clone_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mariadb_credentials**
> delete_mariadb_credentials(credentials_id)

Delete MariaDB credentials

Delete MariaDB credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in MariaDB if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete MariaDB credentials
        api_instance.delete_mariadb_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_mariadb_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mulesoft_credentials**
> delete_mulesoft_credentials(credentials_id)

Delete MuleSoft credentials

Delete MuleSoft credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored client secret. Rotate it in Anypoint if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete MuleSoft credentials
        api_instance.delete_mulesoft_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_mulesoft_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mysql_credentials**
> delete_mysql_credentials(credentials_id)

Delete MySQL credentials

Delete MySQL credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in MySQL if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete MySQL credentials
        api_instance.delete_mysql_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_mysql_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_oracle_credentials**
> delete_oracle_credentials(credentials_id)

Delete Oracle credentials

Delete Oracle credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Oracle if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Oracle credentials
        api_instance.delete_oracle_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_oracle_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_postgres_credentials**
> delete_postgres_credentials(credentials_id)

Delete PostgreSQL credentials

Delete PostgreSQL credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in PostgreSQL if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete PostgreSQL credentials
        api_instance.delete_postgres_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_postgres_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_power_bi_credentials**
> delete_power_bi_credentials(credentials_id)

Delete Power BI credentials

Delete Power BI credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored client secret or password. Rotate it in Microsoft Entra ID if it must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Power BI credentials
        api_instance.delete_power_bi_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_power_bi_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_redshift_credentials**
> delete_redshift_credentials(credentials_id)

Delete Redshift credentials

Delete Redshift credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored password. Change it in Redshift if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Redshift credentials
        api_instance.delete_redshift_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_redshift_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_salesforce_crm_credentials**
> delete_salesforce_crm_credentials(credentials_id)

Delete Salesforce CRM credentials

Delete Salesforce CRM credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored password, security token or consumer secret. Reset them in Salesforce if
they must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Salesforce CRM credentials
        api_instance.delete_salesforce_crm_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_salesforce_crm_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sap_hana_credentials**
> delete_sap_hana_credentials(credentials_id)

Delete SAP HANA credentials

Delete SAP HANA credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in SAP HANA if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete SAP HANA credentials
        api_instance.delete_sap_hana_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_sap_hana_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snowflake_credentials**
> delete_snowflake_credentials(credentials_id)

Delete Snowflake credentials

Delete Snowflake credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored key. Rotate or revoke the key pair in Snowflake if the key itself must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Snowflake credentials
        api_instance.delete_snowflake_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_snowflake_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sql_server_credentials**
> delete_sql_server_credentials(credentials_id)

Delete SQL Server credentials

Delete SQL Server credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored password or keytab. Change the password in SQL Server or Active Directory
if it must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete SQL Server credentials
        api_instance.delete_sql_server_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_sql_server_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_starburst_enterprise_credentials**
> delete_starburst_enterprise_credentials(credentials_id)

Delete Starburst Enterprise credentials

Delete Starburst Enterprise credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Starburst Enterprise if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Starburst Enterprise credentials
        api_instance.delete_starburst_enterprise_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_starburst_enterprise_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_starburst_galaxy_credentials**
> delete_starburst_galaxy_credentials(credentials_id)

Delete Starburst Galaxy credentials

Delete Starburst Galaxy credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Starburst Galaxy if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Starburst Galaxy credentials
        api_instance.delete_starburst_galaxy_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_starburst_galaxy_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tableau_credentials**
> delete_tableau_credentials(credentials_id)

Delete Tableau credentials

Delete Tableau credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored password or secret. Revoke it in Tableau if the secret itself must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Tableau credentials
        api_instance.delete_tableau_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_tableau_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_teradata_credentials**
> delete_teradata_credentials(credentials_id)

Delete Teradata credentials

Delete Teradata credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it where Teradata checks it if the password itself must be
retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Delete Teradata credentials
        api_instance.delete_teradata_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_teradata_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

void (empty response body)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airflow_credentials**
> AirflowCredentialsOut get_airflow_credentials(credentials_id)

Get Airflow credentials

Get one set of Airflow connection details.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.airflow_credentials_out import AirflowCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Airflow credentials
        api_response = api_instance.get_airflow_credentials(credentials_id)
        print("The response of CredentialsApi->get_airflow_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_airflow_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**AirflowCredentialsOut**](AirflowCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_athena_credentials**
> AthenaCredentialsOut get_athena_credentials(credentials_id)

Get Athena credentials

Get one set of Athena credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.athena_credentials_out import AthenaCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Athena credentials
        api_response = api_instance.get_athena_credentials(credentials_id)
        print("The response of CredentialsApi->get_athena_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_athena_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**AthenaCredentialsOut**](AthenaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_secrets_manager_credentials**
> AwsSecretsManagerCredentialsOut get_aws_secrets_manager_credentials(credentials_id)

Get AWS Secrets Manager credentials

Get one set of AWS Secrets Manager credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get AWS Secrets Manager credentials
        api_response = api_instance.get_aws_secrets_manager_credentials(credentials_id)
        print("The response of CredentialsApi->get_aws_secrets_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_aws_secrets_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**AwsSecretsManagerCredentialsOut**](AwsSecretsManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_data_factory_credentials**
> AzureDataFactoryCredentialsOut get_azure_data_factory_credentials(credentials_id)

Get Azure Data Factory credentials

Get one set of Azure Data Factory credentials, without the client secret.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_data_factory_credentials_out import AzureDataFactoryCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Azure Data Factory credentials
        api_response = api_instance.get_azure_data_factory_credentials(credentials_id)
        print("The response of CredentialsApi->get_azure_data_factory_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_azure_data_factory_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**AzureDataFactoryCredentialsOut**](AzureDataFactoryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_dedicated_sql_pool_credentials**
> AzureDedicatedSqlPoolCredentialsOut get_azure_dedicated_sql_pool_credentials(credentials_id)

Get Azure Dedicated SQL Pool credentials

Get one set of Azure Dedicated SQL Pool credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Azure Dedicated SQL Pool credentials
        api_response = api_instance.get_azure_dedicated_sql_pool_credentials(credentials_id)
        print("The response of CredentialsApi->get_azure_dedicated_sql_pool_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_azure_dedicated_sql_pool_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**AzureDedicatedSqlPoolCredentialsOut**](AzureDedicatedSqlPoolCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_key_vault_credentials**
> AzureKeyVaultCredentialsOut get_azure_key_vault_credentials(credentials_id)

Get Azure Key Vault credentials

Get one set of Azure Key Vault credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Azure Key Vault credentials
        api_response = api_instance.get_azure_key_vault_credentials(credentials_id)
        print("The response of CredentialsApi->get_azure_key_vault_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_azure_key_vault_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**AzureKeyVaultCredentialsOut**](AzureKeyVaultCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_azure_sql_database_credentials**
> AzureSqlDatabaseCredentialsOut get_azure_sql_database_credentials(credentials_id)

Get Azure SQL Database credentials

Get one set of Azure SQL Database credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Azure SQL Database credentials
        api_response = api_instance.get_azure_sql_database_credentials(credentials_id)
        print("The response of CredentialsApi->get_azure_sql_database_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_azure_sql_database_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**AzureSqlDatabaseCredentialsOut**](AzureSqlDatabaseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bigquery_credentials**
> BigQueryCredentialsOut get_bigquery_credentials(credentials_id)

Get BigQuery credentials

Get one set of BigQuery credentials, without the key.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.big_query_credentials_out import BigQueryCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get BigQuery credentials
        api_response = api_instance.get_bigquery_credentials(credentials_id)
        print("The response of CredentialsApi->get_bigquery_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_bigquery_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**BigQueryCredentialsOut**](BigQueryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clickhouse_credentials**
> ClickHouseCredentialsOut get_clickhouse_credentials(credentials_id)

Get ClickHouse credentials

Get one set of ClickHouse credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.click_house_credentials_out import ClickHouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get ClickHouse credentials
        api_response = api_instance.get_clickhouse_credentials(credentials_id)
        print("The response of CredentialsApi->get_clickhouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_clickhouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**ClickHouseCredentialsOut**](ClickHouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databricks_metastore_sql_warehouse_credentials**
> DatabricksMetastoreSqlWarehouseCredentialsOut get_databricks_metastore_sql_warehouse_credentials(credentials_id)

Get Databricks metadata collection credentials

Get one set of Databricks metadata collection credentials, without the secrets.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Databricks metadata collection credentials
        api_response = api_instance.get_databricks_metastore_sql_warehouse_credentials(credentials_id)
        print("The response of CredentialsApi->get_databricks_metastore_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**DatabricksMetastoreSqlWarehouseCredentialsOut**](DatabricksMetastoreSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databricks_sql_warehouse_credentials**
> DatabricksSqlWarehouseCredentialsOut get_databricks_sql_warehouse_credentials(credentials_id)

Get Databricks query credentials

Get one set of Databricks query credentials, without the secrets.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Databricks query credentials
        api_response = api_instance.get_databricks_sql_warehouse_credentials(credentials_id)
        print("The response of CredentialsApi->get_databricks_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_databricks_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**DatabricksSqlWarehouseCredentialsOut**](DatabricksSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_db2_credentials**
> Db2CredentialsOut get_db2_credentials(credentials_id)

Get Db2 credentials

Get one set of Db2 credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.db2_credentials_out import Db2CredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Db2 credentials
        api_response = api_instance.get_db2_credentials(credentials_id)
        print("The response of CredentialsApi->get_db2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_db2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**Db2CredentialsOut**](Db2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dbt_cloud_webhook_credentials**
> DbtCloudWebhookCredentialsOut get_dbt_cloud_webhook_credentials(credentials_id)

Get dbt Cloud webhook credentials

Get one set of dbt Cloud webhook credentials, without the service token and the HMAC
secret.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.dbt_cloud_webhook_credentials_out import DbtCloudWebhookCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get dbt Cloud webhook credentials
        api_response = api_instance.get_dbt_cloud_webhook_credentials(credentials_id)
        print("The response of CredentialsApi->get_dbt_cloud_webhook_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_dbt_cloud_webhook_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**DbtCloudWebhookCredentialsOut**](DbtCloudWebhookCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_env_var_credentials**
> EnvVarCredentialsOut get_env_var_credentials(credentials_id)

Get environment variable credentials

Get one set of environment variable credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.env_var_credentials_out import EnvVarCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get environment variable credentials
        api_response = api_instance.get_env_var_credentials(credentials_id)
        print("The response of CredentialsApi->get_env_var_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_env_var_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**EnvVarCredentialsOut**](EnvVarCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_credentials**
> FileCredentialsOut get_file_credentials(credentials_id)

Get file credentials

Get one set of file credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.file_credentials_out import FileCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get file credentials
        api_response = api_instance.get_file_credentials(credentials_id)
        print("The response of CredentialsApi->get_file_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_file_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**FileCredentialsOut**](FileCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fivetran_credentials**
> FivetranCredentialsOut get_fivetran_credentials(credentials_id)

Get Fivetran credentials

Get one set of Fivetran credentials, without the API key and its secret.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.fivetran_credentials_out import FivetranCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Fivetran credentials
        api_response = api_instance.get_fivetran_credentials(credentials_id)
        print("The response of CredentialsApi->get_fivetran_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_fivetran_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**FivetranCredentialsOut**](FivetranCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_dataform_credentials**
> GcpDataformCredentialsOut get_gcp_dataform_credentials(credentials_id)

Get GCP Dataform credentials

Get one set of GCP Dataform credentials, without the key.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_dataform_credentials_out import GcpDataformCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get GCP Dataform credentials
        api_response = api_instance.get_gcp_dataform_credentials(credentials_id)
        print("The response of CredentialsApi->get_gcp_dataform_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_gcp_dataform_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**GcpDataformCredentialsOut**](GcpDataformCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gcp_secret_manager_credentials**
> GcpSecretManagerCredentialsOut get_gcp_secret_manager_credentials(credentials_id)

Get GCP Secret Manager credentials

Get one set of GCP Secret Manager credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get GCP Secret Manager credentials
        api_response = api_instance.get_gcp_secret_manager_credentials(credentials_id)
        print("The response of CredentialsApi->get_gcp_secret_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_gcp_secret_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**GcpSecretManagerCredentialsOut**](GcpSecretManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_glue_credentials**
> GlueCredentialsOut get_glue_credentials(credentials_id)

Get Glue credentials

Get one set of Glue credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.glue_credentials_out import GlueCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Glue credentials
        api_response = api_instance.get_glue_credentials(credentials_id)
        print("The response of CredentialsApi->get_glue_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_glue_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**GlueCredentialsOut**](GlueCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_informatica_v2_credentials**
> InformaticaV2CredentialsOut get_informatica_v2_credentials(credentials_id)

Get Informatica credentials

Get one set of Informatica credentials, without the passwords and the client secret.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.informatica_v2_credentials_out import InformaticaV2CredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Informatica credentials
        api_response = api_instance.get_informatica_v2_credentials(credentials_id)
        print("The response of CredentialsApi->get_informatica_v2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_informatica_v2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**InformaticaV2CredentialsOut**](InformaticaV2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_looker_credentials**
> LookerCredentialsOut get_looker_credentials(credentials_id)

Get Looker credentials

Get one set of Looker API credentials, without the client secret.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_credentials_out import LookerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Looker credentials
        api_response = api_instance.get_looker_credentials(credentials_id)
        print("The response of CredentialsApi->get_looker_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_looker_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**LookerCredentialsOut**](LookerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_looker_git_clone_credentials**
> LookerGitCloneCredentialsOut get_looker_git_clone_credentials(credentials_id)

Get LookML repository credentials

Get one set of LookML repository credentials, without the token or the SSH key.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_git_clone_credentials_out import LookerGitCloneCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get LookML repository credentials
        api_response = api_instance.get_looker_git_clone_credentials(credentials_id)
        print("The response of CredentialsApi->get_looker_git_clone_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_looker_git_clone_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**LookerGitCloneCredentialsOut**](LookerGitCloneCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mariadb_credentials**
> MariaDbCredentialsOut get_mariadb_credentials(credentials_id)

Get MariaDB credentials

Get one set of MariaDB credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.maria_db_credentials_out import MariaDbCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get MariaDB credentials
        api_response = api_instance.get_mariadb_credentials(credentials_id)
        print("The response of CredentialsApi->get_mariadb_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_mariadb_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**MariaDbCredentialsOut**](MariaDbCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mulesoft_credentials**
> MulesoftCredentialsOut get_mulesoft_credentials(credentials_id)

Get MuleSoft credentials

Get one set of MuleSoft credentials, without the client secret.

An id that does not exist, belongs to another account, or names credentials of another kind
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.mulesoft_credentials_out import MulesoftCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get MuleSoft credentials
        api_response = api_instance.get_mulesoft_credentials(credentials_id)
        print("The response of CredentialsApi->get_mulesoft_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_mulesoft_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**MulesoftCredentialsOut**](MulesoftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mysql_credentials**
> MySqlCredentialsOut get_mysql_credentials(credentials_id)

Get MySQL credentials

Get one set of MySQL credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.my_sql_credentials_out import MySqlCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get MySQL credentials
        api_response = api_instance.get_mysql_credentials(credentials_id)
        print("The response of CredentialsApi->get_mysql_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_mysql_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**MySqlCredentialsOut**](MySqlCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_oracle_credentials**
> OracleCredentialsOut get_oracle_credentials(credentials_id)

Get Oracle credentials

Get one set of Oracle credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.oracle_credentials_out import OracleCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Oracle credentials
        api_response = api_instance.get_oracle_credentials(credentials_id)
        print("The response of CredentialsApi->get_oracle_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_oracle_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**OracleCredentialsOut**](OracleCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_postgres_credentials**
> PostgresCredentialsOut get_postgres_credentials(credentials_id)

Get PostgreSQL credentials

Get one set of PostgreSQL credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.postgres_credentials_out import PostgresCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get PostgreSQL credentials
        api_response = api_instance.get_postgres_credentials(credentials_id)
        print("The response of CredentialsApi->get_postgres_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_postgres_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**PostgresCredentialsOut**](PostgresCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_credentials**
> PowerBiCredentialsOut get_power_bi_credentials(credentials_id)

Get Power BI credentials

Get one set of Power BI credentials, without the client secret or the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.power_bi_credentials_out import PowerBiCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Power BI credentials
        api_response = api_instance.get_power_bi_credentials(credentials_id)
        print("The response of CredentialsApi->get_power_bi_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_power_bi_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**PowerBiCredentialsOut**](PowerBiCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_redshift_credentials**
> RedshiftCredentialsOut get_redshift_credentials(credentials_id)

Get Redshift credentials

Get one set of Redshift credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.redshift_credentials_out import RedshiftCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Redshift credentials
        api_response = api_instance.get_redshift_credentials(credentials_id)
        print("The response of CredentialsApi->get_redshift_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_redshift_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**RedshiftCredentialsOut**](RedshiftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_salesforce_crm_credentials**
> SalesforceCrmCredentialsOut get_salesforce_crm_credentials(credentials_id)

Get Salesforce CRM credentials

Get one set of Salesforce CRM credentials, without the password, the security token or
the consumer secret.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.salesforce_crm_credentials_out import SalesforceCrmCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Salesforce CRM credentials
        api_response = api_instance.get_salesforce_crm_credentials(credentials_id)
        print("The response of CredentialsApi->get_salesforce_crm_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_salesforce_crm_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**SalesforceCrmCredentialsOut**](SalesforceCrmCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sap_hana_credentials**
> SapHanaCredentialsOut get_sap_hana_credentials(credentials_id)

Get SAP HANA credentials

Get one set of SAP HANA credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sap_hana_credentials_out import SapHanaCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get SAP HANA credentials
        api_response = api_instance.get_sap_hana_credentials(credentials_id)
        print("The response of CredentialsApi->get_sap_hana_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_sap_hana_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**SapHanaCredentialsOut**](SapHanaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snowflake_credentials**
> SnowflakeCredentialsOut get_snowflake_credentials(credentials_id)

Get Snowflake credentials

Get one set of Snowflake credentials, without the key.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.snowflake_credentials_out import SnowflakeCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Snowflake credentials
        api_response = api_instance.get_snowflake_credentials(credentials_id)
        print("The response of CredentialsApi->get_snowflake_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_snowflake_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**SnowflakeCredentialsOut**](SnowflakeCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_server_credentials**
> SqlServerCredentialsOut get_sql_server_credentials(credentials_id)

Get SQL Server credentials

Get one set of SQL Server credentials, without the password or the keytab.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sql_server_credentials_out import SqlServerCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get SQL Server credentials
        api_response = api_instance.get_sql_server_credentials(credentials_id)
        print("The response of CredentialsApi->get_sql_server_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_sql_server_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**SqlServerCredentialsOut**](SqlServerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_starburst_enterprise_credentials**
> StarburstEnterpriseCredentialsOut get_starburst_enterprise_credentials(credentials_id)

Get Starburst Enterprise credentials

Get one set of Starburst Enterprise credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Starburst Enterprise credentials
        api_response = api_instance.get_starburst_enterprise_credentials(credentials_id)
        print("The response of CredentialsApi->get_starburst_enterprise_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_starburst_enterprise_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**StarburstEnterpriseCredentialsOut**](StarburstEnterpriseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_starburst_galaxy_credentials**
> StarburstGalaxyCredentialsOut get_starburst_galaxy_credentials(credentials_id)

Get Starburst Galaxy credentials

Get one set of Starburst Galaxy credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Starburst Galaxy credentials
        api_response = api_instance.get_starburst_galaxy_credentials(credentials_id)
        print("The response of CredentialsApi->get_starburst_galaxy_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_starburst_galaxy_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**StarburstGalaxyCredentialsOut**](StarburstGalaxyCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tableau_credentials**
> TableauCredentialsOut get_tableau_credentials(credentials_id)

Get Tableau credentials

Get one set of Tableau credentials, without the password or the secrets.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.tableau_credentials_out import TableauCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get Tableau credentials
        api_response = api_instance.get_tableau_credentials(credentials_id)
        print("The response of CredentialsApi->get_tableau_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_tableau_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 

### Return type

[**TableauCredentialsOut**](TableauCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teradata_credentials**
> TeradataCredentialsOut get_teradata_credentials(credentials_id)

Get Teradata credentials

Get one set of Teradata credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.teradata_credentials_out import TeradataCredentialsOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.

    try:
        # Get Teradata credentials
        api_response = api_instance.get_teradata_credentials(credentials_id)
        print("The response of CredentialsApi->get_teradata_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_teradata_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 

### Return type

[**TeradataCredentialsOut**](TeradataCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> PagedCredentialsSummaryOut list_credentials(cursor=cursor, limit=limit, with_count=with_count)

List credentials

List the credentials in your account, of every kind, a page at a time.

Credentials are returned oldest first. Each entry says what connection type it is for and
where its secret lives; read the typed endpoint for that kind to see its other fields.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.paged_credentials_summary_out import PagedCredentialsSummaryOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    cursor = 'cursor_example' # str | Position to continue from, as returned in `next_cursor` by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. (optional)
    limit = 50 # int | Maximum number of items to return, between 1 and 100. (optional) (default to 50)
    with_count = False # bool | Whether to also return the total number of items across every page, in `count`. Off by default: counting costs an extra query. (optional) (default to False)

    try:
        # List credentials
        api_response = api_instance.list_credentials(cursor=cursor, limit=limit, with_count=with_count)
        print("The response of CredentialsApi->list_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Position to continue from, as returned in &#x60;next_cursor&#x60; by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. | [optional] 
 **limit** | **int**| Maximum number of items to return, between 1 and 100. | [optional] [default to 50]
 **with_count** | **bool**| Whether to also return the total number of items across every page, in &#x60;count&#x60;. Off by default: counting costs an extra query. | [optional] [default to False]

### Return type

[**PagedCredentialsSummaryOut**](PagedCredentialsSummaryOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_airflow_credentials**
> AirflowCredentialsOut update_airflow_credentials(credentials_id, airflow_credentials_patch)

Update Airflow credentials

Change Airflow connection details in place.

Every connection using the credentials picks up the change. Sending an empty body returns the
credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.airflow_credentials_out import AirflowCredentialsOut
from pycarlo2.models.airflow_credentials_patch import AirflowCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    airflow_credentials_patch = pycarlo2.AirflowCredentialsPatch() # AirflowCredentialsPatch | 

    try:
        # Update Airflow credentials
        api_response = api_instance.update_airflow_credentials(credentials_id, airflow_credentials_patch)
        print("The response of CredentialsApi->update_airflow_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_airflow_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **airflow_credentials_patch** | [**AirflowCredentialsPatch**](AirflowCredentialsPatch.md)|  | 

### Return type

[**AirflowCredentialsOut**](AirflowCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_athena_credentials**
> AthenaCredentialsOut update_athena_credentials(credentials_id, athena_credentials_patch)

Update Athena credentials

Change Athena credentials in place.

Every connection using the credentials picks up the change. Sending an empty body returns
the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.athena_credentials_out import AthenaCredentialsOut
from pycarlo2.models.athena_credentials_patch import AthenaCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    athena_credentials_patch = pycarlo2.AthenaCredentialsPatch() # AthenaCredentialsPatch | 

    try:
        # Update Athena credentials
        api_response = api_instance.update_athena_credentials(credentials_id, athena_credentials_patch)
        print("The response of CredentialsApi->update_athena_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_athena_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **athena_credentials_patch** | [**AthenaCredentialsPatch**](AthenaCredentialsPatch.md)|  | 

### Return type

[**AthenaCredentialsOut**](AthenaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_secrets_manager_credentials**
> AwsSecretsManagerCredentialsOut update_aws_secrets_manager_credentials(credentials_id, aws_secrets_manager_credentials_patch)

Update AWS Secrets Manager credentials

Change AWS Secrets Manager credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, and an optional field set to null is cleared.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from pycarlo2.models.aws_secrets_manager_credentials_patch import AwsSecretsManagerCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    aws_secrets_manager_credentials_patch = pycarlo2.AwsSecretsManagerCredentialsPatch() # AwsSecretsManagerCredentialsPatch | 

    try:
        # Update AWS Secrets Manager credentials
        api_response = api_instance.update_aws_secrets_manager_credentials(credentials_id, aws_secrets_manager_credentials_patch)
        print("The response of CredentialsApi->update_aws_secrets_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_aws_secrets_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **aws_secrets_manager_credentials_patch** | [**AwsSecretsManagerCredentialsPatch**](AwsSecretsManagerCredentialsPatch.md)|  | 

### Return type

[**AwsSecretsManagerCredentialsOut**](AwsSecretsManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_data_factory_credentials**
> AzureDataFactoryCredentialsOut update_azure_data_factory_credentials(credentials_id, azure_data_factory_credentials_patch)

Update Azure Data Factory credentials

Change Azure Data Factory credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_data_factory_credentials_out import AzureDataFactoryCredentialsOut
from pycarlo2.models.azure_data_factory_credentials_patch import AzureDataFactoryCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_data_factory_credentials_patch = pycarlo2.AzureDataFactoryCredentialsPatch() # AzureDataFactoryCredentialsPatch | 

    try:
        # Update Azure Data Factory credentials
        api_response = api_instance.update_azure_data_factory_credentials(credentials_id, azure_data_factory_credentials_patch)
        print("The response of CredentialsApi->update_azure_data_factory_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_azure_data_factory_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **azure_data_factory_credentials_patch** | [**AzureDataFactoryCredentialsPatch**](AzureDataFactoryCredentialsPatch.md)|  | 

### Return type

[**AzureDataFactoryCredentialsOut**](AzureDataFactoryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_dedicated_sql_pool_credentials**
> AzureDedicatedSqlPoolCredentialsOut update_azure_dedicated_sql_pool_credentials(credentials_id, azure_dedicated_sql_pool_credentials_patch)

Update Azure Dedicated SQL Pool credentials

Change Azure Dedicated SQL Pool credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, and `password` set to null is unchanged. Sending an empty body
returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from pycarlo2.models.azure_dedicated_sql_pool_credentials_patch import AzureDedicatedSqlPoolCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_dedicated_sql_pool_credentials_patch = pycarlo2.AzureDedicatedSqlPoolCredentialsPatch() # AzureDedicatedSqlPoolCredentialsPatch | 

    try:
        # Update Azure Dedicated SQL Pool credentials
        api_response = api_instance.update_azure_dedicated_sql_pool_credentials(credentials_id, azure_dedicated_sql_pool_credentials_patch)
        print("The response of CredentialsApi->update_azure_dedicated_sql_pool_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_azure_dedicated_sql_pool_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_dedicated_sql_pool_credentials_patch** | [**AzureDedicatedSqlPoolCredentialsPatch**](AzureDedicatedSqlPoolCredentialsPatch.md)|  | 

### Return type

[**AzureDedicatedSqlPoolCredentialsOut**](AzureDedicatedSqlPoolCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_key_vault_credentials**
> AzureKeyVaultCredentialsOut update_azure_key_vault_credentials(credentials_id, azure_key_vault_credentials_patch)

Update Azure Key Vault credentials

Change Azure Key Vault credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, and an optional field set to null is cleared, as
long as the vault stays named one way. Sending an empty body returns the credentials as
they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from pycarlo2.models.azure_key_vault_credentials_patch import AzureKeyVaultCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_key_vault_credentials_patch = pycarlo2.AzureKeyVaultCredentialsPatch() # AzureKeyVaultCredentialsPatch | 

    try:
        # Update Azure Key Vault credentials
        api_response = api_instance.update_azure_key_vault_credentials(credentials_id, azure_key_vault_credentials_patch)
        print("The response of CredentialsApi->update_azure_key_vault_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_azure_key_vault_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_key_vault_credentials_patch** | [**AzureKeyVaultCredentialsPatch**](AzureKeyVaultCredentialsPatch.md)|  | 

### Return type

[**AzureKeyVaultCredentialsOut**](AzureKeyVaultCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_sql_database_credentials**
> AzureSqlDatabaseCredentialsOut update_azure_sql_database_credentials(credentials_id, azure_sql_database_credentials_patch)

Update Azure SQL Database credentials

Change Azure SQL Database credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, and `password` set to null is unchanged. Sending an empty body
returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from pycarlo2.models.azure_sql_database_credentials_patch import AzureSqlDatabaseCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_sql_database_credentials_patch = pycarlo2.AzureSqlDatabaseCredentialsPatch() # AzureSqlDatabaseCredentialsPatch | 

    try:
        # Update Azure SQL Database credentials
        api_response = api_instance.update_azure_sql_database_credentials(credentials_id, azure_sql_database_credentials_patch)
        print("The response of CredentialsApi->update_azure_sql_database_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_azure_sql_database_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_sql_database_credentials_patch** | [**AzureSqlDatabaseCredentialsPatch**](AzureSqlDatabaseCredentialsPatch.md)|  | 

### Return type

[**AzureSqlDatabaseCredentialsOut**](AzureSqlDatabaseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bigquery_credentials**
> BigQueryCredentialsOut update_bigquery_credentials(credentials_id, big_query_credentials_patch)

Update BigQuery credentials

Replace the key of BigQuery credentials in place.

Every connection using the credentials picks up the change. A new `service_account_key`
replaces the stored key whole. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.big_query_credentials_out import BigQueryCredentialsOut
from pycarlo2.models.big_query_credentials_patch import BigQueryCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    big_query_credentials_patch = pycarlo2.BigQueryCredentialsPatch() # BigQueryCredentialsPatch | 

    try:
        # Update BigQuery credentials
        api_response = api_instance.update_bigquery_credentials(credentials_id, big_query_credentials_patch)
        print("The response of CredentialsApi->update_bigquery_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_bigquery_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **big_query_credentials_patch** | [**BigQueryCredentialsPatch**](BigQueryCredentialsPatch.md)|  | 

### Return type

[**BigQueryCredentialsOut**](BigQueryCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_clickhouse_credentials**
> ClickHouseCredentialsOut update_clickhouse_credentials(credentials_id, click_house_credentials_patch)

Update ClickHouse credentials

Change ClickHouse credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` set to null is cleared, and `password` set to null is
unchanged. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.click_house_credentials_out import ClickHouseCredentialsOut
from pycarlo2.models.click_house_credentials_patch import ClickHouseCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    click_house_credentials_patch = pycarlo2.ClickHouseCredentialsPatch() # ClickHouseCredentialsPatch | 

    try:
        # Update ClickHouse credentials
        api_response = api_instance.update_clickhouse_credentials(credentials_id, click_house_credentials_patch)
        print("The response of CredentialsApi->update_clickhouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_clickhouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **click_house_credentials_patch** | [**ClickHouseCredentialsPatch**](ClickHouseCredentialsPatch.md)|  | 

### Return type

[**ClickHouseCredentialsOut**](ClickHouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_databricks_metastore_sql_warehouse_credentials**
> DatabricksMetastoreSqlWarehouseCredentialsOut update_databricks_metastore_sql_warehouse_credentials(credentials_id, databricks_metastore_sql_warehouse_credentials_patch)

Update Databricks metadata collection credentials

Change Databricks metadata collection credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. Sending `token` drops the stored OAuth client and its Azure fields. Sending the
OAuth client drops the stored token. Sending an empty body returns the credentials as
they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_patch import DatabricksMetastoreSqlWarehouseCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    databricks_metastore_sql_warehouse_credentials_patch = pycarlo2.DatabricksMetastoreSqlWarehouseCredentialsPatch() # DatabricksMetastoreSqlWarehouseCredentialsPatch | 

    try:
        # Update Databricks metadata collection credentials
        api_response = api_instance.update_databricks_metastore_sql_warehouse_credentials(credentials_id, databricks_metastore_sql_warehouse_credentials_patch)
        print("The response of CredentialsApi->update_databricks_metastore_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **databricks_metastore_sql_warehouse_credentials_patch** | [**DatabricksMetastoreSqlWarehouseCredentialsPatch**](DatabricksMetastoreSqlWarehouseCredentialsPatch.md)|  | 

### Return type

[**DatabricksMetastoreSqlWarehouseCredentialsOut**](DatabricksMetastoreSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_databricks_sql_warehouse_credentials**
> DatabricksSqlWarehouseCredentialsOut update_databricks_sql_warehouse_credentials(credentials_id, databricks_sql_warehouse_credentials_patch)

Update Databricks query credentials

Change Databricks query credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. Sending `token` drops the stored OAuth client and its Azure fields. Sending the
OAuth client drops the stored token. Sending an empty body returns the credentials as
they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from pycarlo2.models.databricks_sql_warehouse_credentials_patch import DatabricksSqlWarehouseCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    databricks_sql_warehouse_credentials_patch = pycarlo2.DatabricksSqlWarehouseCredentialsPatch() # DatabricksSqlWarehouseCredentialsPatch | 

    try:
        # Update Databricks query credentials
        api_response = api_instance.update_databricks_sql_warehouse_credentials(credentials_id, databricks_sql_warehouse_credentials_patch)
        print("The response of CredentialsApi->update_databricks_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_databricks_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **databricks_sql_warehouse_credentials_patch** | [**DatabricksSqlWarehouseCredentialsPatch**](DatabricksSqlWarehouseCredentialsPatch.md)|  | 

### Return type

[**DatabricksSqlWarehouseCredentialsOut**](DatabricksSqlWarehouseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_db2_credentials**
> Db2CredentialsOut update_db2_credentials(credentials_id, db2_credentials_patch)

Update Db2 credentials

Change Db2 credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` or an `ssl_*` field set to null is cleared, and
`password` set to null is unchanged. Sending an empty body returns the credentials as they
are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.db2_credentials_out import Db2CredentialsOut
from pycarlo2.models.db2_credentials_patch import Db2CredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    db2_credentials_patch = pycarlo2.Db2CredentialsPatch() # Db2CredentialsPatch | 

    try:
        # Update Db2 credentials
        api_response = api_instance.update_db2_credentials(credentials_id, db2_credentials_patch)
        print("The response of CredentialsApi->update_db2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_db2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **db2_credentials_patch** | [**Db2CredentialsPatch**](Db2CredentialsPatch.md)|  | 

### Return type

[**Db2CredentialsOut**](Db2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dbt_cloud_webhook_credentials**
> DbtCloudWebhookCredentialsOut update_dbt_cloud_webhook_credentials(credentials_id, dbt_cloud_webhook_credentials_patch)

Update dbt Cloud webhook credentials

Change dbt Cloud webhook credentials in place.

The connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

A new `account_id`, `webhook_id` or `hmac_secret` moves the connection to the new webhook
or secret at once. A webhook another connection already receives is refused with 409.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.dbt_cloud_webhook_credentials_out import DbtCloudWebhookCredentialsOut
from pycarlo2.models.dbt_cloud_webhook_credentials_patch import DbtCloudWebhookCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    dbt_cloud_webhook_credentials_patch = pycarlo2.DbtCloudWebhookCredentialsPatch() # DbtCloudWebhookCredentialsPatch | 

    try:
        # Update dbt Cloud webhook credentials
        api_response = api_instance.update_dbt_cloud_webhook_credentials(credentials_id, dbt_cloud_webhook_credentials_patch)
        print("The response of CredentialsApi->update_dbt_cloud_webhook_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_dbt_cloud_webhook_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **dbt_cloud_webhook_credentials_patch** | [**DbtCloudWebhookCredentialsPatch**](DbtCloudWebhookCredentialsPatch.md)|  | 

### Return type

[**DbtCloudWebhookCredentialsOut**](DbtCloudWebhookCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**409** | Conflict |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_env_var_credentials**
> EnvVarCredentialsOut update_env_var_credentials(credentials_id, env_var_credentials_patch)

Update environment variable credentials

Change environment variable credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, and an optional field set to null is cleared.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.env_var_credentials_out import EnvVarCredentialsOut
from pycarlo2.models.env_var_credentials_patch import EnvVarCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    env_var_credentials_patch = pycarlo2.EnvVarCredentialsPatch() # EnvVarCredentialsPatch | 

    try:
        # Update environment variable credentials
        api_response = api_instance.update_env_var_credentials(credentials_id, env_var_credentials_patch)
        print("The response of CredentialsApi->update_env_var_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_env_var_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **env_var_credentials_patch** | [**EnvVarCredentialsPatch**](EnvVarCredentialsPatch.md)|  | 

### Return type

[**EnvVarCredentialsOut**](EnvVarCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_credentials**
> FileCredentialsOut update_file_credentials(credentials_id, file_credentials_patch)

Update file credentials

Change file credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, and an optional field set to null is cleared.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.file_credentials_out import FileCredentialsOut
from pycarlo2.models.file_credentials_patch import FileCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    file_credentials_patch = pycarlo2.FileCredentialsPatch() # FileCredentialsPatch | 

    try:
        # Update file credentials
        api_response = api_instance.update_file_credentials(credentials_id, file_credentials_patch)
        print("The response of CredentialsApi->update_file_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_file_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **file_credentials_patch** | [**FileCredentialsPatch**](FileCredentialsPatch.md)|  | 

### Return type

[**FileCredentialsOut**](FileCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fivetran_credentials**
> FivetranCredentialsOut update_fivetran_credentials(credentials_id, fivetran_credentials_patch)

Update Fivetran credentials

Change Fivetran credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.fivetran_credentials_out import FivetranCredentialsOut
from pycarlo2.models.fivetran_credentials_patch import FivetranCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    fivetran_credentials_patch = pycarlo2.FivetranCredentialsPatch() # FivetranCredentialsPatch | 

    try:
        # Update Fivetran credentials
        api_response = api_instance.update_fivetran_credentials(credentials_id, fivetran_credentials_patch)
        print("The response of CredentialsApi->update_fivetran_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_fivetran_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **fivetran_credentials_patch** | [**FivetranCredentialsPatch**](FivetranCredentialsPatch.md)|  | 

### Return type

[**FivetranCredentialsOut**](FivetranCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_dataform_credentials**
> GcpDataformCredentialsOut update_gcp_dataform_credentials(credentials_id, gcp_dataform_credentials_patch)

Update GCP Dataform credentials

Change GCP Dataform credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_dataform_credentials_out import GcpDataformCredentialsOut
from pycarlo2.models.gcp_dataform_credentials_patch import GcpDataformCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    gcp_dataform_credentials_patch = pycarlo2.GcpDataformCredentialsPatch() # GcpDataformCredentialsPatch | 

    try:
        # Update GCP Dataform credentials
        api_response = api_instance.update_gcp_dataform_credentials(credentials_id, gcp_dataform_credentials_patch)
        print("The response of CredentialsApi->update_gcp_dataform_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_gcp_dataform_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **gcp_dataform_credentials_patch** | [**GcpDataformCredentialsPatch**](GcpDataformCredentialsPatch.md)|  | 

### Return type

[**GcpDataformCredentialsOut**](GcpDataformCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_secret_manager_credentials**
> GcpSecretManagerCredentialsOut update_gcp_secret_manager_credentials(credentials_id, gcp_secret_manager_credentials_patch)

Update GCP Secret Manager credentials

Change GCP Secret Manager credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, and an optional field set to null is cleared.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from pycarlo2.models.gcp_secret_manager_credentials_patch import GcpSecretManagerCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    gcp_secret_manager_credentials_patch = pycarlo2.GcpSecretManagerCredentialsPatch() # GcpSecretManagerCredentialsPatch | 

    try:
        # Update GCP Secret Manager credentials
        api_response = api_instance.update_gcp_secret_manager_credentials(credentials_id, gcp_secret_manager_credentials_patch)
        print("The response of CredentialsApi->update_gcp_secret_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_gcp_secret_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **gcp_secret_manager_credentials_patch** | [**GcpSecretManagerCredentialsPatch**](GcpSecretManagerCredentialsPatch.md)|  | 

### Return type

[**GcpSecretManagerCredentialsOut**](GcpSecretManagerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_glue_credentials**
> GlueCredentialsOut update_glue_credentials(credentials_id, glue_credentials_patch)

Update Glue credentials

Change Glue credentials in place.

Every connection using the credentials picks up the change. Sending an empty body returns
the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.glue_credentials_out import GlueCredentialsOut
from pycarlo2.models.glue_credentials_patch import GlueCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    glue_credentials_patch = pycarlo2.GlueCredentialsPatch() # GlueCredentialsPatch | 

    try:
        # Update Glue credentials
        api_response = api_instance.update_glue_credentials(credentials_id, glue_credentials_patch)
        print("The response of CredentialsApi->update_glue_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_glue_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **glue_credentials_patch** | [**GlueCredentialsPatch**](GlueCredentialsPatch.md)|  | 

### Return type

[**GlueCredentialsOut**](GlueCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_informatica_v2_credentials**
> InformaticaV2CredentialsOut update_informatica_v2_credentials(credentials_id, informatica_v2_credentials_patch)

Update Informatica credentials

Change Informatica credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.informatica_v2_credentials_out import InformaticaV2CredentialsOut
from pycarlo2.models.informatica_v2_credentials_patch import InformaticaV2CredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    informatica_v2_credentials_patch = pycarlo2.InformaticaV2CredentialsPatch() # InformaticaV2CredentialsPatch | 

    try:
        # Update Informatica credentials
        api_response = api_instance.update_informatica_v2_credentials(credentials_id, informatica_v2_credentials_patch)
        print("The response of CredentialsApi->update_informatica_v2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_informatica_v2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **informatica_v2_credentials_patch** | [**InformaticaV2CredentialsPatch**](InformaticaV2CredentialsPatch.md)|  | 

### Return type

[**InformaticaV2CredentialsOut**](InformaticaV2CredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_looker_credentials**
> LookerCredentialsOut update_looker_credentials(credentials_id, looker_credentials_patch)

Update Looker credentials

Change Looker API credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_credentials_out import LookerCredentialsOut
from pycarlo2.models.looker_credentials_patch import LookerCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    looker_credentials_patch = pycarlo2.LookerCredentialsPatch() # LookerCredentialsPatch | 

    try:
        # Update Looker credentials
        api_response = api_instance.update_looker_credentials(credentials_id, looker_credentials_patch)
        print("The response of CredentialsApi->update_looker_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_looker_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **looker_credentials_patch** | [**LookerCredentialsPatch**](LookerCredentialsPatch.md)|  | 

### Return type

[**LookerCredentialsOut**](LookerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_looker_git_clone_credentials**
> LookerGitCloneCredentialsOut update_looker_git_clone_credentials(credentials_id, looker_git_clone_credentials_patch)

Update LookML repository credentials

Change LookML repository credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. Sending `ssh_key` drops a stored username and token, and sending `username` or
`token` drops a stored key. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_git_clone_credentials_out import LookerGitCloneCredentialsOut
from pycarlo2.models.looker_git_clone_credentials_patch import LookerGitCloneCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    looker_git_clone_credentials_patch = pycarlo2.LookerGitCloneCredentialsPatch() # LookerGitCloneCredentialsPatch | 

    try:
        # Update LookML repository credentials
        api_response = api_instance.update_looker_git_clone_credentials(credentials_id, looker_git_clone_credentials_patch)
        print("The response of CredentialsApi->update_looker_git_clone_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_looker_git_clone_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **looker_git_clone_credentials_patch** | [**LookerGitCloneCredentialsPatch**](LookerGitCloneCredentialsPatch.md)|  | 

### Return type

[**LookerGitCloneCredentialsOut**](LookerGitCloneCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mariadb_credentials**
> MariaDbCredentialsOut update_mariadb_credentials(credentials_id, maria_db_credentials_patch)

Update MariaDB credentials

Change MariaDB credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` set to null is cleared, and `password` set to null is
unchanged. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.maria_db_credentials_out import MariaDbCredentialsOut
from pycarlo2.models.maria_db_credentials_patch import MariaDbCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    maria_db_credentials_patch = pycarlo2.MariaDbCredentialsPatch() # MariaDbCredentialsPatch | 

    try:
        # Update MariaDB credentials
        api_response = api_instance.update_mariadb_credentials(credentials_id, maria_db_credentials_patch)
        print("The response of CredentialsApi->update_mariadb_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_mariadb_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **maria_db_credentials_patch** | [**MariaDbCredentialsPatch**](MariaDbCredentialsPatch.md)|  | 

### Return type

[**MariaDbCredentialsOut**](MariaDbCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mulesoft_credentials**
> MulesoftCredentialsOut update_mulesoft_credentials(credentials_id, mulesoft_credentials_patch)

Update MuleSoft credentials

Change MuleSoft credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.mulesoft_credentials_out import MulesoftCredentialsOut
from pycarlo2.models.mulesoft_credentials_patch import MulesoftCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    mulesoft_credentials_patch = pycarlo2.MulesoftCredentialsPatch() # MulesoftCredentialsPatch | 

    try:
        # Update MuleSoft credentials
        api_response = api_instance.update_mulesoft_credentials(credentials_id, mulesoft_credentials_patch)
        print("The response of CredentialsApi->update_mulesoft_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_mulesoft_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **mulesoft_credentials_patch** | [**MulesoftCredentialsPatch**](MulesoftCredentialsPatch.md)|  | 

### Return type

[**MulesoftCredentialsOut**](MulesoftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mysql_credentials**
> MySqlCredentialsOut update_mysql_credentials(credentials_id, my_sql_credentials_patch)

Update MySQL credentials

Change MySQL credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` or an `ssl_*` field set to null is cleared, and
`password` set to null is unchanged. Sending an empty body returns the credentials as they
are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.my_sql_credentials_out import MySqlCredentialsOut
from pycarlo2.models.my_sql_credentials_patch import MySqlCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    my_sql_credentials_patch = pycarlo2.MySqlCredentialsPatch() # MySqlCredentialsPatch | 

    try:
        # Update MySQL credentials
        api_response = api_instance.update_mysql_credentials(credentials_id, my_sql_credentials_patch)
        print("The response of CredentialsApi->update_mysql_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_mysql_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **my_sql_credentials_patch** | [**MySqlCredentialsPatch**](MySqlCredentialsPatch.md)|  | 

### Return type

[**MySqlCredentialsOut**](MySqlCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_oracle_credentials**
> OracleCredentialsOut update_oracle_credentials(credentials_id, oracle_credentials_patch)

Update Oracle credentials

Change Oracle credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, an `ssl_*` field set to null is cleared, and `password` set to null
is unchanged. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.oracle_credentials_out import OracleCredentialsOut
from pycarlo2.models.oracle_credentials_patch import OracleCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    oracle_credentials_patch = pycarlo2.OracleCredentialsPatch() # OracleCredentialsPatch | 

    try:
        # Update Oracle credentials
        api_response = api_instance.update_oracle_credentials(credentials_id, oracle_credentials_patch)
        print("The response of CredentialsApi->update_oracle_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_oracle_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **oracle_credentials_patch** | [**OracleCredentialsPatch**](OracleCredentialsPatch.md)|  | 

### Return type

[**OracleCredentialsOut**](OracleCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_postgres_credentials**
> PostgresCredentialsOut update_postgres_credentials(credentials_id, postgres_credentials_patch)

Update PostgreSQL credentials

Change PostgreSQL credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, a setting or an `ssl_*` field set to null is cleared, and
`password` set to null is unchanged. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.postgres_credentials_out import PostgresCredentialsOut
from pycarlo2.models.postgres_credentials_patch import PostgresCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    postgres_credentials_patch = pycarlo2.PostgresCredentialsPatch() # PostgresCredentialsPatch | 

    try:
        # Update PostgreSQL credentials
        api_response = api_instance.update_postgres_credentials(credentials_id, postgres_credentials_patch)
        print("The response of CredentialsApi->update_postgres_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_postgres_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **postgres_credentials_patch** | [**PostgresCredentialsPatch**](PostgresCredentialsPatch.md)|  | 

### Return type

[**PostgresCredentialsOut**](PostgresCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_credentials**
> PowerBiCredentialsOut update_power_bi_credentials(credentials_id, power_bi_credentials_patch)

Update Power BI credentials

Change Power BI credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. A new `auth_mode` drops the fields of the old one, so send the new mode's fields
with it. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.power_bi_credentials_out import PowerBiCredentialsOut
from pycarlo2.models.power_bi_credentials_patch import PowerBiCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    power_bi_credentials_patch = pycarlo2.PowerBiCredentialsPatch() # PowerBiCredentialsPatch | 

    try:
        # Update Power BI credentials
        api_response = api_instance.update_power_bi_credentials(credentials_id, power_bi_credentials_patch)
        print("The response of CredentialsApi->update_power_bi_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_power_bi_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **power_bi_credentials_patch** | [**PowerBiCredentialsPatch**](PowerBiCredentialsPatch.md)|  | 

### Return type

[**PowerBiCredentialsOut**](PowerBiCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_redshift_credentials**
> RedshiftCredentialsOut update_redshift_credentials(credentials_id, redshift_credentials_patch)

Update Redshift credentials

Change Redshift credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, an `ssl_*` field set to null is cleared, and
`password` set to null is unchanged. Sending an empty body returns the credentials as they
are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.redshift_credentials_out import RedshiftCredentialsOut
from pycarlo2.models.redshift_credentials_patch import RedshiftCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    redshift_credentials_patch = pycarlo2.RedshiftCredentialsPatch() # RedshiftCredentialsPatch | 

    try:
        # Update Redshift credentials
        api_response = api_instance.update_redshift_credentials(credentials_id, redshift_credentials_patch)
        print("The response of CredentialsApi->update_redshift_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_redshift_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **redshift_credentials_patch** | [**RedshiftCredentialsPatch**](RedshiftCredentialsPatch.md)|  | 

### Return type

[**RedshiftCredentialsOut**](RedshiftCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_salesforce_crm_credentials**
> SalesforceCrmCredentialsOut update_salesforce_crm_credentials(credentials_id, salesforce_crm_credentials_patch)

Update Salesforce CRM credentials

Change Salesforce CRM credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
A new `auth_mode` drops the fields and the secrets of the old one, so send all of the new
mode's fields with it. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.salesforce_crm_credentials_out import SalesforceCrmCredentialsOut
from pycarlo2.models.salesforce_crm_credentials_patch import SalesforceCrmCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    salesforce_crm_credentials_patch = pycarlo2.SalesforceCrmCredentialsPatch() # SalesforceCrmCredentialsPatch | 

    try:
        # Update Salesforce CRM credentials
        api_response = api_instance.update_salesforce_crm_credentials(credentials_id, salesforce_crm_credentials_patch)
        print("The response of CredentialsApi->update_salesforce_crm_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_salesforce_crm_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **salesforce_crm_credentials_patch** | [**SalesforceCrmCredentialsPatch**](SalesforceCrmCredentialsPatch.md)|  | 

### Return type

[**SalesforceCrmCredentialsOut**](SalesforceCrmCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sap_hana_credentials**
> SapHanaCredentialsOut update_sap_hana_credentials(credentials_id, sap_hana_credentials_patch)

Update SAP HANA credentials

Change SAP HANA credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, and `password` set to null is unchanged. Sending an empty body
returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sap_hana_credentials_out import SapHanaCredentialsOut
from pycarlo2.models.sap_hana_credentials_patch import SapHanaCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    sap_hana_credentials_patch = pycarlo2.SapHanaCredentialsPatch() # SapHanaCredentialsPatch | 

    try:
        # Update SAP HANA credentials
        api_response = api_instance.update_sap_hana_credentials(credentials_id, sap_hana_credentials_patch)
        print("The response of CredentialsApi->update_sap_hana_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_sap_hana_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **sap_hana_credentials_patch** | [**SapHanaCredentialsPatch**](SapHanaCredentialsPatch.md)|  | 

### Return type

[**SapHanaCredentialsOut**](SapHanaCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snowflake_credentials**
> SnowflakeCredentialsOut update_snowflake_credentials(credentials_id, snowflake_credentials_patch)

Update Snowflake credentials

Change Snowflake credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change: a field left out is unchanged, `warehouse` set to null is cleared, and a new
`private_key` replaces the whole key pair. Sending an empty body returns the credentials as
they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.snowflake_credentials_out import SnowflakeCredentialsOut
from pycarlo2.models.snowflake_credentials_patch import SnowflakeCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    snowflake_credentials_patch = pycarlo2.SnowflakeCredentialsPatch() # SnowflakeCredentialsPatch | 

    try:
        # Update Snowflake credentials
        api_response = api_instance.update_snowflake_credentials(credentials_id, snowflake_credentials_patch)
        print("The response of CredentialsApi->update_snowflake_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_snowflake_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **snowflake_credentials_patch** | [**SnowflakeCredentialsPatch**](SnowflakeCredentialsPatch.md)|  | 

### Return type

[**SnowflakeCredentialsOut**](SnowflakeCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sql_server_credentials**
> SqlServerCredentialsOut update_sql_server_credentials(credentials_id, sql_server_credentials_patch)

Update SQL Server credentials

Change SQL Server credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change.
A new `auth_mode` drops the fields and the secret of the old one, so send the new mode's
fields with it. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sql_server_credentials_out import SqlServerCredentialsOut
from pycarlo2.models.sql_server_credentials_patch import SqlServerCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    sql_server_credentials_patch = pycarlo2.SqlServerCredentialsPatch() # SqlServerCredentialsPatch | 

    try:
        # Update SQL Server credentials
        api_response = api_instance.update_sql_server_credentials(credentials_id, sql_server_credentials_patch)
        print("The response of CredentialsApi->update_sql_server_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_sql_server_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **sql_server_credentials_patch** | [**SqlServerCredentialsPatch**](SqlServerCredentialsPatch.md)|  | 

### Return type

[**SqlServerCredentialsOut**](SqlServerCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_starburst_enterprise_credentials**
> StarburstEnterpriseCredentialsOut update_starburst_enterprise_credentials(credentials_id, starburst_enterprise_credentials_patch)

Update Starburst Enterprise credentials

Change Starburst Enterprise credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` or an `ssl_*` field set to null is cleared, and
`password` set to null is unchanged. Sending an empty body returns the credentials as they
are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from pycarlo2.models.starburst_enterprise_credentials_patch import StarburstEnterpriseCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    starburst_enterprise_credentials_patch = pycarlo2.StarburstEnterpriseCredentialsPatch() # StarburstEnterpriseCredentialsPatch | 

    try:
        # Update Starburst Enterprise credentials
        api_response = api_instance.update_starburst_enterprise_credentials(credentials_id, starburst_enterprise_credentials_patch)
        print("The response of CredentialsApi->update_starburst_enterprise_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_starburst_enterprise_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **starburst_enterprise_credentials_patch** | [**StarburstEnterpriseCredentialsPatch**](StarburstEnterpriseCredentialsPatch.md)|  | 

### Return type

[**StarburstEnterpriseCredentialsOut**](StarburstEnterpriseCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_starburst_galaxy_credentials**
> StarburstGalaxyCredentialsOut update_starburst_galaxy_credentials(credentials_id, starburst_galaxy_credentials_patch)

Update Starburst Galaxy credentials

Change Starburst Galaxy credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name` set to null is cleared, and `password` set to null is
unchanged. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from pycarlo2.models.starburst_galaxy_credentials_patch import StarburstGalaxyCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    starburst_galaxy_credentials_patch = pycarlo2.StarburstGalaxyCredentialsPatch() # StarburstGalaxyCredentialsPatch | 

    try:
        # Update Starburst Galaxy credentials
        api_response = api_instance.update_starburst_galaxy_credentials(credentials_id, starburst_galaxy_credentials_patch)
        print("The response of CredentialsApi->update_starburst_galaxy_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_starburst_galaxy_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **starburst_galaxy_credentials_patch** | [**StarburstGalaxyCredentialsPatch**](StarburstGalaxyCredentialsPatch.md)|  | 

### Return type

[**StarburstGalaxyCredentialsOut**](StarburstGalaxyCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tableau_credentials**
> TableauCredentialsOut update_tableau_credentials(credentials_id, tableau_credentials_patch)

Update Tableau credentials

Change Tableau credentials in place.

Every connection using the credentials picks up the change. Send only the fields to
change. Sending a field of another way to sign in drops the stored one. Moving to a
connected app is refused while a connection using the credentials runs on a deployment
too old for connected apps. Sending an empty body returns the credentials as they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.tableau_credentials_out import TableauCredentialsOut
from pycarlo2.models.tableau_credentials_patch import TableauCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    tableau_credentials_patch = pycarlo2.TableauCredentialsPatch() # TableauCredentialsPatch | 

    try:
        # Update Tableau credentials
        api_response = api_instance.update_tableau_credentials(credentials_id, tableau_credentials_patch)
        print("The response of CredentialsApi->update_tableau_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_tableau_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**|  | 
 **tableau_credentials_patch** | [**TableauCredentialsPatch**](TableauCredentialsPatch.md)|  | 

### Return type

[**TableauCredentialsOut**](TableauCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**409** | Conflict |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_teradata_credentials**
> TeradataCredentialsOut update_teradata_credentials(credentials_id, teradata_credentials_patch)

Update Teradata credentials

Change Teradata credentials in place.

Every connection using the credentials picks up the change. Send only the fields to change: a
field left out is unchanged, `db_name`, a setting or an `ssl_*` field set to null is cleared,
and `password` set to null is unchanged. Sending an empty body returns the credentials as
they are.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.teradata_credentials_out import TeradataCredentialsOut
from pycarlo2.models.teradata_credentials_patch import TeradataCredentialsPatch
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    teradata_credentials_patch = pycarlo2.TeradataCredentialsPatch() # TeradataCredentialsPatch | 

    try:
        # Update Teradata credentials
        api_response = api_instance.update_teradata_credentials(credentials_id, teradata_credentials_patch)
        print("The response of CredentialsApi->update_teradata_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_teradata_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **teradata_credentials_patch** | [**TeradataCredentialsPatch**](TeradataCredentialsPatch.md)|  | 

### Return type

[**TeradataCredentialsOut**](TeradataCredentialsOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_athena_credentials**
> ValidationRunOut validate_athena_credentials(athena_credentials_validate_in)

Validate Athena credentials

Check candidate Athena credentials against your AWS account.

No credentials are created. Send the fields you would create the credentials with, and a
deployment to run them from, and the checks run against Athena.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.athena_credentials_validate_in import AthenaCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    athena_credentials_validate_in = pycarlo2.AthenaCredentialsValidateIn() # AthenaCredentialsValidateIn | 

    try:
        # Validate Athena credentials
        api_response = api_instance.validate_athena_credentials(athena_credentials_validate_in)
        print("The response of CredentialsApi->validate_athena_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_athena_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **athena_credentials_validate_in** | [**AthenaCredentialsValidateIn**](AthenaCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_athena_credentials_change**
> ValidationRunOut validate_athena_credentials_change(credentials_id, athena_credentials_change_validate_in)

Validate a change to Athena credentials

Check a change to Athena credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.athena_credentials_change_validate_in import AthenaCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    athena_credentials_change_validate_in = pycarlo2.AthenaCredentialsChangeValidateIn() # AthenaCredentialsChangeValidateIn | 

    try:
        # Validate a change to Athena credentials
        api_response = api_instance.validate_athena_credentials_change(credentials_id, athena_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_athena_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_athena_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **athena_credentials_change_validate_in** | [**AthenaCredentialsChangeValidateIn**](AthenaCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_aws_secrets_manager_credentials**
> ValidationRunOut validate_aws_secrets_manager_credentials(aws_secrets_manager_credentials_validate_in)

Validate AWS Secrets Manager credentials

Check candidate AWS Secrets Manager credentials against the system they are for.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against that system.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.aws_secrets_manager_credentials_validate_in import AwsSecretsManagerCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    aws_secrets_manager_credentials_validate_in = pycarlo2.AwsSecretsManagerCredentialsValidateIn() # AwsSecretsManagerCredentialsValidateIn | 

    try:
        # Validate AWS Secrets Manager credentials
        api_response = api_instance.validate_aws_secrets_manager_credentials(aws_secrets_manager_credentials_validate_in)
        print("The response of CredentialsApi->validate_aws_secrets_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_aws_secrets_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_secrets_manager_credentials_validate_in** | [**AwsSecretsManagerCredentialsValidateIn**](AwsSecretsManagerCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_aws_secrets_manager_credentials_change**
> ValidationRunOut validate_aws_secrets_manager_credentials_change(credentials_id, aws_secrets_manager_credentials_change_validate_in)

Validate a change to AWS Secrets Manager credentials

Check a change to AWS Secrets Manager credentials against the system they are for.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
storage returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.aws_secrets_manager_credentials_change_validate_in import AwsSecretsManagerCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    aws_secrets_manager_credentials_change_validate_in = pycarlo2.AwsSecretsManagerCredentialsChangeValidateIn() # AwsSecretsManagerCredentialsChangeValidateIn | 

    try:
        # Validate a change to AWS Secrets Manager credentials
        api_response = api_instance.validate_aws_secrets_manager_credentials_change(credentials_id, aws_secrets_manager_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_aws_secrets_manager_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_aws_secrets_manager_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **aws_secrets_manager_credentials_change_validate_in** | [**AwsSecretsManagerCredentialsChangeValidateIn**](AwsSecretsManagerCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_data_factory_credentials**
> ValidationRunOut validate_azure_data_factory_credentials(azure_data_factory_credentials_validate_in)

Validate Azure Data Factory credentials

Check candidate Azure Data Factory credentials against Azure Data Factory.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your data factory.

The response is the run as it starts, and `Location` names where to read it. Poll that until the
run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_data_factory_credentials_validate_in import AzureDataFactoryCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_data_factory_credentials_validate_in = pycarlo2.AzureDataFactoryCredentialsValidateIn() # AzureDataFactoryCredentialsValidateIn | 

    try:
        # Validate Azure Data Factory credentials
        api_response = api_instance.validate_azure_data_factory_credentials(azure_data_factory_credentials_validate_in)
        print("The response of CredentialsApi->validate_azure_data_factory_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_data_factory_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_data_factory_credentials_validate_in** | [**AzureDataFactoryCredentialsValidateIn**](AzureDataFactoryCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_data_factory_credentials_change**
> ValidationRunOut validate_azure_data_factory_credentials_change(credentials_id, azure_data_factory_credentials_change_validate_in)

Validate a change to Azure Data Factory credentials

Check a change to Azure Data Factory credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_data_factory_credentials_change_validate_in import AzureDataFactoryCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_data_factory_credentials_change_validate_in = pycarlo2.AzureDataFactoryCredentialsChangeValidateIn() # AzureDataFactoryCredentialsChangeValidateIn | 

    try:
        # Validate a change to Azure Data Factory credentials
        api_response = api_instance.validate_azure_data_factory_credentials_change(credentials_id, azure_data_factory_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_azure_data_factory_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_data_factory_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_data_factory_credentials_change_validate_in** | [**AzureDataFactoryCredentialsChangeValidateIn**](AzureDataFactoryCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_dedicated_sql_pool_credentials**
> ValidationRunOut validate_azure_dedicated_sql_pool_credentials(azure_dedicated_sql_pool_credentials_validate_in)

Validate Azure Dedicated SQL Pool credentials

Check a candidate Azure Dedicated SQL Pool login against Azure Dedicated SQL Pool.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Azure Dedicated SQL Pool.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_dedicated_sql_pool_credentials_validate_in import AzureDedicatedSqlPoolCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_dedicated_sql_pool_credentials_validate_in = pycarlo2.AzureDedicatedSqlPoolCredentialsValidateIn() # AzureDedicatedSqlPoolCredentialsValidateIn | 

    try:
        # Validate Azure Dedicated SQL Pool credentials
        api_response = api_instance.validate_azure_dedicated_sql_pool_credentials(azure_dedicated_sql_pool_credentials_validate_in)
        print("The response of CredentialsApi->validate_azure_dedicated_sql_pool_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_dedicated_sql_pool_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_dedicated_sql_pool_credentials_validate_in** | [**AzureDedicatedSqlPoolCredentialsValidateIn**](AzureDedicatedSqlPoolCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_dedicated_sql_pool_credentials_change**
> ValidationRunOut validate_azure_dedicated_sql_pool_credentials_change(credentials_id, azure_dedicated_sql_pool_credentials_change_validate_in)

Validate a change to Azure Dedicated SQL Pool credentials

Check a change to Azure Dedicated SQL Pool credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_dedicated_sql_pool_credentials_change_validate_in import AzureDedicatedSqlPoolCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_dedicated_sql_pool_credentials_change_validate_in = pycarlo2.AzureDedicatedSqlPoolCredentialsChangeValidateIn() # AzureDedicatedSqlPoolCredentialsChangeValidateIn | 

    try:
        # Validate a change to Azure Dedicated SQL Pool credentials
        api_response = api_instance.validate_azure_dedicated_sql_pool_credentials_change(credentials_id, azure_dedicated_sql_pool_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_azure_dedicated_sql_pool_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_dedicated_sql_pool_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_dedicated_sql_pool_credentials_change_validate_in** | [**AzureDedicatedSqlPoolCredentialsChangeValidateIn**](AzureDedicatedSqlPoolCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_key_vault_credentials**
> ValidationRunOut validate_azure_key_vault_credentials(azure_key_vault_credentials_validate_in)

Validate Azure Key Vault credentials

Check candidate Azure Key Vault credentials against the system they are for.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against that system.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_key_vault_credentials_validate_in import AzureKeyVaultCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_key_vault_credentials_validate_in = pycarlo2.AzureKeyVaultCredentialsValidateIn() # AzureKeyVaultCredentialsValidateIn | 

    try:
        # Validate Azure Key Vault credentials
        api_response = api_instance.validate_azure_key_vault_credentials(azure_key_vault_credentials_validate_in)
        print("The response of CredentialsApi->validate_azure_key_vault_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_key_vault_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_key_vault_credentials_validate_in** | [**AzureKeyVaultCredentialsValidateIn**](AzureKeyVaultCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_key_vault_credentials_change**
> ValidationRunOut validate_azure_key_vault_credentials_change(credentials_id, azure_key_vault_credentials_change_validate_in)

Validate a change to Azure Key Vault credentials

Check a change to Azure Key Vault credentials against the system they are for.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
storage returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_key_vault_credentials_change_validate_in import AzureKeyVaultCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_key_vault_credentials_change_validate_in = pycarlo2.AzureKeyVaultCredentialsChangeValidateIn() # AzureKeyVaultCredentialsChangeValidateIn | 

    try:
        # Validate a change to Azure Key Vault credentials
        api_response = api_instance.validate_azure_key_vault_credentials_change(credentials_id, azure_key_vault_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_azure_key_vault_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_key_vault_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_key_vault_credentials_change_validate_in** | [**AzureKeyVaultCredentialsChangeValidateIn**](AzureKeyVaultCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_sql_database_credentials**
> ValidationRunOut validate_azure_sql_database_credentials(azure_sql_database_credentials_validate_in)

Validate Azure SQL Database credentials

Check a candidate Azure SQL Database login against Azure SQL Database.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Azure SQL Database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_sql_database_credentials_validate_in import AzureSqlDatabaseCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    azure_sql_database_credentials_validate_in = pycarlo2.AzureSqlDatabaseCredentialsValidateIn() # AzureSqlDatabaseCredentialsValidateIn | 

    try:
        # Validate Azure SQL Database credentials
        api_response = api_instance.validate_azure_sql_database_credentials(azure_sql_database_credentials_validate_in)
        print("The response of CredentialsApi->validate_azure_sql_database_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_sql_database_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_sql_database_credentials_validate_in** | [**AzureSqlDatabaseCredentialsValidateIn**](AzureSqlDatabaseCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_azure_sql_database_credentials_change**
> ValidationRunOut validate_azure_sql_database_credentials_change(credentials_id, azure_sql_database_credentials_change_validate_in)

Validate a change to Azure SQL Database credentials

Check a change to Azure SQL Database credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.azure_sql_database_credentials_change_validate_in import AzureSqlDatabaseCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    azure_sql_database_credentials_change_validate_in = pycarlo2.AzureSqlDatabaseCredentialsChangeValidateIn() # AzureSqlDatabaseCredentialsChangeValidateIn | 

    try:
        # Validate a change to Azure SQL Database credentials
        api_response = api_instance.validate_azure_sql_database_credentials_change(credentials_id, azure_sql_database_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_azure_sql_database_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_azure_sql_database_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **azure_sql_database_credentials_change_validate_in** | [**AzureSqlDatabaseCredentialsChangeValidateIn**](AzureSqlDatabaseCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_bigquery_credentials**
> ValidationRunOut validate_bigquery_credentials(big_query_credentials_validate_in)

Validate BigQuery credentials

Check a candidate BigQuery service account key against BigQuery.

No credentials are created. Send the key you would create the credentials with, and a
deployment to run it from, and the checks run against your Google Cloud project.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.big_query_credentials_validate_in import BigQueryCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    big_query_credentials_validate_in = pycarlo2.BigQueryCredentialsValidateIn() # BigQueryCredentialsValidateIn | 

    try:
        # Validate BigQuery credentials
        api_response = api_instance.validate_bigquery_credentials(big_query_credentials_validate_in)
        print("The response of CredentialsApi->validate_bigquery_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_bigquery_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **big_query_credentials_validate_in** | [**BigQueryCredentialsValidateIn**](BigQueryCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_bigquery_credentials_change**
> ValidationRunOut validate_bigquery_credentials_change(credentials_id, big_query_credentials_change_validate_in)

Validate a change to BigQuery credentials

Check a change to BigQuery credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.big_query_credentials_change_validate_in import BigQueryCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    big_query_credentials_change_validate_in = pycarlo2.BigQueryCredentialsChangeValidateIn() # BigQueryCredentialsChangeValidateIn | 

    try:
        # Validate a change to BigQuery credentials
        api_response = api_instance.validate_bigquery_credentials_change(credentials_id, big_query_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_bigquery_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_bigquery_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **big_query_credentials_change_validate_in** | [**BigQueryCredentialsChangeValidateIn**](BigQueryCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_clickhouse_credentials**
> ValidationRunOut validate_clickhouse_credentials(click_house_credentials_validate_in)

Validate ClickHouse credentials

Check a candidate ClickHouse login against ClickHouse.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your ClickHouse database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.click_house_credentials_validate_in import ClickHouseCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    click_house_credentials_validate_in = pycarlo2.ClickHouseCredentialsValidateIn() # ClickHouseCredentialsValidateIn | 

    try:
        # Validate ClickHouse credentials
        api_response = api_instance.validate_clickhouse_credentials(click_house_credentials_validate_in)
        print("The response of CredentialsApi->validate_clickhouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_clickhouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **click_house_credentials_validate_in** | [**ClickHouseCredentialsValidateIn**](ClickHouseCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_clickhouse_credentials_change**
> ValidationRunOut validate_clickhouse_credentials_change(credentials_id, click_house_credentials_change_validate_in)

Validate a change to ClickHouse credentials

Check a change to ClickHouse credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.click_house_credentials_change_validate_in import ClickHouseCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    click_house_credentials_change_validate_in = pycarlo2.ClickHouseCredentialsChangeValidateIn() # ClickHouseCredentialsChangeValidateIn | 

    try:
        # Validate a change to ClickHouse credentials
        api_response = api_instance.validate_clickhouse_credentials_change(credentials_id, click_house_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_clickhouse_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_clickhouse_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **click_house_credentials_change_validate_in** | [**ClickHouseCredentialsChangeValidateIn**](ClickHouseCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_databricks_metastore_sql_warehouse_credentials**
> ValidationRunOut validate_databricks_metastore_sql_warehouse_credentials(databricks_metastore_sql_warehouse_credentials_validate_in)

Validate Databricks metadata collection credentials

Check candidate Databricks metadata collection credentials against Databricks.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Databricks workspace.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_validate_in import DatabricksMetastoreSqlWarehouseCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    databricks_metastore_sql_warehouse_credentials_validate_in = pycarlo2.DatabricksMetastoreSqlWarehouseCredentialsValidateIn() # DatabricksMetastoreSqlWarehouseCredentialsValidateIn | 

    try:
        # Validate Databricks metadata collection credentials
        api_response = api_instance.validate_databricks_metastore_sql_warehouse_credentials(databricks_metastore_sql_warehouse_credentials_validate_in)
        print("The response of CredentialsApi->validate_databricks_metastore_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databricks_metastore_sql_warehouse_credentials_validate_in** | [**DatabricksMetastoreSqlWarehouseCredentialsValidateIn**](DatabricksMetastoreSqlWarehouseCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_databricks_metastore_sql_warehouse_credentials_change**
> ValidationRunOut validate_databricks_metastore_sql_warehouse_credentials_change(credentials_id, databricks_metastore_sql_warehouse_credentials_change_validate_in)

Validate a change to Databricks metadata collection credentials

Check a change to Databricks metadata collection credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_metastore_sql_warehouse_credentials_change_validate_in import DatabricksMetastoreSqlWarehouseCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    databricks_metastore_sql_warehouse_credentials_change_validate_in = pycarlo2.DatabricksMetastoreSqlWarehouseCredentialsChangeValidateIn() # DatabricksMetastoreSqlWarehouseCredentialsChangeValidateIn | 

    try:
        # Validate a change to Databricks metadata collection credentials
        api_response = api_instance.validate_databricks_metastore_sql_warehouse_credentials_change(credentials_id, databricks_metastore_sql_warehouse_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_databricks_metastore_sql_warehouse_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_databricks_metastore_sql_warehouse_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **databricks_metastore_sql_warehouse_credentials_change_validate_in** | [**DatabricksMetastoreSqlWarehouseCredentialsChangeValidateIn**](DatabricksMetastoreSqlWarehouseCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_databricks_sql_warehouse_credentials**
> ValidationRunOut validate_databricks_sql_warehouse_credentials(databricks_sql_warehouse_credentials_validate_in)

Validate Databricks query credentials

Check candidate Databricks query credentials against Databricks.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Databricks workspace.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_sql_warehouse_credentials_validate_in import DatabricksSqlWarehouseCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    databricks_sql_warehouse_credentials_validate_in = pycarlo2.DatabricksSqlWarehouseCredentialsValidateIn() # DatabricksSqlWarehouseCredentialsValidateIn | 

    try:
        # Validate Databricks query credentials
        api_response = api_instance.validate_databricks_sql_warehouse_credentials(databricks_sql_warehouse_credentials_validate_in)
        print("The response of CredentialsApi->validate_databricks_sql_warehouse_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_databricks_sql_warehouse_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **databricks_sql_warehouse_credentials_validate_in** | [**DatabricksSqlWarehouseCredentialsValidateIn**](DatabricksSqlWarehouseCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_databricks_sql_warehouse_credentials_change**
> ValidationRunOut validate_databricks_sql_warehouse_credentials_change(credentials_id, databricks_sql_warehouse_credentials_change_validate_in)

Validate a change to Databricks query credentials

Check a change to Databricks query credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.databricks_sql_warehouse_credentials_change_validate_in import DatabricksSqlWarehouseCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    databricks_sql_warehouse_credentials_change_validate_in = pycarlo2.DatabricksSqlWarehouseCredentialsChangeValidateIn() # DatabricksSqlWarehouseCredentialsChangeValidateIn | 

    try:
        # Validate a change to Databricks query credentials
        api_response = api_instance.validate_databricks_sql_warehouse_credentials_change(credentials_id, databricks_sql_warehouse_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_databricks_sql_warehouse_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_databricks_sql_warehouse_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **databricks_sql_warehouse_credentials_change_validate_in** | [**DatabricksSqlWarehouseCredentialsChangeValidateIn**](DatabricksSqlWarehouseCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_db2_credentials**
> ValidationRunOut validate_db2_credentials(db2_credentials_validate_in)

Validate Db2 credentials

Check a candidate Db2 login against Db2.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Db2 database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.db2_credentials_validate_in import Db2CredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    db2_credentials_validate_in = pycarlo2.Db2CredentialsValidateIn() # Db2CredentialsValidateIn | 

    try:
        # Validate Db2 credentials
        api_response = api_instance.validate_db2_credentials(db2_credentials_validate_in)
        print("The response of CredentialsApi->validate_db2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_db2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db2_credentials_validate_in** | [**Db2CredentialsValidateIn**](Db2CredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_db2_credentials_change**
> ValidationRunOut validate_db2_credentials_change(credentials_id, db2_credentials_change_validate_in)

Validate a change to Db2 credentials

Check a change to Db2 credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.db2_credentials_change_validate_in import Db2CredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    db2_credentials_change_validate_in = pycarlo2.Db2CredentialsChangeValidateIn() # Db2CredentialsChangeValidateIn | 

    try:
        # Validate a change to Db2 credentials
        api_response = api_instance.validate_db2_credentials_change(credentials_id, db2_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_db2_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_db2_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **db2_credentials_change_validate_in** | [**Db2CredentialsChangeValidateIn**](Db2CredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_dbt_cloud_webhook_credentials**
> ValidationRunOut validate_dbt_cloud_webhook_credentials(dbt_cloud_webhook_credentials_validate_in)

Validate dbt Cloud webhook credentials

Check candidate dbt Cloud webhook credentials against dbt Cloud.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from. The checks run against your dbt Cloud account.

The response is the run as it starts. `Location` names where to read it. Poll that until the
run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.dbt_cloud_webhook_credentials_validate_in import DbtCloudWebhookCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    dbt_cloud_webhook_credentials_validate_in = pycarlo2.DbtCloudWebhookCredentialsValidateIn() # DbtCloudWebhookCredentialsValidateIn | 

    try:
        # Validate dbt Cloud webhook credentials
        api_response = api_instance.validate_dbt_cloud_webhook_credentials(dbt_cloud_webhook_credentials_validate_in)
        print("The response of CredentialsApi->validate_dbt_cloud_webhook_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_dbt_cloud_webhook_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dbt_cloud_webhook_credentials_validate_in** | [**DbtCloudWebhookCredentialsValidateIn**](DbtCloudWebhookCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_dbt_cloud_webhook_credentials_change**
> ValidationRunOut validate_dbt_cloud_webhook_credentials_change(credentials_id, dbt_cloud_webhook_credentials_change_validate_in)

Validate a change to dbt Cloud webhook credentials

Check a change to dbt Cloud webhook credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials. The checks run against that
copy. The credentials and the connection using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts. `Location` names where to read it. Poll that until the
run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.dbt_cloud_webhook_credentials_change_validate_in import DbtCloudWebhookCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    dbt_cloud_webhook_credentials_change_validate_in = pycarlo2.DbtCloudWebhookCredentialsChangeValidateIn() # DbtCloudWebhookCredentialsChangeValidateIn | 

    try:
        # Validate a change to dbt Cloud webhook credentials
        api_response = api_instance.validate_dbt_cloud_webhook_credentials_change(credentials_id, dbt_cloud_webhook_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_dbt_cloud_webhook_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_dbt_cloud_webhook_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **dbt_cloud_webhook_credentials_change_validate_in** | [**DbtCloudWebhookCredentialsChangeValidateIn**](DbtCloudWebhookCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_env_var_credentials**
> ValidationRunOut validate_env_var_credentials(env_var_credentials_validate_in)

Validate environment variable credentials

Check candidate environment variable credentials against the system they are for.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against that system.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.env_var_credentials_validate_in import EnvVarCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    env_var_credentials_validate_in = pycarlo2.EnvVarCredentialsValidateIn() # EnvVarCredentialsValidateIn | 

    try:
        # Validate environment variable credentials
        api_response = api_instance.validate_env_var_credentials(env_var_credentials_validate_in)
        print("The response of CredentialsApi->validate_env_var_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_env_var_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env_var_credentials_validate_in** | [**EnvVarCredentialsValidateIn**](EnvVarCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_env_var_credentials_change**
> ValidationRunOut validate_env_var_credentials_change(credentials_id, env_var_credentials_change_validate_in)

Validate a change to environment variable credentials

Check a change to environment variable credentials against the system they are for.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
storage returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.env_var_credentials_change_validate_in import EnvVarCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    env_var_credentials_change_validate_in = pycarlo2.EnvVarCredentialsChangeValidateIn() # EnvVarCredentialsChangeValidateIn | 

    try:
        # Validate a change to environment variable credentials
        api_response = api_instance.validate_env_var_credentials_change(credentials_id, env_var_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_env_var_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_env_var_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **env_var_credentials_change_validate_in** | [**EnvVarCredentialsChangeValidateIn**](EnvVarCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_file_credentials**
> ValidationRunOut validate_file_credentials(file_credentials_validate_in)

Validate file credentials

Check candidate file credentials against the system they are for.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against that system.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.file_credentials_validate_in import FileCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    file_credentials_validate_in = pycarlo2.FileCredentialsValidateIn() # FileCredentialsValidateIn | 

    try:
        # Validate file credentials
        api_response = api_instance.validate_file_credentials(file_credentials_validate_in)
        print("The response of CredentialsApi->validate_file_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_file_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_credentials_validate_in** | [**FileCredentialsValidateIn**](FileCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_file_credentials_change**
> ValidationRunOut validate_file_credentials_change(credentials_id, file_credentials_change_validate_in)

Validate a change to file credentials

Check a change to file credentials against the system they are for.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
storage returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.file_credentials_change_validate_in import FileCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    file_credentials_change_validate_in = pycarlo2.FileCredentialsChangeValidateIn() # FileCredentialsChangeValidateIn | 

    try:
        # Validate a change to file credentials
        api_response = api_instance.validate_file_credentials_change(credentials_id, file_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_file_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_file_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **file_credentials_change_validate_in** | [**FileCredentialsChangeValidateIn**](FileCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_fivetran_credentials**
> ValidationRunOut validate_fivetran_credentials(fivetran_credentials_validate_in)

Validate Fivetran credentials

Check candidate Fivetran credentials against Fivetran.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Fivetran account.

The response is the run as it starts, and `Location` names where to read it. Poll that until the
run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.fivetran_credentials_validate_in import FivetranCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    fivetran_credentials_validate_in = pycarlo2.FivetranCredentialsValidateIn() # FivetranCredentialsValidateIn | 

    try:
        # Validate Fivetran credentials
        api_response = api_instance.validate_fivetran_credentials(fivetran_credentials_validate_in)
        print("The response of CredentialsApi->validate_fivetran_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_fivetran_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fivetran_credentials_validate_in** | [**FivetranCredentialsValidateIn**](FivetranCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_fivetran_credentials_change**
> ValidationRunOut validate_fivetran_credentials_change(credentials_id, fivetran_credentials_change_validate_in)

Validate a change to Fivetran credentials

Check a change to Fivetran credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.fivetran_credentials_change_validate_in import FivetranCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    fivetran_credentials_change_validate_in = pycarlo2.FivetranCredentialsChangeValidateIn() # FivetranCredentialsChangeValidateIn | 

    try:
        # Validate a change to Fivetran credentials
        api_response = api_instance.validate_fivetran_credentials_change(credentials_id, fivetran_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_fivetran_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_fivetran_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **fivetran_credentials_change_validate_in** | [**FivetranCredentialsChangeValidateIn**](FivetranCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_dataform_credentials**
> ValidationRunOut validate_gcp_dataform_credentials(gcp_dataform_credentials_validate_in)

Validate GCP Dataform credentials

Check candidate GCP Dataform credentials against GCP Dataform.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against Dataform in your project.

The response is the run as it starts, and `Location` names where to read it. Poll that until the
run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_dataform_credentials_validate_in import GcpDataformCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    gcp_dataform_credentials_validate_in = pycarlo2.GcpDataformCredentialsValidateIn() # GcpDataformCredentialsValidateIn | 

    try:
        # Validate GCP Dataform credentials
        api_response = api_instance.validate_gcp_dataform_credentials(gcp_dataform_credentials_validate_in)
        print("The response of CredentialsApi->validate_gcp_dataform_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_gcp_dataform_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_dataform_credentials_validate_in** | [**GcpDataformCredentialsValidateIn**](GcpDataformCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_dataform_credentials_change**
> ValidationRunOut validate_gcp_dataform_credentials_change(credentials_id, gcp_dataform_credentials_change_validate_in)

Validate a change to GCP Dataform credentials

Check a change to GCP Dataform credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_dataform_credentials_change_validate_in import GcpDataformCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    gcp_dataform_credentials_change_validate_in = pycarlo2.GcpDataformCredentialsChangeValidateIn() # GcpDataformCredentialsChangeValidateIn | 

    try:
        # Validate a change to GCP Dataform credentials
        api_response = api_instance.validate_gcp_dataform_credentials_change(credentials_id, gcp_dataform_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_gcp_dataform_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_gcp_dataform_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **gcp_dataform_credentials_change_validate_in** | [**GcpDataformCredentialsChangeValidateIn**](GcpDataformCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_secret_manager_credentials**
> ValidationRunOut validate_gcp_secret_manager_credentials(gcp_secret_manager_credentials_validate_in)

Validate GCP Secret Manager credentials

Check candidate GCP Secret Manager credentials against the system they are for.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against that system.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_secret_manager_credentials_validate_in import GcpSecretManagerCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    gcp_secret_manager_credentials_validate_in = pycarlo2.GcpSecretManagerCredentialsValidateIn() # GcpSecretManagerCredentialsValidateIn | 

    try:
        # Validate GCP Secret Manager credentials
        api_response = api_instance.validate_gcp_secret_manager_credentials(gcp_secret_manager_credentials_validate_in)
        print("The response of CredentialsApi->validate_gcp_secret_manager_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_gcp_secret_manager_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_secret_manager_credentials_validate_in** | [**GcpSecretManagerCredentialsValidateIn**](GcpSecretManagerCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_gcp_secret_manager_credentials_change**
> ValidationRunOut validate_gcp_secret_manager_credentials_change(credentials_id, gcp_secret_manager_credentials_change_validate_in)

Validate a change to GCP Secret Manager credentials

Check a change to GCP Secret Manager credentials against the system they are for.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
storage returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.gcp_secret_manager_credentials_change_validate_in import GcpSecretManagerCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    gcp_secret_manager_credentials_change_validate_in = pycarlo2.GcpSecretManagerCredentialsChangeValidateIn() # GcpSecretManagerCredentialsChangeValidateIn | 

    try:
        # Validate a change to GCP Secret Manager credentials
        api_response = api_instance.validate_gcp_secret_manager_credentials_change(credentials_id, gcp_secret_manager_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_gcp_secret_manager_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_gcp_secret_manager_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **gcp_secret_manager_credentials_change_validate_in** | [**GcpSecretManagerCredentialsChangeValidateIn**](GcpSecretManagerCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_glue_credentials**
> ValidationRunOut validate_glue_credentials(glue_credentials_validate_in)

Validate Glue credentials

Check candidate Glue credentials against your AWS account.

No credentials are created. Send the fields you would create the credentials with, and a
deployment to run them from, and the checks run against your Glue catalog.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.glue_credentials_validate_in import GlueCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    glue_credentials_validate_in = pycarlo2.GlueCredentialsValidateIn() # GlueCredentialsValidateIn | 

    try:
        # Validate Glue credentials
        api_response = api_instance.validate_glue_credentials(glue_credentials_validate_in)
        print("The response of CredentialsApi->validate_glue_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_glue_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **glue_credentials_validate_in** | [**GlueCredentialsValidateIn**](GlueCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_glue_credentials_change**
> ValidationRunOut validate_glue_credentials_change(credentials_id, glue_credentials_change_validate_in)

Validate a change to Glue credentials

Check a change to Glue credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.glue_credentials_change_validate_in import GlueCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    glue_credentials_change_validate_in = pycarlo2.GlueCredentialsChangeValidateIn() # GlueCredentialsChangeValidateIn | 

    try:
        # Validate a change to Glue credentials
        api_response = api_instance.validate_glue_credentials_change(credentials_id, glue_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_glue_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_glue_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **glue_credentials_change_validate_in** | [**GlueCredentialsChangeValidateIn**](GlueCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_informatica_v2_credentials**
> ValidationRunOut validate_informatica_v2_credentials(informatica_v2_credentials_validate_in)

Validate Informatica credentials

Check candidate Informatica credentials against Informatica.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Informatica organization.

The response is the run as it starts, and `Location` names where to read it. Poll that until the
run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.informatica_v2_credentials_validate_in import InformaticaV2CredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    informatica_v2_credentials_validate_in = pycarlo2.InformaticaV2CredentialsValidateIn() # InformaticaV2CredentialsValidateIn | 

    try:
        # Validate Informatica credentials
        api_response = api_instance.validate_informatica_v2_credentials(informatica_v2_credentials_validate_in)
        print("The response of CredentialsApi->validate_informatica_v2_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_informatica_v2_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **informatica_v2_credentials_validate_in** | [**InformaticaV2CredentialsValidateIn**](InformaticaV2CredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_informatica_v2_credentials_change**
> ValidationRunOut validate_informatica_v2_credentials_change(credentials_id, informatica_v2_credentials_change_validate_in)

Validate a change to Informatica credentials

Check a change to Informatica credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.informatica_v2_credentials_change_validate_in import InformaticaV2CredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    informatica_v2_credentials_change_validate_in = pycarlo2.InformaticaV2CredentialsChangeValidateIn() # InformaticaV2CredentialsChangeValidateIn | 

    try:
        # Validate a change to Informatica credentials
        api_response = api_instance.validate_informatica_v2_credentials_change(credentials_id, informatica_v2_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_informatica_v2_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_informatica_v2_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **informatica_v2_credentials_change_validate_in** | [**InformaticaV2CredentialsChangeValidateIn**](InformaticaV2CredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_looker_credentials**
> ValidationRunOut validate_looker_credentials(looker_credentials_validate_in)

Validate Looker credentials

Check candidate Looker API credentials against Looker.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Looker instance.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_credentials_validate_in import LookerCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    looker_credentials_validate_in = pycarlo2.LookerCredentialsValidateIn() # LookerCredentialsValidateIn | 

    try:
        # Validate Looker credentials
        api_response = api_instance.validate_looker_credentials(looker_credentials_validate_in)
        print("The response of CredentialsApi->validate_looker_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_looker_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **looker_credentials_validate_in** | [**LookerCredentialsValidateIn**](LookerCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_looker_credentials_change**
> ValidationRunOut validate_looker_credentials_change(credentials_id, looker_credentials_change_validate_in)

Validate a change to Looker credentials

Check a change to Looker credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_credentials_change_validate_in import LookerCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    looker_credentials_change_validate_in = pycarlo2.LookerCredentialsChangeValidateIn() # LookerCredentialsChangeValidateIn | 

    try:
        # Validate a change to Looker credentials
        api_response = api_instance.validate_looker_credentials_change(credentials_id, looker_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_looker_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_looker_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **looker_credentials_change_validate_in** | [**LookerCredentialsChangeValidateIn**](LookerCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_looker_git_clone_credentials**
> ValidationRunOut validate_looker_git_clone_credentials(looker_git_clone_credentials_validate_in)

Validate LookML repository credentials

Check candidate LookML repository credentials against the repository.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your git server.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_git_clone_credentials_validate_in import LookerGitCloneCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    looker_git_clone_credentials_validate_in = pycarlo2.LookerGitCloneCredentialsValidateIn() # LookerGitCloneCredentialsValidateIn | 

    try:
        # Validate LookML repository credentials
        api_response = api_instance.validate_looker_git_clone_credentials(looker_git_clone_credentials_validate_in)
        print("The response of CredentialsApi->validate_looker_git_clone_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_looker_git_clone_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **looker_git_clone_credentials_validate_in** | [**LookerGitCloneCredentialsValidateIn**](LookerGitCloneCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_looker_git_clone_credentials_change**
> ValidationRunOut validate_looker_git_clone_credentials_change(credentials_id, looker_git_clone_credentials_change_validate_in)

Validate a change to LookML repository credentials

Check a change to LookML repository credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.looker_git_clone_credentials_change_validate_in import LookerGitCloneCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    looker_git_clone_credentials_change_validate_in = pycarlo2.LookerGitCloneCredentialsChangeValidateIn() # LookerGitCloneCredentialsChangeValidateIn | 

    try:
        # Validate a change to LookML repository credentials
        api_response = api_instance.validate_looker_git_clone_credentials_change(credentials_id, looker_git_clone_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_looker_git_clone_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_looker_git_clone_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **looker_git_clone_credentials_change_validate_in** | [**LookerGitCloneCredentialsChangeValidateIn**](LookerGitCloneCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mariadb_credentials**
> ValidationRunOut validate_mariadb_credentials(maria_db_credentials_validate_in)

Validate MariaDB credentials

Check a candidate MariaDB login against MariaDB.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your MariaDB database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.maria_db_credentials_validate_in import MariaDbCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    maria_db_credentials_validate_in = pycarlo2.MariaDbCredentialsValidateIn() # MariaDbCredentialsValidateIn | 

    try:
        # Validate MariaDB credentials
        api_response = api_instance.validate_mariadb_credentials(maria_db_credentials_validate_in)
        print("The response of CredentialsApi->validate_mariadb_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mariadb_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maria_db_credentials_validate_in** | [**MariaDbCredentialsValidateIn**](MariaDbCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mariadb_credentials_change**
> ValidationRunOut validate_mariadb_credentials_change(credentials_id, maria_db_credentials_change_validate_in)

Validate a change to MariaDB credentials

Check a change to MariaDB credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.maria_db_credentials_change_validate_in import MariaDbCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    maria_db_credentials_change_validate_in = pycarlo2.MariaDbCredentialsChangeValidateIn() # MariaDbCredentialsChangeValidateIn | 

    try:
        # Validate a change to MariaDB credentials
        api_response = api_instance.validate_mariadb_credentials_change(credentials_id, maria_db_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_mariadb_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mariadb_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **maria_db_credentials_change_validate_in** | [**MariaDbCredentialsChangeValidateIn**](MariaDbCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mulesoft_credentials**
> ValidationRunOut validate_mulesoft_credentials(mulesoft_credentials_validate_in)

Validate MuleSoft credentials

Check candidate MuleSoft credentials against MuleSoft.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Anypoint organization.

The response is the run as it starts, and `Location` names where to read it. Poll that until the
run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.mulesoft_credentials_validate_in import MulesoftCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    mulesoft_credentials_validate_in = pycarlo2.MulesoftCredentialsValidateIn() # MulesoftCredentialsValidateIn | 

    try:
        # Validate MuleSoft credentials
        api_response = api_instance.validate_mulesoft_credentials(mulesoft_credentials_validate_in)
        print("The response of CredentialsApi->validate_mulesoft_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mulesoft_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mulesoft_credentials_validate_in** | [**MulesoftCredentialsValidateIn**](MulesoftCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mulesoft_credentials_change**
> ValidationRunOut validate_mulesoft_credentials_change(credentials_id, mulesoft_credentials_change_validate_in)

Validate a change to MuleSoft credentials

Check a change to MuleSoft credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.mulesoft_credentials_change_validate_in import MulesoftCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    mulesoft_credentials_change_validate_in = pycarlo2.MulesoftCredentialsChangeValidateIn() # MulesoftCredentialsChangeValidateIn | 

    try:
        # Validate a change to MuleSoft credentials
        api_response = api_instance.validate_mulesoft_credentials_change(credentials_id, mulesoft_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_mulesoft_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mulesoft_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **mulesoft_credentials_change_validate_in** | [**MulesoftCredentialsChangeValidateIn**](MulesoftCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mysql_credentials**
> ValidationRunOut validate_mysql_credentials(my_sql_credentials_validate_in)

Validate MySQL credentials

Check a candidate MySQL login against MySQL.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your MySQL database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.my_sql_credentials_validate_in import MySqlCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    my_sql_credentials_validate_in = pycarlo2.MySqlCredentialsValidateIn() # MySqlCredentialsValidateIn | 

    try:
        # Validate MySQL credentials
        api_response = api_instance.validate_mysql_credentials(my_sql_credentials_validate_in)
        print("The response of CredentialsApi->validate_mysql_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mysql_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **my_sql_credentials_validate_in** | [**MySqlCredentialsValidateIn**](MySqlCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_mysql_credentials_change**
> ValidationRunOut validate_mysql_credentials_change(credentials_id, my_sql_credentials_change_validate_in)

Validate a change to MySQL credentials

Check a change to MySQL credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.my_sql_credentials_change_validate_in import MySqlCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    my_sql_credentials_change_validate_in = pycarlo2.MySqlCredentialsChangeValidateIn() # MySqlCredentialsChangeValidateIn | 

    try:
        # Validate a change to MySQL credentials
        api_response = api_instance.validate_mysql_credentials_change(credentials_id, my_sql_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_mysql_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_mysql_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **my_sql_credentials_change_validate_in** | [**MySqlCredentialsChangeValidateIn**](MySqlCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_oracle_credentials**
> ValidationRunOut validate_oracle_credentials(oracle_credentials_validate_in)

Validate Oracle credentials

Check a candidate Oracle login against Oracle.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Oracle database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.oracle_credentials_validate_in import OracleCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    oracle_credentials_validate_in = pycarlo2.OracleCredentialsValidateIn() # OracleCredentialsValidateIn | 

    try:
        # Validate Oracle credentials
        api_response = api_instance.validate_oracle_credentials(oracle_credentials_validate_in)
        print("The response of CredentialsApi->validate_oracle_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_oracle_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oracle_credentials_validate_in** | [**OracleCredentialsValidateIn**](OracleCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_oracle_credentials_change**
> ValidationRunOut validate_oracle_credentials_change(credentials_id, oracle_credentials_change_validate_in)

Validate a change to Oracle credentials

Check a change to Oracle credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.oracle_credentials_change_validate_in import OracleCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    oracle_credentials_change_validate_in = pycarlo2.OracleCredentialsChangeValidateIn() # OracleCredentialsChangeValidateIn | 

    try:
        # Validate a change to Oracle credentials
        api_response = api_instance.validate_oracle_credentials_change(credentials_id, oracle_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_oracle_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_oracle_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **oracle_credentials_change_validate_in** | [**OracleCredentialsChangeValidateIn**](OracleCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_postgres_credentials**
> ValidationRunOut validate_postgres_credentials(postgres_credentials_validate_in)

Validate PostgreSQL credentials

Check a candidate PostgreSQL login against PostgreSQL.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your PostgreSQL database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.postgres_credentials_validate_in import PostgresCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    postgres_credentials_validate_in = pycarlo2.PostgresCredentialsValidateIn() # PostgresCredentialsValidateIn | 

    try:
        # Validate PostgreSQL credentials
        api_response = api_instance.validate_postgres_credentials(postgres_credentials_validate_in)
        print("The response of CredentialsApi->validate_postgres_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_postgres_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postgres_credentials_validate_in** | [**PostgresCredentialsValidateIn**](PostgresCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_postgres_credentials_change**
> ValidationRunOut validate_postgres_credentials_change(credentials_id, postgres_credentials_change_validate_in)

Validate a change to PostgreSQL credentials

Check a change to PostgreSQL credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.postgres_credentials_change_validate_in import PostgresCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    postgres_credentials_change_validate_in = pycarlo2.PostgresCredentialsChangeValidateIn() # PostgresCredentialsChangeValidateIn | 

    try:
        # Validate a change to PostgreSQL credentials
        api_response = api_instance.validate_postgres_credentials_change(credentials_id, postgres_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_postgres_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_postgres_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **postgres_credentials_change_validate_in** | [**PostgresCredentialsChangeValidateIn**](PostgresCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_power_bi_credentials**
> ValidationRunOut validate_power_bi_credentials(power_bi_credentials_validate_in)

Validate Power BI credentials

Check candidate Power BI credentials against Power BI.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Power BI tenant.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.power_bi_credentials_validate_in import PowerBiCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    power_bi_credentials_validate_in = pycarlo2.PowerBiCredentialsValidateIn() # PowerBiCredentialsValidateIn | 

    try:
        # Validate Power BI credentials
        api_response = api_instance.validate_power_bi_credentials(power_bi_credentials_validate_in)
        print("The response of CredentialsApi->validate_power_bi_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_power_bi_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_bi_credentials_validate_in** | [**PowerBiCredentialsValidateIn**](PowerBiCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_power_bi_credentials_change**
> ValidationRunOut validate_power_bi_credentials_change(credentials_id, power_bi_credentials_change_validate_in)

Validate a change to Power BI credentials

Check a change to Power BI credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.power_bi_credentials_change_validate_in import PowerBiCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    power_bi_credentials_change_validate_in = pycarlo2.PowerBiCredentialsChangeValidateIn() # PowerBiCredentialsChangeValidateIn | 

    try:
        # Validate a change to Power BI credentials
        api_response = api_instance.validate_power_bi_credentials_change(credentials_id, power_bi_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_power_bi_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_power_bi_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **power_bi_credentials_change_validate_in** | [**PowerBiCredentialsChangeValidateIn**](PowerBiCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_redshift_credentials**
> ValidationRunOut validate_redshift_credentials(redshift_credentials_validate_in)

Validate Redshift credentials

Check a candidate Redshift login against Redshift.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Redshift database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.redshift_credentials_validate_in import RedshiftCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    redshift_credentials_validate_in = pycarlo2.RedshiftCredentialsValidateIn() # RedshiftCredentialsValidateIn | 

    try:
        # Validate Redshift credentials
        api_response = api_instance.validate_redshift_credentials(redshift_credentials_validate_in)
        print("The response of CredentialsApi->validate_redshift_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_redshift_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redshift_credentials_validate_in** | [**RedshiftCredentialsValidateIn**](RedshiftCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_redshift_credentials_change**
> ValidationRunOut validate_redshift_credentials_change(credentials_id, redshift_credentials_change_validate_in)

Validate a change to Redshift credentials

Check a change to Redshift credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.redshift_credentials_change_validate_in import RedshiftCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    redshift_credentials_change_validate_in = pycarlo2.RedshiftCredentialsChangeValidateIn() # RedshiftCredentialsChangeValidateIn | 

    try:
        # Validate a change to Redshift credentials
        api_response = api_instance.validate_redshift_credentials_change(credentials_id, redshift_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_redshift_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_redshift_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **redshift_credentials_change_validate_in** | [**RedshiftCredentialsChangeValidateIn**](RedshiftCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_salesforce_crm_credentials**
> ValidationRunOut validate_salesforce_crm_credentials(salesforce_crm_credentials_validate_in)

Validate Salesforce CRM credentials

Check a candidate Salesforce sign-in against Salesforce.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Salesforce org.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.salesforce_crm_credentials_validate_in import SalesforceCrmCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    salesforce_crm_credentials_validate_in = pycarlo2.SalesforceCrmCredentialsValidateIn() # SalesforceCrmCredentialsValidateIn | 

    try:
        # Validate Salesforce CRM credentials
        api_response = api_instance.validate_salesforce_crm_credentials(salesforce_crm_credentials_validate_in)
        print("The response of CredentialsApi->validate_salesforce_crm_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_salesforce_crm_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_crm_credentials_validate_in** | [**SalesforceCrmCredentialsValidateIn**](SalesforceCrmCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_salesforce_crm_credentials_change**
> ValidationRunOut validate_salesforce_crm_credentials_change(credentials_id, salesforce_crm_credentials_change_validate_in)

Validate a change to Salesforce CRM credentials

Check a change to Salesforce CRM credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`. Each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.salesforce_crm_credentials_change_validate_in import SalesforceCrmCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    salesforce_crm_credentials_change_validate_in = pycarlo2.SalesforceCrmCredentialsChangeValidateIn() # SalesforceCrmCredentialsChangeValidateIn | 

    try:
        # Validate a change to Salesforce CRM credentials
        api_response = api_instance.validate_salesforce_crm_credentials_change(credentials_id, salesforce_crm_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_salesforce_crm_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_salesforce_crm_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **salesforce_crm_credentials_change_validate_in** | [**SalesforceCrmCredentialsChangeValidateIn**](SalesforceCrmCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sap_hana_credentials**
> ValidationRunOut validate_sap_hana_credentials(sap_hana_credentials_validate_in)

Validate SAP HANA credentials

Check a candidate SAP HANA login against SAP HANA.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your SAP HANA database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sap_hana_credentials_validate_in import SapHanaCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    sap_hana_credentials_validate_in = pycarlo2.SapHanaCredentialsValidateIn() # SapHanaCredentialsValidateIn | 

    try:
        # Validate SAP HANA credentials
        api_response = api_instance.validate_sap_hana_credentials(sap_hana_credentials_validate_in)
        print("The response of CredentialsApi->validate_sap_hana_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_sap_hana_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sap_hana_credentials_validate_in** | [**SapHanaCredentialsValidateIn**](SapHanaCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sap_hana_credentials_change**
> ValidationRunOut validate_sap_hana_credentials_change(credentials_id, sap_hana_credentials_change_validate_in)

Validate a change to SAP HANA credentials

Check a change to SAP HANA credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sap_hana_credentials_change_validate_in import SapHanaCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    sap_hana_credentials_change_validate_in = pycarlo2.SapHanaCredentialsChangeValidateIn() # SapHanaCredentialsChangeValidateIn | 

    try:
        # Validate a change to SAP HANA credentials
        api_response = api_instance.validate_sap_hana_credentials_change(credentials_id, sap_hana_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_sap_hana_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_sap_hana_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **sap_hana_credentials_change_validate_in** | [**SapHanaCredentialsChangeValidateIn**](SapHanaCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_snowflake_credentials**
> ValidationRunOut validate_snowflake_credentials(snowflake_credentials_validate_in)

Validate Snowflake credentials

Check a candidate Snowflake key pair against Snowflake.

No credentials are created. Send the values you would create the credentials with, and
a deployment to run them from, and the checks run against your Snowflake account.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.snowflake_credentials_validate_in import SnowflakeCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    snowflake_credentials_validate_in = pycarlo2.SnowflakeCredentialsValidateIn() # SnowflakeCredentialsValidateIn | 

    try:
        # Validate Snowflake credentials
        api_response = api_instance.validate_snowflake_credentials(snowflake_credentials_validate_in)
        print("The response of CredentialsApi->validate_snowflake_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_snowflake_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snowflake_credentials_validate_in** | [**SnowflakeCredentialsValidateIn**](SnowflakeCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_snowflake_credentials_change**
> ValidationRunOut validate_snowflake_credentials_change(credentials_id, snowflake_credentials_change_validate_in)

Validate a change to Snowflake credentials

Check a change to Snowflake credentials against Snowflake before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.snowflake_credentials_change_validate_in import SnowflakeCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    snowflake_credentials_change_validate_in = pycarlo2.SnowflakeCredentialsChangeValidateIn() # SnowflakeCredentialsChangeValidateIn | 

    try:
        # Validate a change to Snowflake credentials
        api_response = api_instance.validate_snowflake_credentials_change(credentials_id, snowflake_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_snowflake_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_snowflake_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **snowflake_credentials_change_validate_in** | [**SnowflakeCredentialsChangeValidateIn**](SnowflakeCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sql_server_credentials**
> ValidationRunOut validate_sql_server_credentials(sql_server_credentials_validate_in)

Validate SQL Server credentials

Check a candidate SQL Server login against SQL Server.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your SQL Server database. Kerberos
needs a deployment whose agent can reach the key distribution center.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sql_server_credentials_validate_in import SqlServerCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    sql_server_credentials_validate_in = pycarlo2.SqlServerCredentialsValidateIn() # SqlServerCredentialsValidateIn | 

    try:
        # Validate SQL Server credentials
        api_response = api_instance.validate_sql_server_credentials(sql_server_credentials_validate_in)
        print("The response of CredentialsApi->validate_sql_server_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_sql_server_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sql_server_credentials_validate_in** | [**SqlServerCredentialsValidateIn**](SqlServerCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_sql_server_credentials_change**
> ValidationRunOut validate_sql_server_credentials_change(credentials_id, sql_server_credentials_change_validate_in)

Validate a change to SQL Server credentials

Check a change to SQL Server credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.sql_server_credentials_change_validate_in import SqlServerCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    sql_server_credentials_change_validate_in = pycarlo2.SqlServerCredentialsChangeValidateIn() # SqlServerCredentialsChangeValidateIn | 

    try:
        # Validate a change to SQL Server credentials
        api_response = api_instance.validate_sql_server_credentials_change(credentials_id, sql_server_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_sql_server_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_sql_server_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **sql_server_credentials_change_validate_in** | [**SqlServerCredentialsChangeValidateIn**](SqlServerCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_starburst_enterprise_credentials**
> ValidationRunOut validate_starburst_enterprise_credentials(starburst_enterprise_credentials_validate_in)

Validate Starburst Enterprise credentials

Check a candidate Starburst Enterprise login against Starburst Enterprise.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Starburst Enterprise database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_enterprise_credentials_validate_in import StarburstEnterpriseCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    starburst_enterprise_credentials_validate_in = pycarlo2.StarburstEnterpriseCredentialsValidateIn() # StarburstEnterpriseCredentialsValidateIn | 

    try:
        # Validate Starburst Enterprise credentials
        api_response = api_instance.validate_starburst_enterprise_credentials(starburst_enterprise_credentials_validate_in)
        print("The response of CredentialsApi->validate_starburst_enterprise_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_starburst_enterprise_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starburst_enterprise_credentials_validate_in** | [**StarburstEnterpriseCredentialsValidateIn**](StarburstEnterpriseCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_starburst_enterprise_credentials_change**
> ValidationRunOut validate_starburst_enterprise_credentials_change(credentials_id, starburst_enterprise_credentials_change_validate_in)

Validate a change to Starburst Enterprise credentials

Check a change to Starburst Enterprise credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_enterprise_credentials_change_validate_in import StarburstEnterpriseCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    starburst_enterprise_credentials_change_validate_in = pycarlo2.StarburstEnterpriseCredentialsChangeValidateIn() # StarburstEnterpriseCredentialsChangeValidateIn | 

    try:
        # Validate a change to Starburst Enterprise credentials
        api_response = api_instance.validate_starburst_enterprise_credentials_change(credentials_id, starburst_enterprise_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_starburst_enterprise_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_starburst_enterprise_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **starburst_enterprise_credentials_change_validate_in** | [**StarburstEnterpriseCredentialsChangeValidateIn**](StarburstEnterpriseCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_starburst_galaxy_credentials**
> ValidationRunOut validate_starburst_galaxy_credentials(starburst_galaxy_credentials_validate_in)

Validate Starburst Galaxy credentials

Check a candidate Starburst Galaxy login against Starburst Galaxy.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Starburst Galaxy database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_galaxy_credentials_validate_in import StarburstGalaxyCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    starburst_galaxy_credentials_validate_in = pycarlo2.StarburstGalaxyCredentialsValidateIn() # StarburstGalaxyCredentialsValidateIn | 

    try:
        # Validate Starburst Galaxy credentials
        api_response = api_instance.validate_starburst_galaxy_credentials(starburst_galaxy_credentials_validate_in)
        print("The response of CredentialsApi->validate_starburst_galaxy_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_starburst_galaxy_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starburst_galaxy_credentials_validate_in** | [**StarburstGalaxyCredentialsValidateIn**](StarburstGalaxyCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_starburst_galaxy_credentials_change**
> ValidationRunOut validate_starburst_galaxy_credentials_change(credentials_id, starburst_galaxy_credentials_change_validate_in)

Validate a change to Starburst Galaxy credentials

Check a change to Starburst Galaxy credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.starburst_galaxy_credentials_change_validate_in import StarburstGalaxyCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    starburst_galaxy_credentials_change_validate_in = pycarlo2.StarburstGalaxyCredentialsChangeValidateIn() # StarburstGalaxyCredentialsChangeValidateIn | 

    try:
        # Validate a change to Starburst Galaxy credentials
        api_response = api_instance.validate_starburst_galaxy_credentials_change(credentials_id, starburst_galaxy_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_starburst_galaxy_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_starburst_galaxy_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **starburst_galaxy_credentials_change_validate_in** | [**StarburstGalaxyCredentialsChangeValidateIn**](StarburstGalaxyCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_tableau_credentials**
> ValidationRunOut validate_tableau_credentials(tableau_credentials_validate_in)

Validate Tableau credentials

Check candidate Tableau credentials against Tableau.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Tableau server.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.tableau_credentials_validate_in import TableauCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    tableau_credentials_validate_in = pycarlo2.TableauCredentialsValidateIn() # TableauCredentialsValidateIn | 

    try:
        # Validate Tableau credentials
        api_response = api_instance.validate_tableau_credentials(tableau_credentials_validate_in)
        print("The response of CredentialsApi->validate_tableau_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_tableau_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tableau_credentials_validate_in** | [**TableauCredentialsValidateIn**](TableauCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_tableau_credentials_change**
> ValidationRunOut validate_tableau_credentials_change(credentials_id, tableau_credentials_change_validate_in)

Validate a change to Tableau credentials

Check a change to Tableau credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.tableau_credentials_change_validate_in import TableauCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    tableau_credentials_change_validate_in = pycarlo2.TableauCredentialsChangeValidateIn() # TableauCredentialsChangeValidateIn | 

    try:
        # Validate a change to Tableau credentials
        api_response = api_instance.validate_tableau_credentials_change(credentials_id, tableau_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_tableau_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_tableau_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **tableau_credentials_change_validate_in** | [**TableauCredentialsChangeValidateIn**](TableauCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_teradata_credentials**
> ValidationRunOut validate_teradata_credentials(teradata_credentials_validate_in)

Validate Teradata credentials

Check a candidate Teradata login against Teradata.

No credentials are created. Send the values you would create the credentials with, and a
deployment to run them from, and the checks run against your Teradata database.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.teradata_credentials_validate_in import TeradataCredentialsValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    teradata_credentials_validate_in = pycarlo2.TeradataCredentialsValidateIn() # TeradataCredentialsValidateIn | 

    try:
        # Validate Teradata credentials
        api_response = api_instance.validate_teradata_credentials(teradata_credentials_validate_in)
        print("The response of CredentialsApi->validate_teradata_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_teradata_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teradata_credentials_validate_in** | [**TeradataCredentialsValidateIn**](TeradataCredentialsValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_teradata_credentials_change**
> ValidationRunOut validate_teradata_credentials_change(credentials_id, teradata_credentials_change_validate_in)

Validate a change to Teradata credentials

Check a change to Teradata credentials before making it.

Send the fields you would update the credentials with, and a deployment to run them from.
The change is applied to a copy of the stored credentials, and the checks run against
that copy. The credentials and the connections using them are left as they are.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.teradata_credentials_change_validate_in import TeradataCredentialsChangeValidateIn
from pycarlo2.models.validation_run_out import ValidationRunOut
from pycarlo2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pycarlo2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = pycarlo2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pycarlo2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pycarlo2.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the credentials, as returned when they are created or listed.
    teradata_credentials_change_validate_in = pycarlo2.TeradataCredentialsChangeValidateIn() # TeradataCredentialsChangeValidateIn | 

    try:
        # Validate a change to Teradata credentials
        api_response = api_instance.validate_teradata_credentials_change(credentials_id, teradata_credentials_change_validate_in)
        print("The response of CredentialsApi->validate_teradata_credentials_change:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->validate_teradata_credentials_change: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **UUID**| Id of the credentials, as returned when they are created or listed. | 
 **teradata_credentials_change_validate_in** | [**TeradataCredentialsChangeValidateIn**](TeradataCredentialsChangeValidateIn.md)|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

