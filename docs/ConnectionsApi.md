# montecarlo.ConnectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /api/v2/connections | Create a connection
[**delete_connection**](ConnectionsApi.md#delete_connection) | **DELETE** /api/v2/connections/{connection_id} | Delete a connection
[**get_connection**](ConnectionsApi.md#get_connection) | **GET** /api/v2/connections/{connection_id} | Get a connection
[**list_connections**](ConnectionsApi.md#list_connections) | **GET** /api/v2/connections | List connections
[**update_connection**](ConnectionsApi.md#update_connection) | **PATCH** /api/v2/connections/{connection_id} | Update a connection
[**validate_connection**](ConnectionsApi.md#validate_connection) | **POST** /api/v2/connections/{connection_id}/validate | Validate a connection


# **create_connection**
> ConnectionOut create_connection(connection_in)

Create a connection

Add a connection to a warehouse or a BI container.

Create the credentials first, through one of the credentials endpoints, then name them
here. The connection's type comes from them, and has to be a type the parent accepts and
its deployment supports. Send `warehouse_id` or `bi_container_id`, exactly one.

A type that depends on a metastore, such as `databricks-sql-warehouse`, goes on a data
lake warehouse that already has a metastore connection. Tableau, Looker and Power BI
credentials go on a BI container of the same tool; a `looker` container takes both the
`looker` and the `looker-git-clone` connection.

Omit `job_types` to run what the type runs by default.

An unknown warehouse, BI container or credentials id returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.connection_in import ConnectionIn
from montecarlo.models.connection_out import ConnectionOut
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
    api_instance = montecarlo.ConnectionsApi(api_client)
    connection_in = montecarlo.ConnectionIn() # ConnectionIn | 

    try:
        # Create a connection
        api_response = api_instance.create_connection(connection_in)
        print("The response of ConnectionsApi->create_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_in** | [**ConnectionIn**](ConnectionIn.md)|  | 

### Return type

[**ConnectionOut**](ConnectionOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(connection_id)

Delete a connection

Delete a connection.

The warehouse or BI container and the credentials are left in place. Delete each of those
through its own endpoint once nothing uses it. Deleting the connection also deletes its
own schedules, monitors and rules.

Deleting a warehouse's last connection is refused when that would also take monitors,
rules or use cases that belong to the warehouse as a whole. Delete the warehouse instead.
Deleting a custom BI connector's connection is refused too, since its BI container and
the assets collected through it would go with it.

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
    api_instance = montecarlo.ConnectionsApi(api_client)
    connection_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a connection
        api_instance.delete_connection(connection_id)
    except Exception as e:
        print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **UUID**|  | 

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

# **get_connection**
> ConnectionOut get_connection(connection_id)

Get a connection

Get one connection.

An id that does not exist, belongs to another account, or names a connection your domain
restrictions hide from you returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.connection_out import ConnectionOut
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
    api_instance = montecarlo.ConnectionsApi(api_client)
    connection_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a connection
        api_response = api_instance.get_connection(connection_id)
        print("The response of ConnectionsApi->get_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->get_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **UUID**|  | 

### Return type

[**ConnectionOut**](ConnectionOut.md)

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

# **list_connections**
> PagedConnectionOut list_connections(warehouse_id=warehouse_id, bi_container_id=bi_container_id, cursor=cursor, limit=limit, with_count=with_count)

List connections

List the connections in your account, a page at a time.

Connections are returned oldest first. Pass `warehouse_id` or `bi_container_id` to list
one warehouse's or one BI container's connections; an id you cannot see returns an empty
page. A caller whose asset access is restricted to certain domains sees only the
connections of warehouses holding assets in those domains, and every BI connection.

Connections that belong to an ETL integration are not listed here.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.paged_connection_out import PagedConnectionOut
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
    api_instance = montecarlo.ConnectionsApi(api_client)
    warehouse_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only list connections on this warehouse. Omit it to list every connection in your account. (optional)
    bi_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only list connections on this BI container. Omit it to list every connection in your account. (optional)
    cursor = 'cursor_example' # str | Position to continue from, as returned in `next_cursor` by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. (optional)
    limit = 50 # int | Maximum number of items to return, between 1 and 100. (optional) (default to 50)
    with_count = False # bool | Whether to also return the total number of items across every page, in `count`. Off by default: counting costs an extra query. (optional) (default to False)

    try:
        # List connections
        api_response = api_instance.list_connections(warehouse_id=warehouse_id, bi_container_id=bi_container_id, cursor=cursor, limit=limit, with_count=with_count)
        print("The response of ConnectionsApi->list_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->list_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | **UUID**| Only list connections on this warehouse. Omit it to list every connection in your account. | [optional] 
 **bi_container_id** | **UUID**| Only list connections on this BI container. Omit it to list every connection in your account. | [optional] 
 **cursor** | **str**| Position to continue from, as returned in &#x60;next_cursor&#x60; by the previous page. Omit it to start from the first page. The value is opaque; do not build or modify one. | [optional] 
 **limit** | **int**| Maximum number of items to return, between 1 and 100. | [optional] [default to 50]
 **with_count** | **bool**| Whether to also return the total number of items across every page, in &#x60;count&#x60;. Off by default: counting costs an extra query. | [optional] [default to False]

### Return type

[**PagedConnectionOut**](PagedConnectionOut.md)

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

# **update_connection**
> ConnectionOut update_connection(connection_id, connection_patch)

Update a connection

Rename a connection.

The name is the only thing you can change. The type, the warehouse or BI container and the
credentials are fixed when the connection is created. Two connections on one warehouse or
BI container cannot share a name. Sending an empty body leaves the connection as it is and
returns it.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.connection_out import ConnectionOut
from montecarlo.models.connection_patch import ConnectionPatch
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
    api_instance = montecarlo.ConnectionsApi(api_client)
    connection_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    connection_patch = montecarlo.ConnectionPatch() # ConnectionPatch | 

    try:
        # Update a connection
        api_response = api_instance.update_connection(connection_id, connection_patch)
        print("The response of ConnectionsApi->update_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->update_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **UUID**|  | 
 **connection_patch** | [**ConnectionPatch**](ConnectionPatch.md)|  | 

### Return type

[**ConnectionOut**](ConnectionOut.md)

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

# **validate_connection**
> ValidationRunOut validate_connection(connection_id)

Validate a connection

Check a connection against the system it reads from.

Tests the connection as it stands, with the credentials it already uses. Nothing is
changed, and you send no credentials.

The response is the run as it starts, and `Location` names where to read it. Poll that
until the run's status is `completed`; each validation carries its own verdict.

An id that does not exist or belongs to another account returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
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
    api_instance = montecarlo.ConnectionsApi(api_client)
    connection_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Validate a connection
        api_response = api_instance.validate_connection(connection_id)
        print("The response of ConnectionsApi->validate_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionsApi->validate_connection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **UUID**|  | 

### Return type

[**ValidationRunOut**](ValidationRunOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

