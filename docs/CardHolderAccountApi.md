# citypay.CardHolderAccountApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_card_delete_request**](CardHolderAccountApi.md#account_card_delete_request) | **DELETE** /v6/account/{accountid}/card/{cardId} | Card Deletion
[**account_card_register_request**](CardHolderAccountApi.md#account_card_register_request) | **POST** /v6/account/{accountid}/register | Card Registration
[**account_card_status_request**](CardHolderAccountApi.md#account_card_status_request) | **POST** /v6/account/{accountid}/card/{cardId}/status | Card Status
[**account_change_contact_request**](CardHolderAccountApi.md#account_change_contact_request) | **POST** /v6/account/{accountid}/contact | Contact Details Update
[**account_create**](CardHolderAccountApi.md#account_create) | **POST** /v6/account/create | Account Create
[**account_delete_request**](CardHolderAccountApi.md#account_delete_request) | **DELETE** /v6/account/{accountid} | Account Deletion
[**account_exists_request**](CardHolderAccountApi.md#account_exists_request) | **GET** /v6/account-exists/{accountid} | Account Exists
[**account_retrieve_request**](CardHolderAccountApi.md#account_retrieve_request) | **GET** /v6/account/{accountid} | Account Retrieval
[**account_status_request**](CardHolderAccountApi.md#account_status_request) | **POST** /v6/account/{accountid}/status | Account Status
[**charge_request**](CardHolderAccountApi.md#charge_request) | **POST** /v6/charge | Charge


# **account_card_delete_request**
> Acknowledgement account_card_delete_request(accountid, card_id, force=force)

Card Deletion

Deletes a card from the account. The card will be marked for deletion before a subsequent
purge will clear the card permanently.


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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
    card_id = 'card_id_example' # str | The id of the card that is presented by a call to retrieve a card holder account.
    force = True # bool | Requests that the item is forced immediately. (optional)

    try:
        # Card Deletion
        api_response = api_instance.account_card_delete_request(accountid, card_id, force=force)
        print("The response of CardHolderAccountApi->account_card_delete_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardHolderAccountApi->account_card_delete_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 
 **card_id** | **str**| The id of the card that is presented by a call to retrieve a card holder account. | 
 **force** | **bool**| Requests that the item is forced immediately. | [optional] 

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
**200** | Acknowledges the card has been requested for deletion. A response code of &#x60;001&#x60; is returned if the account is available for deletion otherwise an error code is returned. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_card_register_request**
> CardHolderAccount account_card_register_request(accountid, register_card)

Card Registration

Allows for a card to be registered for the account. The card will be added for future 
processing and will be available as a tokenised value for future processing.

The card will be validated for

0. Being a valid card number (luhn check)
0. Having a valid expiry date
0. Being a valid bin value.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.card_holder_account import CardHolderAccount
from citypay.models.register_card import RegisterCard
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
    register_card = citypay.RegisterCard() # RegisterCard | 

    try:
        # Card Registration
        api_response = api_instance.account_card_register_request(accountid, register_card)
        print("The response of CardHolderAccountApi->account_card_register_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | A successfully registered card provides a reload of the account including the new card. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_card_status_request**
> Acknowledgement account_card_status_request(accountid, card_id, card_status)

Card Status

Updates the status of a card for processing. The following values are available

| Status | Description | 
|--------|-------------|
| Active | The card is active for processing and can be used for charging against with a valid token |
| Inactive | The card is inactive for processing and cannot be used for processing, it will require reactivation before being used to charge |
| Expired | The card has expired either due to the expiry date no longer being valid or due to a replacement card being issued |


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.card_status import CardStatus
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
    card_id = 'card_id_example' # str | The id of the card that is presented by a call to retrieve a card holder account.
    card_status = citypay.CardStatus() # CardStatus | 

    try:
        # Card Status
        api_response = api_instance.account_card_status_request(accountid, card_id, card_status)
        print("The response of CardHolderAccountApi->account_card_status_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | Acknowledges the card status has changed, returning a response code of &#x60;001&#x60; for a valid change or &#x60;000&#x60; for a non valid change. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_change_contact_request**
> CardHolderAccount account_change_contact_request(accountid, contact_details)

Contact Details Update

Allows for the ability to change the contact details for an account.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.card_holder_account import CardHolderAccount
from citypay.models.contact_details import ContactDetails
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
    contact_details = citypay.ContactDetails() # ContactDetails | 

    try:
        # Contact Details Update
        api_response = api_instance.account_change_contact_request(accountid, contact_details)
        print("The response of CardHolderAccountApi->account_change_contact_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | A revised account with the new details set. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_create**
> CardHolderAccount account_create(account_create)

Account Create

Creates a new card holder account and initialises the account ready for adding cards.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.account_create import AccountCreate
from citypay.models.card_holder_account import CardHolderAccount
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    account_create = citypay.AccountCreate() # AccountCreate | 

    try:
        # Account Create
        api_response = api_instance.account_create(account_create)
        print("The response of CardHolderAccountApi->account_create:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | Provides an initialised account. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_delete_request**
> Acknowledgement account_delete_request(accountid)

Account Deletion

Allows for the deletion of an account. The account will marked for deletion and subsequent purging. No further
transactions will be alowed to be processed or actioned against this account.


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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.

    try:
        # Account Deletion
        api_response = api_instance.account_delete_request(accountid)
        print("The response of CardHolderAccountApi->account_delete_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | An acknowledgment code of &#x60;001&#x60; that the card holder account has been marked for deletion. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_exists_request**
> Exists account_exists_request(accountid)

Account Exists

Checks that an account exists and is active by providing the account id as a url parameter.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.exists import Exists
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.

    try:
        # Account Exists
        api_response = api_instance.account_exists_request(accountid)
        print("The response of CardHolderAccountApi->account_exists_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CardHolderAccountApi->account_exists_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountid** | **str**| The account id that refers to the customer&#39;s account no. This value will have been provided when setting up the card holder account. | 

### Return type

[**Exists**](Exists.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response model determining whether the account exists, if exists is true, a last modified date of the account is also provided. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_retrieve_request**
> CardHolderAccount account_retrieve_request(accountid)

Account Retrieval

Allows for the retrieval of a card holder account for the given `id`. Should duplicate accounts exist
for the same `id`, the first account created with that `id` will be returned.

The account can be used for tokenisation processing by listing all cards assigned to the account.
The returned cards will include all `active`, `inactive` and `expired` cards. This can be used to 
enable a card holder to view their wallet and make constructive choices on which card to use.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.card_holder_account import CardHolderAccount
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.

    try:
        # Account Retrieval
        api_response = api_instance.account_retrieve_request(accountid)
        print("The response of CardHolderAccountApi->account_retrieve_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | A card holder account that matches the account id provided in the request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_status_request**
> Acknowledgement account_status_request(accountid, account_status)

Account Status

Updates the status of an account. An account can have the following statuses applied

| Status | Description |
|--------|-------------|
| Active | The account is active for processing |
| Disabled | The account has been disabled and cannot be used for processing. The account will require reactivation to continue procesing |


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.account_status import AccountStatus
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
    account_status = citypay.AccountStatus() # AccountStatus | 

    try:
        # Account Status
        api_response = api_instance.account_status_request(accountid, account_status)
        print("The response of CardHolderAccountApi->account_status_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | An acknowledgment that the card holder account status has been updated.&lt;/br&gt;&lt;/br&gt;A response code of &#x60;001&#x60; is returned if the request was accepted or no change required.&lt;/br&gt;&lt;/br&gt;A response code of &#x60;000&#x60; is returned if the request contains invalid data. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **charge_request**
> Decision charge_request(charge_request)

Charge

A charge process obtains an authorisation using a tokenised value which represents a stored card 
on a card holder account. 
A card must previously be registered by calling `/account-register-card` with the card details 
or retrieved using `/account-retrieve`

Tokens are generated whenever a previously registered list of cards are retrieved. Each token has, by design a 
relatively short time to live of 30 minutes. This is both to safe guard the merchant and card holder from 
replay attacks. Tokens are also restricted to your account, preventing malicious actors from stealing details
for use elsewhere.  

If a token is reused after it has expired it will be rejected and a new token will be required.
 
Tokenisation can be used for
 
- repeat authorisations on a previously stored card
- easy authorisations just requiring CSC values to be entered
- can be used for credential on file style payments
- can require full 3-D Secure authentication to retain the liability shift
- wallet style usage
 

_Should an account be used with 3DSv2, the card holder name should also be stored alongside the card as this is a
required field with both Visa and MasterCard for risk analysis._.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.charge_request import ChargeRequest
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
    api_instance = citypay.CardHolderAccountApi(api_client)
    charge_request = citypay.ChargeRequest() # ChargeRequest | 

    try:
        # Charge
        api_response = api_instance.charge_request(charge_request)
        print("The response of CardHolderAccountApi->charge_request:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | A decision met by the result of the charge. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

