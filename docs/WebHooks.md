# citypay.WebHooks

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**web_hook_channel_create_request**](WebHooks.md#web_hook_channel_create_request) | **POST** /hooks/channel/create | Web Hook Channel Create Request
[**web_hook_channel_delete_request**](WebHooks.md#web_hook_channel_delete_request) | **POST** /hooks/channel/delete | Web Hook Channel Delete Request
[**web_hook_subscription_request**](WebHooks.md#web_hook_subscription_request) | **POST** /hooks/subscribe | Web Hook Subscription Request
[**web_hook_unsubscribe_request**](WebHooks.md#web_hook_unsubscribe_request) | **POST** /hooks/unsubscribe | Web Hook Unsubscribe Request


# **web_hook_channel_create_request**
> WebHookChannelCreateResponse web_hook_channel_create_request(web_hook_channel_create_request)

Web Hook Channel Create Request

A WebHookChannel is required to establish a connection with our event notification system. The channel serves as the
communication link between your application and the events generated by the payment gateway. When you register a
WebHookChannel, you're defining the endpoint where we will deliver notifications, such as payment events.

The WebHookChannel encapsulates important configuration details like the endpoint type (e.g., HTTP), the client ID,
and security parameters. However, the channel itself does not specify which events will
be sent but should be considered as the pipeline for receiving those events. After registering a channel, you can then
configure triggers separately using a subscription request to define which specific payment events
should flow through this channel.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.web_hook_channel_create_request import WebHookChannelCreateRequest
from citypay.models.web_hook_channel_create_response import WebHookChannelCreateResponse
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
    api_instance = citypay.WebHooks(api_client)
    web_hook_channel_create_request = citypay.WebHookChannelCreateRequest() # WebHookChannelCreateRequest | 

    try:
        # Web Hook Channel Create Request
        api_response = api_instance.web_hook_channel_create_request(web_hook_channel_create_request)
        print("The response of WebHooks->web_hook_channel_create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHooks->web_hook_channel_create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_channel_create_request** | [**WebHookChannelCreateRequest**](WebHookChannelCreateRequest.md)|  | 

### Return type

[**WebHookChannelCreateResponse**](WebHookChannelCreateResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created a new web hook channel. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_channel_delete_request**
> Acknowledgement web_hook_channel_delete_request(web_hook_channel_delete_request)

Web Hook Channel Delete Request

The WebHookChannelDeleteRequest allows you to remove an existing WebHookChannel from the event notification system. 
By specifying the channel ID, you can deactivate the communication link between your application and the payment 
gateway’s event system. Deleting a channel effectively halts any further notifications being sent to the associated 
endpoint, ensuring that no additional events are processed through that channel.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.web_hook_channel_delete_request import WebHookChannelDeleteRequest
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
    api_instance = citypay.WebHooks(api_client)
    web_hook_channel_delete_request = citypay.WebHookChannelDeleteRequest() # WebHookChannelDeleteRequest | 

    try:
        # Web Hook Channel Delete Request
        api_response = api_instance.web_hook_channel_delete_request(web_hook_channel_delete_request)
        print("The response of WebHooks->web_hook_channel_delete_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHooks->web_hook_channel_delete_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_channel_delete_request** | [**WebHookChannelDeleteRequest**](WebHookChannelDeleteRequest.md)|  | 

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
**200** | Result of deleting the web hook channel. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_subscription_request**
> WebHookSubscriptionResponse web_hook_subscription_request(web_hook_subscription_request)

Web Hook Subscription Request

The WebHookSubscriptionRequest is used to define and activate event triggers for an existing WebHookChannel. This 
request specifies the events or conditions that your application wants to be notified about, ensuring that only 
relevant event data flows through the channel.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.web_hook_subscription_request import WebHookSubscriptionRequest
from citypay.models.web_hook_subscription_response import WebHookSubscriptionResponse
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
    api_instance = citypay.WebHooks(api_client)
    web_hook_subscription_request = citypay.WebHookSubscriptionRequest() # WebHookSubscriptionRequest | 

    try:
        # Web Hook Subscription Request
        api_response = api_instance.web_hook_subscription_request(web_hook_subscription_request)
        print("The response of WebHooks->web_hook_subscription_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHooks->web_hook_subscription_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_subscription_request** | [**WebHookSubscriptionRequest**](WebHookSubscriptionRequest.md)|  | 

### Return type

[**WebHookSubscriptionResponse**](WebHookSubscriptionResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Subscribe a new web hook. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hook_unsubscribe_request**
> Acknowledgement web_hook_unsubscribe_request(web_hook_unsubscribe_request)

Web Hook Unsubscribe Request

The WebHookUnsubscribeRequest is used to remove an existing webhook subscription from the system. This allows clients 
to stop receiving event notifications for specific webhook subscriptions that are no longer needed.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.web_hook_unsubscribe_request import WebHookUnsubscribeRequest
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
    api_instance = citypay.WebHooks(api_client)
    web_hook_unsubscribe_request = citypay.WebHookUnsubscribeRequest() # WebHookUnsubscribeRequest | 

    try:
        # Web Hook Unsubscribe Request
        api_response = api_instance.web_hook_unsubscribe_request(web_hook_unsubscribe_request)
        print("The response of WebHooks->web_hook_unsubscribe_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHooks->web_hook_unsubscribe_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_unsubscribe_request** | [**WebHookUnsubscribeRequest**](WebHookUnsubscribeRequest.md)|  | 

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
**200** | Unsubscribes a web hook. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

