# citypay.BatchProcessingApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_process_request**](BatchProcessingApi.md#batch_process_request) | **POST** /v6/batch/process | Batch Process Request
[**batch_report_request**](BatchProcessingApi.md#batch_report_request) | **POST** /v6/batch/retrieve | BatchReportRequest
[**check_batch_status_request**](BatchProcessingApi.md#check_batch_status_request) | **POST** /v6/batch/status | CheckBatchStatus


# **batch_process_request**
> ProcessBatchResponse batch_process_request(process_batch_request)

Batch Process Request

A batch process request is used to start the batch process workflow by uploading batch data and initialising a new batch for processing. Once validated the batch will be queued for processing and further updates can be received by a subsequent call to retrieve the batch status. 

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import batch_processing_api__
from citypay.model.process_batch_response import ProcessBatchResponse
from citypay.model.error import Error
from citypay.model.process_batch_request import ProcessBatchRequest
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
    api_instance = batch_processing_api__.BatchProcessingApi(api_client)
    process_batch_request = ProcessBatchRequest(
        batch_date=dateutil_parser('Thu Jan 02 00:00:00 UTC 2020').date(),
        batch_id=35,
        client_account_id="AC1",
        transactions=[
            BatchTransaction(
                account_id="aaabbb-cccddd-eee",
                amount=3600,
                identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
                merchantid=11223344,
            ),
        ],
    ) # ProcessBatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Batch Process Request
        api_response = api_instance.batch_process_request(process_batch_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling BatchProcessingApi->batch_process_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_batch_request** | [**ProcessBatchRequest**](ProcessBatchRequest.md)|  |

### Return type

[**ProcessBatchResponse**](ProcessBatchResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request to process a batch provided in the request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_report_request**
> BatchReportResponseModel batch_report_request(batch_report_request)

BatchReportRequest

The operation is used to retrieve a report of the result of a batch process.

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import batch_processing_api__
from citypay.model.batch_report_request import BatchReportRequest
from citypay.model.batch_report_response_model import BatchReportResponseModel
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
    api_instance = batch_processing_api__.BatchProcessingApi(api_client)
    batch_report_request = BatchReportRequest(
        batch_id=35,
        client_account_id="AC1",
    ) # BatchReportRequest | 

    # example passing only required values which don't have defaults set
    try:
        # BatchReportRequest
        api_response = api_instance.batch_report_request(batch_report_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling BatchProcessingApi->batch_report_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_report_request** | [**BatchReportRequest**](BatchReportRequest.md)|  |

### Return type

[**BatchReportResponseModel**](BatchReportResponseModel.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The report for a given batch. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_batch_status_request**
> CheckBatchStatusResponse check_batch_status_request(check_batch_status)

CheckBatchStatus

The operation is used to retrieve the status of a batch process.

### Example

* Api Key Authentication (cp-api-key):

```python
import time
import citypay
from citypay.api import batch_processing_api__
from citypay.model.check_batch_status_response import CheckBatchStatusResponse
from citypay.model.error import Error
from citypay.model.check_batch_status import CheckBatchStatus
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
    api_instance = batch_processing_api__.BatchProcessingApi(api_client)
    check_batch_status = CheckBatchStatus(
        batch_id=[
            78,
        ],
        client_account_id="AC1",
    ) # CheckBatchStatus | 

    # example passing only required values which don't have defaults set
    try:
        # CheckBatchStatus
        api_response = api_instance.check_batch_status_request(check_batch_status)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling BatchProcessingApi->check_batch_status_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_batch_status** | [**CheckBatchStatus**](CheckBatchStatus.md)|  |

### Return type

[**CheckBatchStatusResponse**](CheckBatchStatusResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status of batches provided in the request. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

