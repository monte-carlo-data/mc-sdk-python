# montecarlo.CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_secrets_manager_credentials**](CredentialsApi.md#create_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws | Create AWS Secrets Manager credentials
[**create_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#create_azure_dedicated_sql_pool_credentials) | **POST** /api/v2/credentials/azure-dedicated-sql-pool | Create Azure Dedicated SQL Pool credentials
[**create_azure_key_vault_credentials**](CredentialsApi.md#create_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure | Create Azure Key Vault credentials
[**create_azure_sql_database_credentials**](CredentialsApi.md#create_azure_sql_database_credentials) | **POST** /api/v2/credentials/azure-sql-database | Create Azure SQL Database credentials
[**create_bigquery_credentials**](CredentialsApi.md#create_bigquery_credentials) | **POST** /api/v2/credentials/bigquery | Create BigQuery credentials
[**create_clickhouse_credentials**](CredentialsApi.md#create_clickhouse_credentials) | **POST** /api/v2/credentials/clickhouse | Create ClickHouse credentials
[**create_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse | Create Databricks metadata collection credentials
[**create_databricks_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse | Create Databricks query credentials
[**create_db2_credentials**](CredentialsApi.md#create_db2_credentials) | **POST** /api/v2/credentials/db2 | Create Db2 credentials
[**create_env_var_credentials**](CredentialsApi.md#create_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var | Create environment variable credentials
[**create_file_credentials**](CredentialsApi.md#create_file_credentials) | **POST** /api/v2/credentials/self-hosted/file | Create file credentials
[**create_gcp_secret_manager_credentials**](CredentialsApi.md#create_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp | Create GCP Secret Manager credentials
[**create_mariadb_credentials**](CredentialsApi.md#create_mariadb_credentials) | **POST** /api/v2/credentials/mariadb | Create MariaDB credentials
[**create_mysql_credentials**](CredentialsApi.md#create_mysql_credentials) | **POST** /api/v2/credentials/mysql | Create MySQL credentials
[**create_oracle_credentials**](CredentialsApi.md#create_oracle_credentials) | **POST** /api/v2/credentials/oracle | Create Oracle credentials
[**create_postgres_credentials**](CredentialsApi.md#create_postgres_credentials) | **POST** /api/v2/credentials/postgres | Create PostgreSQL credentials
[**create_redshift_credentials**](CredentialsApi.md#create_redshift_credentials) | **POST** /api/v2/credentials/redshift | Create Redshift credentials
[**create_sap_hana_credentials**](CredentialsApi.md#create_sap_hana_credentials) | **POST** /api/v2/credentials/sap-hana | Create SAP HANA credentials
[**create_snowflake_credentials**](CredentialsApi.md#create_snowflake_credentials) | **POST** /api/v2/credentials/snowflake | Create Snowflake credentials
[**create_starburst_enterprise_credentials**](CredentialsApi.md#create_starburst_enterprise_credentials) | **POST** /api/v2/credentials/starburst-enterprise | Create Starburst Enterprise credentials
[**create_starburst_galaxy_credentials**](CredentialsApi.md#create_starburst_galaxy_credentials) | **POST** /api/v2/credentials/starburst-galaxy | Create Starburst Galaxy credentials
[**create_teradata_credentials**](CredentialsApi.md#create_teradata_credentials) | **POST** /api/v2/credentials/teradata | Create Teradata credentials
[**delete_aws_secrets_manager_credentials**](CredentialsApi.md#delete_aws_secrets_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/aws/{credentials_id} | Delete AWS Secrets Manager credentials
[**delete_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#delete_azure_dedicated_sql_pool_credentials) | **DELETE** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Delete Azure Dedicated SQL Pool credentials
[**delete_azure_key_vault_credentials**](CredentialsApi.md#delete_azure_key_vault_credentials) | **DELETE** /api/v2/credentials/self-hosted/azure/{credentials_id} | Delete Azure Key Vault credentials
[**delete_azure_sql_database_credentials**](CredentialsApi.md#delete_azure_sql_database_credentials) | **DELETE** /api/v2/credentials/azure-sql-database/{credentials_id} | Delete Azure SQL Database credentials
[**delete_bigquery_credentials**](CredentialsApi.md#delete_bigquery_credentials) | **DELETE** /api/v2/credentials/bigquery/{credentials_id} | Delete BigQuery credentials
[**delete_clickhouse_credentials**](CredentialsApi.md#delete_clickhouse_credentials) | **DELETE** /api/v2/credentials/clickhouse/{credentials_id} | Delete ClickHouse credentials
[**delete_credentials**](CredentialsApi.md#delete_credentials) | **DELETE** /api/v2/credentials/{credentials_id} | Delete credentials
[**delete_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_metastore_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Delete Databricks metadata collection credentials
[**delete_databricks_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Delete Databricks query credentials
[**delete_db2_credentials**](CredentialsApi.md#delete_db2_credentials) | **DELETE** /api/v2/credentials/db2/{credentials_id} | Delete Db2 credentials
[**delete_env_var_credentials**](CredentialsApi.md#delete_env_var_credentials) | **DELETE** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Delete environment variable credentials
[**delete_file_credentials**](CredentialsApi.md#delete_file_credentials) | **DELETE** /api/v2/credentials/self-hosted/file/{credentials_id} | Delete file credentials
[**delete_gcp_secret_manager_credentials**](CredentialsApi.md#delete_gcp_secret_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Delete GCP Secret Manager credentials
[**delete_mariadb_credentials**](CredentialsApi.md#delete_mariadb_credentials) | **DELETE** /api/v2/credentials/mariadb/{credentials_id} | Delete MariaDB credentials
[**delete_mysql_credentials**](CredentialsApi.md#delete_mysql_credentials) | **DELETE** /api/v2/credentials/mysql/{credentials_id} | Delete MySQL credentials
[**delete_oracle_credentials**](CredentialsApi.md#delete_oracle_credentials) | **DELETE** /api/v2/credentials/oracle/{credentials_id} | Delete Oracle credentials
[**delete_postgres_credentials**](CredentialsApi.md#delete_postgres_credentials) | **DELETE** /api/v2/credentials/postgres/{credentials_id} | Delete PostgreSQL credentials
[**delete_redshift_credentials**](CredentialsApi.md#delete_redshift_credentials) | **DELETE** /api/v2/credentials/redshift/{credentials_id} | Delete Redshift credentials
[**delete_sap_hana_credentials**](CredentialsApi.md#delete_sap_hana_credentials) | **DELETE** /api/v2/credentials/sap-hana/{credentials_id} | Delete SAP HANA credentials
[**delete_snowflake_credentials**](CredentialsApi.md#delete_snowflake_credentials) | **DELETE** /api/v2/credentials/snowflake/{credentials_id} | Delete Snowflake credentials
[**delete_starburst_enterprise_credentials**](CredentialsApi.md#delete_starburst_enterprise_credentials) | **DELETE** /api/v2/credentials/starburst-enterprise/{credentials_id} | Delete Starburst Enterprise credentials
[**delete_starburst_galaxy_credentials**](CredentialsApi.md#delete_starburst_galaxy_credentials) | **DELETE** /api/v2/credentials/starburst-galaxy/{credentials_id} | Delete Starburst Galaxy credentials
[**delete_teradata_credentials**](CredentialsApi.md#delete_teradata_credentials) | **DELETE** /api/v2/credentials/teradata/{credentials_id} | Delete Teradata credentials
[**get_aws_secrets_manager_credentials**](CredentialsApi.md#get_aws_secrets_manager_credentials) | **GET** /api/v2/credentials/self-hosted/aws/{credentials_id} | Get AWS Secrets Manager credentials
[**get_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#get_azure_dedicated_sql_pool_credentials) | **GET** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Get Azure Dedicated SQL Pool credentials
[**get_azure_key_vault_credentials**](CredentialsApi.md#get_azure_key_vault_credentials) | **GET** /api/v2/credentials/self-hosted/azure/{credentials_id} | Get Azure Key Vault credentials
[**get_azure_sql_database_credentials**](CredentialsApi.md#get_azure_sql_database_credentials) | **GET** /api/v2/credentials/azure-sql-database/{credentials_id} | Get Azure SQL Database credentials
[**get_bigquery_credentials**](CredentialsApi.md#get_bigquery_credentials) | **GET** /api/v2/credentials/bigquery/{credentials_id} | Get BigQuery credentials
[**get_clickhouse_credentials**](CredentialsApi.md#get_clickhouse_credentials) | **GET** /api/v2/credentials/clickhouse/{credentials_id} | Get ClickHouse credentials
[**get_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_metastore_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Get Databricks metadata collection credentials
[**get_databricks_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Get Databricks query credentials
[**get_db2_credentials**](CredentialsApi.md#get_db2_credentials) | **GET** /api/v2/credentials/db2/{credentials_id} | Get Db2 credentials
[**get_env_var_credentials**](CredentialsApi.md#get_env_var_credentials) | **GET** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Get environment variable credentials
[**get_file_credentials**](CredentialsApi.md#get_file_credentials) | **GET** /api/v2/credentials/self-hosted/file/{credentials_id} | Get file credentials
[**get_gcp_secret_manager_credentials**](CredentialsApi.md#get_gcp_secret_manager_credentials) | **GET** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Get GCP Secret Manager credentials
[**get_mariadb_credentials**](CredentialsApi.md#get_mariadb_credentials) | **GET** /api/v2/credentials/mariadb/{credentials_id} | Get MariaDB credentials
[**get_mysql_credentials**](CredentialsApi.md#get_mysql_credentials) | **GET** /api/v2/credentials/mysql/{credentials_id} | Get MySQL credentials
[**get_oracle_credentials**](CredentialsApi.md#get_oracle_credentials) | **GET** /api/v2/credentials/oracle/{credentials_id} | Get Oracle credentials
[**get_postgres_credentials**](CredentialsApi.md#get_postgres_credentials) | **GET** /api/v2/credentials/postgres/{credentials_id} | Get PostgreSQL credentials
[**get_redshift_credentials**](CredentialsApi.md#get_redshift_credentials) | **GET** /api/v2/credentials/redshift/{credentials_id} | Get Redshift credentials
[**get_sap_hana_credentials**](CredentialsApi.md#get_sap_hana_credentials) | **GET** /api/v2/credentials/sap-hana/{credentials_id} | Get SAP HANA credentials
[**get_snowflake_credentials**](CredentialsApi.md#get_snowflake_credentials) | **GET** /api/v2/credentials/snowflake/{credentials_id} | Get Snowflake credentials
[**get_starburst_enterprise_credentials**](CredentialsApi.md#get_starburst_enterprise_credentials) | **GET** /api/v2/credentials/starburst-enterprise/{credentials_id} | Get Starburst Enterprise credentials
[**get_starburst_galaxy_credentials**](CredentialsApi.md#get_starburst_galaxy_credentials) | **GET** /api/v2/credentials/starburst-galaxy/{credentials_id} | Get Starburst Galaxy credentials
[**get_teradata_credentials**](CredentialsApi.md#get_teradata_credentials) | **GET** /api/v2/credentials/teradata/{credentials_id} | Get Teradata credentials
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /api/v2/credentials | List credentials
[**update_aws_secrets_manager_credentials**](CredentialsApi.md#update_aws_secrets_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/aws/{credentials_id} | Update AWS Secrets Manager credentials
[**update_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#update_azure_dedicated_sql_pool_credentials) | **PATCH** /api/v2/credentials/azure-dedicated-sql-pool/{credentials_id} | Update Azure Dedicated SQL Pool credentials
[**update_azure_key_vault_credentials**](CredentialsApi.md#update_azure_key_vault_credentials) | **PATCH** /api/v2/credentials/self-hosted/azure/{credentials_id} | Update Azure Key Vault credentials
[**update_azure_sql_database_credentials**](CredentialsApi.md#update_azure_sql_database_credentials) | **PATCH** /api/v2/credentials/azure-sql-database/{credentials_id} | Update Azure SQL Database credentials
[**update_bigquery_credentials**](CredentialsApi.md#update_bigquery_credentials) | **PATCH** /api/v2/credentials/bigquery/{credentials_id} | Update BigQuery credentials
[**update_clickhouse_credentials**](CredentialsApi.md#update_clickhouse_credentials) | **PATCH** /api/v2/credentials/clickhouse/{credentials_id} | Update ClickHouse credentials
[**update_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_metastore_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Update Databricks metadata collection credentials
[**update_databricks_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Update Databricks query credentials
[**update_db2_credentials**](CredentialsApi.md#update_db2_credentials) | **PATCH** /api/v2/credentials/db2/{credentials_id} | Update Db2 credentials
[**update_env_var_credentials**](CredentialsApi.md#update_env_var_credentials) | **PATCH** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Update environment variable credentials
[**update_file_credentials**](CredentialsApi.md#update_file_credentials) | **PATCH** /api/v2/credentials/self-hosted/file/{credentials_id} | Update file credentials
[**update_gcp_secret_manager_credentials**](CredentialsApi.md#update_gcp_secret_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Update GCP Secret Manager credentials
[**update_mariadb_credentials**](CredentialsApi.md#update_mariadb_credentials) | **PATCH** /api/v2/credentials/mariadb/{credentials_id} | Update MariaDB credentials
[**update_mysql_credentials**](CredentialsApi.md#update_mysql_credentials) | **PATCH** /api/v2/credentials/mysql/{credentials_id} | Update MySQL credentials
[**update_oracle_credentials**](CredentialsApi.md#update_oracle_credentials) | **PATCH** /api/v2/credentials/oracle/{credentials_id} | Update Oracle credentials
[**update_postgres_credentials**](CredentialsApi.md#update_postgres_credentials) | **PATCH** /api/v2/credentials/postgres/{credentials_id} | Update PostgreSQL credentials
[**update_redshift_credentials**](CredentialsApi.md#update_redshift_credentials) | **PATCH** /api/v2/credentials/redshift/{credentials_id} | Update Redshift credentials
[**update_sap_hana_credentials**](CredentialsApi.md#update_sap_hana_credentials) | **PATCH** /api/v2/credentials/sap-hana/{credentials_id} | Update SAP HANA credentials
[**update_snowflake_credentials**](CredentialsApi.md#update_snowflake_credentials) | **PATCH** /api/v2/credentials/snowflake/{credentials_id} | Update Snowflake credentials
[**update_starburst_enterprise_credentials**](CredentialsApi.md#update_starburst_enterprise_credentials) | **PATCH** /api/v2/credentials/starburst-enterprise/{credentials_id} | Update Starburst Enterprise credentials
[**update_starburst_galaxy_credentials**](CredentialsApi.md#update_starburst_galaxy_credentials) | **PATCH** /api/v2/credentials/starburst-galaxy/{credentials_id} | Update Starburst Galaxy credentials
[**update_teradata_credentials**](CredentialsApi.md#update_teradata_credentials) | **PATCH** /api/v2/credentials/teradata/{credentials_id} | Update Teradata credentials
[**validate_aws_secrets_manager_credentials**](CredentialsApi.md#validate_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws/validate | Validate AWS Secrets Manager credentials
[**validate_azure_dedicated_sql_pool_credentials**](CredentialsApi.md#validate_azure_dedicated_sql_pool_credentials) | **POST** /api/v2/credentials/azure-dedicated-sql-pool/validate | Validate Azure Dedicated SQL Pool credentials
[**validate_azure_key_vault_credentials**](CredentialsApi.md#validate_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure/validate | Validate Azure Key Vault credentials
[**validate_azure_sql_database_credentials**](CredentialsApi.md#validate_azure_sql_database_credentials) | **POST** /api/v2/credentials/azure-sql-database/validate | Validate Azure SQL Database credentials
[**validate_bigquery_credentials**](CredentialsApi.md#validate_bigquery_credentials) | **POST** /api/v2/credentials/bigquery/validate | Validate BigQuery credentials
[**validate_clickhouse_credentials**](CredentialsApi.md#validate_clickhouse_credentials) | **POST** /api/v2/credentials/clickhouse/validate | Validate ClickHouse credentials
[**validate_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse/validate | Validate Databricks metadata collection credentials
[**validate_databricks_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse/validate | Validate Databricks query credentials
[**validate_db2_credentials**](CredentialsApi.md#validate_db2_credentials) | **POST** /api/v2/credentials/db2/validate | Validate Db2 credentials
[**validate_env_var_credentials**](CredentialsApi.md#validate_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var/validate | Validate environment variable credentials
[**validate_file_credentials**](CredentialsApi.md#validate_file_credentials) | **POST** /api/v2/credentials/self-hosted/file/validate | Validate file credentials
[**validate_gcp_secret_manager_credentials**](CredentialsApi.md#validate_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp/validate | Validate GCP Secret Manager credentials
[**validate_mariadb_credentials**](CredentialsApi.md#validate_mariadb_credentials) | **POST** /api/v2/credentials/mariadb/validate | Validate MariaDB credentials
[**validate_mysql_credentials**](CredentialsApi.md#validate_mysql_credentials) | **POST** /api/v2/credentials/mysql/validate | Validate MySQL credentials
[**validate_oracle_credentials**](CredentialsApi.md#validate_oracle_credentials) | **POST** /api/v2/credentials/oracle/validate | Validate Oracle credentials
[**validate_postgres_credentials**](CredentialsApi.md#validate_postgres_credentials) | **POST** /api/v2/credentials/postgres/validate | Validate PostgreSQL credentials
[**validate_redshift_credentials**](CredentialsApi.md#validate_redshift_credentials) | **POST** /api/v2/credentials/redshift/validate | Validate Redshift credentials
[**validate_sap_hana_credentials**](CredentialsApi.md#validate_sap_hana_credentials) | **POST** /api/v2/credentials/sap-hana/validate | Validate SAP HANA credentials
[**validate_snowflake_credentials**](CredentialsApi.md#validate_snowflake_credentials) | **POST** /api/v2/credentials/snowflake/validate | Validate Snowflake credentials
[**validate_starburst_enterprise_credentials**](CredentialsApi.md#validate_starburst_enterprise_credentials) | **POST** /api/v2/credentials/starburst-enterprise/validate | Validate Starburst Enterprise credentials
[**validate_starburst_galaxy_credentials**](CredentialsApi.md#validate_starburst_galaxy_credentials) | **POST** /api/v2/credentials/starburst-galaxy/validate | Validate Starburst Galaxy credentials
[**validate_teradata_credentials**](CredentialsApi.md#validate_teradata_credentials) | **POST** /api/v2/credentials/teradata/validate | Validate Teradata credentials


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
import montecarlo
from montecarlo.models.aws_secrets_manager_credentials_in import AwsSecretsManagerCredentialsIn
from montecarlo.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    aws_secrets_manager_credentials_in = montecarlo.AwsSecretsManagerCredentialsIn() # AwsSecretsManagerCredentialsIn | 

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
import montecarlo
from montecarlo.models.azure_dedicated_sql_pool_credentials_in import AzureDedicatedSqlPoolCredentialsIn
from montecarlo.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_dedicated_sql_pool_credentials_in = montecarlo.AzureDedicatedSqlPoolCredentialsIn() # AzureDedicatedSqlPoolCredentialsIn | 

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
import montecarlo
from montecarlo.models.azure_key_vault_credentials_in import AzureKeyVaultCredentialsIn
from montecarlo.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_key_vault_credentials_in = montecarlo.AzureKeyVaultCredentialsIn() # AzureKeyVaultCredentialsIn | 

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
import montecarlo
from montecarlo.models.azure_sql_database_credentials_in import AzureSqlDatabaseCredentialsIn
from montecarlo.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_sql_database_credentials_in = montecarlo.AzureSqlDatabaseCredentialsIn() # AzureSqlDatabaseCredentialsIn | 

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
import montecarlo
from montecarlo.models.big_query_credentials_in import BigQueryCredentialsIn
from montecarlo.models.big_query_credentials_out import BigQueryCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    big_query_credentials_in = montecarlo.BigQueryCredentialsIn() # BigQueryCredentialsIn | 

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
import montecarlo
from montecarlo.models.click_house_credentials_in import ClickHouseCredentialsIn
from montecarlo.models.click_house_credentials_out import ClickHouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    click_house_credentials_in = montecarlo.ClickHouseCredentialsIn() # ClickHouseCredentialsIn | 

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
import montecarlo
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_in import DatabricksMetastoreSqlWarehouseCredentialsIn
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    databricks_metastore_sql_warehouse_credentials_in = montecarlo.DatabricksMetastoreSqlWarehouseCredentialsIn() # DatabricksMetastoreSqlWarehouseCredentialsIn | 

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
import montecarlo
from montecarlo.models.databricks_sql_warehouse_credentials_in import DatabricksSqlWarehouseCredentialsIn
from montecarlo.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    databricks_sql_warehouse_credentials_in = montecarlo.DatabricksSqlWarehouseCredentialsIn() # DatabricksSqlWarehouseCredentialsIn | 

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
import montecarlo
from montecarlo.models.db2_credentials_in import Db2CredentialsIn
from montecarlo.models.db2_credentials_out import Db2CredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    db2_credentials_in = montecarlo.Db2CredentialsIn() # Db2CredentialsIn | 

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
import montecarlo
from montecarlo.models.env_var_credentials_in import EnvVarCredentialsIn
from montecarlo.models.env_var_credentials_out import EnvVarCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    env_var_credentials_in = montecarlo.EnvVarCredentialsIn() # EnvVarCredentialsIn | 

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
import montecarlo
from montecarlo.models.file_credentials_in import FileCredentialsIn
from montecarlo.models.file_credentials_out import FileCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    file_credentials_in = montecarlo.FileCredentialsIn() # FileCredentialsIn | 

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
import montecarlo
from montecarlo.models.gcp_secret_manager_credentials_in import GcpSecretManagerCredentialsIn
from montecarlo.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    gcp_secret_manager_credentials_in = montecarlo.GcpSecretManagerCredentialsIn() # GcpSecretManagerCredentialsIn | 

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
import montecarlo
from montecarlo.models.maria_db_credentials_in import MariaDbCredentialsIn
from montecarlo.models.maria_db_credentials_out import MariaDbCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    maria_db_credentials_in = montecarlo.MariaDbCredentialsIn() # MariaDbCredentialsIn | 

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
import montecarlo
from montecarlo.models.my_sql_credentials_in import MySqlCredentialsIn
from montecarlo.models.my_sql_credentials_out import MySqlCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    my_sql_credentials_in = montecarlo.MySqlCredentialsIn() # MySqlCredentialsIn | 

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
import montecarlo
from montecarlo.models.oracle_credentials_in import OracleCredentialsIn
from montecarlo.models.oracle_credentials_out import OracleCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    oracle_credentials_in = montecarlo.OracleCredentialsIn() # OracleCredentialsIn | 

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
import montecarlo
from montecarlo.models.postgres_credentials_in import PostgresCredentialsIn
from montecarlo.models.postgres_credentials_out import PostgresCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    postgres_credentials_in = montecarlo.PostgresCredentialsIn() # PostgresCredentialsIn | 

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
import montecarlo
from montecarlo.models.redshift_credentials_in import RedshiftCredentialsIn
from montecarlo.models.redshift_credentials_out import RedshiftCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    redshift_credentials_in = montecarlo.RedshiftCredentialsIn() # RedshiftCredentialsIn | 

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
import montecarlo
from montecarlo.models.sap_hana_credentials_in import SapHanaCredentialsIn
from montecarlo.models.sap_hana_credentials_out import SapHanaCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    sap_hana_credentials_in = montecarlo.SapHanaCredentialsIn() # SapHanaCredentialsIn | 

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
import montecarlo
from montecarlo.models.snowflake_credentials_in import SnowflakeCredentialsIn
from montecarlo.models.snowflake_credentials_out import SnowflakeCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    snowflake_credentials_in = montecarlo.SnowflakeCredentialsIn() # SnowflakeCredentialsIn | 

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
import montecarlo
from montecarlo.models.starburst_enterprise_credentials_in import StarburstEnterpriseCredentialsIn
from montecarlo.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    starburst_enterprise_credentials_in = montecarlo.StarburstEnterpriseCredentialsIn() # StarburstEnterpriseCredentialsIn | 

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
import montecarlo
from montecarlo.models.starburst_galaxy_credentials_in import StarburstGalaxyCredentialsIn
from montecarlo.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    starburst_galaxy_credentials_in = montecarlo.StarburstGalaxyCredentialsIn() # StarburstGalaxyCredentialsIn | 

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
import montecarlo
from montecarlo.models.teradata_credentials_in import TeradataCredentialsIn
from montecarlo.models.teradata_credentials_out import TeradataCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    teradata_credentials_in = montecarlo.TeradataCredentialsIn() # TeradataCredentialsIn | 

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

# **delete_aws_secrets_manager_credentials**
> delete_aws_secrets_manager_credentials(credentials_id)

Delete AWS Secrets Manager credentials

Delete AWS Secrets Manager credentials.

Refused while a connection still uses them. Delete the connection first. The secret in AWS
is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete AWS Secrets Manager credentials
        api_instance.delete_aws_secrets_manager_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_aws_secrets_manager_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Azure Dedicated SQL Pool credentials
        api_instance.delete_azure_dedicated_sql_pool_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_dedicated_sql_pool_credentials: %s\n" % e)
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

# **delete_azure_key_vault_credentials**
> delete_azure_key_vault_credentials(credentials_id)

Delete Azure Key Vault credentials

Delete Azure Key Vault credentials.

Refused while a connection still uses them. Delete the connection first. The secret in Azure
is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Azure Key Vault credentials
        api_instance.delete_azure_key_vault_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_key_vault_credentials: %s\n" % e)
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

# **delete_azure_sql_database_credentials**
> delete_azure_sql_database_credentials(credentials_id)

Delete Azure SQL Database credentials

Delete Azure SQL Database credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Azure SQL Database if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Azure SQL Database credentials
        api_instance.delete_azure_sql_database_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_azure_sql_database_credentials: %s\n" % e)
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

# **delete_bigquery_credentials**
> delete_bigquery_credentials(credentials_id)

Delete BigQuery credentials

Delete BigQuery credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops
using the stored key. Revoke the key in Google Cloud if the key itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete BigQuery credentials
        api_instance.delete_bigquery_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_bigquery_credentials: %s\n" % e)
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

# **delete_clickhouse_credentials**
> delete_clickhouse_credentials(credentials_id)

Delete ClickHouse credentials

Delete ClickHouse credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in ClickHouse if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete ClickHouse credentials
        api_instance.delete_clickhouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_clickhouse_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete credentials
        api_instance.delete_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Databricks metadata collection credentials
        api_instance.delete_databricks_metastore_sql_warehouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_databricks_metastore_sql_warehouse_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Databricks query credentials
        api_instance.delete_databricks_sql_warehouse_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_databricks_sql_warehouse_credentials: %s\n" % e)
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

# **delete_db2_credentials**
> delete_db2_credentials(credentials_id)

Delete Db2 credentials

Delete Db2 credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Db2 if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Db2 credentials
        api_instance.delete_db2_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_db2_credentials: %s\n" % e)
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

# **delete_env_var_credentials**
> delete_env_var_credentials(credentials_id)

Delete environment variable credentials

Delete environment variable credentials.

Refused while a connection still uses them. Delete the connection first. The variable on the
deployment is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete environment variable credentials
        api_instance.delete_env_var_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_env_var_credentials: %s\n" % e)
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

# **delete_file_credentials**
> delete_file_credentials(credentials_id)

Delete file credentials

Delete file credentials.

Refused while a connection still uses them. Delete the connection first. The file on the
deployment is untouched.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete file credentials
        api_instance.delete_file_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_file_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete GCP Secret Manager credentials
        api_instance.delete_gcp_secret_manager_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_gcp_secret_manager_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete MariaDB credentials
        api_instance.delete_mariadb_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_mariadb_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete MySQL credentials
        api_instance.delete_mysql_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_mysql_credentials: %s\n" % e)
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

# **delete_oracle_credentials**
> delete_oracle_credentials(credentials_id)

Delete Oracle credentials

Delete Oracle credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Oracle if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Oracle credentials
        api_instance.delete_oracle_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_oracle_credentials: %s\n" % e)
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

# **delete_postgres_credentials**
> delete_postgres_credentials(credentials_id)

Delete PostgreSQL credentials

Delete PostgreSQL credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in PostgreSQL if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete PostgreSQL credentials
        api_instance.delete_postgres_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_postgres_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Redshift credentials
        api_instance.delete_redshift_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_redshift_credentials: %s\n" % e)
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

# **delete_sap_hana_credentials**
> delete_sap_hana_credentials(credentials_id)

Delete SAP HANA credentials

Delete SAP HANA credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in SAP HANA if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete SAP HANA credentials
        api_instance.delete_sap_hana_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_sap_hana_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Snowflake credentials
        api_instance.delete_snowflake_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_snowflake_credentials: %s\n" % e)
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

# **delete_starburst_enterprise_credentials**
> delete_starburst_enterprise_credentials(credentials_id)

Delete Starburst Enterprise credentials

Delete Starburst Enterprise credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Starburst Enterprise if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Starburst Enterprise credentials
        api_instance.delete_starburst_enterprise_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_starburst_enterprise_credentials: %s\n" % e)
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

# **delete_starburst_galaxy_credentials**
> delete_starburst_galaxy_credentials(credentials_id)

Delete Starburst Galaxy credentials

Delete Starburst Galaxy credentials.

Refused while a connection still uses them. Delete the connection first. Monte Carlo stops using
the stored password. Change it in Starburst Galaxy if the password itself must be retired.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Starburst Galaxy credentials
        api_instance.delete_starburst_galaxy_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_starburst_galaxy_credentials: %s\n" % e)
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
import montecarlo
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete Teradata credentials
        api_instance.delete_teradata_credentials(credentials_id)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_teradata_credentials: %s\n" % e)
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

# **get_aws_secrets_manager_credentials**
> AwsSecretsManagerCredentialsOut get_aws_secrets_manager_credentials(credentials_id)

Get AWS Secrets Manager credentials

Get one set of AWS Secrets Manager credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_azure_dedicated_sql_pool_credentials**
> AzureDedicatedSqlPoolCredentialsOut get_azure_dedicated_sql_pool_credentials(credentials_id)

Get Azure Dedicated SQL Pool credentials

Get one set of Azure Dedicated SQL Pool credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.big_query_credentials_out import BigQueryCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.click_house_credentials_out import ClickHouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.db2_credentials_out import Db2CredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_env_var_credentials**
> EnvVarCredentialsOut get_env_var_credentials(credentials_id)

Get environment variable credentials

Get one set of environment variable credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.env_var_credentials_out import EnvVarCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.file_credentials_out import FileCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_gcp_secret_manager_credentials**
> GcpSecretManagerCredentialsOut get_gcp_secret_manager_credentials(credentials_id)

Get GCP Secret Manager credentials

Get one set of GCP Secret Manager credentials.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_mariadb_credentials**
> MariaDbCredentialsOut get_mariadb_credentials(credentials_id)

Get MariaDB credentials

Get one set of MariaDB credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.maria_db_credentials_out import MariaDbCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_mysql_credentials**
> MySqlCredentialsOut get_mysql_credentials(credentials_id)

Get MySQL credentials

Get one set of MySQL credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.my_sql_credentials_out import MySqlCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.oracle_credentials_out import OracleCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.postgres_credentials_out import PostgresCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_redshift_credentials**
> RedshiftCredentialsOut get_redshift_credentials(credentials_id)

Get Redshift credentials

Get one set of Redshift credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.redshift_credentials_out import RedshiftCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_sap_hana_credentials**
> SapHanaCredentialsOut get_sap_hana_credentials(credentials_id)

Get SAP HANA credentials

Get one set of SAP HANA credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.sap_hana_credentials_out import SapHanaCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.snowflake_credentials_out import SnowflakeCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_starburst_enterprise_credentials**
> StarburstEnterpriseCredentialsOut get_starburst_enterprise_credentials(credentials_id)

Get Starburst Enterprise credentials

Get one set of Starburst Enterprise credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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

# **get_teradata_credentials**
> TeradataCredentialsOut get_teradata_credentials(credentials_id)

Get Teradata credentials

Get one set of Teradata credentials, without the password.

An id that does not exist, belongs to another account, or names credentials of another
kind returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.teradata_credentials_out import TeradataCredentialsOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

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
 **credentials_id** | **UUID**|  | 

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
import montecarlo
from montecarlo.models.paged_credentials_summary_out import PagedCredentialsSummaryOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
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
import montecarlo
from montecarlo.models.aws_secrets_manager_credentials_out import AwsSecretsManagerCredentialsOut
from montecarlo.models.aws_secrets_manager_credentials_patch import AwsSecretsManagerCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    aws_secrets_manager_credentials_patch = montecarlo.AwsSecretsManagerCredentialsPatch() # AwsSecretsManagerCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.azure_dedicated_sql_pool_credentials_out import AzureDedicatedSqlPoolCredentialsOut
from montecarlo.models.azure_dedicated_sql_pool_credentials_patch import AzureDedicatedSqlPoolCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_dedicated_sql_pool_credentials_patch = montecarlo.AzureDedicatedSqlPoolCredentialsPatch() # AzureDedicatedSqlPoolCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.azure_key_vault_credentials_out import AzureKeyVaultCredentialsOut
from montecarlo.models.azure_key_vault_credentials_patch import AzureKeyVaultCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_key_vault_credentials_patch = montecarlo.AzureKeyVaultCredentialsPatch() # AzureKeyVaultCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.azure_sql_database_credentials_out import AzureSqlDatabaseCredentialsOut
from montecarlo.models.azure_sql_database_credentials_patch import AzureSqlDatabaseCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_sql_database_credentials_patch = montecarlo.AzureSqlDatabaseCredentialsPatch() # AzureSqlDatabaseCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.big_query_credentials_out import BigQueryCredentialsOut
from montecarlo.models.big_query_credentials_patch import BigQueryCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    big_query_credentials_patch = montecarlo.BigQueryCredentialsPatch() # BigQueryCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.click_house_credentials_out import ClickHouseCredentialsOut
from montecarlo.models.click_house_credentials_patch import ClickHouseCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    click_house_credentials_patch = montecarlo.ClickHouseCredentialsPatch() # ClickHouseCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_out import DatabricksMetastoreSqlWarehouseCredentialsOut
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_patch import DatabricksMetastoreSqlWarehouseCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    databricks_metastore_sql_warehouse_credentials_patch = montecarlo.DatabricksMetastoreSqlWarehouseCredentialsPatch() # DatabricksMetastoreSqlWarehouseCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.databricks_sql_warehouse_credentials_out import DatabricksSqlWarehouseCredentialsOut
from montecarlo.models.databricks_sql_warehouse_credentials_patch import DatabricksSqlWarehouseCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    databricks_sql_warehouse_credentials_patch = montecarlo.DatabricksSqlWarehouseCredentialsPatch() # DatabricksSqlWarehouseCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.db2_credentials_out import Db2CredentialsOut
from montecarlo.models.db2_credentials_patch import Db2CredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    db2_credentials_patch = montecarlo.Db2CredentialsPatch() # Db2CredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.env_var_credentials_out import EnvVarCredentialsOut
from montecarlo.models.env_var_credentials_patch import EnvVarCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    env_var_credentials_patch = montecarlo.EnvVarCredentialsPatch() # EnvVarCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.file_credentials_out import FileCredentialsOut
from montecarlo.models.file_credentials_patch import FileCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    file_credentials_patch = montecarlo.FileCredentialsPatch() # FileCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.gcp_secret_manager_credentials_out import GcpSecretManagerCredentialsOut
from montecarlo.models.gcp_secret_manager_credentials_patch import GcpSecretManagerCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    gcp_secret_manager_credentials_patch = montecarlo.GcpSecretManagerCredentialsPatch() # GcpSecretManagerCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.maria_db_credentials_out import MariaDbCredentialsOut
from montecarlo.models.maria_db_credentials_patch import MariaDbCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    maria_db_credentials_patch = montecarlo.MariaDbCredentialsPatch() # MariaDbCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.my_sql_credentials_out import MySqlCredentialsOut
from montecarlo.models.my_sql_credentials_patch import MySqlCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    my_sql_credentials_patch = montecarlo.MySqlCredentialsPatch() # MySqlCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.oracle_credentials_out import OracleCredentialsOut
from montecarlo.models.oracle_credentials_patch import OracleCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    oracle_credentials_patch = montecarlo.OracleCredentialsPatch() # OracleCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.postgres_credentials_out import PostgresCredentialsOut
from montecarlo.models.postgres_credentials_patch import PostgresCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    postgres_credentials_patch = montecarlo.PostgresCredentialsPatch() # PostgresCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.redshift_credentials_out import RedshiftCredentialsOut
from montecarlo.models.redshift_credentials_patch import RedshiftCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    redshift_credentials_patch = montecarlo.RedshiftCredentialsPatch() # RedshiftCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.sap_hana_credentials_out import SapHanaCredentialsOut
from montecarlo.models.sap_hana_credentials_patch import SapHanaCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    sap_hana_credentials_patch = montecarlo.SapHanaCredentialsPatch() # SapHanaCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.snowflake_credentials_out import SnowflakeCredentialsOut
from montecarlo.models.snowflake_credentials_patch import SnowflakeCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    snowflake_credentials_patch = montecarlo.SnowflakeCredentialsPatch() # SnowflakeCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.starburst_enterprise_credentials_out import StarburstEnterpriseCredentialsOut
from montecarlo.models.starburst_enterprise_credentials_patch import StarburstEnterpriseCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    starburst_enterprise_credentials_patch = montecarlo.StarburstEnterpriseCredentialsPatch() # StarburstEnterpriseCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.starburst_galaxy_credentials_out import StarburstGalaxyCredentialsOut
from montecarlo.models.starburst_galaxy_credentials_patch import StarburstGalaxyCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    starburst_galaxy_credentials_patch = montecarlo.StarburstGalaxyCredentialsPatch() # StarburstGalaxyCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.teradata_credentials_out import TeradataCredentialsOut
from montecarlo.models.teradata_credentials_patch import TeradataCredentialsPatch
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    credentials_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    teradata_credentials_patch = montecarlo.TeradataCredentialsPatch() # TeradataCredentialsPatch | 

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
 **credentials_id** | **UUID**|  | 
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
import montecarlo
from montecarlo.models.aws_secrets_manager_credentials_validate_in import AwsSecretsManagerCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    aws_secrets_manager_credentials_validate_in = montecarlo.AwsSecretsManagerCredentialsValidateIn() # AwsSecretsManagerCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.azure_dedicated_sql_pool_credentials_validate_in import AzureDedicatedSqlPoolCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_dedicated_sql_pool_credentials_validate_in = montecarlo.AzureDedicatedSqlPoolCredentialsValidateIn() # AzureDedicatedSqlPoolCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.azure_key_vault_credentials_validate_in import AzureKeyVaultCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_key_vault_credentials_validate_in = montecarlo.AzureKeyVaultCredentialsValidateIn() # AzureKeyVaultCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.azure_sql_database_credentials_validate_in import AzureSqlDatabaseCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    azure_sql_database_credentials_validate_in = montecarlo.AzureSqlDatabaseCredentialsValidateIn() # AzureSqlDatabaseCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.big_query_credentials_validate_in import BigQueryCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    big_query_credentials_validate_in = montecarlo.BigQueryCredentialsValidateIn() # BigQueryCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.click_house_credentials_validate_in import ClickHouseCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    click_house_credentials_validate_in = montecarlo.ClickHouseCredentialsValidateIn() # ClickHouseCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.databricks_metastore_sql_warehouse_credentials_validate_in import DatabricksMetastoreSqlWarehouseCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    databricks_metastore_sql_warehouse_credentials_validate_in = montecarlo.DatabricksMetastoreSqlWarehouseCredentialsValidateIn() # DatabricksMetastoreSqlWarehouseCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.databricks_sql_warehouse_credentials_validate_in import DatabricksSqlWarehouseCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    databricks_sql_warehouse_credentials_validate_in = montecarlo.DatabricksSqlWarehouseCredentialsValidateIn() # DatabricksSqlWarehouseCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.db2_credentials_validate_in import Db2CredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    db2_credentials_validate_in = montecarlo.Db2CredentialsValidateIn() # Db2CredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.env_var_credentials_validate_in import EnvVarCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    env_var_credentials_validate_in = montecarlo.EnvVarCredentialsValidateIn() # EnvVarCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.file_credentials_validate_in import FileCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    file_credentials_validate_in = montecarlo.FileCredentialsValidateIn() # FileCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.gcp_secret_manager_credentials_validate_in import GcpSecretManagerCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    gcp_secret_manager_credentials_validate_in = montecarlo.GcpSecretManagerCredentialsValidateIn() # GcpSecretManagerCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.maria_db_credentials_validate_in import MariaDbCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    maria_db_credentials_validate_in = montecarlo.MariaDbCredentialsValidateIn() # MariaDbCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.my_sql_credentials_validate_in import MySqlCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    my_sql_credentials_validate_in = montecarlo.MySqlCredentialsValidateIn() # MySqlCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.oracle_credentials_validate_in import OracleCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    oracle_credentials_validate_in = montecarlo.OracleCredentialsValidateIn() # OracleCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.postgres_credentials_validate_in import PostgresCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    postgres_credentials_validate_in = montecarlo.PostgresCredentialsValidateIn() # PostgresCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.redshift_credentials_validate_in import RedshiftCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    redshift_credentials_validate_in = montecarlo.RedshiftCredentialsValidateIn() # RedshiftCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.sap_hana_credentials_validate_in import SapHanaCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    sap_hana_credentials_validate_in = montecarlo.SapHanaCredentialsValidateIn() # SapHanaCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.snowflake_credentials_validate_in import SnowflakeCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    snowflake_credentials_validate_in = montecarlo.SnowflakeCredentialsValidateIn() # SnowflakeCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.starburst_enterprise_credentials_validate_in import StarburstEnterpriseCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    starburst_enterprise_credentials_validate_in = montecarlo.StarburstEnterpriseCredentialsValidateIn() # StarburstEnterpriseCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.starburst_galaxy_credentials_validate_in import StarburstGalaxyCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    starburst_galaxy_credentials_validate_in = montecarlo.StarburstGalaxyCredentialsValidateIn() # StarburstGalaxyCredentialsValidateIn | 

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
import montecarlo
from montecarlo.models.teradata_credentials_validate_in import TeradataCredentialsValidateIn
from montecarlo.models.validation_run_out import ValidationRunOut
from montecarlo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = montecarlo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: GatewayAuth
configuration = montecarlo.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with montecarlo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = montecarlo.CredentialsApi(api_client)
    teradata_credentials_validate_in = montecarlo.TeradataCredentialsValidateIn() # TeradataCredentialsValidateIn | 

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

