# montecarlo.ValidationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_validation_run**](ValidationsApi.md#get_validation_run) | **GET** /api/v2/validations/{run_id} | Get a validation run


# **get_validation_run**
> ValidationRunOut get_validation_run(run_id, since=since, if_none_match=if_none_match)

Get a validation run

Read a validation run started by a validate operation.

Poll this until `status` is `completed`. Each validation carries its own `status` and,
once it has one, a `passed` verdict with the problems behind it.

Pass the `revision` from each response as `since` on the next poll to get only the
validations that changed. The run's other fields are always returned in full.

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
    since = 56 # int | The `revision` from the previous response. Only validations that changed after it are returned. Omit it to get every validation. (optional)
    if_none_match = 'if_none_match_example' # str | The `ETag` from a previous response. The read answers 304 with no body while the run's `revision` is unchanged. (optional)

    try:
        # Get a validation run
        api_response = api_instance.get_validation_run(run_id, since=since, if_none_match=if_none_match)
        print("The response of ValidationsApi->get_validation_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationsApi->get_validation_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **run_id** | **UUID**| Id of the validation run, as returned by the operation that started it. | 
 **since** | **int**| The &#x60;revision&#x60; from the previous response. Only validations that changed after it are returned. Omit it to get every validation. | [optional] 
 **if_none_match** | **str**| The &#x60;ETag&#x60; from a previous response. The read answers 304 with no body while the run&#39;s &#x60;revision&#x60; is unchanged. | [optional] 

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
**304** | Not Modified |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

