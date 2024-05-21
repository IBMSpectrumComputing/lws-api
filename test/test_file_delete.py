import lsf_client, os, base64
from lsf_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8088/lsf
# See configuration.py for a list of all supported configuration parameters.
configuration = lsf_client.Configuration(
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
with lsf_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lsf_client.FileOperationsApi(api_client)
    file_path = base64.b64encode(b'/home/georgeg/test/job_input.inp').decode('utf-8') # str | base64 encoded file path
    #file_path='L2hvbWUvZ2VvcmdlZy9FTlYvZG9ja2VyLnRhci5nego='
    #file_path=file_path_b.decode('utf-8')
    print(file_path)

    try:
        # Download a single file
        api_response=api_instance.delete(file_path)
        print(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->download: %s\n" % e)

