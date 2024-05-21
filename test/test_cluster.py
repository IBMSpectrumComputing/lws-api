import os
import lsf_client
from lsf_client.models.lsfcli_result import LSFCLIResult
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
    api_instance = lsf_client.LSFClusterApi(api_client)
    command = 'bjobs -u all' # str |
    env = '' # str | A string of JSON Object which contains an array of environment variables' key-value

    try:
        # Execute LSF command
        api_response = api_instance.execute_lsf_cli(command, env=env)
        print("The response of LSFClusterApi->execute_lsf_cli:\n")
        print(api_response)
    except Exception as e:
        print("Exception when calling LSFClusterApi->execute_lsf_cli: %s\n" % e)

