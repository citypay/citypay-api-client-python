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
> AuthResponse direct_c_res_auth_request(uuid)

Handles a CRes response from ACS, returning back the result of authorisation

Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData` value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to perform a `Direct Post` integration who wish to handle the challenge flow themselves. 

### Example


```python
import time
import citypay
from citypay.api import direct_post_api__
from citypay.model.error import Error
from citypay.model.auth_response import AuthResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)


# Enter a context with an instance of the API client
with citypay.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = direct_post_api__.DirectPostApi(api_client)
    uuid = "uuid_example" # str | An identifier used to track the CReq/CRes cycle.
    cres = "x90+vZ/7Ll05Vid/jPfQn8adw+4D/vRDUGT19kndW97Hfirbv66ycfSp8jNlvy7PkHbx44NEt3vo..." # str | The CRES from the ACS. (optional)
    three_ds_session_data = "three_ds_session_data_example" # str | The session data from the ACS. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Handles a CRes response from ACS, returning back the result of authorisation
        api_response = api_instance.direct_c_res_auth_request(uuid)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling DirectPostApi->direct_c_res_auth_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Handles a CRes response from ACS, returning back the result of authorisation
        api_response = api_instance.direct_c_res_auth_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)
        pprint(api_response)
    except citypay.ApiException as e:
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
> TokenisationResponseModel direct_c_res_tokenise_request(uuid)

Handles a CRes response from ACS, returning back a token for future authorisation

Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData` value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to perform a `Direct Post` integration who wish to handle the challenge flow themselves. 

### Example


```python
import time
import citypay
from citypay.api import direct_post_api__
from citypay.model.tokenisation_response_model import TokenisationResponseModel
from citypay.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)


# Enter a context with an instance of the API client
with citypay.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = direct_post_api__.DirectPostApi(api_client)
    uuid = "uuid_example" # str | An identifier used to track the CReq/CRes cycle.
    cres = "x90+vZ/7Ll05Vid/jPfQn8adw+4D/vRDUGT19kndW97Hfirbv66ycfSp8jNlvy7PkHbx44NEt3vo..." # str | The CRES from the ACS. (optional)
    three_ds_session_data = "three_ds_session_data_example" # str | The session data from the ACS. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Handles a CRes response from ACS, returning back a token for future authorisation
        api_response = api_instance.direct_c_res_tokenise_request(uuid)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling DirectPostApi->direct_c_res_tokenise_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Handles a CRes response from ACS, returning back a token for future authorisation
        api_response = api_instance.direct_c_res_tokenise_request(uuid, cres=cres, three_ds_session_data=three_ds_session_data)
        pprint(api_response)
    except citypay.ApiException as e:
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

Used to initiate a direct post request transaction flow.  <pre class=\"inline-code language-bash\"> <code> curl https://api.citypay.com/v6/direct?cp-domain-key=n834ytqp84y... \\  -d \"amount=7500&identifier=example_trans&cardnumber=4000000000000002&expmonth=9&expyear=2028&bill_to_postcode=L1+7ZW </code> </pre>. 

### Example

* Api Key Authentication (cp-api-key):
* Api Key Authentication (cp-domain-key):

