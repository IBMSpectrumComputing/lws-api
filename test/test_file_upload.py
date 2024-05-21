import lsf_client, os
from lsf_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080/lsf
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
    #f = open("job_input.inp", "r")
    file = 'job_input.inp' # bytearray |
    path = '/home/georgeg/test' # str |  (optional)
    compress = '' # str | A filename extension, if specified, the uploaded file will be automatically de-compressed by related command (optional)

    try:
        # Upload a single file
        api_instance.upload(file, path=path, compress=compress)
    except Exception as e:
        print("Exception when calling FileOperationsApi->upload: %s\n" % e)

