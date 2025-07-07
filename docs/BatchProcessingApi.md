# citypay.BatchProcessingApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_process_request**](BatchProcessingApi.md#batch_process_request) | **POST** /v6/batch/process | Batch Process Request
[**batch_retrieve_request**](BatchProcessingApi.md#batch_retrieve_request) | **POST** /v6/batch/retrieve | Batch Retrieve Request
[**check_batch_status_request**](BatchProcessingApi.md#check_batch_status_request) | **POST** /v6/batch/status | Check Batch Status


# **batch_process_request**
> ProcessBatchResponse batch_process_request(process_batch_request)

Batch Process Request

A batch process request is used to start the batch process workflow by uploading batch
data and initialising a new batch for processing. Once validated the batch will be queued
for processing and further updates can be received by a subsequent call to retrieve the batch
status.


### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.process_batch_request import ProcessBatchRequest
from citypay.models.process_batch_response import ProcessBatchResponse
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
    api_instance = citypay.BatchProcessingApi(api_client)
    process_batch_request = citypay.ProcessBatchRequest() # ProcessBatchRequest | 

    try:
        # Batch Process Request
        api_response = api_instance.batch_process_request(process_batch_request)
        print("The response of BatchProcessingApi->batch_process_request:\n")
        pprint(api_response)
    except Exception as e:
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

# **batch_retrieve_request**
> BatchReportResponseModel batch_retrieve_request(batch_report_request)

Batch Retrieve Request

Obtains a batch and installment (BIS) report for a given batch id.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.batch_report_request import BatchReportRequest
from citypay.models.batch_report_response_model import BatchReportResponseModel
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
    api_instance = citypay.BatchProcessingApi(api_client)
    batch_report_request = citypay.BatchReportRequest() # BatchReportRequest | 

    try:
        # Batch Retrieve Request
        api_response = api_instance.batch_retrieve_request(batch_report_request)
        print("The response of BatchProcessingApi->batch_retrieve_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatchProcessingApi->batch_retrieve_request: %s\n" % e)
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

Check Batch Status

The operation is used to retrieve the status of a batch process.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.check_batch_status import CheckBatchStatus
from citypay.models.check_batch_status_response import CheckBatchStatusResponse
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
    api_instance = citypay.BatchProcessingApi(api_client)
    check_batch_status = citypay.CheckBatchStatus() # CheckBatchStatus | 

    try:
        # Check Batch Status
        api_response = api_instance.check_batch_status_request(check_batch_status)
        print("The response of BatchProcessingApi->check_batch_status_request:\n")
        pprint(api_response)
    except Exception as e:
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

