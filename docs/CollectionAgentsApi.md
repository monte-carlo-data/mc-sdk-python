# montecarlo.CollectionAgentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_generic_collection_agent_oauth_client**](CollectionAgentsApi.md#create_generic_collection_agent_oauth_client) | **POST** /api/v2/collection-agents/generic/credentials/oauth | Create an OAuth client for a generic collection agent
[**create_generic_collection_agent_token**](CollectionAgentsApi.md#create_generic_collection_agent_token) | **POST** /api/v2/collection-agents/generic/credentials/token | Create a token for a generic collection agent
[**delete_aws_collection_agent**](CollectionAgentsApi.md#delete_aws_collection_agent) | **DELETE** /api/v2/collection-agents/aws/{collection_agent_id} | Delete an AWS collection agent
[**delete_azure_collection_agent**](CollectionAgentsApi.md#delete_azure_collection_agent) | **DELETE** /api/v2/collection-agents/azure/{collection_agent_id} | Delete an Azure collection agent
[**delete_gcp_collection_agent**](CollectionAgentsApi.md#delete_gcp_collection_agent) | **DELETE** /api/v2/collection-agents/gcp/{collection_agent_id} | Delete a GCP collection agent
[**delete_generic_collection_agent**](CollectionAgentsApi.md#delete_generic_collection_agent) | **DELETE** /api/v2/collection-agents/generic/{collection_agent_id} | Delete a generic collection agent
[**delete_generic_collection_agent_oauth_client**](CollectionAgentsApi.md#delete_generic_collection_agent_oauth_client) | **DELETE** /api/v2/collection-agents/generic/credentials/oauth/{credential_id} | Delete a generic collection agent OAuth client
[**delete_generic_collection_agent_token**](CollectionAgentsApi.md#delete_generic_collection_agent_token) | **DELETE** /api/v2/collection-agents/generic/credentials/token/{credential_id} | Delete a generic collection agent token
[**get_aws_collection_agent**](CollectionAgentsApi.md#get_aws_collection_agent) | **GET** /api/v2/collection-agents/aws/{collection_agent_id} | Get an AWS collection agent
[**get_azure_collection_agent**](CollectionAgentsApi.md#get_azure_collection_agent) | **GET** /api/v2/collection-agents/azure/{collection_agent_id} | Get an Azure collection agent
[**get_gcp_collection_agent**](CollectionAgentsApi.md#get_gcp_collection_agent) | **GET** /api/v2/collection-agents/gcp/{collection_agent_id} | Get a GCP collection agent
[**get_generic_collection_agent**](CollectionAgentsApi.md#get_generic_collection_agent) | **GET** /api/v2/collection-agents/generic/{collection_agent_id} | Get a generic collection agent
[**get_generic_collection_agent_oauth_client**](CollectionAgentsApi.md#get_generic_collection_agent_oauth_client) | **GET** /api/v2/collection-agents/generic/credentials/oauth/{credential_id} | Get a generic collection agent OAuth client
[**get_generic_collection_agent_token**](CollectionAgentsApi.md#get_generic_collection_agent_token) | **GET** /api/v2/collection-agents/generic/credentials/token/{credential_id} | Get a generic collection agent token
[**list_collection_agents**](CollectionAgentsApi.md#list_collection_agents) | **GET** /api/v2/collection-agents | List collection agents
[**list_generic_collection_agent_credentials**](CollectionAgentsApi.md#list_generic_collection_agent_credentials) | **GET** /api/v2/collection-agents/generic/credentials | List generic collection agent credentials
[**register_aws_collection_agent**](CollectionAgentsApi.md#register_aws_collection_agent) | **POST** /api/v2/collection-agents/aws | Register an AWS collection agent
[**register_azure_collection_agent**](CollectionAgentsApi.md#register_azure_collection_agent) | **POST** /api/v2/collection-agents/azure | Register an Azure collection agent
[**register_gcp_collection_agent**](CollectionAgentsApi.md#register_gcp_collection_agent) | **POST** /api/v2/collection-agents/gcp | Register a GCP collection agent
[**register_generic_collection_agent**](CollectionAgentsApi.md#register_generic_collection_agent) | **POST** /api/v2/collection-agents/generic | Register a generic collection agent
[**update_aws_collection_agent**](CollectionAgentsApi.md#update_aws_collection_agent) | **PATCH** /api/v2/collection-agents/aws/{collection_agent_id} | Update an AWS collection agent
[**update_azure_collection_agent**](CollectionAgentsApi.md#update_azure_collection_agent) | **PATCH** /api/v2/collection-agents/azure/{collection_agent_id} | Update an Azure collection agent
[**update_gcp_collection_agent**](CollectionAgentsApi.md#update_gcp_collection_agent) | **PATCH** /api/v2/collection-agents/gcp/{collection_agent_id} | Update a GCP collection agent
[**update_generic_collection_agent**](CollectionAgentsApi.md#update_generic_collection_agent) | **PATCH** /api/v2/collection-agents/generic/{collection_agent_id} | Update a generic collection agent


# **create_generic_collection_agent_oauth_client**
> GenericCollectionAgentOAuthClientCreatedOut create_generic_collection_agent_oauth_client(generic_collection_agent_o_auth_client_in)

Create an OAuth client for a generic collection agent

Create an OAuth 2.0 client for a deployment's generic collection agent.

The agent presents the client id and secret as `client_id` and `client_secret`, and
exchanges them for short-lived access tokens on its own. The secret is returned by this
call and never again, so store it where the agent will read it. A deployment can hold any
number of clients, so create the next one before deleting the last when rotating.

The deployment must have been provisioned for a generic collection agent. It does not have
to be registered yet; creating a credential is what comes before running the agent.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_o_auth_client_created_out import GenericCollectionAgentOAuthClientCreatedOut
from montecarlo.models.generic_collection_agent_o_auth_client_in import GenericCollectionAgentOAuthClientIn
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    generic_collection_agent_o_auth_client_in = montecarlo.GenericCollectionAgentOAuthClientIn() # GenericCollectionAgentOAuthClientIn | 

    try:
        # Create an OAuth client for a generic collection agent
        api_response = api_instance.create_generic_collection_agent_oauth_client(generic_collection_agent_o_auth_client_in)
        print("The response of CollectionAgentsApi->create_generic_collection_agent_oauth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->create_generic_collection_agent_oauth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_collection_agent_o_auth_client_in** | [**GenericCollectionAgentOAuthClientIn**](GenericCollectionAgentOAuthClientIn.md)|  | 

### Return type

[**GenericCollectionAgentOAuthClientCreatedOut**](GenericCollectionAgentOAuthClientCreatedOut.md)

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

# **create_generic_collection_agent_token**
> GenericCollectionAgentTokenCreatedOut create_generic_collection_agent_token(generic_collection_agent_token_in)

Create a token for a generic collection agent

Create a key and secret for a deployment's generic collection agent.

The agent presents them as `mcd_id` and `mcd_token`. The secret is returned by this call
and never again, so store it where the agent will read it. A deployment can hold any number
of tokens, so create the next one before deleting the last when rotating.

The deployment must have been provisioned for a generic collection agent. It does not have
to be registered yet; creating a credential is what comes before running the agent.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_token_created_out import GenericCollectionAgentTokenCreatedOut
from montecarlo.models.generic_collection_agent_token_in import GenericCollectionAgentTokenIn
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    generic_collection_agent_token_in = montecarlo.GenericCollectionAgentTokenIn() # GenericCollectionAgentTokenIn | 

    try:
        # Create a token for a generic collection agent
        api_response = api_instance.create_generic_collection_agent_token(generic_collection_agent_token_in)
        print("The response of CollectionAgentsApi->create_generic_collection_agent_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->create_generic_collection_agent_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_collection_agent_token_in** | [**GenericCollectionAgentTokenIn**](GenericCollectionAgentTokenIn.md)|  | 

### Return type

[**GenericCollectionAgentTokenCreatedOut**](GenericCollectionAgentTokenCreatedOut.md)

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

# **delete_aws_collection_agent**
> delete_aws_collection_agent(collection_agent_id)

Delete an AWS collection agent

Deregister an AWS collection agent.

Its deployment is left without an agent. Reprovision that deployment before registering
another agent on it.

An agent cannot be deleted while its deployment still has a connection running through
it. Delete or move those connections first.

An id that names an agent on another platform, or no agent in your account, returns 404.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an AWS collection agent
        api_instance.delete_aws_collection_agent(collection_agent_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_aws_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

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

# **delete_azure_collection_agent**
> delete_azure_collection_agent(collection_agent_id)

Delete an Azure collection agent

Deregister an Azure collection agent.

Its deployment is left without an agent. Reprovision that deployment before registering
another agent on it.

An agent cannot be deleted while its deployment still has a connection running through it.
Delete or move those connections first.

An id that names an agent on another platform, or no agent in your account, returns 404.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete an Azure collection agent
        api_instance.delete_azure_collection_agent(collection_agent_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_azure_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

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

# **delete_gcp_collection_agent**
> delete_gcp_collection_agent(collection_agent_id)

Delete a GCP collection agent

Deregister a GCP collection agent.

Its deployment is left without an agent. Reprovision that deployment before registering
another agent on it.

An agent cannot be deleted while its deployment still has a connection running through it.
Delete or move those connections first.

An id that names an agent on another platform, or no agent in your account, returns 404.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a GCP collection agent
        api_instance.delete_gcp_collection_agent(collection_agent_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_gcp_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

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

# **delete_generic_collection_agent**
> delete_generic_collection_agent(collection_agent_id)

Delete a generic collection agent

Deregister a generic collection agent.

Every credential created for its deployment is deleted with it, so a running agent stops
being able to connect. Its deployment is left without an agent. Reprovision that deployment
before registering another agent on it.

An agent cannot be deleted while its deployment still has a connection running through it.
Delete or move those connections first.

An id that names an agent on another platform, or no agent in your account, returns 404.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a generic collection agent
        api_instance.delete_generic_collection_agent(collection_agent_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_generic_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

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

# **delete_generic_collection_agent_oauth_client**
> delete_generic_collection_agent_oauth_client(credential_id)

Delete a generic collection agent OAuth client

Delete an OAuth client.

An agent still running with it stops being able to get new access tokens. Access tokens it
already holds stay valid until they expire.

Deleting an id your account does not hold, or has already deleted, also returns 204.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Delete a generic collection agent OAuth client
        api_instance.delete_generic_collection_agent_oauth_client(credential_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_generic_collection_agent_oauth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

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
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_generic_collection_agent_token**
> delete_generic_collection_agent_token(credential_id)

Delete a generic collection agent token

Delete a token. An agent still running with it stops being able to connect.

Deleting an id your account does not hold, or has already deleted, also returns 204.

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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Delete a generic collection agent token
        api_instance.delete_generic_collection_agent_token(credential_id)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->delete_generic_collection_agent_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

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
**429** | Too Many Requests |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_collection_agent**
> AwsCollectionAgentOut get_aws_collection_agent(collection_agent_id)

Get an AWS collection agent

Get one collection agent running on AWS, including its external id.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_agent_out import AwsCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an AWS collection agent
        api_response = api_instance.get_aws_collection_agent(collection_agent_id)
        print("The response of CollectionAgentsApi->get_aws_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_aws_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

### Return type

[**AwsCollectionAgentOut**](AwsCollectionAgentOut.md)

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

# **get_azure_collection_agent**
> AzureCollectionAgentOut get_azure_collection_agent(collection_agent_id)

Get an Azure collection agent

Get one collection agent running on Azure.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_agent_out import AzureCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get an Azure collection agent
        api_response = api_instance.get_azure_collection_agent(collection_agent_id)
        print("The response of CollectionAgentsApi->get_azure_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_azure_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

### Return type

[**AzureCollectionAgentOut**](AzureCollectionAgentOut.md)

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

# **get_gcp_collection_agent**
> GcpCollectionAgentOut get_gcp_collection_agent(collection_agent_id)

Get a GCP collection agent

Get one collection agent running on GCP.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_agent_out import GcpCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a GCP collection agent
        api_response = api_instance.get_gcp_collection_agent(collection_agent_id)
        print("The response of CollectionAgentsApi->get_gcp_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_gcp_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

### Return type

[**GcpCollectionAgentOut**](GcpCollectionAgentOut.md)

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

# **get_generic_collection_agent**
> GenericCollectionAgentOut get_generic_collection_agent(collection_agent_id)

Get a generic collection agent

Get one generic collection agent.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_out import GenericCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a generic collection agent
        api_response = api_instance.get_generic_collection_agent(collection_agent_id)
        print("The response of CollectionAgentsApi->get_generic_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_generic_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 

### Return type

[**GenericCollectionAgentOut**](GenericCollectionAgentOut.md)

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

# **get_generic_collection_agent_oauth_client**
> GenericCollectionAgentOAuthClientOut get_generic_collection_agent_oauth_client(credential_id)

Get a generic collection agent OAuth client

Get one OAuth client. The secret is not part of it.

An id that names another kind of credential, or no credential in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_o_auth_client_out import GenericCollectionAgentOAuthClientOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Get a generic collection agent OAuth client
        api_response = api_instance.get_generic_collection_agent_oauth_client(credential_id)
        print("The response of CollectionAgentsApi->get_generic_collection_agent_oauth_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_generic_collection_agent_oauth_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

[**GenericCollectionAgentOAuthClientOut**](GenericCollectionAgentOAuthClientOut.md)

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

# **get_generic_collection_agent_token**
> GenericCollectionAgentTokenOut get_generic_collection_agent_token(credential_id)

Get a generic collection agent token

Get one token. The secret is not part of it.

An id that names another kind of credential, or no credential in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_token_out import GenericCollectionAgentTokenOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    credential_id = 'credential_id_example' # str | 

    try:
        # Get a generic collection agent token
        api_response = api_instance.get_generic_collection_agent_token(credential_id)
        print("The response of CollectionAgentsApi->get_generic_collection_agent_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->get_generic_collection_agent_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_id** | **str**|  | 

### Return type

[**GenericCollectionAgentTokenOut**](GenericCollectionAgentTokenOut.md)

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

# **list_collection_agents**
> List[CollectionAgentOut] list_collection_agents()

List collection agents

List the collection agents in your account, on every platform.

Only agents on deployments running Monte Carlo's current collection platform are listed.
Agents on the older platform are managed separately and do not appear here.

Agents are sorted by name, ignoring case. Agents with no name come last.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.collection_agent_out import CollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)

    try:
        # List collection agents
        api_response = api_instance.list_collection_agents()
        print("The response of CollectionAgentsApi->list_collection_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->list_collection_agents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CollectionAgentOut]**](CollectionAgentOut.md)

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

# **list_generic_collection_agent_credentials**
> List[CollectionAgentCredentialOut] list_generic_collection_agent_credentials(deployment_id=deployment_id)

List generic collection agent credentials

List the credentials your generic collection agents present, of both kinds.

No secret is part of the list. Credentials are sorted oldest first.

The list is not paged. A deployment holds a credential or two in normal use, so the list
stays short, but nothing caps how many you can create.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.collection_agent_credential_out import CollectionAgentCredentialOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    deployment_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | Only the credentials of this deployment's agent. (optional)

    try:
        # List generic collection agent credentials
        api_response = api_instance.list_generic_collection_agent_credentials(deployment_id=deployment_id)
        print("The response of CollectionAgentsApi->list_generic_collection_agent_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->list_generic_collection_agent_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **UUID**| Only the credentials of this deployment&#39;s agent. | [optional] 

### Return type

[**List[CollectionAgentCredentialOut]**](CollectionAgentCredentialOut.md)

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

# **register_aws_collection_agent**
> AwsCollectionAgentOut register_aws_collection_agent(aws_collection_agent_in)

Register an AWS collection agent

Register the collection agent a deployment was provisioned for, on AWS.

This is the second of the two calls that connect an agent. Provision the deployment
first, deploy the agent yourself, then call this with the deployment's id, the agent's
Lambda function ARN, and the ARN of the role Monte Carlo assumes to invoke it. The
deployment must have been provisioned for an AWS collection agent, and that role's trust
policy must already carry the deployment's external id.

Monte Carlo reaches the agent and checks it before enabling it. If the check fails,
nothing is registered, and you can call this again once the cause is fixed.

Calling this a second time with the same ARNs returns the agent that is already there, so
a retry is safe. Registering different ARNs over an agent that is already registered is
refused. A new `name` is applied either way.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_agent_in import AwsCollectionAgentIn
from montecarlo.models.aws_collection_agent_out import AwsCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    aws_collection_agent_in = montecarlo.AwsCollectionAgentIn() # AwsCollectionAgentIn | 

    try:
        # Register an AWS collection agent
        api_response = api_instance.register_aws_collection_agent(aws_collection_agent_in)
        print("The response of CollectionAgentsApi->register_aws_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->register_aws_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aws_collection_agent_in** | [**AwsCollectionAgentIn**](AwsCollectionAgentIn.md)|  | 

### Return type

[**AwsCollectionAgentOut**](AwsCollectionAgentOut.md)

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

# **register_azure_collection_agent**
> AzureCollectionAgentOut register_azure_collection_agent(azure_collection_agent_in)

Register an Azure collection agent

Register the collection agent a deployment was provisioned for, on Azure.

This is the second of the two calls that connect an agent. Provision the deployment first,
deploy the agent yourself, then call this with the deployment's id, the function app's URL,
and the credentials for the way you want Monte Carlo to authenticate. The deployment must
have been provisioned for an Azure collection agent.

Monte Carlo reaches the agent and checks it before enabling it. If the check fails, nothing
is registered, and you can call this again once the cause is fixed.

Calling this a second time with the same details returns the agent that is already there,
so a retry is safe. Registering a different function app or different credentials over an
agent that is already registered is refused. A new `name` is applied either way.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_agent_in import AzureCollectionAgentIn
from montecarlo.models.azure_collection_agent_out import AzureCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    azure_collection_agent_in = montecarlo.AzureCollectionAgentIn() # AzureCollectionAgentIn | 

    try:
        # Register an Azure collection agent
        api_response = api_instance.register_azure_collection_agent(azure_collection_agent_in)
        print("The response of CollectionAgentsApi->register_azure_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->register_azure_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **azure_collection_agent_in** | [**AzureCollectionAgentIn**](AzureCollectionAgentIn.md)|  | 

### Return type

[**AzureCollectionAgentOut**](AzureCollectionAgentOut.md)

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

# **register_gcp_collection_agent**
> GcpCollectionAgentOut register_gcp_collection_agent(gcp_collection_agent_in)

Register a GCP collection agent

Register the collection agent a deployment was provisioned for, on GCP.

This is the second of the two calls that connect an agent. Provision the deployment first,
deploy the agent yourself, then call this with the deployment's id, the Cloud Run service's
URL, and the credentials Monte Carlo should authenticate with. The deployment must have
been provisioned for a GCP collection agent.

Monte Carlo reaches the agent and checks it before enabling it. If the check fails, nothing
is registered, and you can call this again once the cause is fixed.

Calling this a second time with the same details returns the agent that is already there,
so a retry is safe. Registering a different Cloud Run service or different credentials over
an agent that is already registered is refused. A new `name` is applied either way.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_agent_in import GcpCollectionAgentIn
from montecarlo.models.gcp_collection_agent_out import GcpCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    gcp_collection_agent_in = montecarlo.GcpCollectionAgentIn() # GcpCollectionAgentIn | 

    try:
        # Register a GCP collection agent
        api_response = api_instance.register_gcp_collection_agent(gcp_collection_agent_in)
        print("The response of CollectionAgentsApi->register_gcp_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->register_gcp_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gcp_collection_agent_in** | [**GcpCollectionAgentIn**](GcpCollectionAgentIn.md)|  | 

### Return type

[**GcpCollectionAgentOut**](GcpCollectionAgentOut.md)

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

# **register_generic_collection_agent**
> GenericCollectionAgentOut register_generic_collection_agent(generic_collection_agent_in)

Register a generic collection agent

Enable the generic collection agent a deployment was provisioned for.

A generic agent connects out to Monte Carlo, so registering it takes three steps.
Provision the deployment, create a credential for it, and run the agent with that
credential. Then call this with the deployment's id. Monte Carlo checks that the agent has
connected and enables it.

If the agent has not connected yet, this answers 503 and nothing changes, so call it again
once the agent is up. Calling it on an agent that is already enabled returns the agent, so
a retry is safe. A new `name` is applied either way.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_in import GenericCollectionAgentIn
from montecarlo.models.generic_collection_agent_out import GenericCollectionAgentOut
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    generic_collection_agent_in = montecarlo.GenericCollectionAgentIn() # GenericCollectionAgentIn | 

    try:
        # Register a generic collection agent
        api_response = api_instance.register_generic_collection_agent(generic_collection_agent_in)
        print("The response of CollectionAgentsApi->register_generic_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->register_generic_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generic_collection_agent_in** | [**GenericCollectionAgentIn**](GenericCollectionAgentIn.md)|  | 

### Return type

[**GenericCollectionAgentOut**](GenericCollectionAgentOut.md)

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

# **update_aws_collection_agent**
> AwsCollectionAgentOut update_aws_collection_agent(collection_agent_id, aws_collection_agent_patch)

Update an AWS collection agent

Change the Lambda function, the role or the name of an AWS collection agent.

Send any of the fields, in any combination. Anything you leave out is kept as it is. An
agent that has no Lambda function yet needs one supplied here, since there would otherwise
be nothing for Monte Carlo to reach.

Monte Carlo reaches the agent and checks it again before saving the change, and re-enables
the agent if it was disabled. A successful response therefore always describes a working
agent. If the check fails, nothing about the agent changes. Sending only `name` skips the
check.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.aws_collection_agent_out import AwsCollectionAgentOut
from montecarlo.models.aws_collection_agent_patch import AwsCollectionAgentPatch
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    aws_collection_agent_patch = montecarlo.AwsCollectionAgentPatch() # AwsCollectionAgentPatch | 

    try:
        # Update an AWS collection agent
        api_response = api_instance.update_aws_collection_agent(collection_agent_id, aws_collection_agent_patch)
        print("The response of CollectionAgentsApi->update_aws_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->update_aws_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 
 **aws_collection_agent_patch** | [**AwsCollectionAgentPatch**](AwsCollectionAgentPatch.md)|  | 

### Return type

[**AwsCollectionAgentOut**](AwsCollectionAgentOut.md)

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

# **update_azure_collection_agent**
> AzureCollectionAgentOut update_azure_collection_agent(collection_agent_id, azure_collection_agent_patch)

Update an Azure collection agent

Change the function app, the credentials, the authentication type or the name.

Send any of the fields, in any combination. An agent that has no function app URL yet needs
one supplied here, since there would otherwise be nothing for Monte Carlo to reach. Sending
credentials replaces the stored ones, so send every field of the object you send, along with
the matching `authentication_type`. Sending both is also how you move an agent from one
authentication type to the other. An agent that authenticates some other way refuses a
credentials or authentication type change, since this endpoint only manages the two Azure
function authentication types.

Monte Carlo reaches the agent and checks it again before saving the change, and re-enables
the agent if it was disabled. A successful response therefore always describes a working
agent. If the check fails, nothing about the agent changes. Sending only `name` skips the
check.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.azure_collection_agent_out import AzureCollectionAgentOut
from montecarlo.models.azure_collection_agent_patch import AzureCollectionAgentPatch
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    azure_collection_agent_patch = montecarlo.AzureCollectionAgentPatch() # AzureCollectionAgentPatch | 

    try:
        # Update an Azure collection agent
        api_response = api_instance.update_azure_collection_agent(collection_agent_id, azure_collection_agent_patch)
        print("The response of CollectionAgentsApi->update_azure_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->update_azure_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 
 **azure_collection_agent_patch** | [**AzureCollectionAgentPatch**](AzureCollectionAgentPatch.md)|  | 

### Return type

[**AzureCollectionAgentOut**](AzureCollectionAgentOut.md)

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

# **update_gcp_collection_agent**
> GcpCollectionAgentOut update_gcp_collection_agent(collection_agent_id, gcp_collection_agent_patch)

Update a GCP collection agent

Change the Cloud Run service, the credentials, the authentication type or the name.

Send any of the fields, in any combination. An agent that has no Cloud Run URL yet needs
one supplied here, since there would otherwise be nothing for Monte Carlo to reach. Sending
credentials replaces the stored ones, and sending `authentication_type` along with them
moves the agent between the two GCP authentication types. An agent that authenticates some
other way refuses a Cloud Run URL or credentials change, since this endpoint only manages
the two GCP authentication types.

Monte Carlo reaches the agent and checks it again before saving the change, and re-enables
the agent if it was disabled. A successful response therefore always describes a working
agent. If the check fails, nothing about the agent changes. Sending only `name` skips the
check.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.gcp_collection_agent_out import GcpCollectionAgentOut
from montecarlo.models.gcp_collection_agent_patch import GcpCollectionAgentPatch
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    gcp_collection_agent_patch = montecarlo.GcpCollectionAgentPatch() # GcpCollectionAgentPatch | 

    try:
        # Update a GCP collection agent
        api_response = api_instance.update_gcp_collection_agent(collection_agent_id, gcp_collection_agent_patch)
        print("The response of CollectionAgentsApi->update_gcp_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->update_gcp_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 
 **gcp_collection_agent_patch** | [**GcpCollectionAgentPatch**](GcpCollectionAgentPatch.md)|  | 

### Return type

[**GcpCollectionAgentOut**](GcpCollectionAgentOut.md)

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

# **update_generic_collection_agent**
> GenericCollectionAgentOut update_generic_collection_agent(collection_agent_id, generic_collection_agent_patch)

Update a generic collection agent

Rename a generic collection agent.

The name is the only thing you can change. How the agent authenticates is managed through
its deployment's credentials, and where it runs is yours to manage. Sending an empty body
leaves the agent as it is and returns it.

An id that names an agent on another platform, or no agent in your account, returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import montecarlo
from montecarlo.models.generic_collection_agent_out import GenericCollectionAgentOut
from montecarlo.models.generic_collection_agent_patch import GenericCollectionAgentPatch
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
    api_instance = montecarlo.CollectionAgentsApi(api_client)
    collection_agent_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    generic_collection_agent_patch = montecarlo.GenericCollectionAgentPatch() # GenericCollectionAgentPatch | 

    try:
        # Update a generic collection agent
        api_response = api_instance.update_generic_collection_agent(collection_agent_id, generic_collection_agent_patch)
        print("The response of CollectionAgentsApi->update_generic_collection_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionAgentsApi->update_generic_collection_agent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_agent_id** | **UUID**|  | 
 **generic_collection_agent_patch** | [**GenericCollectionAgentPatch**](GenericCollectionAgentPatch.md)|  | 

### Return type

[**GenericCollectionAgentOut**](GenericCollectionAgentOut.md)

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

