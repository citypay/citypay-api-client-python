# citypay.OperationalApi

All URIs are relative to *https://api.citypay.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acl_check_request**](OperationalApi.md#acl_check_request) | **POST** /acl/check | ACL Check Request
[**list_merchants_request**](OperationalApi.md#list_merchants_request) | **GET** /merchants/{clientid} | List Merchants Request
[**ping_request**](OperationalApi.md#ping_request) | **POST** /ping | Ping Request


# **acl_check_request**
> AclCheckResponseModel acl_check_request(acl_check_request)

ACL Check Request

Allows the checking of IP addresses against configured ACLs. Requests can perform a lookup of addresses in subnets and services such as AWS or Azure to check that those addresses are listed in the ACLs. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import operational_api
from citypay.model.acl_check_response_model import AclCheckResponseModel
from citypay.model.error import Error
from citypay.model.acl_check_request import AclCheckRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.citypay.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = operational_api.OperationalApi(api_client)
    acl_check_request = AclCheckRequest(
        ip="8.8.8.8",
    ) # AclCheckRequest | 

    # example passing only required values which don't have defaults set
    try:
        # ACL Check Request
        api_response = api_instance.acl_check_request(acl_check_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling OperationalApi->acl_check_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_check_request** | [**AclCheckRequest**](AclCheckRequest.md)|  |

### Return type

[**AclCheckResponseModel**](AclCheckResponseModel.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response to the ACL Check request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merchants_request**
> ListMerchantsResponse list_merchants_request(clientid)

List Merchants Request

An operational request to list current merchants for a client.  ### Sorting  Sorting can be performed by include a query parameter i.e. `/merchants/?sort=merchantid`  Fields that can be sorted are `merchantid` or `name`. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import operational_api
from citypay.model.error import Error
from citypay.model.list_merchants_response import ListMerchantsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.citypay.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = operational_api.OperationalApi(api_client)
    clientid = "clientid_example" # str | The client id to return merchants for, specifying \"default\" will use the value in your api key.

    # example passing only required values which don't have defaults set
    try:
        # List Merchants Request
        api_response = api_instance.list_merchants_request(clientid)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling OperationalApi->list_merchants_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **str**| The client id to return merchants for, specifying \&quot;default\&quot; will use the value in your api key. |

### Return type

[**ListMerchantsResponse**](ListMerchantsResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of merchants that are configured against the client id. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_request**
> Acknowledgement ping_request(ping)

Ping Request

A ping request which performs a connection and authentication test to the CityPay API server. The request will return a standard Acknowledgement with a response code `044` to signify a successful ping.  The ping call is useful to confirm that you will be able to access  the API from behind any firewalls and that the permission model is granting access from your source. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import operational_api
from citypay.model.ping import Ping
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.citypay.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = operational_api.OperationalApi(api_client)
    ping = Ping(
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
    ) # Ping | 

    # example passing only required values which don't have defaults set
    try:
        # Ping Request
        api_response = api_instance.ping_request(ping)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling OperationalApi->ping_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ping** | [**Ping**](Ping.md)|  |

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of the ping request, returning on 044 response code on successful receipt of the ping request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

