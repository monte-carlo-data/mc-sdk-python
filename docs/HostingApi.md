# pycarlo2.HostingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hosting_domains**](HostingApi.md#get_hosting_domains) | **GET** /api/v2/hosting/domains | Get the hosting domains
[**get_hosting_network**](HostingApi.md#get_hosting_network) | **GET** /api/v2/hosting/network | Get the hosting network
[**get_hosting_private_link**](HostingApi.md#get_hosting_private_link) | **GET** /api/v2/hosting/private-link | Get the hosting private link details


# **get_hosting_domains**
> HostingDomainsOut get_hosting_domains()

Get the hosting domains

Get the URLs your Monte Carlo instance serves.

Some integrations need one of these URLs before they can be set up. dbt Cloud, for
example, issues a webhook secret only after you give it `dbt_cloud_webhook_url`.

Every caller in an instance gets the same values.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.hosting_domains_out import HostingDomainsOut
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
    api_instance = pycarlo2.HostingApi(api_client)

    try:
        # Get the hosting domains
        api_response = api_instance.get_hosting_domains()
        print("The response of HostingApi->get_hosting_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_hosting_domains: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HostingDomainsOut**](HostingDomainsOut.md)

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

# **get_hosting_network**
> HostingNetworkOut get_hosting_network(instance_region=instance_region)

Get the hosting network

Get the public IP addresses one region of your Monte Carlo instance connects from.

Allowlist them where Monte Carlo reaches your resources over the internet. Asking for the
secondary region of an instance without disaster recovery returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.hosting_network_out import HostingNetworkOut
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
    api_instance = pycarlo2.HostingApi(api_client)
    instance_region = pycarlo2.InstanceRegion() # InstanceRegion | The region of your Monte Carlo instance to read. `primary`, the default, is the region serving your instance, which is the recovery region during a failover. `secondary` is the disaster recovery region, and only an instance with disaster recovery has one. With disaster recovery, read both and allow both, so access keeps working after a failover. During a failover both read the recovery region, so applying your policies then drops the original primary region until you apply them again after failing back. (optional)

    try:
        # Get the hosting network
        api_response = api_instance.get_hosting_network(instance_region=instance_region)
        print("The response of HostingApi->get_hosting_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_hosting_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_region** | [**InstanceRegion**](.md)| The region of your Monte Carlo instance to read. &#x60;primary&#x60;, the default, is the region serving your instance, which is the recovery region during a failover. &#x60;secondary&#x60; is the disaster recovery region, and only an instance with disaster recovery has one. With disaster recovery, read both and allow both, so access keeps working after a failover. During a failover both read the recovery region, so applying your policies then drops the original primary region until you apply them again after failing back. | [optional] 

### Return type

[**HostingNetworkOut**](HostingNetworkOut.md)

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

# **get_hosting_private_link**
> HostingPrivateLinkOut get_hosting_private_link(instance_region=instance_region)

Get the hosting private link details

Get how one region of your Monte Carlo instance reaches your AWS resources privately.

Use the VPC endpoint of the region you deploy to in an `aws:SourceVpce` condition, and the
private subnet CIDRs in an allowlist. Asking for the secondary region of an instance
without disaster recovery returns 404.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.hosting_private_link_out import HostingPrivateLinkOut
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
    api_instance = pycarlo2.HostingApi(api_client)
    instance_region = pycarlo2.InstanceRegion() # InstanceRegion | The region of your Monte Carlo instance to read. `primary`, the default, is the region serving your instance, which is the recovery region during a failover. `secondary` is the disaster recovery region, and only an instance with disaster recovery has one. With disaster recovery, read both and allow both, so access keeps working after a failover. During a failover both read the recovery region, so applying your policies then drops the original primary region until you apply them again after failing back. (optional)

    try:
        # Get the hosting private link details
        api_response = api_instance.get_hosting_private_link(instance_region=instance_region)
        print("The response of HostingApi->get_hosting_private_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostingApi->get_hosting_private_link: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_region** | [**InstanceRegion**](.md)| The region of your Monte Carlo instance to read. &#x60;primary&#x60;, the default, is the region serving your instance, which is the recovery region during a failover. &#x60;secondary&#x60; is the disaster recovery region, and only an instance with disaster recovery has one. With disaster recovery, read both and allow both, so access keeps working after a failover. During a failover both read the recovery region, so applying your policies then drops the original primary region until you apply them again after failing back. | [optional] 

### Return type

[**HostingPrivateLinkOut**](HostingPrivateLinkOut.md)

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

