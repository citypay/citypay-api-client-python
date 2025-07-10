# citypay.AuthorisationAndPaymentApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorisation_request**](AuthorisationAndPaymentApi.md#authorisation_request) | **POST** /v6/authorise | Authorisation
[**bin_range_lookup_request**](AuthorisationAndPaymentApi.md#bin_range_lookup_request) | **POST** /v6/bin | Bin Lookup
[**c_res_request**](AuthorisationAndPaymentApi.md#c_res_request) | **POST** /v6/cres | CRes
[**capture_request**](AuthorisationAndPaymentApi.md#capture_request) | **POST** /v6/capture | Capture
[**card_tokenisation_request**](AuthorisationAndPaymentApi.md#card_tokenisation_request) | **POST** /v6/tokenise | Card Tokenisation Request
[**refund_request**](AuthorisationAndPaymentApi.md#refund_request) | **POST** /v6/refund | Refund
[**retrieval_request**](AuthorisationAndPaymentApi.md#retrieval_request) | **POST** /v6/retrieve | Transaction Retrieval
[**verification_request**](AuthorisationAndPaymentApi.md#verification_request) | **POST** /v6/verify | Verification
[**void_request**](AuthorisationAndPaymentApi.md#void_request) | **POST** /v6/void | Void


# **authorisation_request**
> Decision authorisation_request(auth_request)

Authorisation

Performs a request for authorisation for a card payment request.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.auth_request import AuthRequest
from citypay.models.decision import Decision
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    auth_request = citypay.AuthRequest() # AuthRequest | 

    try:
        # Authorisation
        api_response = api_instance.authorisation_request(auth_request)
        print("The response of AuthorisationAndPaymentApi->authorisation_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->authorisation_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**Decision**](Decision.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A decision made by the result of processing. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bin_range_lookup_request**
> Bin bin_range_lookup_request(bin_lookup)

Bin Lookup

A bin range lookup service can be used to check what a card is, as seen by the gateway. Each card number's 
leading digits help to identify who

0. the card scheme is such as Visa, MasterCard or American Express 
1. the issuer of the card, such as the bank
2. it's country of origin
3. it's currency of origin

Our gateway has 450 thousand possible bin ranges and uses a number of algorithms to determine the likelihood of the bin
data. The request requires a bin value of between 6 and 12 digits. The more digits provided may ensure a more accurate
result.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.bin import Bin
from citypay.models.bin_lookup import BinLookup
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    bin_lookup = citypay.BinLookup() # BinLookup | 

    try:
        # Bin Lookup
        api_response = api_instance.bin_range_lookup_request(bin_lookup)
        print("The response of AuthorisationAndPaymentApi->bin_range_lookup_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->bin_range_lookup_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bin_lookup** | [**BinLookup**](BinLookup.md)|  | 

### Return type

[**Bin**](Bin.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of the bin lookup request returning a bin object determined by the gateway service. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_res_request**
> AuthResponse c_res_request(c_res_auth_request)

CRes

The CRes request performs authorisation processing once a challenge request has been completed
with an Authentication Server (ACS). This challenge response contains confirmation that will
allow the API systems to return an authorisation response based on the result. Our systems will 
know out of band via an `RReq` call by the ACS to notify us if the liability shift has been issued.

Any call to the CRes operation will require a previous authorisation request and cannot be called 
on its own without a previous [request challenge](#requestchallenged) being obtained.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.models.c_res_auth_request import CResAuthRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    c_res_auth_request = citypay.CResAuthRequest() # CResAuthRequest | 

    try:
        # CRes
        api_response = api_instance.c_res_request(c_res_auth_request)
        print("The response of AuthorisationAndPaymentApi->c_res_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->c_res_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c_res_auth_request** | [**CResAuthRequest**](CResAuthRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of processing the 3DSv2 authorisation data. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **capture_request**
> Acknowledgement capture_request(capture_request)

Capture

_The capture process only applies to transactions which have been pre-authorised only._ 

The capture process will ensure
that a transaction will now settle. It is expected that a capture call will be provided within 3 days or
a maximum of 7 days.

A capture request is provided to confirm that you wish the transaction to be settled. This request can
contain a final amount for the transaction which is different to the original authorisation amount. This
may be useful in a delayed system process such as waiting for stock to be ordered, confirmed, or services
provided before the final cost is known.

When a transaction is completed, a new authorisation code may be created and a new confirmation
can be sent online to the acquiring bank.

Once the transaction has been processed. A standard [`Acknowledgement`](#acknowledgement) will be returned,
outlining the result of the transaction. On a successful completion process, the transaction will
be available for the settlement and completed at the end of the day.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.capture_request import CaptureRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    capture_request = citypay.CaptureRequest() # CaptureRequest | 

    try:
        # Capture
        api_response = api_instance.capture_request(capture_request)
        print("The response of AuthorisationAndPaymentApi->capture_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->capture_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capture_request** | [**CaptureRequest**](CaptureRequest.md)|  | 

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
**200** | A result and acknowledgement of the capture request. The response will return a &#x60;000/001&#x60; response on a successful capture otherwise an error code response explaining the error. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **card_tokenisation_request**
> CardTokenisationResponse card_tokenisation_request(card_tokenisation_request)

Card Tokenisation Request

Performs a tokenisation request for card details.

### Example

* Api Key Authentication (cp-domain-key):
* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.card_tokenisation_request import CardTokenisationRequest
from citypay.models.card_tokenisation_response import CardTokenisationResponse
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
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    card_tokenisation_request = citypay.CardTokenisationRequest() # CardTokenisationRequest | 

    try:
        # Card Tokenisation Request
        api_response = api_instance.card_tokenisation_request(card_tokenisation_request)
        print("The response of AuthorisationAndPaymentApi->card_tokenisation_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->card_tokenisation_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_tokenisation_request** | [**CardTokenisationRequest**](CardTokenisationRequest.md)|  | 

### Return type

[**CardTokenisationResponse**](CardTokenisationResponse.md)

### Authorization

[cp-domain-key](../README.md#cp-domain-key), [cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of the tokenisation request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_request**
> AuthResponse refund_request(refund_request)

Refund

A refund request which allows for the refunding of a previous transaction up 
and to the amount of the original sale. A refund will be performed against the 
original card used to process the transaction.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.auth_response import AuthResponse
from citypay.models.refund_request import RefundRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    refund_request = citypay.RefundRequest() # RefundRequest | 

    try:
        # Refund
        api_response = api_instance.refund_request(refund_request)
        print("The response of AuthorisationAndPaymentApi->refund_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->refund_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_request** | [**RefundRequest**](RefundRequest.md)|  | 

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of the refund of sale processing. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieval_request**
> AuthReferences retrieval_request(retrieve_request)

Transaction Retrieval

A retrieval request which allows an integration to obtain the result of a transaction processed
in the last 90 days. The request allows for retrieval based on the identifier or transaction 
number. 

The process may return multiple results in particular where a transaction was processed multiple
times against the same identifier. This can happen if errors were first received. The API therefore
returns up to the first 5 transactions in the latest date time order.

It is not intended for this operation to be a replacement for reporting and only allows for base transaction
information to be returned.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.auth_references import AuthReferences
from citypay.models.retrieve_request import RetrieveRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    retrieve_request = citypay.RetrieveRequest() # RetrieveRequest | 

    try:
        # Transaction Retrieval
        api_response = api_instance.retrieval_request(retrieve_request)
        print("The response of AuthorisationAndPaymentApi->retrieval_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->retrieval_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retrieve_request** | [**RetrieveRequest**](RetrieveRequest.md)|  | 

### Return type

[**AuthReferences**](AuthReferences.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A result of the retrieval request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verification_request**
> Decision verification_request(verification_request)

Verification

Performs a request for verification for a card payment request.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.decision import Decision
from citypay.models.verification_request import VerificationRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    verification_request = citypay.VerificationRequest() # VerificationRequest | 

    try:
        # Verification
        api_response = api_instance.verification_request(verification_request)
        print("The response of AuthorisationAndPaymentApi->verification_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->verification_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verification_request** | [**VerificationRequest**](VerificationRequest.md)|  | 

### Return type

[**Decision**](Decision.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A decision made by the result of verification. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_request**
> Acknowledgement void_request(void_request)

Void

_The void process generally applies to transactions which have been pre-authorised only however voids can occur 
on the same day if performed before batching and settlement._ 

The void process will ensure that a transaction will now settle. It is expected that a void call will be 
provided on the same day before batching and settlement or within 3 days or within a maximum of 7 days.

Once the transaction has been processed as a void, an [`Acknowledgement`](#acknowledgement) will be returned,
outlining the result of the transaction.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.void_request import VoidRequest
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

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.AuthorisationAndPaymentApi(api_client)
    void_request = citypay.VoidRequest() # VoidRequest | 

    try:
        # Void
        api_response = api_instance.void_request(void_request)
        print("The response of AuthorisationAndPaymentApi->void_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorisationAndPaymentApi->void_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **void_request** | [**VoidRequest**](VoidRequest.md)|  | 

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
**200** | &lt;/br&gt;A result and acknowledgement of the void request, returning an &#x60;080/003&#x60; response code on successful void/cancellation of the transaction.&lt;/br&gt;&lt;/br&gt;If an error occurs an error code will be returned explaining the failure. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

