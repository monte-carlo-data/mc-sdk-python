# montecarlo.DeploymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment**](DeploymentsApi.md#create_deployment) | **POST** /api/v2/deployments | Create a deployment
[**delete_deployment**](DeploymentsApi.md#delete_deployment) | **DELETE** /api/v2/deployments/{deployment_id} | Delete a deployment
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /api/v2/deployments/{deployment_id} | Get a deployment
[**list_deployments**](DeploymentsApi.md#list_deployments) | **GET** /api/v2/deployments | List deployments
[**reprovision_deployment**](DeploymentsApi.md#reprovision_deployment) | **POST** /api/v2/deployments/{deployment_id}/reprovision | Reprovision a deployment
[**update_deployment**](DeploymentsApi.md#update_deployment) | **PATCH** /api/v2/deployments/{deployment_id} | Update a deployment


# **create_deployment**
> DeploymentOut create_deployment(deployment_in)

Create a deployment

Provision a deployment for a collection agent or a data store to be registered on.

Connecting either one takes two calls, and this is the first. Monte Carlo allocates the
deployment, and returns an external id for a deployment it will reach by assuming a role.
Registering on the deployment is the second call, and that is what enables it.

The new deployment is not enabled and serves no connections until something is registered
on it. It counts against your account's deployment limit as soon as it is created, whether
or not anything ever is.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.deployment_in import DeploymentIn
from montecarlo.models.deployment_out import DeploymentOut
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
    api_instance = montecarlo.DeploymentsApi(api_client)
    deployment_in = montecarlo.DeploymentIn() # DeploymentIn | 

    try:
        # Create a deployment
        api_response = api_instance.create_deployment(deployment_in)
        print("The response of DeploymentsApi->create_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->create_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_in** | [**DeploymentIn**](DeploymentIn.md)|  | 

### Return type

[**DeploymentOut**](DeploymentOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment**
> delete_deployment(deployment_id)

Delete a deployment

Delete a deployment, releasing the infrastructure Monte Carlo runs for it.

The deployment's storage is deleted with it, so empty that storage first. A deployment
with an enabled collection agent or data store, or with connections still running through
it, cannot be deleted. Neither can one hosted by Monte Carlo, which this API does not
provision. One that is not enabled is deleted along with the deployment.

Deleting reaches several systems and can stop partway through. Repeating the request
picks up where it stopped, so clear whatever a refusal named and send it again.

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
    api_instance = montecarlo.DeploymentsApi(api_client)
    deployment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a deployment
        api_instance.delete_deployment(deployment_id)
    except Exception as e:
        print("Exception when calling DeploymentsApi->delete_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **UUID**|  | 

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
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment**
> DeploymentOut get_deployment(deployment_id)

Get a deployment

Get one deployment. An AWS deployment includes the external id needed to register on it.

An id that does not exist, belongs to another account, or names a deployment on Monte
Carlo's older collection platform all return 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.deployment_out import DeploymentOut
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
    api_instance = montecarlo.DeploymentsApi(api_client)
    deployment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a deployment
        api_response = api_instance.get_deployment(deployment_id)
        print("The response of DeploymentsApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **UUID**|  | 

### Return type

[**DeploymentOut**](DeploymentOut.md)

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
**404** | Not Found |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployments**
> List[DeploymentSummaryOut] list_deployments()

List deployments

List the deployments in your account.

A deployment is the infrastructure that connects Monte Carlo to your environment. Each
one hosts a collection agent or a data store, or is hosted by Monte Carlo itself.

Only deployments on Monte Carlo's current collection platform are listed. Deployments on
the older platform are managed separately and do not appear here.

Deployments are sorted by name, ignoring case.

A deployment's external id is returned by the single-deployment read, not by this list.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.deployment_summary_out import DeploymentSummaryOut
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
    api_instance = montecarlo.DeploymentsApi(api_client)

    try:
        # List deployments
        api_response = api_instance.list_deployments()
        print("The response of DeploymentsApi->list_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->list_deployments: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DeploymentSummaryOut]**](DeploymentSummaryOut.md)

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

# **reprovision_deployment**
> DeploymentOut reprovision_deployment(deployment_id, deployment_in)

Reprovision a deployment

Give a deployment something fresh to register.

Use this to recover a deployment whose collection agent or data store was deleted, and to
change what a deployment hosts. The deployment itself is kept, so it does not count
against your account's limit a second time, and what it hosted is discarded. An AWS
deployment is given a new external id, so a role trust policy naming the old one has to be
updated.

A deployment whose collection agent or data store is enabled cannot be reprovisioned;
delete that first. Neither can one hosted by Monte Carlo, which this API does not
provision.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.deployment_in import DeploymentIn
from montecarlo.models.deployment_out import DeploymentOut
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
    api_instance = montecarlo.DeploymentsApi(api_client)
    deployment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    deployment_in = montecarlo.DeploymentIn() # DeploymentIn | 

    try:
        # Reprovision a deployment
        api_response = api_instance.reprovision_deployment(deployment_id, deployment_in)
        print("The response of DeploymentsApi->reprovision_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->reprovision_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **UUID**|  | 
 **deployment_in** | [**DeploymentIn**](DeploymentIn.md)|  | 

### Return type

[**DeploymentOut**](DeploymentOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment**
> DeploymentOut update_deployment(deployment_id, deployment_patch)

Update a deployment

Rename a deployment.

The name is the only thing you can change here. What a deployment hosts and where it runs
are settled when it is provisioned, so use reprovision to change either.

Renaming changes nothing about the infrastructure behind the deployment. Every deployment
can be renamed, including one hosted by Monte Carlo. Sending an empty body leaves the
deployment as it is and returns it.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.deployment_out import DeploymentOut
from montecarlo.models.deployment_patch import DeploymentPatch
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
    api_instance = montecarlo.DeploymentsApi(api_client)
    deployment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    deployment_patch = montecarlo.DeploymentPatch() # DeploymentPatch | 

    try:
        # Update a deployment
        api_response = api_instance.update_deployment(deployment_id, deployment_patch)
        print("The response of DeploymentsApi->update_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->update_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **UUID**|  | 
 **deployment_patch** | [**DeploymentPatch**](DeploymentPatch.md)|  | 

### Return type

[**DeploymentOut**](DeploymentOut.md)

### Authorization

[GatewayAuth](../README.md#GatewayAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

