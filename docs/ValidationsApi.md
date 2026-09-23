# montecarlo.ValidationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_validation_run**](ValidationsApi.md#get_validation_run) | **GET** /api/v2/validations/{run_id} | Get a validation run


# **get_validation_run**
> ValidationRunOut get_validation_run(run_id)

Get a validation run

Read a validation run started by a validate operation.

Poll this until `status` is `completed`. Each validation carries its own `status` and,
once it has one, a `passed` verdict with the problems behind it.

A run is kept for a limited time after it starts and then forgotten. An id that has
expired, never existed, or belongs to another account all return 404.

`Retry-After` says how long to wait before polling again.

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
    api_instance = montecarlo.ValidationsApi(api_client)
    run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Id of the validation run, as returned by the operation that started it.

    try:
        # Get a validation run
        api_response = api_instance.get_validation_run(run_id)
        print("The response of ValidationsApi->get_validation_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationsApi->get_validation_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| Id of the validation run, as returned by the operation that started it. | 

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
**200** | OK |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

