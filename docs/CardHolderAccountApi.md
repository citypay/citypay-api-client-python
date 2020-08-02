# citypay.CardHolderAccountApi

All URIs are relative to *https://api.citypay.com/v6*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_card_delete_request**](CardHolderAccountApi.md#account_card_delete_request) | **DELETE** /account/{accountid}/card/{cardId} | Card Deletion
[**account_card_register_request**](CardHolderAccountApi.md#account_card_register_request) | **POST** /account/{accountid}/register | Card Registration
[**account_card_status_request**](CardHolderAccountApi.md#account_card_status_request) | **POST** /account/{accountid}/card/{cardId}/status | Card Status
[**account_change_contact_request**](CardHolderAccountApi.md#account_change_contact_request) | **POST** /account/{accountid}/contact | Contact Details Update
[**account_create**](CardHolderAccountApi.md#account_create) | **POST** /account/create | Account Create
[**account_delete_request**](CardHolderAccountApi.md#account_delete_request) | **DELETE** /account/{accountid} | Account Deletion
[**account_retrieve_request**](CardHolderAccountApi.md#account_retrieve_request) | **GET** /account/{accountid} | Account Retrieval
[**account_status_request**](CardHolderAccountApi.md#account_status_request) | **POST** /account/{accountid}/status | Account Status
[**charge_request**](CardHolderAccountApi.md#charge_request) | **POST** /charge | Charge


# **account_card_delete_request**
> Acknowledgement account_card_delete_request(accountid, card_id)

Card Deletion

Deletes a card from the account. The card will be marked for deletion before a subsequent purge will clear the card permanently. 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
card_id = 'card_id_example' # str | The id of the card that is presented by a call to retrieve a card holder account.

    try:
        # Card Deletion
        api_response = api_instance.account_card_delete_request(accountid, card_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_card_delete_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **card_id** | **str**| The id of the card that is presented by a call to retrieve a card holder account. | 

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
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | Acknowledges the card has been requested for deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_card_register_request**
> CardHolderAccount account_card_register_request(accountid, register_card)

Card Registration

Allows for a card to be registered for the account. The card will be added for future  processing and will be available as a tokenised value for future processing.  The card will be validated for  0. Being a valid card number (luhn check) 0. Having a valid expiry date 0. Being a valid bin value. 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
register_card = citypay.RegisterCard() # RegisterCard | 

    try:
        # Card Registration
        api_response = api_instance.account_card_register_request(accountid, register_card)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_card_register_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **register_card** | [**RegisterCard**](RegisterCard.md)|  | 

### Return type

[**CardHolderAccount**](CardHolderAccount.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | A successfully registered card provides a reload of the account including the new card. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_card_status_request**
> Acknowledgement account_card_status_request(accountid, card_id, card_status)

Card Status

Updates the status of a card for processing. The following values are available  | Status | Description |  |--------|-------------| | Active | The card is active for processing and can be used for charging against with a valid token | | Inactive | The card is inactive for processing and cannot be used for processing, it will require reactivation before being used to charge | | Expired | The card has expired either due to the expiry date no longer being valid or due to a replacement card being issued | 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
card_id = 'card_id_example' # str | The id of the card that is presented by a call to retrieve a card holder account.
card_status = citypay.CardStatus() # CardStatus | 

    try:
        # Card Status
        api_response = api_instance.account_card_status_request(accountid, card_id, card_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_card_status_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **card_id** | **str**| The id of the card that is presented by a call to retrieve a card holder account. | 
 **card_status** | [**CardStatus**](CardStatus.md)|  | 

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
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | Acknowledges the card status has changed, returning 01 for a valid change or 00 for non valid change. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_change_contact_request**
> CardHolderAccount account_change_contact_request(accountid, contact_details)

Contact Details Update

Allows for the ability to change the contact details for an account.

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
contact_details = citypay.ContactDetails() # ContactDetails | 

    try:
        # Contact Details Update
        api_response = api_instance.account_change_contact_request(accountid, contact_details)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_change_contact_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **contact_details** | [**ContactDetails**](ContactDetails.md)|  | 

### Return type

[**CardHolderAccount**](CardHolderAccount.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | A revised account with the new details set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_create**
> CardHolderAccount account_create(account_create)

Account Create

Creates a new card holder account and initialises the account ready for adding cards.

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    account_create = citypay.AccountCreate() # AccountCreate | 

    try:
        # Account Create
        api_response = api_instance.account_create(account_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_create** | [**AccountCreate**](AccountCreate.md)|  | 

### Return type

[**CardHolderAccount**](CardHolderAccount.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | Provides an initialised account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_delete_request**
> Acknowledgement account_delete_request(accountid)

Account Deletion

Allows for the deletion of an account. The account will marked for deletion and subsequent purging. No further transactions will be alowed to be processed or actioned against this account. 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.

    try:
        # Account Deletion
        api_response = api_instance.account_delete_request(accountid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_delete_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 

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
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | An acknowledgment that the card holder account has been marked for deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_retrieve_request**
> CardHolderAccount account_retrieve_request(accountid)

Account Retrieval

Allows for the retrieval of a card holder account for the given `id`. Should duplicate accounts exist for the same `id`, the first account created with that `id` will be returned.  The account can be used for tokenisation processing by listing all cards assigned to the account. The returned cards will include all `active`, `inactive` and `expired` cards. This can be used to  enable a card holder to view their wallet and make constructive choices on which card to use. 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.

    try:
        # Account Retrieval
        api_response = api_instance.account_retrieve_request(accountid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_retrieve_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 

### Return type

[**CardHolderAccount**](CardHolderAccount.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | A card holder account that matches the account id provided in the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_status_request**
> Acknowledgement account_status_request(accountid, account_status)

Account Status

Updates the status of an account. An account can have the following statuses applied  | Status | Description | |--------|-------------| | Active | The account is active for processing | | Disabled | The account has been disabled and cannot be used for processing. The account will require reactivation to continue procesing | 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
account_status = citypay.AccountStatus() # AccountStatus | 

    try:
        # Account Status
        api_response = api_instance.account_status_request(accountid, account_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_status_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **account_status** | [**AccountStatus**](AccountStatus.md)|  | 

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
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | An acknowledgment that the card holder account status has been updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_request**
> Decision charge_request(charge_request)

Charge

A charge process obtains an authorisation using a tokenised value which represents a stored card  on a card holder account.  A card must previously be registered by calling `/account-register-card` with the card details  or retrieved using `/account-retrieve`  Tokens are generated whenever a previously registered list of cards are retrieved. Each token has, by design a  relatively short time to live of 30 minutes. This is both to safe guard the merchant and card holder from  replay attacks. Tokens are also restricted to your account, preventing malicious actors from stealing details for use elsewhere.    If a token is reused after it has expired it will be rejected and a new token will be required.   Tokenisation can be used for   - repeat authorisations on a previously stored card - easy authorisations just requiring CSC values to be entered - can be used for credential on file style payments - can require full 3-D Secure authentication to retain the liability shift - wallet style usage. 

### Example

* Api Key Authentication (cp-api-key):
```python
from __future__ import print_function
import time
import citypay
from citypay.rest import ApiException
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
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    charge_request = citypay.ChargeRequest() # ChargeRequest | 

    try:
        # Charge
        api_response = api_instance.charge_request(charge_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->charge_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **charge_request** | [**ChargeRequest**](ChargeRequest.md)|  | 

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
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**200** | A decision met by the result of the charge. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

