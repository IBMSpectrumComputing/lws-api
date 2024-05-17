# openapi_client.FileOperationsApi

All URIs are relative to *http://localhost:8088/lsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](FileOperationsApi.md#delete) | **DELETE** /v1/files/{filePath} | Delete file by a specific path
[**download**](FileOperationsApi.md#download) | **GET** /v1/files/{filePath} | Download a single file
[**file_tree**](FileOperationsApi.md#file_tree) | **GET** /v1/files | List file under a specific path
[**list_repos**](FileOperationsApi.md#list_repos) | **GET** /v1/repos | List repositories
[**upload**](FileOperationsApi.md#upload) | **POST** /v1/files | Upload a single file


# **delete**
> delete(file_path)

Delete file by a specific path

Delete file by a specific path, wildcard '*' and '?' are both supported

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FileOperationsApi(api_client)
    file_path = 'file_path_example' # str | base64 encoded file path

    try:
        # Delete file by a specific path
        api_instance.delete(file_path)
    except Exception as e:
        print("Exception when calling FileOperationsApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| base64 encoded file path | 

### Return type

void (empty response body)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete file successfully |  -  |
**400** | Cannot delete the file |  -  |
**401** | Invalid session |  -  |
**403** | Permission denied |  -  |
**404** | File not found |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> bytearray download(file_path)

Download a single file

Download a single file

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FileOperationsApi(api_client)
    file_path = 'file_path_example' # str | base64 encoded file path

    try:
        # Download a single file
        api_response = api_instance.download(file_path)
        print("The response of FileOperationsApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| base64 encoded file path | 

### Return type

**bytearray**

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download file successfully |  -  |
**400** | Cannot download a directory |  -  |
**401** | Invalid session |  -  |
**403** | Permission denied |  -  |
**404** | File not found |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_tree**
> TreeNode file_tree(path=path)

List file under a specific path

List file under a specific path

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.models.tree_node import TreeNode
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FileOperationsApi(api_client)
    path = 'path_example' # str |  (optional)

    try:
        # List file under a specific path
        api_response = api_instance.file_tree(path=path)
        print("The response of FileOperationsApi->file_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_tree: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**|  | [optional] 

### Return type

[**TreeNode**](TreeNode.md)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List file successfully |  -  |
**401** | Invalid session |  -  |
**403** | Permission denied |  -  |
**404** | File not found |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repos**
> Repositories list_repos()

List repositories

List repositories to current logged in user

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.models.repositories import Repositories
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FileOperationsApi(api_client)

    try:
        # List repositories
        api_response = api_instance.list_repos()
        print("The response of FileOperationsApi->list_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->list_repos: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Repositories**](Repositories.md)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Download file successfully |  -  |
**401** | Invalid session |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload**
> upload(file, path=path, compress=compress)

Upload a single file

Upload a single file

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.FileOperationsApi(api_client)
    file = None # bytearray | 
    path = 'path_example' # str |  (optional)
    compress = 'compress_example' # str | A filename extension, if specified, the uploaded file will be automatically de-compressed by related command (optional)

    try:
        # Upload a single file
        api_instance.upload(file, path=path, compress=compress)
    except Exception as e:
        print("Exception when calling FileOperationsApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | 
 **path** | **str**|  | [optional] 
 **compress** | **str**| A filename extension, if specified, the uploaded file will be automatically de-compressed by related command | [optional] 

### Return type

void (empty response body)

### Authorization

[LSF-Web-Service-authentication](../README.md#LSF-Web-Service-authentication)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Upload file successfully |  -  |
**401** | Invalid session |  -  |
**403** | Permission denied |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

