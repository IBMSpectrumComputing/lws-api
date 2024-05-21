# lsf_client.PingApi

All URIs are relative to *http://localhost:8088/lsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](PingApi.md#ping) | **GET** /v1/ping | Ping service


# **ping**
> ReturnMessage ping()

Ping service

Ping service availability

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import lsf_client
from lsf_client.models.return_message import ReturnMessage
from lsf_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = lsf_client.Configuration(
    host = "http://localhost:8088/lsf"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: LSF-Web-Service-authentication
configuration.api_key['LSF-Web-Service-authentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['LSF-Web-Service-authentication'] = 'Bearer'

# Enter a context with an instance of the API client
with lsf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lsf_client.PingApi(api_client)

    try:
        # Ping service
        api_response = api_instance.ping()
        print("The response of PingApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PingApi->ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ReturnMessage**](ReturnMessage.md)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ping success |  -  |
**401** | Invalid session |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

