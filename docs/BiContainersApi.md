# pycarlo2.BiContainersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bi_container**](BiContainersApi.md#create_bi_container) | **POST** /api/v2/bi-containers | Create a BI container
[**delete_bi_container**](BiContainersApi.md#delete_bi_container) | **DELETE** /api/v2/bi-containers/{bi_container_id} | Delete a BI container
[**get_bi_container**](BiContainersApi.md#get_bi_container) | **GET** /api/v2/bi-containers/{bi_container_id} | Get a BI container
[**list_bi_containers**](BiContainersApi.md#list_bi_containers) | **GET** /api/v2/bi-containers | List BI containers
[**update_bi_container**](BiContainersApi.md#update_bi_container) | **PATCH** /api/v2/bi-containers/{bi_container_id} | Update a BI container


# **create_bi_container**
> BiContainerOut create_bi_container(bi_container_in)

Create a BI container

Create an empty BI container.

The container holds no connections until you add some. Its type is fixed at creation and
decides which connections it accepts. A `looker` container takes both the Looker API
connection and the LookML git connection. The deployment has to be one the deployments
list returns; any other id returns 404. A deployment that does not support the BI tool,
or needs an upgrade first, returns 409.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.bi_container_in import BiContainerIn
from pycarlo2.models.bi_container_out import BiContainerOut
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
    api_instance = pycarlo2.BiContainersApi(api_client)
    bi_container_in = pycarlo2.BiContainerIn() # BiContainerIn | 

    try:
        # Create a BI container
        api_response = api_instance.create_bi_container(bi_container_in)
        print("The response of BiContainersApi->create_bi_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiContainersApi->create_bi_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bi_container_in** | [**BiContainerIn**](BiContainerIn.md)|  | 

### Return type

[**BiContainerOut**](BiContainerOut.md)

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

# **delete_bi_container**
> delete_bi_container(bi_container_id)

Delete a BI container

Delete a BI container.

Only an empty container can be deleted. Connections are managed as their own resources
and are never deleted with a container, so remove them first. Deleting the container also
removes the BI assets, such as dashboards and reports, collected through it.

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
    api_instance = pycarlo2.BiContainersApi(api_client)
    bi_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a BI container
        api_instance.delete_bi_container(bi_container_id)
    except Exception as e:
        print("Exception when calling BiContainersApi->delete_bi_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bi_container_id** | **UUID**|  | 

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

# **get_bi_container**
> BiContainerOut get_bi_container(bi_container_id)

Get a BI container

Get one BI container.

An id that does not exist or belongs to another account returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.bi_container_out import BiContainerOut
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
    api_instance = pycarlo2.BiContainersApi(api_client)
    bi_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a BI container
        api_response = api_instance.get_bi_container(bi_container_id)
        print("The response of BiContainersApi->get_bi_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiContainersApi->get_bi_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bi_container_id** | **UUID**|  | 

### Return type

[**BiContainerOut**](BiContainerOut.md)

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

# **list_bi_containers**
> List[BiContainerOut] list_bi_containers()

List BI containers

List every BI container in your account, oldest first.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.bi_container_out import BiContainerOut
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
    api_instance = pycarlo2.BiContainersApi(api_client)

    try:
        # List BI containers
        api_response = api_instance.list_bi_containers()
        print("The response of BiContainersApi->list_bi_containers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiContainersApi->list_bi_containers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BiContainerOut]**](BiContainerOut.md)

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

# **update_bi_container**
> BiContainerOut update_bi_container(bi_container_id, bi_container_patch)

Update a BI container

Rename a BI container.

The name is the only thing you can change. The type and the deployment are fixed when the
container is created. Sending an empty body leaves the container as it is and returns it.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.bi_container_out import BiContainerOut
from pycarlo2.models.bi_container_patch import BiContainerPatch
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
    api_instance = pycarlo2.BiContainersApi(api_client)
    bi_container_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    bi_container_patch = pycarlo2.BiContainerPatch() # BiContainerPatch | 

    try:
        # Update a BI container
        api_response = api_instance.update_bi_container(bi_container_id, bi_container_patch)
        print("The response of BiContainersApi->update_bi_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BiContainersApi->update_bi_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bi_container_id** | **UUID**|  | 
 **bi_container_patch** | [**BiContainerPatch**](BiContainerPatch.md)|  | 

### Return type

[**BiContainerOut**](BiContainerOut.md)

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
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

