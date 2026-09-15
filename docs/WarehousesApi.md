# montecarlo.WarehousesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_warehouse**](WarehousesApi.md#create_warehouse) | **POST** /api/v2/warehouses | Create a warehouse
[**delete_warehouse**](WarehousesApi.md#delete_warehouse) | **DELETE** /api/v2/warehouses/{warehouse_id} | Delete a warehouse
[**get_warehouse**](WarehousesApi.md#get_warehouse) | **GET** /api/v2/warehouses/{warehouse_id} | Get a warehouse
[**list_warehouses**](WarehousesApi.md#list_warehouses) | **GET** /api/v2/warehouses | List warehouses
[**update_warehouse**](WarehousesApi.md#update_warehouse) | **PATCH** /api/v2/warehouses/{warehouse_id} | Update a warehouse


# **create_warehouse**
> WarehouseOut create_warehouse(warehouse_in)

Create a warehouse

Create an empty warehouse.

The warehouse holds no connections until you add some. Its type is fixed at creation and
decides which connections it accepts. The deployment has to be one the deployments list
returns; any other id returns 404.

Two warehouses of the same type cannot share a name.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.warehouse_in import WarehouseIn
from montecarlo.models.warehouse_out import WarehouseOut
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
    api_instance = montecarlo.WarehousesApi(api_client)
    warehouse_in = montecarlo.WarehouseIn() # WarehouseIn | 

    try:
        # Create a warehouse
        api_response = api_instance.create_warehouse(warehouse_in)
        print("The response of WarehousesApi->create_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->create_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_in** | [**WarehouseIn**](WarehouseIn.md)|  | 

### Return type

[**WarehouseOut**](WarehouseOut.md)

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

# **delete_warehouse**
> delete_warehouse(warehouse_id)

Delete a warehouse

Delete a warehouse.

Only an empty warehouse can be deleted: one that still has connections, or that other
warehouses consume from, is refused. Connections are managed as their own resources and
are never deleted with a warehouse. Remove them first.

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
    api_instance = montecarlo.WarehousesApi(api_client)
    warehouse_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a warehouse
        api_instance.delete_warehouse(warehouse_id)
    except Exception as e:
        print("Exception when calling WarehousesApi->delete_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **UUID**|  | 

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

# **get_warehouse**
> WarehouseOut get_warehouse(warehouse_id)

Get a warehouse

Get one warehouse.

An id that does not exist, belongs to another account, or names a warehouse your domain
restrictions hide from you returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.warehouse_out import WarehouseOut
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
    api_instance = montecarlo.WarehousesApi(api_client)
    warehouse_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a warehouse
        api_response = api_instance.get_warehouse(warehouse_id)
        print("The response of WarehousesApi->get_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->get_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **UUID**|  | 

### Return type

[**WarehouseOut**](WarehouseOut.md)

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

# **list_warehouses**
> PagedWarehouseOut list_warehouses(cursor=cursor, limit=limit, with_count=with_count)

List warehouses

List the warehouses in your account, a page at a time.

Warehouses are returned oldest first. A caller whose asset access is restricted to
certain domains sees only the warehouses holding assets in those domains.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.paged_warehouse_out import PagedWarehouseOut
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
    api_instance = montecarlo.WarehousesApi(api_client)
    cursor = 'cursor_example' # str | Position to continue from, as returned in `next_cursor` by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. (optional)
    limit = 50 # int | Maximum number of items to return, between 1 and 100. (optional) (default to 50)
    with_count = False # bool | Whether to also return the total number of items across every page, in `count`. Off by default: counting costs an extra query. (optional) (default to False)

    try:
        # List warehouses
        api_response = api_instance.list_warehouses(cursor=cursor, limit=limit, with_count=with_count)
        print("The response of WarehousesApi->list_warehouses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->list_warehouses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Position to continue from, as returned in &#x60;next_cursor&#x60; by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. | [optional] 
 **limit** | **int**| Maximum number of items to return, between 1 and 100. | [optional] [default to 50]
 **with_count** | **bool**| Whether to also return the total number of items across every page, in &#x60;count&#x60;. Off by default: counting costs an extra query. | [optional] [default to False]

### Return type

[**PagedWarehouseOut**](PagedWarehouseOut.md)

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

# **update_warehouse**
> WarehouseOut update_warehouse(warehouse_id, warehouse_patch)

Update a warehouse

Rename a warehouse.

The name is the only thing you can change. The type and the deployment are fixed when
the warehouse is created. Two warehouses of the same type cannot share a name. Sending an
empty body leaves the warehouse as it is and returns it.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.warehouse_out import WarehouseOut
from montecarlo.models.warehouse_patch import WarehousePatch
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
    api_instance = montecarlo.WarehousesApi(api_client)
    warehouse_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    warehouse_patch = montecarlo.WarehousePatch() # WarehousePatch | 

    try:
        # Update a warehouse
        api_response = api_instance.update_warehouse(warehouse_id, warehouse_patch)
        print("The response of WarehousesApi->update_warehouse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WarehousesApi->update_warehouse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **UUID**|  | 
 **warehouse_patch** | [**WarehousePatch**](WarehousePatch.md)|  | 

### Return type

[**WarehouseOut**](WarehouseOut.md)

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

