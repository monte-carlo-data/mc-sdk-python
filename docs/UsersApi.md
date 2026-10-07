# pycarlo2.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /api/v2/users/me | Get the current user


# **get_current_user**
> CurrentUserOut get_current_user()

Get the current user

Return the identity this request was authenticated as, along with its account.

Use it to confirm that a set of credentials works, to find out which account they belong
to, and to read the authorization groups that decide what the caller may do.

Any authenticated caller may call this operation, and it keeps answering while an account
is paused. A client can therefore learn that the account is paused, rather than only
seeing every other operation refused.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.current_user_out import CurrentUserOut
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
    api_instance = pycarlo2.UsersApi(api_client)

    try:
        # Get the current user
        api_response = api_instance.get_current_user()
        print("The response of UsersApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrentUserOut**](CurrentUserOut.md)

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

