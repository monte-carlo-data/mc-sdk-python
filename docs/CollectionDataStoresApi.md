# montecarlo.CollectionDataStoresApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_aws_collection_data_store**](CollectionDataStoresApi.md#delete_aws_collection_data_store) | **DELETE** /api/v2/collection-data-stores/aws/{collection_data_store_id} | Delete an AWS collection data store
[**delete_azure_collection_data_store**](CollectionDataStoresApi.md#delete_azure_collection_data_store) | **DELETE** /api/v2/collection-data-stores/azure/{collection_data_store_id} | Delete an Azure collection data store
[**delete_gcp_collection_data_store**](CollectionDataStoresApi.md#delete_gcp_collection_data_store) | **DELETE** /api/v2/collection-data-stores/gcp/{collection_data_store_id} | Delete a GCP collection data store
[**get_aws_collection_data_store**](CollectionDataStoresApi.md#get_aws_collection_data_store) | **GET** /api/v2/collection-data-stores/aws/{collection_data_store_id} | Get an AWS collection data store
[**get_azure_collection_data_store**](CollectionDataStoresApi.md#get_azure_collection_data_store) | **GET** /api/v2/collection-data-stores/azure/{collection_data_store_id} | Get an Azure collection data store
[**get_gcp_collection_data_store**](CollectionDataStoresApi.md#get_gcp_collection_data_store) | **GET** /api/v2/collection-data-stores/gcp/{collection_data_store_id} | Get a GCP collection data store
[**list_collection_data_stores**](CollectionDataStoresApi.md#list_collection_data_stores) | **GET** /api/v2/collection-data-stores | List collection data stores
[**register_aws_collection_data_store**](CollectionDataStoresApi.md#register_aws_collection_data_store) | **POST** /api/v2/collection-data-stores/aws | Register an AWS collection data store
[**register_azure_collection_data_store**](CollectionDataStoresApi.md#register_azure_collection_data_store) | **POST** /api/v2/collection-data-stores/azure | Register an Azure collection data store
[**register_gcp_collection_data_store**](CollectionDataStoresApi.md#register_gcp_collection_data_store) | **POST** /api/v2/collection-data-stores/gcp | Register a GCP collection data store
[**update_aws_collection_data_store**](CollectionDataStoresApi.md#update_aws_collection_data_store) | **PATCH** /api/v2/collection-data-stores/aws/{collection_data_store_id} | Update an AWS collection data store
[**update_azure_collection_data_store**](CollectionDataStoresApi.md#update_azure_collection_data_store) | **PATCH** /api/v2/collection-data-stores/azure/{collection_data_store_id} | Update an Azure collection data store
[**update_gcp_collection_data_store**](CollectionDataStoresApi.md#update_gcp_collection_data_store) | **PATCH** /api/v2/collection-data-stores/gcp/{collection_data_store_id} | Update a GCP collection data store


# **delete_aws_collection_data_store**
> delete_aws_collection_data_store(collection_data_store_id)

Delete an AWS collection data store

Deregister an S3 data store.

Its deployment is left without one. Reprovision that deployment before registering another.

The bucket itself is yours and is not deleted.

A data store cannot be deleted while its deployment still has a connection running through
it. Delete or move those connections first.

An id that names a data store on another platform, or no data store in your account,
returns 404.

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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an AWS collection data store
        api_instance.delete_aws_collection_data_store(collection_data_store_id)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->delete_aws_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

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

# **delete_azure_collection_data_store**
> delete_azure_collection_data_store(collection_data_store_id)

Delete an Azure collection data store

Deregister a data store held in Azure Blob Storage.

Its deployment is left without one. Reprovision that deployment before registering another.

The container itself is yours and is not deleted.

A data store cannot be deleted while its deployment still has a connection running through
it. Delete or move those connections first.

An id that names a data store on another platform, or no data store in your account,
returns 404.

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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an Azure collection data store
        api_instance.delete_azure_collection_data_store(collection_data_store_id)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->delete_azure_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

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

# **delete_gcp_collection_data_store**
> delete_gcp_collection_data_store(collection_data_store_id)

Delete a GCP collection data store

Deregister a data store held in Google Cloud Storage.

Its deployment is left without one. Reprovision that deployment before registering another.

The bucket itself is yours and is not deleted.

A data store cannot be deleted while its deployment still has a connection running through
it. Delete or move those connections first.

An id that names a data store on another platform, or no data store in your account,
returns 404.

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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a GCP collection data store
        api_instance.delete_gcp_collection_data_store(collection_data_store_id)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->delete_gcp_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

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

# **get_aws_collection_data_store**
> AwsCollectionDataStoreOut get_aws_collection_data_store(collection_data_store_id)

Get an AWS collection data store

Get one data store held in an S3 bucket, including its external id.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_data_store_out import AwsCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an AWS collection data store
        api_response = api_instance.get_aws_collection_data_store(collection_data_store_id)
        print("The response of CollectionDataStoresApi->get_aws_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->get_aws_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

### Return type

[**AwsCollectionDataStoreOut**](AwsCollectionDataStoreOut.md)

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

# **get_azure_collection_data_store**
> AzureCollectionDataStoreOut get_azure_collection_data_store(collection_data_store_id)

Get an Azure collection data store

Read one data store held in Azure Blob Storage.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_data_store_out import AzureCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an Azure collection data store
        api_response = api_instance.get_azure_collection_data_store(collection_data_store_id)
        print("The response of CollectionDataStoresApi->get_azure_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->get_azure_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

### Return type

[**AzureCollectionDataStoreOut**](AzureCollectionDataStoreOut.md)

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

# **get_gcp_collection_data_store**
> GcpCollectionDataStoreOut get_gcp_collection_data_store(collection_data_store_id)

Get a GCP collection data store

Read one data store held in Google Cloud Storage.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_data_store_out import GcpCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a GCP collection data store
        api_response = api_instance.get_gcp_collection_data_store(collection_data_store_id)
        print("The response of CollectionDataStoresApi->get_gcp_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->get_gcp_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 

### Return type

[**GcpCollectionDataStoreOut**](GcpCollectionDataStoreOut.md)

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

# **list_collection_data_stores**
> List[CollectionDataStoreOut] list_collection_data_stores()

List collection data stores

List the data stores in your account, on every platform.

Only data stores on deployments running Monte Carlo's current collection platform are
listed. Data stores on the older platform are managed separately and do not appear here.

Data stores are sorted by name, ignoring case. Data stores with no name come last.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.collection_data_store_out import CollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)

    try:
        # List collection data stores
        api_response = api_instance.list_collection_data_stores()
        print("The response of CollectionDataStoresApi->list_collection_data_stores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->list_collection_data_stores: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionDataStoreOut]**](CollectionDataStoreOut.md)

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

# **register_aws_collection_data_store**
> AwsCollectionDataStoreOut register_aws_collection_data_store(aws_collection_data_store_in)

Register an AWS collection data store

Register the data store a deployment was provisioned for, on AWS.

The second of the two calls that connect a data store. Provision the deployment first, then
create the bucket and the role yourself. The role's trust policy must already carry the
deployment's external id.

Monte Carlo writes a test object to the bucket and reads it back before enabling the data
store. Nothing is registered if that fails, so call this again once you have fixed the
cause.

Sending the same bucket and role twice returns the data store already there, so a retry is
safe. A different bucket or role over a registered one is refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_data_store_in import AwsCollectionDataStoreIn
from montecarlo.models.aws_collection_data_store_out import AwsCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    aws_collection_data_store_in = montecarlo.AwsCollectionDataStoreIn() # AwsCollectionDataStoreIn | 

    try:
        # Register an AWS collection data store
        api_response = api_instance.register_aws_collection_data_store(aws_collection_data_store_in)
        print("The response of CollectionDataStoresApi->register_aws_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->register_aws_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_collection_data_store_in** | [**AwsCollectionDataStoreIn**](AwsCollectionDataStoreIn.md)|  | 

### Return type

[**AwsCollectionDataStoreOut**](AwsCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_azure_collection_data_store**
> AzureCollectionDataStoreOut register_azure_collection_data_store(azure_collection_data_store_in)

Register an Azure collection data store

Register the data store a deployment was provisioned for, in Azure Blob Storage.

The second of the two calls that connect a data store. Provision the deployment first, then
create the container yourself and grant Monte Carlo access to it.

Send `authentication_type` with the one credentials object that goes with it. The
credentials name the storage account, so it is not a field of its own. A connection string
carries it, and a service principal names it in `account_url`.

Monte Carlo writes a test object to the container and reads it back before enabling the data
store. Nothing is registered if that fails, so call this again once you have fixed the
cause.

Sending the same details twice returns the data store already there, so a retry is safe.
Different details over a registered one are refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_data_store_in import AzureCollectionDataStoreIn
from montecarlo.models.azure_collection_data_store_out import AzureCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    azure_collection_data_store_in = montecarlo.AzureCollectionDataStoreIn() # AzureCollectionDataStoreIn | 

    try:
        # Register an Azure collection data store
        api_response = api_instance.register_azure_collection_data_store(azure_collection_data_store_in)
        print("The response of CollectionDataStoresApi->register_azure_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->register_azure_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_collection_data_store_in** | [**AzureCollectionDataStoreIn**](AzureCollectionDataStoreIn.md)|  | 

### Return type

[**AzureCollectionDataStoreOut**](AzureCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_gcp_collection_data_store**
> GcpCollectionDataStoreOut register_gcp_collection_data_store(gcp_collection_data_store_in)

Register a GCP collection data store

Register the data store a deployment was provisioned for, in Google Cloud Storage.

The second of the two calls that connect a data store. Provision the deployment first, then
create the bucket yourself and grant the service account access to it.

Send the service account key as the contents of the JSON key file Google issued for it.

Monte Carlo writes a test object to the bucket and reads it back before enabling the data
store. Nothing is registered if that fails, so call this again once you have fixed the
cause.

Sending the same details twice returns the data store already there, so a retry is safe.
Different details over a registered one are refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_data_store_in import GcpCollectionDataStoreIn
from montecarlo.models.gcp_collection_data_store_out import GcpCollectionDataStoreOut
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    gcp_collection_data_store_in = montecarlo.GcpCollectionDataStoreIn() # GcpCollectionDataStoreIn | 

    try:
        # Register a GCP collection data store
        api_response = api_instance.register_gcp_collection_data_store(gcp_collection_data_store_in)
        print("The response of CollectionDataStoresApi->register_gcp_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->register_gcp_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_collection_data_store_in** | [**GcpCollectionDataStoreIn**](GcpCollectionDataStoreIn.md)|  | 

### Return type

[**GcpCollectionDataStoreOut**](GcpCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aws_collection_data_store**
> AwsCollectionDataStoreOut update_aws_collection_data_store(collection_data_store_id, aws_collection_data_store_patch)

Update an AWS collection data store

Change the bucket, the role or the name of an S3 data store.

Send any of the three. Anything you leave out is kept as it is. A data store with no bucket
yet needs one supplied here.

A new bucket or role is checked before it is saved, and re-enables a data store that had
been disabled. Nothing changes if that check fails. Sending only `name` skips the check.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_data_store_out import AwsCollectionDataStoreOut
from montecarlo.models.aws_collection_data_store_patch import AwsCollectionDataStorePatch
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    aws_collection_data_store_patch = montecarlo.AwsCollectionDataStorePatch() # AwsCollectionDataStorePatch | 

    try:
        # Update an AWS collection data store
        api_response = api_instance.update_aws_collection_data_store(collection_data_store_id, aws_collection_data_store_patch)
        print("The response of CollectionDataStoresApi->update_aws_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->update_aws_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 
 **aws_collection_data_store_patch** | [**AwsCollectionDataStorePatch**](AwsCollectionDataStorePatch.md)|  | 

### Return type

[**AwsCollectionDataStoreOut**](AwsCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_azure_collection_data_store**
> AzureCollectionDataStoreOut update_azure_collection_data_store(collection_data_store_id, azure_collection_data_store_patch)

Update an Azure collection data store

Change the container, the credentials, the authentication type or the name.

Send any of them. Anything you leave out is kept as it is. A data store with no container
yet needs one supplied here.

A credentials object replaces the stored credentials rather than merging into them, so send
every field of it, along with the `authentication_type` it belongs to. That is also how you
move a data store between the two authentication types.

Anything Monte Carlo validates against your storage is checked before it is saved, and
re-enables a data store that had been disabled. Nothing changes if that check fails. Sending
only `name` skips the check.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_data_store_out import AzureCollectionDataStoreOut
from montecarlo.models.azure_collection_data_store_patch import AzureCollectionDataStorePatch
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_collection_data_store_patch = montecarlo.AzureCollectionDataStorePatch() # AzureCollectionDataStorePatch | 

    try:
        # Update an Azure collection data store
        api_response = api_instance.update_azure_collection_data_store(collection_data_store_id, azure_collection_data_store_patch)
        print("The response of CollectionDataStoresApi->update_azure_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->update_azure_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 
 **azure_collection_data_store_patch** | [**AzureCollectionDataStorePatch**](AzureCollectionDataStorePatch.md)|  | 

### Return type

[**AzureCollectionDataStoreOut**](AzureCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_gcp_collection_data_store**
> GcpCollectionDataStoreOut update_gcp_collection_data_store(collection_data_store_id, gcp_collection_data_store_patch)

Update a GCP collection data store

Change the bucket, the service account key or the name.

Send any of them. Anything you leave out is kept as it is. A data store with no bucket yet
needs one supplied here.

The service account key replaces the stored key rather than merging into it.

Anything Monte Carlo validates against your storage is checked before it is saved, and
re-enables a data store that had been disabled. Nothing changes if that check fails. Sending
only `name` skips the check.

An id that names a data store on another platform, or no data store in your account,
returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_data_store_out import GcpCollectionDataStoreOut
from montecarlo.models.gcp_collection_data_store_patch import GcpCollectionDataStorePatch
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
    api_instance = montecarlo.CollectionDataStoresApi(api_client)
    collection_data_store_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    gcp_collection_data_store_patch = montecarlo.GcpCollectionDataStorePatch() # GcpCollectionDataStorePatch | 

    try:
        # Update a GCP collection data store
        api_response = api_instance.update_gcp_collection_data_store(collection_data_store_id, gcp_collection_data_store_patch)
        print("The response of CollectionDataStoresApi->update_gcp_collection_data_store:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionDataStoresApi->update_gcp_collection_data_store: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_data_store_id** | **UUID**|  | 
 **gcp_collection_data_store_patch** | [**GcpCollectionDataStorePatch**](GcpCollectionDataStorePatch.md)|  | 

### Return type

[**GcpCollectionDataStoreOut**](GcpCollectionDataStoreOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

