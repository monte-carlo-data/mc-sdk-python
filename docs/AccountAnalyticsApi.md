# pycarlo2.AccountAnalyticsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_analytics_catalog**](AccountAnalyticsApi.md#get_account_analytics_catalog) | **GET** /api/v2/account-analytics/catalog | List metrics, or the dimensions that work with chosen metrics
[**get_account_analytics_docs**](AccountAnalyticsApi.md#get_account_analytics_docs) | **GET** /api/v2/account-analytics/docs | List the Analytics API docs, or read pages
[**query_account_analytics**](AccountAnalyticsApi.md#query_account_analytics) | **POST** /api/v2/account-analytics/query | Query metrics


# **get_account_analytics_catalog**
> CatalogOut get_account_analytics_catalog(metrics=metrics, search=search)

List metrics, or the dimensions that work with chosen metrics

List the metrics you can query, or the dimensions that work with the metrics you chose.

Without `metrics`, the answer lists every metric you can query, with its label and
description. A metric marked `requires_metric_time` answers only when the query groups by
`metric_time`.

With `metrics`, the answer lists the dimensions you can group and filter all of them by.
A time dimension lists its grains: `metric_time` with `week` is queried as
`metric_time__week`. Per-domain metrics, such as `domain_coverage_rate`, count an asset
once in each domain it belongs to, so the domains do not add up to the account total.
Metrics can be grouped only by dimensions they share: ask with `metrics` first.

`search` keeps only the items whose name, label or description contains a text, ignoring
case. The unfiltered list of metrics is long. Fields without a value, such as `type` for a
metric, are left out.

An unknown metric is refused with a 422 that says why. Its `detail` names metrics and
fields; `extra.user_message` says it in words to show a person. Requires dashboard access.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.catalog_out import CatalogOut
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
    api_instance = pycarlo2.AccountAnalyticsApi(api_client)
    metrics = 'metrics_example' # str | Comma-separated metric names, such as `coverage_rate,covered_assets`. With them, the answer lists the dimensions all of them can be grouped and filtered by. Without them, it lists every metric. Send the names in one parameter: only the last of a repeated parameter is read. (optional)
    search = 'search_example' # str | Keeps the metrics, or the dimensions, whose name, label or description contains this text, ignoring case, such as `incident`. (optional)

    try:
        # List metrics, or the dimensions that work with chosen metrics
        api_response = api_instance.get_account_analytics_catalog(metrics=metrics, search=search)
        print("The response of AccountAnalyticsApi->get_account_analytics_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountAnalyticsApi->get_account_analytics_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics** | **str**| Comma-separated metric names, such as &#x60;coverage_rate,covered_assets&#x60;. With them, the answer lists the dimensions all of them can be grouped and filtered by. Without them, it lists every metric. Send the names in one parameter: only the last of a repeated parameter is read. | [optional] 
 **search** | **str**| Keeps the metrics, or the dimensions, whose name, label or description contains this text, ignoring case, such as &#x60;incident&#x60;. | [optional] 

### Return type

[**CatalogOut**](CatalogOut.md)

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_analytics_docs**
> DocsOut get_account_analytics_docs(slug=slug)

List the Analytics API docs, or read pages

List the pages of the Analytics API docs, or read some.

Without `slug`, the answer lists every page with its slug, title, summary and parent page,
and the prompt of each dashboard example.
With `slug`, one slug or several comma-separated, it returns those pages with their bodies
as Markdown, in that order. The pages are the ones
published at docs.getmontecarlo.com: how to query, the data catalog, the dashboard examples
and the dashboard style. `doc:<slug>` links in a body name other pages.

An unknown slug is refused with a 422 `docs_page_not_found`. Requires dashboard access.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.docs_out import DocsOut
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
    api_instance = pycarlo2.AccountAnalyticsApi(api_client)
    slug = 'slug_example' # str | The pages to read: one slug, or up to 10 comma-separated, such as `analytics-api-dashboard-style,analytics-api-dimensions`. The answer has them in that order. Without it, the answer lists every page without its body. (optional)

    try:
        # List the Analytics API docs, or read pages
        api_response = api_instance.get_account_analytics_docs(slug=slug)
        print("The response of AccountAnalyticsApi->get_account_analytics_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountAnalyticsApi->get_account_analytics_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| The pages to read: one slug, or up to 10 comma-separated, such as &#x60;analytics-api-dashboard-style,analytics-api-dimensions&#x60;. The answer has them in that order. Without it, the answer lists every page without its body. | [optional] 

### Return type

[**DocsOut**](DocsOut.md)

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
**422** | Unprocessable Entity |  -  |
**429** | Too Many Requests |  -  |
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_account_analytics**
> MetricsQueryOut query_account_analytics(metrics_query)

Query metrics

Answer one question about your account: metrics, grouped by dimensions, with filters.

Names come from `get_account_analytics_catalog`. A dimension a metric cannot reach is
refused with a 422, and the message lists the dimensions that work. So is a metric that
needs `metric_time` in `group_by` when the query has none. A refusal's `detail` names
metrics and fields; `extra.user_message` says it in words to show a person.

The answer has one row per combination of `group_by` values, at most `limit` rows. `limit`
defaults to 1,000 and is at most 10,000. `rows_returned` counts the rows in the answer and
`total_rows` the rows the query matched: read them instead of counting `rows`. `truncated`
says when more rows matched, and then `warnings` says how to narrow the query. Add filters,
narrow the time range or group by fewer dimensions. `warnings` is empty when there is
nothing to note. Every answer carries `data_as_of`, the
time the data in the answer reflects. The data is refreshed periodically, not in real time,
so later changes are not in it.

Filters take `in`, `not_in`, `gte`, `lte`, `gt`, `lt`, `contains` and `is_null`. `not_in`
keeps rows where the dimension is empty. `is_null` takes `true` or `false` and selects, or
drops, those rows. `gte`, `lte`, `gt`, `lt` and `in` never match an empty dimension.
`contains` takes a text and matches it anywhere in the value, ignoring case. A value in
`in` cannot be null: use `is_null`.

Groups overlap. A table in two domains counts in both, so per-domain numbers do not add up
to the account total: ask for the total without a domain grouping. History covers the 13
full calendar months before the current month and the current month to date. Some metrics
keep less.

If you can see only some domains, the answer covers only those domains. Alert, event and
monitor metrics and monitor credits then answer only in their `monitor_domain_` versions,
such as `monitor_domain_incident_count`. A metric that cannot be split by domain is refused
for you, and so are monitor run metrics. Grouping or filtering by a single user, such as
`user__user_email`, needs the Account Owner role.
Account-level counts are available to everyone with dashboard access.

This operation changes nothing. It is a `POST` because the query is a structured body.

### Example

* Bearer Authentication (GatewayAuth):

```python
import pycarlo2
from pycarlo2.models.metrics_query import MetricsQuery
from pycarlo2.models.metrics_query_out import MetricsQueryOut
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
    api_instance = pycarlo2.AccountAnalyticsApi(api_client)
    metrics_query = pycarlo2.MetricsQuery() # MetricsQuery | 

    try:
        # Query metrics
        api_response = api_instance.query_account_analytics(metrics_query)
        print("The response of AccountAnalyticsApi->query_account_analytics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountAnalyticsApi->query_account_analytics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metrics_query** | [**MetricsQuery**](MetricsQuery.md)|  | 

### Return type

[**MetricsQueryOut**](MetricsQueryOut.md)

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
**503** | Service Unavailable |  -  |
**401** | Authentication credentials are missing or invalid. |  -  |
**403** | The request was authenticated, but the caller is not allowed to perform this operation. Read &#x60;code&#x60; to tell the reasons apart: &#x60;account_frozen&#x60; means the account is paused, rather than that the caller lacks permission. |  -  |
**500** | An unexpected error prevented the request from being processed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

