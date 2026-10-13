# pycarlo2.EtlContainersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_etl_container**](EtlContainersApi.md#create_etl_container) | **POST** /api/v2/etl-containers | Create an ETL container
[**delete_etl_container**](EtlContainersApi.md#delete_etl_container) | **DELETE** /api/v2/etl-containers/{etl_container_id} | Delete an ETL container
[**get_etl_container**](EtlContainersApi.md#get_etl_container) | **GET** /api/v2/etl-containers/{etl_container_id} | Get an ETL container
[**list_etl_containers**](EtlContainersApi.md#list_etl_containers) | **GET** /api/v2/etl-containers | List ETL containers
[**update_etl_container**](EtlContainersApi.md#update_etl_container) | **PATCH** /api/v2/etl-containers/{etl_container_id} | Update an ETL container


# **create_etl_container**
> EtlContainerOut create_etl_container(etl_container_in)

Create an ETL container

Create an empty ETL container.

The container holds no connection until you add one. Its type is fixed at creation and
decides which connection it accepts. Every type except `airflow` runs through a
deployment, which has to be one the deployments list returns; any other id returns 404.
A deployment that does not support the ETL tool, or needs an upgrade first, returns 409.
A deployment takes one `fivetran` container. A name another container of the same type
already uses returns 409. A type your account's plan does not include returns 403.

A push-only `custom-etl-connector` container receives jobs and runs pushed with a key from
`POST /integration-keys/ingestion`. An `airflow` container receives runs reported with a
key from `POST /integration-keys/airflow-callbacks`.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.etl_container_in import EtlContainerIn
from pycarlo2.models.etl_container_out import EtlContainerOut
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
    api_instance = pycarlo2.EtlContainersApi(api_client)
    etl_container_in = pycarlo2.EtlContainerIn() # EtlContainerIn | 

    try:
        # Create an ETL container
        api_response = api_instance.create_etl_container(etl_container_in)
        print("The response of EtlContainersApi->create_etl_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtlContainersApi->create_etl_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etl_container_in** | [**EtlContainerIn**](EtlContainerIn.md)|  | 

### Return type

[**EtlContainerOut**](EtlContainerOut.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_etl_container**
> delete_etl_container(etl_container_id)

Delete an ETL container

Delete an ETL container.

Only an empty container can be deleted. A connection is managed as its own resource and
is never deleted with its container, so remove it first. A synthetic container cannot be
deleted here. Both refusals return 409. Deleting a container revokes the integration keys
scoped to it.

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
    api_instance = pycarlo2.EtlContainersApi(api_client)
    etl_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an ETL container
        api_instance.delete_etl_container(etl_container_id)
    except Exception as e:
        print("Exception when calling EtlContainersApi->delete_etl_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etl_container_id** | **UUID**|  | 

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

# **get_etl_container**
> EtlContainerOut get_etl_container(etl_container_id)

Get an ETL container

Get one ETL container.

An id that does not exist or belongs to another account returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.etl_container_out import EtlContainerOut
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
    api_instance = pycarlo2.EtlContainersApi(api_client)
    etl_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an ETL container
        api_response = api_instance.get_etl_container(etl_container_id)
        print("The response of EtlContainersApi->get_etl_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtlContainersApi->get_etl_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etl_container_id** | **UUID**|  | 

### Return type

[**EtlContainerOut**](EtlContainerOut.md)

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

# **list_etl_containers**
> List[EtlContainerOut] list_etl_containers()

List ETL containers

List every ETL container in your account, oldest first.

The list includes synthetic containers, which this API does not create or delete.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.etl_container_out import EtlContainerOut
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
    api_instance = pycarlo2.EtlContainersApi(api_client)

    try:
        # List ETL containers
        api_response = api_instance.list_etl_containers()
        print("The response of EtlContainersApi->list_etl_containers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtlContainersApi->list_etl_containers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EtlContainerOut]**](EtlContainerOut.md)

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

# **update_etl_container**
> EtlContainerOut update_etl_container(etl_container_id, etl_container_patch)

Update an ETL container

Rename an ETL container.

The name is the only thing you can change. The type and the deployment are fixed when the
container is created. A name another container of the same type already uses returns 409.
Sending an empty body leaves the container as it is and returns it.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.etl_container_out import EtlContainerOut
from pycarlo2.models.etl_container_patch import EtlContainerPatch
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
    api_instance = pycarlo2.EtlContainersApi(api_client)
    etl_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    etl_container_patch = pycarlo2.EtlContainerPatch() # EtlContainerPatch | 

    try:
        # Update an ETL container
        api_response = api_instance.update_etl_container(etl_container_id, etl_container_patch)
        print("The response of EtlContainersApi->update_etl_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EtlContainersApi->update_etl_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **etl_container_id** | **UUID**|  | 
 **etl_container_patch** | [**EtlContainerPatch**](EtlContainerPatch.md)|  | 

### Return type

[**EtlContainerOut**](EtlContainerOut.md)

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
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

