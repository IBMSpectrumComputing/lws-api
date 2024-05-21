# lsf_client.LSFClusterApi

All URIs are relative to *http://localhost:8088/lsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_lsf_cli**](LSFClusterApi.md#execute_lsf_cli) | **POST** /v1/cluster/usercmd | Execute LSF command
[**get_cluster_info**](LSFClusterApi.md#get_cluster_info) | **GET** /v1/cluster | Get LSF cluster information


# **execute_lsf_cli**
> LSFCLIResult execute_lsf_cli(command, env=env)

Execute LSF command

Execute LSF command

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import lsf_client
from lsf_client.models.lsfcli_result import LSFCLIResult
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
    api_instance = lsf_client.LSFClusterApi(api_client)
    command = 'command_example' # str | 
    env = 'env_example' # str | A string of JSON Object which contains an array of environment variables' key-value pair to be used in LSF command (optional)

    try:
        # Execute LSF command
        api_response = api_instance.execute_lsf_cli(command, env=env)
        print("The response of LSFClusterApi->execute_lsf_cli:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSFClusterApi->execute_lsf_cli: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **command** | **str**|  | 
 **env** | **str**| A string of JSON Object which contains an array of environment variables&#39; key-value pair to be used in LSF command | [optional] 

### Return type

[**LSFCLIResult**](LSFCLIResult.md)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Execute command successfully |  -  |
**400** | Command not allowed |  -  |
**401** | Invalid session |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_info**
> LSFCluster get_cluster_info()

Get LSF cluster information

Get LSF cluster information

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import lsf_client
from lsf_client.models.lsf_cluster import LSFCluster
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
    api_instance = lsf_client.LSFClusterApi(api_client)

    try:
        # Get LSF cluster information
        api_response = api_instance.get_cluster_info()
        print("The response of LSFClusterApi->get_cluster_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LSFClusterApi->get_cluster_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LSFCluster**](LSFCluster.md)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get information successfully |  -  |
**401** | Invalid session |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

