# openapi_client.AuthenticationApi

All URIs are relative to *http://localhost:8088/lsf*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logon**](AuthenticationApi.md#logon) | **POST** /v1/auth/logon | User log on
[**logout**](AuthenticationApi.md#logout) | **POST** /v1/auth/logout | User log off


# **logon**
> Session logon(user=user)

User log on

User log on

### Example


```python
import openapi_client
from openapi_client.models.session import Session
from openapi_client.models.user import User
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8088/lsf"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AuthenticationApi(api_client)
    user = openapi_client.User() # User |  (optional)

    try:
        # User log on
        api_response = api_instance.logon(user=user)
        print("The response of AuthenticationApi->logon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logon: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User log on successfully |  -  |
**400** | Incorrect payload |  -  |
**403** | Forbidden user |  -  |
**404** | Cannot find LSF cluter |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> ReturnMessage logout()

User log off

User log off

### Example

* Api Key Authentication (LSF-Web-Service-authentication):

```python
import openapi_client
from openapi_client.models.return_message import ReturnMessage
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
    api_instance = openapi_client.AuthenticationApi(api_client)

    try:
        # User log off
        api_response = api_instance.logout()
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
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
**200** | User log off successfully |  -  |
**401** | Invalid session |  -  |
**500** | Internal service error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

