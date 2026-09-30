# montecarlo.CredentialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_secrets_manager_credentials**](CredentialsApi.md#create_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws | Create AWS Secrets Manager credentials
[**create_azure_key_vault_credentials**](CredentialsApi.md#create_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure | Create Azure Key Vault credentials
[**create_bigquery_credentials**](CredentialsApi.md#create_bigquery_credentials) | **POST** /api/v2/credentials/bigquery | Create BigQuery credentials
[**create_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse | Create Databricks metadata collection credentials
[**create_databricks_sql_warehouse_credentials**](CredentialsApi.md#create_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse | Create Databricks query credentials
[**create_env_var_credentials**](CredentialsApi.md#create_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var | Create environment variable credentials
[**create_file_credentials**](CredentialsApi.md#create_file_credentials) | **POST** /api/v2/credentials/self-hosted/file | Create file credentials
[**create_gcp_secret_manager_credentials**](CredentialsApi.md#create_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp | Create GCP Secret Manager credentials
[**create_redshift_credentials**](CredentialsApi.md#create_redshift_credentials) | **POST** /api/v2/credentials/redshift | Create Redshift credentials
[**create_snowflake_credentials**](CredentialsApi.md#create_snowflake_credentials) | **POST** /api/v2/credentials/snowflake | Create Snowflake credentials
[**delete_aws_secrets_manager_credentials**](CredentialsApi.md#delete_aws_secrets_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/aws/{credentials_id} | Delete AWS Secrets Manager credentials
[**delete_azure_key_vault_credentials**](CredentialsApi.md#delete_azure_key_vault_credentials) | **DELETE** /api/v2/credentials/self-hosted/azure/{credentials_id} | Delete Azure Key Vault credentials
[**delete_bigquery_credentials**](CredentialsApi.md#delete_bigquery_credentials) | **DELETE** /api/v2/credentials/bigquery/{credentials_id} | Delete BigQuery credentials
[**delete_credentials**](CredentialsApi.md#delete_credentials) | **DELETE** /api/v2/credentials/{credentials_id} | Delete credentials
[**delete_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_metastore_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Delete Databricks metadata collection credentials
[**delete_databricks_sql_warehouse_credentials**](CredentialsApi.md#delete_databricks_sql_warehouse_credentials) | **DELETE** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Delete Databricks query credentials
[**delete_env_var_credentials**](CredentialsApi.md#delete_env_var_credentials) | **DELETE** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Delete environment variable credentials
[**delete_file_credentials**](CredentialsApi.md#delete_file_credentials) | **DELETE** /api/v2/credentials/self-hosted/file/{credentials_id} | Delete file credentials
[**delete_gcp_secret_manager_credentials**](CredentialsApi.md#delete_gcp_secret_manager_credentials) | **DELETE** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Delete GCP Secret Manager credentials
[**delete_redshift_credentials**](CredentialsApi.md#delete_redshift_credentials) | **DELETE** /api/v2/credentials/redshift/{credentials_id} | Delete Redshift credentials
[**delete_snowflake_credentials**](CredentialsApi.md#delete_snowflake_credentials) | **DELETE** /api/v2/credentials/snowflake/{credentials_id} | Delete Snowflake credentials
[**get_aws_secrets_manager_credentials**](CredentialsApi.md#get_aws_secrets_manager_credentials) | **GET** /api/v2/credentials/self-hosted/aws/{credentials_id} | Get AWS Secrets Manager credentials
[**get_azure_key_vault_credentials**](CredentialsApi.md#get_azure_key_vault_credentials) | **GET** /api/v2/credentials/self-hosted/azure/{credentials_id} | Get Azure Key Vault credentials
[**get_bigquery_credentials**](CredentialsApi.md#get_bigquery_credentials) | **GET** /api/v2/credentials/bigquery/{credentials_id} | Get BigQuery credentials
[**get_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_metastore_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Get Databricks metadata collection credentials
[**get_databricks_sql_warehouse_credentials**](CredentialsApi.md#get_databricks_sql_warehouse_credentials) | **GET** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Get Databricks query credentials
[**get_env_var_credentials**](CredentialsApi.md#get_env_var_credentials) | **GET** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Get environment variable credentials
[**get_file_credentials**](CredentialsApi.md#get_file_credentials) | **GET** /api/v2/credentials/self-hosted/file/{credentials_id} | Get file credentials
[**get_gcp_secret_manager_credentials**](CredentialsApi.md#get_gcp_secret_manager_credentials) | **GET** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Get GCP Secret Manager credentials
[**get_redshift_credentials**](CredentialsApi.md#get_redshift_credentials) | **GET** /api/v2/credentials/redshift/{credentials_id} | Get Redshift credentials
[**get_snowflake_credentials**](CredentialsApi.md#get_snowflake_credentials) | **GET** /api/v2/credentials/snowflake/{credentials_id} | Get Snowflake credentials
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /api/v2/credentials | List credentials
[**update_aws_secrets_manager_credentials**](CredentialsApi.md#update_aws_secrets_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/aws/{credentials_id} | Update AWS Secrets Manager credentials
[**update_azure_key_vault_credentials**](CredentialsApi.md#update_azure_key_vault_credentials) | **PATCH** /api/v2/credentials/self-hosted/azure/{credentials_id} | Update Azure Key Vault credentials
[**update_bigquery_credentials**](CredentialsApi.md#update_bigquery_credentials) | **PATCH** /api/v2/credentials/bigquery/{credentials_id} | Update BigQuery credentials
[**update_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_metastore_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-metastore-sql-warehouse/{credentials_id} | Update Databricks metadata collection credentials
[**update_databricks_sql_warehouse_credentials**](CredentialsApi.md#update_databricks_sql_warehouse_credentials) | **PATCH** /api/v2/credentials/databricks-sql-warehouse/{credentials_id} | Update Databricks query credentials
[**update_env_var_credentials**](CredentialsApi.md#update_env_var_credentials) | **PATCH** /api/v2/credentials/self-hosted/env-var/{credentials_id} | Update environment variable credentials
[**update_file_credentials**](CredentialsApi.md#update_file_credentials) | **PATCH** /api/v2/credentials/self-hosted/file/{credentials_id} | Update file credentials
[**update_gcp_secret_manager_credentials**](CredentialsApi.md#update_gcp_secret_manager_credentials) | **PATCH** /api/v2/credentials/self-hosted/gcp/{credentials_id} | Update GCP Secret Manager credentials
[**update_redshift_credentials**](CredentialsApi.md#update_redshift_credentials) | **PATCH** /api/v2/credentials/redshift/{credentials_id} | Update Redshift credentials
[**update_snowflake_credentials**](CredentialsApi.md#update_snowflake_credentials) | **PATCH** /api/v2/credentials/snowflake/{credentials_id} | Update Snowflake credentials
[**validate_aws_secrets_manager_credentials**](CredentialsApi.md#validate_aws_secrets_manager_credentials) | **POST** /api/v2/credentials/self-hosted/aws/validate | Validate AWS Secrets Manager credentials
[**validate_azure_key_vault_credentials**](CredentialsApi.md#validate_azure_key_vault_credentials) | **POST** /api/v2/credentials/self-hosted/azure/validate | Validate Azure Key Vault credentials
[**validate_bigquery_credentials**](CredentialsApi.md#validate_bigquery_credentials) | **POST** /api/v2/credentials/bigquery/validate | Validate BigQuery credentials
[**validate_databricks_metastore_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_metastore_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-metastore-sql-warehouse/validate | Validate Databricks metadata collection credentials
[**validate_databricks_sql_warehouse_credentials**](CredentialsApi.md#validate_databricks_sql_warehouse_credentials) | **POST** /api/v2/credentials/databricks-sql-warehouse/validate | Validate Databricks query credentials
[**validate_env_var_credentials**](CredentialsApi.md#validate_env_var_credentials) | **POST** /api/v2/credentials/self-hosted/env-var/validate | Validate environment variable credentials
[**validate_file_credentials**](CredentialsApi.md#validate_file_credentials) | **POST** /api/v2/credentials/self-hosted/file/validate | Validate file credentials
[**validate_gcp_secret_manager_credentials**](CredentialsApi.md#validate_gcp_secret_manager_credentials) | **POST** /api/v2/credentials/self-hosted/gcp/validate | Validate GCP Secret Manager credentials
[**validate_redshift_credentials**](CredentialsApi.md#validate_redshift_credentials) | **POST** /api/v2/credentials/redshift/validate | Validate Redshift credentials
[**validate_snowflake_credentials**](CredentialsApi.md#validate_snowflake_credentials) | **POST** /api/v2/credentials/snowflake/validate | Validate Snowflake credentials


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