```python
import time
import citypay
from citypay.api import direct_post_api__
from citypay.model.error import Error
from citypay.model.auth_response import AuthResponse
from citypay.model.direct_post_request import DirectPostRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_post_api__.DirectPostApi(api_client)
    direct_post_request = DirectPostRequest(
        amount=3600,
        avs_postcode_policy="avs_postcode_policy_example",
        bill_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        cardnumber="4000 0000 0000 0002",
        csc="12",
        csc_policy="csc_policy_example",
        currency="GBP",
        duplicate_policy="duplicate_policy_example",
        expmonth=9,
        expyear=2025,
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
        mac="3896FBC43674AF59478DAF7F546FA4D4CB89981A936E6AAE997E43B55DF6C39D",
        match_avsa="match_avsa_example",
        name_on_card="MR NE BODY",
        nonce="0123456789ABCDEF",
        redirect_failure="https://pay.mystore.com/continue_failure",
        redirect_success="https://pay.mystore.com/continue_success",
        ship_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        threedsecure=ThreeDSecure(
            accept_headers="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            browser_color_depth="browser_color_depth_example",
            browser_ip="browser_ip_example",
            browser_java_enabled="browser_java_enabled_example",
            browser_language="browser_language_example",
            browser_screen_height="browser_screen_height_example",
            browser_screen_width="browser_screen_width_example",
            browser_tz="browser_tz_example",
            cp_bx="FjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAx...",
            downgrade1=True,
            merchant_termurl="https://mysite.com/acs/return",
            tds_policy="tds_policy_example",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        ),
        trans_info="trans_info_example",
        trans_type="trans_type_example",
    ) # DirectPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Direct Post Auth Request
        api_response = api_instance.direct_post_auth_request(direct_post_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling DirectPostApi->direct_post_auth_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_post_request** | [**DirectPostRequest**](DirectPostRequest.md)|  |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key), [cp-domain-key](../README.md#cp-domain-key)

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

Used to initiate a direct post request transaction flow.  <pre class=\"inline-code language-bash\"> <code> curl https://api.citypay.com/v6/direct?cp-domain-key=n834ytqp84y... \\  -d \"amount=7500&identifier=example_trans&cardnumber=4000000000000002&expmonth=9&expyear=2028&bill_to_postcode=L1+7ZW </code> </pre>. 

### Example

* Api Key Authentication (cp-api-key):
* Api Key Authentication (cp-domain-key):

```python
import time
import citypay
from citypay.api import direct_post_api__
from citypay.model.error import Error
from citypay.model.auth_response import AuthResponse
from citypay.model.direct_post_request import DirectPostRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_post_api__.DirectPostApi(api_client)
    direct_post_request = DirectPostRequest(
        amount=3600,
        avs_postcode_policy="avs_postcode_policy_example",
        bill_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        cardnumber="4000 0000 0000 0002",
        csc="12",
        csc_policy="csc_policy_example",
        currency="GBP",
        duplicate_policy="duplicate_policy_example",
        expmonth=9,
        expyear=2025,
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
        mac="3896FBC43674AF59478DAF7F546FA4D4CB89981A936E6AAE997E43B55DF6C39D",
        match_avsa="match_avsa_example",
        name_on_card="MR NE BODY",
        nonce="0123456789ABCDEF",
        redirect_failure="https://pay.mystore.com/continue_failure",
        redirect_success="https://pay.mystore.com/continue_success",
        ship_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        threedsecure=ThreeDSecure(
            accept_headers="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            browser_color_depth="browser_color_depth_example",
            browser_ip="browser_ip_example",
            browser_java_enabled="browser_java_enabled_example",
            browser_language="browser_language_example",
            browser_screen_height="browser_screen_height_example",
            browser_screen_width="browser_screen_width_example",
            browser_tz="browser_tz_example",
            cp_bx="FjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAx...",
            downgrade1=True,
            merchant_termurl="https://mysite.com/acs/return",
            tds_policy="tds_policy_example",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        ),
        trans_info="trans_info_example",
        trans_type="trans_type_example",
    ) # DirectPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Direct Post Tokenise Request
        api_response = api_instance.direct_post_tokenise_request(direct_post_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling DirectPostApi->direct_post_tokenise_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_post_request** | [**DirectPostRequest**](DirectPostRequest.md)|  |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key), [cp-domain-key](../README.md#cp-domain-key)

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

Perform a request for authorisation for a previously generated token. This flow will return an authorisation response stating that the transaction was approved or declined. 

### Example

* Api Key Authentication (cp-api-key):
* Api Key Authentication (cp-domain-key):

```python
import time
import citypay
from citypay.api import direct_post_api__
from citypay.model.error import Error
from citypay.model.auth_response import AuthResponse
from citypay.model.direct_token_auth_request import DirectTokenAuthRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Configure API key authorization: cp-domain-key
configuration.api_key['cp-domain-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-domain-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = direct_post_api__.DirectPostApi(api_client)
    direct_token_auth_request = DirectTokenAuthRequest(
        nonce="0123456789ABCDEF",
        redirect_failure="https://pay.mystore.com/continue_failure",
        redirect_success="https://pay.mystore.com/continue_success",
        token="ctPCAPyNyCkx3Ry8wGyv8khC3ch2hUSB3Db..Qzr",
    ) # DirectTokenAuthRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Direct Post Token Request
        api_response = api_instance.token_request(direct_token_auth_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling DirectPostApi->token_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **direct_token_auth_request** | [**DirectTokenAuthRequest**](DirectTokenAuthRequest.md)|  |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key), [cp-domain-key](../README.md#cp-domain-key)

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

