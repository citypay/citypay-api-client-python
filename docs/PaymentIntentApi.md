# citypay.PaymentIntentApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_intent**](PaymentIntentApi.md#create_payment_intent) | **POST** /v6/intent/create | Create a Payment Intent
[**get_payment_intent**](PaymentIntentApi.md#get_payment_intent) | **POST** /v6/intent/retrieve | Retrieves a Payment Intent


# **create_payment_intent**
> PaymentIntentReference create_payment_intent(payment_intent_request_model)

Create a Payment Intent

This endpoint initiates the creation of a payment intent, which is a precursor to processing a payment. A payment intent
captures the details of a prospective payment transaction, including the payment amount, currency, and associated
billing and shipping information.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.payment_intent_reference import PaymentIntentReference
from citypay.models.payment_intent_request_model import PaymentIntentRequestModel
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
    api_instance = citypay.PaymentIntentApi(api_client)
    payment_intent_request_model = citypay.PaymentIntentRequestModel() # PaymentIntentRequestModel | 

    try:
        # Create a Payment Intent
        api_response = api_instance.create_payment_intent(payment_intent_request_model)
        print("The response of PaymentIntentApi->create_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentIntentApi->create_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_intent_request_model** | [**PaymentIntentRequestModel**](PaymentIntentRequestModel.md)|  | 

### Return type

[**PaymentIntentReference**](PaymentIntentReference.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the id of the payment intent. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_intent**
> PaymentIntentResponseModel get_payment_intent(find_payment_intent_request)

Retrieves a Payment Intent

Obtains a payment intent.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.find_payment_intent_request import FindPaymentIntentRequest
from citypay.models.payment_intent_response_model import PaymentIntentResponseModel
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
    api_instance = citypay.PaymentIntentApi(api_client)
    find_payment_intent_request = citypay.FindPaymentIntentRequest() # FindPaymentIntentRequest | 

    try:
        # Retrieves a Payment Intent
        api_response = api_instance.get_payment_intent(find_payment_intent_request)
        print("The response of PaymentIntentApi->get_payment_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentIntentApi->get_payment_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **find_payment_intent_request** | [**FindPaymentIntentRequest**](FindPaymentIntentRequest.md)|  | 

### Return type

[**PaymentIntentResponseModel**](PaymentIntentResponseModel.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a payment intent and optionally any transactions associated to the intent. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

