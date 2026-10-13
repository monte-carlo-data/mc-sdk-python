# pycarlo2.IntegrationKeysApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_airflow_callbacks_key**](IntegrationKeysApi.md#create_airflow_callbacks_key) | **POST** /api/v2/integration-keys/airflow-callbacks | Create an Airflow callbacks key
[**create_ingestion_key**](IntegrationKeysApi.md#create_ingestion_key) | **POST** /api/v2/integration-keys/ingestion | Create an ingestion key
[**delete_airflow_callbacks_key**](IntegrationKeysApi.md#delete_airflow_callbacks_key) | **DELETE** /api/v2/integration-keys/airflow-callbacks/{key_id} | Delete an Airflow callbacks key
[**delete_ingestion_key**](IntegrationKeysApi.md#delete_ingestion_key) | **DELETE** /api/v2/integration-keys/ingestion/{key_id} | Delete an ingestion key
[**get_airflow_callbacks_key**](IntegrationKeysApi.md#get_airflow_callbacks_key) | **GET** /api/v2/integration-keys/airflow-callbacks/{key_id} | Get an Airflow callbacks key
[**get_ingestion_key**](IntegrationKeysApi.md#get_ingestion_key) | **GET** /api/v2/integration-keys/ingestion/{key_id} | Get an ingestion key
[**list_integration_keys**](IntegrationKeysApi.md#list_integration_keys) | **GET** /api/v2/integration-keys | List integration keys


# **create_airflow_callbacks_key**
> AirflowCallbacksKeyCreatedOut create_airflow_callbacks_key(airflow_callbacks_key_in)

Create an Airflow callbacks key

Create a key an Airflow environment reports its DAG and task runs with.

The key is scoped to one `airflow` ETL container. An ETL container of another type returns
422, and an id your account does not hold returns 404.

The secret is returned by this call and never again. A container can hold any number of
keys, so create the next one before deleting the last when rotating.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.airflow_callbacks_key_created_out import AirflowCallbacksKeyCreatedOut
from pycarlo2.models.airflow_callbacks_key_in import AirflowCallbacksKeyIn
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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    airflow_callbacks_key_in = pycarlo2.AirflowCallbacksKeyIn() # AirflowCallbacksKeyIn | 

    try:
        # Create an Airflow callbacks key
        api_response = api_instance.create_airflow_callbacks_key(airflow_callbacks_key_in)
        print("The response of IntegrationKeysApi->create_airflow_callbacks_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->create_airflow_callbacks_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **airflow_callbacks_key_in** | [**AirflowCallbacksKeyIn**](AirflowCallbacksKeyIn.md)|  | 

### Return type

[**AirflowCallbacksKeyCreatedOut**](AirflowCallbacksKeyCreatedOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ingestion_key**
> IngestionKeyCreatedOut create_ingestion_key(ingestion_key_in)

Create an ingestion key

Create a key that pushes data to one warehouse or container.

Send exactly one of `warehouse_id`, `bi_container_id` and `etl_container_id`. A warehouse
takes pushed metadata, lineage and query logs, a BI container pushed BI assets, and an ETL
container pushed ETL jobs and runs. Data pushed with the key for any other warehouse or
container is refused. An id your account does not hold returns 404.

The secret is returned by this call and never again. A warehouse or container can hold any
number of keys, so create the next one before deleting the last when rotating.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.ingestion_key_created_out import IngestionKeyCreatedOut
from pycarlo2.models.ingestion_key_in import IngestionKeyIn
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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    ingestion_key_in = pycarlo2.IngestionKeyIn() # IngestionKeyIn | 

    try:
        # Create an ingestion key
        api_response = api_instance.create_ingestion_key(ingestion_key_in)
        print("The response of IntegrationKeysApi->create_ingestion_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->create_ingestion_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingestion_key_in** | [**IngestionKeyIn**](IngestionKeyIn.md)|  | 

### Return type

[**IngestionKeyCreatedOut**](IngestionKeyCreatedOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_airflow_callbacks_key**
> delete_airflow_callbacks_key(key_id)

Delete an Airflow callbacks key

Delete an Airflow callbacks key. An Airflow environment still reporting with it is
refused from then on.

Deleting an id your account does not hold, or has already deleted, also returns 204.

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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    key_id = 'key_id_example' # str | Id of the integration key, as returned when it is created or listed.

    try:
        # Delete an Airflow callbacks key
        api_instance.delete_airflow_callbacks_key(key_id)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->delete_airflow_callbacks_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Id of the integration key, as returned when it is created or listed. | 

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
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ingestion_key**
> delete_ingestion_key(key_id)

Delete an ingestion key

Delete an ingestion key. Data pushed with it is refused from then on.

Deleting an id your account does not hold, or has already deleted, also returns 204.

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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    key_id = 'key_id_example' # str | Id of the integration key, as returned when it is created or listed.

    try:
        # Delete an ingestion key
        api_instance.delete_ingestion_key(key_id)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->delete_ingestion_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Id of the integration key, as returned when it is created or listed. | 

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
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_airflow_callbacks_key**
> AirflowCallbacksKeyOut get_airflow_callbacks_key(key_id)

Get an Airflow callbacks key

Get one Airflow callbacks key. The secret is not part of it.

An id that names a key of another scope, or no key in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.airflow_callbacks_key_out import AirflowCallbacksKeyOut
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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    key_id = 'key_id_example' # str | Id of the integration key, as returned when it is created or listed.

    try:
        # Get an Airflow callbacks key
        api_response = api_instance.get_airflow_callbacks_key(key_id)
        print("The response of IntegrationKeysApi->get_airflow_callbacks_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->get_airflow_callbacks_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Id of the integration key, as returned when it is created or listed. | 

### Return type

[**AirflowCallbacksKeyOut**](AirflowCallbacksKeyOut.md)

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
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ingestion_key**
> IngestionKeyOut get_ingestion_key(key_id)

Get an ingestion key

Get one ingestion key. The secret is not part of it.

An id that names a key of another scope, or no key in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.ingestion_key_out import IngestionKeyOut
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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    key_id = 'key_id_example' # str | Id of the integration key, as returned when it is created or listed.

    try:
        # Get an ingestion key
        api_response = api_instance.get_ingestion_key(key_id)
        print("The response of IntegrationKeysApi->get_ingestion_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->get_ingestion_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Id of the integration key, as returned when it is created or listed. | 

### Return type

[**IngestionKeyOut**](IngestionKeyOut.md)

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
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integration_keys**
> List[IntegrationKeyOut] list_integration_keys(scope=scope, parent_id=parent_id)

List integration keys

List your account's ingestion and Airflow callbacks keys.

No secret is part of the list. Keys are sorted oldest first.

The list is not paged. A warehouse or container holds a key or two in normal use.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.integration_key_out import IntegrationKeyOut
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
    api_instance = pycarlo2.IntegrationKeysApi(api_client)
    scope = pycarlo2.IntegrationKeyScope() # IntegrationKeyScope | Only keys of this scope. (optional)
    parent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only keys scoped to this warehouse, BI container or ETL container. (optional)

    try:
        # List integration keys
        api_response = api_instance.list_integration_keys(scope=scope, parent_id=parent_id)
        print("The response of IntegrationKeysApi->list_integration_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntegrationKeysApi->list_integration_keys: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | [**IntegrationKeyScope**](.md)| Only keys of this scope. | [optional] 
 **parent_id** | **UUID**| Only keys scoped to this warehouse, BI container or ETL container. | [optional] 

### Return type

[**List[IntegrationKeyOut]**](IntegrationKeyOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

