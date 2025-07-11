# citypay.PaylinkApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paylink_token_close_request**](PaylinkApi.md#paylink_token_close_request) | **PUT** /paylink/{token}/close | Close Paylink Token
[**token_adjustment_request**](PaylinkApi.md#token_adjustment_request) | **POST** /paylink/{token}/adjustment | Paylink Token Adjustment
[**token_attachment_status**](PaylinkApi.md#token_attachment_status) | **GET** /paylink/{token}/attachment-status/{attachment} | Checks an attachment status
[**token_cancel_request**](PaylinkApi.md#token_cancel_request) | **PUT** /paylink/{token}/cancel | Cancel a Paylink Token
[**token_changes_request**](PaylinkApi.md#token_changes_request) | **POST** /paylink/token/changes | Paylink Token Audit
[**token_create_bill_payment_request**](PaylinkApi.md#token_create_bill_payment_request) | **POST** /paylink/bill-payment | Create Bill Payment Paylink Token
[**token_create_request**](PaylinkApi.md#token_create_request) | **POST** /paylink/create | Create Paylink Token
[**token_purge_attachments_request**](PaylinkApi.md#token_purge_attachments_request) | **PUT** /paylink/{token}/purge-attachments | Purges any attachments for a Paylink Token
[**token_reconciled_request**](PaylinkApi.md#token_reconciled_request) | **PUT** /paylink/{token}/reconciled | Reconcile Paylink Token
[**token_reopen_request**](PaylinkApi.md#token_reopen_request) | **PUT** /paylink/{token}/reopen | Reopen Paylink Token
[**token_resend_notification_request**](PaylinkApi.md#token_resend_notification_request) | **POST** /paylink/{token}/resend-notification | Resend a notification for Paylink Token
[**token_status_request**](PaylinkApi.md#token_status_request) | **GET** /paylink/{token}/status | Paylink Token Status


# **paylink_token_close_request**
> Acknowledgement paylink_token_close_request(token)

Close Paylink Token

Closes a paylink token that was previously created.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Close Paylink Token
        api_response = api_instance.paylink_token_close_request(token)
        print("The response of PaylinkApi->paylink_token_close_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->paylink_token_close_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms that the Paylink token was marked for closure. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_adjustment_request**
> Acknowledgement token_adjustment_request(token, paylink_adjustment_request)

Paylink Token Adjustment

Adjusts a TokenRequest's amount value when for instance 

1. a Token is created and the shopping cart is updated
2. an invoice is adjusted either due to part payment or due to increased incurred costs.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.paylink_adjustment_request import PaylinkAdjustmentRequest
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.
    paylink_adjustment_request = citypay.PaylinkAdjustmentRequest() # PaylinkAdjustmentRequest | 

    try:
        # Paylink Token Adjustment
        api_response = api_instance.token_adjustment_request(token, paylink_adjustment_request)
        print("The response of PaylinkApi->token_adjustment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_adjustment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 
 **paylink_adjustment_request** | [**PaylinkAdjustmentRequest**](PaylinkAdjustmentRequest.md)|  | 

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
**200** | Response defining the result of the token request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_attachment_status**
> Acknowledgement token_attachment_status(token, attachment)

Checks an attachment status

The `TokenAttachmentStatus` processes a request to check the status of a Paylink BPS attachment, 
verifying its successful upload and returning metadata such as the MD5 hash, upload time, 
and content type to ensure file integrity and correctness.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.
    attachment = 'attachment_example' # str | The attachemnt name requested.

    try:
        # Checks an attachment status
        api_response = api_instance.token_attachment_status(token, attachment)
        print("The response of PaylinkApi->token_attachment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_attachment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 
 **attachment** | **str**| The attachemnt name requested. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Verifies that the attachment has been successfully uploaded and returns an MD5 hash of its content to ensure the integrity and correctness of the file during validation. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_cancel_request**
> Acknowledgement token_cancel_request(token)

Cancel a Paylink Token

Marks a Paylink Token as cancelled. This cancels the Token for any future request for processing.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Cancel a Paylink Token
        api_response = api_instance.token_cancel_request(token)
        print("The response of PaylinkApi->token_cancel_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_cancel_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms that the token was marked as cancelled. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_changes_request**
> PaylinkTokenStatusChangeResponse token_changes_request(paylink_token_status_change_request)

Paylink Token Audit

Allows for the changes to a pre-existing token.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.paylink_token_status_change_request import PaylinkTokenStatusChangeRequest
from citypay.models.paylink_token_status_change_response import PaylinkTokenStatusChangeResponse
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
    api_instance = citypay.PaylinkApi(api_client)
    paylink_token_status_change_request = citypay.PaylinkTokenStatusChangeRequest() # PaylinkTokenStatusChangeRequest | 

    try:
        # Paylink Token Audit
        api_response = api_instance.token_changes_request(paylink_token_status_change_request)
        print("The response of PaylinkApi->token_changes_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_changes_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paylink_token_status_change_request** | [**PaylinkTokenStatusChangeRequest**](PaylinkTokenStatusChangeRequest.md)|  | 

### Return type

[**PaylinkTokenStatusChangeResponse**](PaylinkTokenStatusChangeResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes from tokens actioned after the pivotal date provided in the request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_create_bill_payment_request**
> PaylinkTokenCreated token_create_bill_payment_request(paylink_bill_payment_token_request)

Create Bill Payment Paylink Token

CityPay Paylink supports invoice and bill payment services by allowing merchants to raise an invoice in their systems and
associate the invoice with a Paylink checkout token. CityPay will co-ordinate the checkout flow in relationship with
your customer. Our bill payment solution may be used to streamline the payment flow with cardholders to allow your
invoice to be paid promptly and via multiple payment channels such as Card Payment, Apple Pay or Google Pay.

The bill payment service allows

1. setting up notification paths to an end customer, such as SMS or Email
2. enabling attachments to be included with Paylink tokens
3. produce chaser notifications for unpaid invoices
4. provide callbacks for notification of the payment of an invoice
5. support part payments against an invoice
6. support of field guards to protect the payment screen
7. support of status reporting on tokens
8. URL short codes for SMS notifications

<img src="images/merchant-BPS-workflow.png" alt="Paylink BPSv2 Overview" width="50%"/> 


### Notification Paths

Notification paths can be provided which identify the channels for communication of the invoice availability.
Up to 3 notification paths may be provided per request.

Each notification uses a template to generate the body of the message. This allows for variable text to be sent out and
customised for each call.

SMS messages use URL Short Codes (USC) as a payment link to the invoice payment page. This allows for a standard payment
URL to be shortened for optimised usage in SMS. For instance a URL of `https://checkout.citypay.com/PL1234/s348yb8yna4a48n2f8nq2f3msgyng-psn348ynaw8ynaw/en`
becomes `citypay.com/Za48na3x`. Each USC is unique however it is a requirement that each USC generated is protected
with Field Guards to ensure that sensitive data (such as customer contact details and GDPR) is protected.

To send a notification path, append a `notification-path` property to the request.

```json
 {
  "sms_notification_path": {
      "to": "+441534884000"
  },
  "email_notification_path": {
      "to": ["help-desk@citypay.com"],
      "cc": ["third-party@citypay.com"],
      "reply": ["help@my-company.com"]
  }
}
```

Notification paths trigger a number of events which are stored as part of the timeline of events of a Paylink token

- `BillPaymentSmsNotificationQueued` - identifies when an SMS notification has been queued for delivery
- `BillPaymentSmsNotificationSent` - identifies when an SMS notification has been sent to the upstream network
- `BillPaymentSmsNotificationDelivered` - identifies when an SMS notification has been delivered as notified by the upstream network
- `BillPaymentSmsNotificationUndelivered` - identifies when an SMS notification has undelivered notification is provided by the upstream network
- `BillPaymentSmsNotificationFailure` - identifies when an SMS notification has failed
- `BillPaymentEmailNotificationQueued` -  identifies when an email notification has been queued for delivery
- `BillPaymentEmailNotificationSent` -  identifies when an email notification has been accepted by our SMS forwarder
- `BillPaymentEmailNotificationFailure` - identifies when an email notification has failed delivery


#### SMS Notification Path

SMS originated from a CityPay pool of numbers and by default only sends to country codes where the service is registered.
SMSs may contain a From field which is configured as part of you onboarding and have a name associated to identify the service
origin. For example if your business is titled `Health Surgery Ltd` the SMS may be sent to originate from `Health Surgery`. 

SMS is also configured for a "polite mode". This mode ensures that SMSs aren't sent in the middle of the night when backend
services ordinarily run. SMSs will be queued until the time range is deemed as polite. Normally this is between 8am and 9pm.

| Field    | Type     | Usage    | Description                                                                                     |
|----------|----------|----------|-------------------------------------------------------------------------------------------------|
| template | string   | Reserved | An optional template name to use a template other than the default.                             |
| to       | string   | Reserved | The phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format to send the message to. |

#### Email Notification Paths

| Field    | Type     | Usage    | Description                                                                                     |
|----------|----------|----------|-------------------------------------------------------------------------------------------------|
| template | string   | Reserved | An optional template name to use a template other than the default.                             |
| to       | string[] | Required | An array of email addresses to be used for delivery. A maximum of 5 addresses can be added.     |
| cc       | string[] | Required | An array of email addresses to be used for cc delivery. A maximum of 5 addresses can be added.  |
| bcc      | string[] | Required | An array of email addresses to be used for bcc delivery. A maximum of 5 addresses can be added. |
| reply_to | string[] | Required | An array of email addresses to be used for the Reply-To header of an email.     |


### Field Guards

To ensure that invoices are paid by the intended recipient, Paylink supports the addition of Field Guards.

A Field Guard is an intended field which is to be used as a form of guarded authentication. More than 1 field can be
requested.

<img src="images/paylink-field-guards.png" alt="Paylink Field Guards" width="50%"/>

To determine the source value of the field, each field name is searched in the order of

- identifier
- cardholder data such as name
- custom parameters
- pass through data

If no field values are found, the token request returns a D041 validation error.

#### Authentication and Validation

When values are entered by the user, resultant comparisons are performed by

1. Transliteration of both the source value and entered value. For example, names with accents (e.g. é will become e)
2. Only Alphanumeric values are retained any whitespace or special characters are ignored
3. Case is ignored

Should all values match, the user is authenticated and can continue to the payment form rendered by the Paylink server.

On successful login, an event will be added to include that the access guard validated access.

#### Access-Key

To ensure that a user does not need to re-enter these values multiple times, a cookie is pushed to the user’s
browser with an access-key digest value. This value will be presented to the server on each refresh therefore
allowing the guard to accept the call. Each value is uniquely stored per merchant account and cannot be shared cross
merchant. The lifetime of the cookie is set to 24 hours.

#### Brute Force Prevention

To prevent multiple calls hitting the server, attempting a brute force attack, the login process

1. is fronted by a contemporary web application firewall
2. creates an event for each token when access was denied
3. should the number of failed events breach more than 5 in 30 minutes, the token is locked for an hour
4. should the number of events breach more than 20 the token is fully locked

### Attachments

Attachments can be included in the request in 2 ways

1. Via a data element direct in the request
2. Via a URL upload to a provided pre-signed URL

The decision of which option is dependent on the size of the attachments. Should the attachment size be greater than
32kb a URL upload is required. Small attachments can be included in the JSON request. This is to prevent our web
firewall from blocking your request and to also ensure efficiency of larger file uploads.

There is a maximum of 3 attachments that can be added to a request.

```json
    [{
      "filename": "invoice1.pdf",
      "mime-type": "application/pdf"
    },{
      "filename": "invoice2.pdf",
      "data": "b4sE64Enc0dEd...=",
      "mime-type": "application/pdf"
    }]
```

| Field     | Type   | Usage    | Description                                                                                                                                          |
|-----------|--------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| filename  | string | Required | The name of the attachment normally taken from the filename. You should not include the filename path as appropriate                                 |
| data      | string | Optional | base64 encoding of the file if less than 32kb in size                                                                                                |
| mime-type | string | Required | The mime type of the attachment as defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html). Currently only `application/pdf` is supported |


#### Attachment Result

A result of an attachment specifies whether the attachment was successfully added or whether a further upload is requried

| Field  | Type   | Usage    | Description                                                                                                                                       |
|--------|--------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| result | string | Required | `OK` should the file have uploaded or `UPLOAD` if the file is required to be uploaded.                                                            |
| name   | string | Required | The filename that was specified in the upload process                                                                                             |
| url    | string | Optional | Should an upload be required, this URL is available for an upload to be issued. The URL is only available for uploads for 24 hours from creation. |


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.paylink_bill_payment_token_request import PaylinkBillPaymentTokenRequest
from citypay.models.paylink_token_created import PaylinkTokenCreated
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
    api_instance = citypay.PaylinkApi(api_client)
    paylink_bill_payment_token_request = citypay.PaylinkBillPaymentTokenRequest() # PaylinkBillPaymentTokenRequest | 

    try:
        # Create Bill Payment Paylink Token
        api_response = api_instance.token_create_bill_payment_request(paylink_bill_payment_token_request)
        print("The response of PaylinkApi->token_create_bill_payment_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_create_bill_payment_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paylink_bill_payment_token_request** | [**PaylinkBillPaymentTokenRequest**](PaylinkBillPaymentTokenRequest.md)|  | 

### Return type

[**PaylinkTokenCreated**](PaylinkTokenCreated.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response defining the result of the token request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_create_request**
> PaylinkTokenCreated token_create_request(paylink_token_request_model)

Create Paylink Token

Creates a Paylink token from the CityPay API.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.paylink_token_created import PaylinkTokenCreated
from citypay.models.paylink_token_request_model import PaylinkTokenRequestModel
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
    api_instance = citypay.PaylinkApi(api_client)
    paylink_token_request_model = citypay.PaylinkTokenRequestModel() # PaylinkTokenRequestModel | 

    try:
        # Create Paylink Token
        api_response = api_instance.token_create_request(paylink_token_request_model)
        print("The response of PaylinkApi->token_create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **paylink_token_request_model** | [**PaylinkTokenRequestModel**](PaylinkTokenRequestModel.md)|  | 

### Return type

[**PaylinkTokenCreated**](PaylinkTokenCreated.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response defining the result of the token request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_purge_attachments_request**
> Acknowledgement token_purge_attachments_request(token)

Purges any attachments for a Paylink Token

Purges any attachments for a token for GDPR or DP reasons.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Purges any attachments for a Paylink Token
        api_response = api_instance.token_purge_attachments_request(token)
        print("The response of PaylinkApi->token_purge_attachments_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_purge_attachments_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms that the attachments either did not exist or were purged. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_reconciled_request**
> Acknowledgement token_reconciled_request(token)

Reconcile Paylink Token

Marks a Paylink Token as reconciled when reconciliation is performed on the merchant's side.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Reconcile Paylink Token
        api_response = api_instance.token_reconciled_request(token)
        print("The response of PaylinkApi->token_reconciled_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_reconciled_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms that the token was marked as reconciled. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_reopen_request**
> Acknowledgement token_reopen_request(token)

Reopen Paylink Token

Allows for a Paylink Token to be reopened if a Token has been previously closed and payment has not yet been made.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Reopen Paylink Token
        api_response = api_instance.token_reopen_request(token)
        print("The response of PaylinkApi->token_reopen_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_reopen_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**Acknowledgement**](Acknowledgement.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirms that the token was reopened. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_resend_notification_request**
> Acknowledgement token_resend_notification_request(token, paylink_resend_notification_request)

Resend a notification for Paylink Token

Resend a notification for Paylink Token.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.paylink_resend_notification_request import PaylinkResendNotificationRequest
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.
    paylink_resend_notification_request = citypay.PaylinkResendNotificationRequest() # PaylinkResendNotificationRequest | 

    try:
        # Resend a notification for Paylink Token
        api_response = api_instance.token_resend_notification_request(token, paylink_resend_notification_request)
        print("The response of PaylinkApi->token_resend_notification_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_resend_notification_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 
 **paylink_resend_notification_request** | [**PaylinkResendNotificationRequest**](PaylinkResendNotificationRequest.md)|  | 

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
**200** | Confirms that the notification was sent. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_status_request**
> PaylinkTokenStatus token_status_request(token)

Paylink Token Status

Obtains the full status of a given Paylink Token.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.paylink_token_status import PaylinkTokenStatus
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
    api_instance = citypay.PaylinkApi(api_client)
    token = 'token_example' # str | The token returned by the create token process.

    try:
        # Paylink Token Status
        api_response = api_instance.token_status_request(token)
        print("The response of PaylinkApi->token_status_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaylinkApi->token_status_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token returned by the create token process. | 

### Return type

[**PaylinkTokenStatus**](PaylinkTokenStatus.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current status of the token. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

