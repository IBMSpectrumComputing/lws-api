import openapi_client
from openapi_client.models.user import User
from openapi_client.models.session import Session
from openapi_client.rest import ApiException
from pprint import pprint

json = '{"name":"georgeg", "pass":"georgeg"}'
user_instance = User.from_json(json)
configuration = openapi_client.Configuration(
    #host = "http://fp14-rh9x-1:8088/lsf",
    #ssl_ca_cert = None
    host = "https://fp14-rh9x-1:8448/lsf",
    ssl_ca_cert = "cacert.pem"
)
print(configuration.host)
print(user_instance)
with openapi_client.ApiClient(configuration) as api_client:
    api_instance = openapi_client.AuthenticationApi(api_client)
    try:
        api_response = api_instance.logon(user=user_instance)
        print("The response of AuthenticationApi->logon:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logon: %s\n" % e)

