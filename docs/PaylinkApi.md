# citypay.PaylinkApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_adjustment_request**](PaylinkApi.md#token_adjustment_request) | **POST** /paylink/{token}/adjustment | Paylink Token Adjustment
[**token_close_request**](PaylinkApi.md#token_close_request) | **PUT** /paylink/{token}/close | Close Paylink Token
[**token_create_bill_payment_request**](PaylinkApi.md#token_create_bill_payment_request) | **POST** /paylink/bill-payment | Create Bill Payment Paylink Token
[**token_create_request**](PaylinkApi.md#token_create_request) | **POST** /paylink/create | Create Paylink Token
[**token_reconciled_request**](PaylinkApi.md#token_reconciled_request) | **PUT** /paylink/{token}/reconciled | Reconcile Paylink Token
[**token_reopen_request**](PaylinkApi.md#token_reopen_request) | **PUT** /paylink/{token}/reopen | Reopen Paylink Token
[**token_status_changes_request**](PaylinkApi.md#token_status_changes_request) | **POST** /paylink/token/changes | Paylink Token Audit
[**token_status_request**](PaylinkApi.md#token_status_request) | **GET** /paylink/{token}/status | Paylink Token Status


# **token_adjustment_request**
> Acknowledgement token_adjustment_request(token, paylink_adjustment_request)

Paylink Token Adjustment

Adjusts a TokenRequest's amount value when for instance   1. a Token is created and the shopping cart is updated 2. an invoice is adjusted either due to part payment or due to increased incurred costs. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.error import Error
from citypay.model.paylink_adjustment_request import PaylinkAdjustmentRequest
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    token = "token_example" # str | The token returned by the create token process.
    paylink_adjustment_request = PaylinkAdjustmentRequest(
        amount=3600,
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
        reason="reason_example",
    ) # PaylinkAdjustmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Paylink Token Adjustment
        api_response = api_instance.token_adjustment_request(token, paylink_adjustment_request)
        pprint(api_response)
    except citypay.ApiException as e:
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

# **token_close_request**
> Acknowledgement token_close_request(token)

Close Paylink Token

Marks a Paylink Token as closed. This closes the Token for any future action and the Token will not appear in any status request calls. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.error import Error
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    token = "token_example" # str | The token returned by the create token process.

    # example passing only required values which don't have defaults set
    try:
        # Close Paylink Token
        api_response = api_instance.token_close_request(token)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling PaylinkApi->token_close_request: %s\n" % e)
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
**200** | Confirms that the token was marked for closure. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_create_bill_payment_request**
> PaylinkTokenCreated token_create_bill_payment_request(paylink_bill_payment_token_request)

Create Bill Payment Paylink Token

CityPay Paylink supports invoice and bill payment services by allowing merchants to raise an invoice in their systems and associate the invoice with a Paylink checkout token. CityPay will co-ordinate the checkout flow in relationship with your customer. Our bill payment solution may be used to streamline the payment flow with cardholders to allow your invoice to be paid promptly and via multiple payment channels such as Card Payment, Apple Pay or Google Pay.  The bill payment service allows  1. setting up notification paths to an end customer, such as SMS or Email 2. enabling attachments to be included with Paylink tokens 3. produce chaser notifications for unpaid invoices 4. provide callbacks for notification of the payment of an invoice 5. support part payments against an invoice 6. support of field guards to protect the payment screen 7. support of status reporting on tokens 8. URL short codes for SMS notifications  <img src=\"../images/merchant-BPS-workflow.png\" alt=\"Paylink BPSv2 Overview\" width=\"50%\"/>    ### Notification Paths  Notification paths can be provided which identify the channels for communication of the invoice availability. Up to 3 notification paths may be provided per request.  Each notification uses a template to generate the body of the message. This allows for variable text to be sent out and customised for each call.  SMS messages use URL Short Codes (USC) as a payment link to the invoice payment page. This allows for a standard payment URL to be shortened for optimised usage in SMS. For instance a URL of `https://checkout.citypay.com/PL1234/s348yb8yna4a48n2f8nq2f3msgyng-psn348ynaw8ynaw/en` becomes `citypay.com/Za48na3x`. Each USC is unique however it is a requirement that each USC generated is protected with Field Guards to ensure that sensitive data (such as customer contact details and GDPR) is protected.  To send a notification path, append a `notification-path` property to the request.  ```json  {   \"notification-path\": [     {       \"channel\": \"sms\",       \"to\": \"+441534884000\"     },     {       \"channel\": \"email\",       \"to\": [\"help-desk@citypay.com\"],       \"cc\": [\"third-party@citypay.com\"],       \"reply\": [\"help@my-company.com\"]     }   ] }  ```  Notification paths trigger a number of events which are stored as part of the timeline of events of a Paylink token  - `BillPaymentSmsNotificationQueued` - identifies when an SMS notification has been queued for delivery - `BillPaymentSmsNotificationSent` - identifies when an SMS notification has been sent to the upstream network - `BillPaymentSmsNotificationDelivered` - identifies when an SMS notification has been delivered as notified by the upstream network - `BillPaymentSmsNotificationUndelivered` - identifies when an SMS notification has undelivered notification is provided by the upstream network - `BillPaymentSmsNotificationFailure` - identifies when an SMS notification has failed - `BillPaymentEmailNotificationQueued` -  identifies when an email notification has been queued for delivery - `BillPaymentEmailNotificationSent` -  identifies when an email notification has been accepted by our SMS forwarder - `BillPaymentEmailNotificationFailure` - identifies when an email notification has failed delivery   #### SMS Notification Path  SMS originated from a CityPay pool of numbers and by default only sends to country codes where the service is registered. SMSs may contain a From field which is configured as part of you onboarding and have a name associated to identify the service origin. For example if your business is titled `Health Surgery Ltd` the SMS may be sent to originate from `Health Surgery`.   SMS is also configured for a \"polite mode\". This mode ensures that SMSs aren't sent in the middle of the night when backend services ordinarily run. SMSs will be queued until the time range is deemed as polite. Normally this is between 8am and 9pm.  | Field    | Type     | Usage    | Description                                                                                     | |----------|----------|----------|-------------------------------------------------------------------------------------------------| | template | string   | Reserved | An optional template name to use a template other than the default.                             | | to       | string   | Reserved | The phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format to send the message to. |  #### Email Notification Paths  | Field    | Type     | Usage    | Description                                                                                     | |----------|----------|----------|-------------------------------------------------------------------------------------------------| | template | string   | Reserved | An optional template name to use a template other than the default.                             | | to       | string[] | Required | An array of email addresses to be used for delivery. A maximum of 5 addresses can be added.     | | cc       | string[] | Required | An array of email addresses to be used for cc delivery. A maximum of 5 addresses can be added.  | | bcc      | string[] | Required | An array of email addresses to be used for bcc delivery. A maximum of 5 addresses can be added. | | reply_to | string[] | Required | An array of email addresses to be used for the Reply-To header of an email.     |   ### Field Guards  To ensure that invoices are paid by the intended recipient, Paylink supports the addition of Field Guards.  A Field Guard is an intended field which is to be used as a form of guarded authentication. More than 1 field can be requested.  <img src=\"../images/paylink-field-guards.png\" alt=\"Paylink Field Guards\" width=\"50%\"/>  To determine the source value of the field, each field name is searched in the order of  - identifier - cardholder data such as name - custom parameters - pass through data  If no field values are found, the token request returns a D041 validation error.  #### Authentication and Validation  When values are entered by the user, resultant comparisons are performed by  1. Transliteration of both the source value and entered value. For example, names with accents (e.g. é will become e) 2. Only Alphanumeric values are retained any whitespace or special characters are ignored 3. Case is ignored  Should all values match, the user is authenticated and can continue to the payment form rendered by the Paylink server.  On successful login, an event will be added to include that the access guard validated access.  #### Access-Key  To ensure that a user does not need to re-enter these values multiple times, a cookie is pushed to the user’s browser with an access-key digest value. This value will be presented to the server on each refresh therefore allowing the guard to accept the call. Each value is uniquely stored per merchant account and cannot be shared cross merchant. The lifetime of the cookie is set to 24 hours.  #### Brute Force Prevention  To prevent multiple calls hitting the server, attempting a brute force attack, the login process  1. is fronted by a contemporary web application firewall 2. creates an event for each token when access was denied 3. should the number of failed events breach more than 5 in 30 minutes, the token is locked for an hour 4. should the number of events breach more than 20 the token is fully locked  ### Attachments  Attachments can be included in the request in 2 ways  1. Via a data element direct in the request 2. Via a URL upload to a provided pre-signed URL  The decision of which option is dependent on the size of the attachments. Should the attachment size be greater than 32kb a URL upload is required. Small attachments can be included in the JSON request. This is to prevent our web firewall from blocking your request and to also ensure efficiency of larger file uploads.  There is a maximum of 3 attachments that can be added to a request.  ```json     [{       \"filename\": \"invoice1.pdf\",       \"mime-type\": \"application/pdf\"     },{       \"filename\": \"invoice2.pdf\",       \"data\": \"b4sE64Enc0dEd...=\",       \"mime-type\": \"application/pdf\"     }] ```  | Field     | Type   | Usage    | Description                                                                                                                                          | |-----------|--------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------| | filename  | string | Required | The name of the attachment normally taken from the filename. You should not include the filename path as appropriate                                 | | data      | string | Optional | base64 encoding of the file if less than 32kb in size                                                                                                | | mime-type | string | Required | The mime type of the attachment as defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html). Currently only `application/pdf` is supported |   #### Attachment Result  A result of an attachment specifies whether the attachment was successfully added or whether a further upload is requried  | Field  | Type   | Usage    | Description                                                                                                                                       | |--------|--------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------| | result | string | Required | `OK` should the file have uploaded or `UPLOAD` if the file is required to be uploaded.                                                            | | name   | string | Required | The filename that was specified in the upload process                                                                                             | | url    | string | Optional | Should an upload be required, this URL is available for an upload to be issued. The URL is only available for uploads for 24 hours from creation. | 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.paylink_bill_payment_token_request import PaylinkBillPaymentTokenRequest
from citypay.model.error import Error
from citypay.model.paylink_token_created import PaylinkTokenCreated
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    paylink_bill_payment_token_request = PaylinkBillPaymentTokenRequest(
        attachments=[
            PaylinkAttachmentRequest(
                data="data_example",
                filename="filename_example",
                mime_type="mime_type_example",
            ),
        ],
        descriptor="descriptor_example",
        due=dateutil_parser('1970-01-01').date(),
        email_notification_path=PaylinkEmailNotificationPath(
            bcc=[
                "bcc_example",
            ],
            cc=[
                "cc_example",
            ],
            reply_to=[
                "reply_to_example",
            ],
            template="template_example",
            to=[
                "to_example",
            ],
        ),
        request=PaylinkTokenRequestModel(
            accountno="accountno_example",
            amount=1,
            cardholder=PaylinkCardHolder(
                accept_headers="accept_headers_example",
                address=PaylinkAddress(
                    address1="79 Parliament St",
                    address2="Westminster",
                    address3="address3_example",
                    area="London",
                    country="GB",
                    label="Head Office",
                    postcode="L1 789",
                ),
                company="Acme Ltd",
                email="card.holder@citypay.com",
                firstname="John",
                lastname="Smith",
                mobile_no="447790123456",
                remote_addr="remote_addr_example",
                title="Mr",
                user_agent="user_agent_example",
            ),
            cart=PaylinkCart(
                contents=[
                    PaylinkCartItemModel(
                        amount=1,
                        brand="brand_example",
                        category="category_example",
                        count=1,
                        label="label_example",
                        max=1,
                        sku="sku_example",
                        variant="variant_example",
                    ),
                ],
                coupon="coupon_example",
                mode=1,
                product_description="product_description_example",
                product_information="product_information_example",
                shipping=1,
                tax=1,
            ),
            client_version="client_version_example",
            config=PaylinkConfig(
                acs_mode="acs_mode_example",
                custom_params=[
                    PaylinkCustomParam(
                        field_type="field_type_example",
                        group="group_example",
                        label="label_example",
                        locked=True,
                        name="name_example",
                        order=1,
                        pattern="pattern_example",
                        placeholder="placeholder_example",
                        required=True,
                        value="value_example",
                    ),
                ],
                descriptor="descriptor_example",
                expire_in="expire_in_example",
                field_guard=[
                    PaylinkFieldGuardModel(
                        label="label_example",
                        name="name_example",
                        type="type_example",
                    ),
                ],
                lock_params=[
                    "lock_params_example",
                ],
                merch_logo="merch_logo_example",
                merch_terms="merch_terms_example",
                options=[
                    "options_example",
                ],
                part_payments=PaylinkPartPayments(
                    enabled="enabled_example",
                    floor="floor_example",
                    max="max_example",
                    max_rate="max_rate_example",
                    min="min_example",
                    min_rate="min_rate_example",
                ),
                pass_through_data={
                    "key": "key_example",
                },
                pass_through_headers={
                    "key": "key_example",
                },
                postback="postback_example",
                postback_password="postback_password_example",
                postback_policy="postback_policy_example",
                postback_username="postback_username_example",
                redirect_delay=1,
                redirect_failure="redirect_failure_example",
                redirect_success="redirect_success_example",
                renderer="renderer_example",
                return_params=True,
                ui=PaylinkUI(
                    address_mandatory=True,
                    form_auto_complete="true",
                    ordering=1,
                    postcode_mandatory=True,
                ),
            ),
            email="card.holder@citypay.com",
            identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
            merchantid=11223344,
            subscription_id="subscription_id_example",
            tx_type="tx_type_example",
        ),
        sms_notification_path=PaylinkSMSNotificationPath(
            template="template_example",
            to="to_example",
        ),
    ) # PaylinkBillPaymentTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create Bill Payment Paylink Token
        api_response = api_instance.token_create_bill_payment_request(paylink_bill_payment_token_request)
        pprint(api_response)
    except citypay.ApiException as e:
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
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.error import Error
from citypay.model.paylink_token_created import PaylinkTokenCreated
from citypay.model.paylink_token_request_model import PaylinkTokenRequestModel
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    paylink_token_request_model = PaylinkTokenRequestModel(
        accountno="accountno_example",
        amount=1,
        cardholder=PaylinkCardHolder(
            accept_headers="accept_headers_example",
            address=PaylinkAddress(
                address1="79 Parliament St",
                address2="Westminster",
                address3="address3_example",
                area="London",
                country="GB",
                label="Head Office",
                postcode="L1 789",
            ),
            company="Acme Ltd",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            remote_addr="remote_addr_example",
            title="Mr",
            user_agent="user_agent_example",
        ),
        cart=PaylinkCart(
            contents=[
                PaylinkCartItemModel(
                    amount=1,
                    brand="brand_example",
                    category="category_example",
                    count=1,
                    label="label_example",
                    max=1,
                    sku="sku_example",
                    variant="variant_example",
                ),
            ],
            coupon="coupon_example",
            mode=1,
            product_description="product_description_example",
            product_information="product_information_example",
            shipping=1,
            tax=1,
        ),
        client_version="client_version_example",
        config=PaylinkConfig(
            acs_mode="acs_mode_example",
            custom_params=[
                PaylinkCustomParam(
                    field_type="field_type_example",
                    group="group_example",
                    label="label_example",
                    locked=True,
                    name="name_example",
                    order=1,
                    pattern="pattern_example",
                    placeholder="placeholder_example",
                    required=True,
                    value="value_example",
                ),
            ],
            descriptor="descriptor_example",
            expire_in="expire_in_example",
            field_guard=[
                PaylinkFieldGuardModel(
                    label="label_example",
                    name="name_example",
                    type="type_example",
                ),
            ],
            lock_params=[
                "lock_params_example",
            ],
            merch_logo="merch_logo_example",
            merch_terms="merch_terms_example",
            options=[
                "options_example",
            ],
            part_payments=PaylinkPartPayments(
                enabled="enabled_example",
                floor="floor_example",
                max="max_example",
                max_rate="max_rate_example",
                min="min_example",
                min_rate="min_rate_example",
            ),
            pass_through_data={
                "key": "key_example",
            },
            pass_through_headers={
                "key": "key_example",
            },
            postback="postback_example",
            postback_password="postback_password_example",
            postback_policy="postback_policy_example",
            postback_username="postback_username_example",
            redirect_delay=1,
            redirect_failure="redirect_failure_example",
            redirect_success="redirect_success_example",
            renderer="renderer_example",
            return_params=True,
            ui=PaylinkUI(
                address_mandatory=True,
                form_auto_complete="true",
                ordering=1,
                postcode_mandatory=True,
            ),
        ),
        email="card.holder@citypay.com",
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
        merchantid=11223344,
        subscription_id="subscription_id_example",
        tx_type="tx_type_example",
    ) # PaylinkTokenRequestModel | 

    # example passing only required values which don't have defaults set
    try:
        # Create Paylink Token
        api_response = api_instance.token_create_request(paylink_token_request_model)
        pprint(api_response)
    except citypay.ApiException as e:
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

# **token_reconciled_request**
> Acknowledgement token_reconciled_request(token)

Reconcile Paylink Token

Marks a Paylink Token as reconciled when reconcilation is performed on the merchant's side.

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.error import Error
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    token = "token_example" # str | The token returned by the create token process.

    # example passing only required values which don't have defaults set
    try:
        # Reconcile Paylink Token
        api_response = api_instance.token_reconciled_request(token)
        pprint(api_response)
    except citypay.ApiException as e:
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
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.error import Error
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    token = "token_example" # str | The token returned by the create token process.

    # example passing only required values which don't have defaults set
    try:
        # Reopen Paylink Token
        api_response = api_instance.token_reopen_request(token)
        pprint(api_response)
    except citypay.ApiException as e:
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

# **token_status_changes_request**
> PaylinkTokenStatusChangeResponse token_status_changes_request(paylink_token_status_change_request)

Paylink Token Audit

Obtains any changes on Paylink Tokens since a given date and time. This allows for a merchant to regularly check on  activity over a collection of Paylink Tokens and to check on any events that may have occurred. If a Token is `Closed`  it is not considered.  Only statuses that have been appended since the given date and time is returned. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.paylink_token_status_change_response import PaylinkTokenStatusChangeResponse
from citypay.model.paylink_token_status_change_request import PaylinkTokenStatusChangeRequest
from citypay.model.error import Error
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    paylink_token_status_change_request = PaylinkTokenStatusChangeRequest(
        after=dateutil_parser('1970-01-01T00:00:00.00Z'),
        max_results=1,
        merchantid=11223344,
        next_token="next_token_example",
        order_by=[
            "order_by_example",
        ],
    ) # PaylinkTokenStatusChangeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Paylink Token Audit
        api_response = api_instance.token_status_changes_request(paylink_token_status_change_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling PaylinkApi->token_status_changes_request: %s\n" % e)
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

# **token_status_request**
> PaylinkTokenStatus token_status_request(token)

Paylink Token Status

Obtains the full status of a given Paylink Token.

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import paylink_api__
from citypay.model.paylink_token_status import PaylinkTokenStatus
from citypay.model.error import Error
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

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = paylink_api__.PaylinkApi(api_client)
    token = "token_example" # str | The token returned by the create token process.

    # example passing only required values which don't have defaults set
    try:
        # Paylink Token Status
        api_response = api_instance.token_status_request(token)
        pprint(api_response)
    except citypay.ApiException as e:
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

