import openapi_client, os
from openapi_client.models.tree_node import TreeNode
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    #host = "http://fp14-rh9x-1:8088/lsf",
    host = "https://fp14-rh9x-1:8448/lsf",
    ssl_ca_cert = "cacert.pem"
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
    path = '/home/georgeg/ENV' # str |  (optional)

    try:
        # List file under a specific path
        api_response = api_instance.file_tree(path=path)
        print("The response of FileOperationsApi->file_tree:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_tree: %s\n" % e)

