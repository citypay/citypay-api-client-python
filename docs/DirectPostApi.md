# citypay.DirectPostApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**direct_c_res_auth_request**](DirectPostApi.md#direct_c_res_auth_request) | **POST** /direct/cres/auth/{uuid} | Handles a CRes response from ACS, returning back the result of authorisation
[**direct_c_res_tokenise_request**](DirectPostApi.md#direct_c_res_tokenise_request) | **POST** /direct/cres/tokenise/{uuid} | Handles a CRes response from ACS, returning back a token for future authorisation
[**direct_post_auth_request**](DirectPostApi.md#direct_post_auth_request) | **POST** /direct/auth | Direct Post Auth Request
[**direct_post_tokenise_request**](DirectPostApi.md#direct_post_tokenise_request) | **POST** /direct/tokenise | Direct Post Tokenise Request
[**token_request**](DirectPostApi.md#token_request) | **POST** /direct/token | Direct Post Token Request


# **direct_c_res_auth_request**
> AuthResponse direct_c_res_auth_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)

Handles a CRes response from ACS, returning back the result of authorisation

Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData`
value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to
perform a `Direct Post` integration who wish to handle the challenge flow themselves.


### Example


```python
import time
import os
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)


# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.DirectPostApi(api_client)
    uuid = 'uuid_example' # str | An identifier used to track the CReq/CRes cycle.
    cres = 'cres_example' # str | The CRES from the ACS. (optional)
    three_ds_session_data = 'three_ds_session_data_example' # str | The session data from the ACS. (optional)

    try:
        # Handles a CRes response from ACS, returning back the result of authorisation
        api_response = api_instance.direct_c_res_auth_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)
        print("The response of DirectPostApi->direct_c_res_auth_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectPostApi->direct_c_res_auth_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| An identifier used to track the CReq/CRes cycle. | 
 **cres** | **str**| The CRES from the ACS. | [optional] 
 **three_ds_session_data** | **str**| The session data from the ACS. | [optional] 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml, application/x-www-form-urlencoded

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of a successful tokenisation or authorisation process if called via an XHR method. |  -  |
**303** | Redirect. A result of a successful tokenisation or authorisation process, redirecting to the success URL. |  -  |
**307** | Redirect. A result of a non-successful tokenisation or authorisation process, redirecting to the failure URL. |  -  |
**401** | Unauthorized. No domain key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The domain key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**406** | Not Acceptable. Should the incoming data not be validly determined. |  -  |
**412** | Bad Request. Should the incoming data not be validly determined and an error code results. |  -  |
**500** | Server Error. Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_c_res_tokenise_request**
> TokenisationResponseModel direct_c_res_tokenise_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)

Handles a CRes response from ACS, returning back a token for future authorisation

Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData`
value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to
perform a `Direct Post` integration who wish to handle the challenge flow themselves.


### Example


```python
import time
import os
import citypay
from citypay.models.tokenisation_response_model import TokenisationResponseModel
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)


# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.DirectPostApi(api_client)
    uuid = 'uuid_example' # str | An identifier used to track the CReq/CRes cycle.
    cres = 'cres_example' # str | The CRES from the ACS. (optional)
    three_ds_session_data = 'three_ds_session_data_example' # str | The session data from the ACS. (optional)

    try:
        # Handles a CRes response from ACS, returning back a token for future authorisation
        api_response = api_instance.direct_c_res_tokenise_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)
        print("The response of DirectPostApi->direct_c_res_tokenise_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectPostApi->direct_c_res_tokenise_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| An identifier used to track the CReq/CRes cycle. | 
 **cres** | **str**| The CRES from the ACS. | [optional] 
 **three_ds_session_data** | **str**| The session data from the ACS. | [optional] 

### Return type

[**TokenisationResponseModel**](TokenisationResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml, application/x-www-form-urlencoded

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of a successful tokenisation or authorisation process if called via an XHR method. |  -  |
**303** | Redirect. A result of a successful tokenisation or authorisation process, redirecting to the success URL. |  -  |
**307** | Redirect. A result of a non-successful tokenisation or authorisation process, redirecting to the failure URL. |  -  |
**401** | Unauthorized. No domain key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The domain key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**406** | Not Acceptable. Should the incoming data not be validly determined. |  -  |
**412** | Bad Request. Should the incoming data not be validly determined and an error code results. |  -  |
**500** | Server Error. Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_post_auth_request**
> AuthResponse direct_post_auth_request(direct_post_request)

Direct Post Auth Request

Used to initiate a direct post request transaction flow.


### Example

* Api Key Authentication (cp-domain-key):
* Api Key Authentication (cp-api-key):

```python
import time
import os
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.models.direct_post_request import DirectPostRequest
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.DirectPostApi(api_client)
    direct_post_request = citypay.DirectPostRequest() # DirectPostRequest | 

    try:
        # Direct Post Auth Request
        api_response = api_instance.direct_post_auth_request(direct_post_request)
        print("The response of DirectPostApi->direct_post_auth_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectPostApi->direct_post_auth_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_post_request** | [**DirectPostRequest**](DirectPostRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-domain-key](../README.md#cp-domain-key), [cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/xml
 - **Accept**: application/json, application/xml, application/x-www-form-urlencoded, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of a successful tokenisation or authorisation process if called via an XHR method. |  -  |
**303** | Redirect. A result of a successful tokenisation or authorisation process, redirecting to the success URL. |  -  |
**307** | Redirect. A result of a non-successful tokenisation or authorisation process, redirecting to the failure URL. |  -  |
**401** | Unauthorized. No domain key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The domain key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**406** | Not Acceptable. Should the incoming data not be validly determined. |  -  |
**412** | Bad Request. Should the incoming data not be validly determined and an error code results. |  -  |
**500** | Server Error. Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **direct_post_tokenise_request**
> AuthResponse direct_post_tokenise_request(direct_post_request)

Direct Post Tokenise Request

Used to initiate a direct post request transaction flow.


### Example

* Api Key Authentication (cp-domain-key):
* Api Key Authentication (cp-api-key):

```python
import time
import os
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.models.direct_post_request import DirectPostRequest
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.DirectPostApi(api_client)
    direct_post_request = citypay.DirectPostRequest() # DirectPostRequest | 

    try:
        # Direct Post Tokenise Request
        api_response = api_instance.direct_post_tokenise_request(direct_post_request)
        print("The response of DirectPostApi->direct_post_tokenise_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectPostApi->direct_post_tokenise_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_post_request** | [**DirectPostRequest**](DirectPostRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-domain-key](../README.md#cp-domain-key), [cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/xml
 - **Accept**: application/json, application/xml, application/x-www-form-urlencoded, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of a successful tokenisation or authorisation process if called via an XHR method. |  -  |
**303** | Redirect. A result of a successful tokenisation or authorisation process, redirecting to the success URL. |  -  |
**307** | Redirect. A result of a non-successful tokenisation or authorisation process, redirecting to the failure URL. |  -  |
**401** | Unauthorized. No domain key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The domain key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**406** | Not Acceptable. Should the incoming data not be validly determined. |  -  |
**412** | Bad Request. Should the incoming data not be validly determined and an error code results. |  -  |
**500** | Server Error. Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_request**
> AuthResponse token_request(direct_token_auth_request)

Direct Post Token Request

Perform a request for authorisation for a previously generated token. This flow will return an authorisation
response stating that the transaction was approved or declined.


### Example

* Api Key Authentication (cp-domain-key):
* Api Key Authentication (cp-api-key):

```python
import time
import os
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.models.direct_token_auth_request import DirectTokenAuthRequest
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.DirectPostApi(api_client)
    direct_token_auth_request = citypay.DirectTokenAuthRequest() # DirectTokenAuthRequest | 

    try:
        # Direct Post Token Request
        api_response = api_instance.token_request(direct_token_auth_request)
        print("The response of DirectPostApi->token_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DirectPostApi->token_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_token_auth_request** | [**DirectTokenAuthRequest**](DirectTokenAuthRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-domain-key](../README.md#cp-domain-key), [cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/xml
 - **Accept**: application/json, application/xml, application/x-www-form-urlencoded, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of an authorisation process if called via an XHR method. |  -  |
**303** | Redirect. A result of a successful tokenisation or authorisation process, redirecting to the success URL. |  -  |
**307** | Redirect. A result of a non-successful tokenisation or authorisation process, redirecting to the failure URL. |  -  |
**401** | Unauthorized. No domain key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The domain key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**406** | Not Acceptable. Should the incoming data not be validly determined. |  -  |
**412** | Bad Request. Should the incoming data not be validly determined and an error code results. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

