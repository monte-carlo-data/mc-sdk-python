# pycarlo2.CustomConnectorTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_custom_connector_type**](CustomConnectorTypesApi.md#get_custom_connector_type) | **GET** /api/v2/custom-connector-types/{custom_connector_type_id} | Get a custom connector type
[**list_custom_connector_types**](CustomConnectorTypesApi.md#list_custom_connector_types) | **GET** /api/v2/custom-connector-types | List custom connector types


# **get_custom_connector_type**
> CustomConnectorTypeOut get_custom_connector_type(custom_connector_type_id)

Get a custom connector type

Get one custom connector type.

An id that does not exist or belongs to another account returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.custom_connector_type_out import CustomConnectorTypeOut
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
    api_instance = pycarlo2.CustomConnectorTypesApi(api_client)
    custom_connector_type_id = 'custom_connector_type_id_example' # str | Id of the custom connector type, as returned when it is listed.

    try:
        # Get a custom connector type
        api_response = api_instance.get_custom_connector_type(custom_connector_type_id)
        print("The response of CustomConnectorTypesApi->get_custom_connector_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorTypesApi->get_custom_connector_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_connector_type_id** | **str**| Id of the custom connector type, as returned when it is listed. | 

### Return type

[**CustomConnectorTypeOut**](CustomConnectorTypeOut.md)

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

# **list_custom_connector_types**
> List[CustomConnectorTypeOut] list_custom_connector_types(asset_class=asset_class, collection_agent_id=collection_agent_id)

List custom connector types

List the custom connector types your collection agents registered, oldest first.

A type whose collection agent was removed outright is not listed.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.custom_connector_type_out import CustomConnectorTypeOut
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
    api_instance = pycarlo2.CustomConnectorTypesApi(api_client)
    asset_class = pycarlo2.CustomConnectorAssetClass() # CustomConnectorAssetClass | Only connector types of this asset class. (optional)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only connector types this collection agent registered. (optional)

    try:
        # List custom connector types
        api_response = api_instance.list_custom_connector_types(asset_class=asset_class, collection_agent_id=collection_agent_id)
        print("The response of CustomConnectorTypesApi->list_custom_connector_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorTypesApi->list_custom_connector_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_class** | [**CustomConnectorAssetClass**](.md)| Only connector types of this asset class. | [optional] 
 **collection_agent_id** | **UUID**| Only connector types this collection agent registered. | [optional] 

### Return type

[**List[CustomConnectorTypeOut]**](CustomConnectorTypeOut.md)

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

