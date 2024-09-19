# citypay.ReportingApi

All URIs are relative to *https://api.citypay.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batched_transaction_report_request**](ReportingApi.md#batched_transaction_report_request) | **POST** /v6/merchant-batch/{merchantid}/{batch_no}/transactions | Batch Transaction Report Request
[**merchant_batch_report_request**](ReportingApi.md#merchant_batch_report_request) | **POST** /v6/merchant-batch/report | Merchant Batch Report Request
[**merchant_batch_request**](ReportingApi.md#merchant_batch_request) | **GET** /v6/merchant-batch/{merchantid}/{batch_no} | Merchant Batch Request
[**remittance_range_report**](ReportingApi.md#remittance_range_report) | **POST** /v6/remittance/report/{clientid} | Remittance Report Request
[**remittance_report_request**](ReportingApi.md#remittance_report_request) | **GET** /v6/remittance/report/{clientid}/{date} | Remittance Date Report Request


# **batched_transaction_report_request**
> BatchTransactionReportResponse batched_transaction_report_request(merchantid, batch_no, batch_transaction_report_request)

Batch Transaction Report Request

Retrieves transactions available on a given batch.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.batch_transaction_report_request import BatchTransactionReportRequest
from citypay.models.batch_transaction_report_response import BatchTransactionReportResponse
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
    api_instance = citypay.ReportingApi(api_client)
    merchantid = 56 # int | A merchant ID (MID) for which data is requested. This field allows for filtering of the request by a specific merchant account.
    batch_no = 'batch_no_example' # str | The batch number that is being requested.
    batch_transaction_report_request = citypay.BatchTransactionReportRequest() # BatchTransactionReportRequest | 

    try:
        # Batch Transaction Report Request
        api_response = api_instance.batched_transaction_report_request(merchantid, batch_no, batch_transaction_report_request)
        print("The response of ReportingApi->batched_transaction_report_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->batched_transaction_report_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantid** | **int**| A merchant ID (MID) for which data is requested. This field allows for filtering of the request by a specific merchant account. | 
 **batch_no** | **str**| The batch number that is being requested. | 
 **batch_transaction_report_request** | [**BatchTransactionReportRequest**](BatchTransactionReportRequest.md)|  | 

### Return type

[**BatchTransactionReportResponse**](BatchTransactionReportResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A report of the transactions listed on batches. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_batch_report_request**
> MerchantBatchReportResponse merchant_batch_report_request(merchant_batch_report_request)

Merchant Batch Report Request

Retrieves a report of merchant batches within a specified date range.  Batches, which aggregate daily processing activities, are typically generated at `00:00` each day.  These batches play a crucial role in the settlement of funds by summarising daily transactions. 

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.merchant_batch_report_request import MerchantBatchReportRequest
from citypay.models.merchant_batch_report_response import MerchantBatchReportResponse
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
    api_instance = citypay.ReportingApi(api_client)
    merchant_batch_report_request = citypay.MerchantBatchReportRequest() # MerchantBatchReportRequest | 

    try:
        # Merchant Batch Report Request
        api_response = api_instance.merchant_batch_report_request(merchant_batch_report_request)
        print("The response of ReportingApi->merchant_batch_report_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->merchant_batch_report_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_batch_report_request** | [**MerchantBatchReportRequest**](MerchantBatchReportRequest.md)|  | 

### Return type

[**MerchantBatchReportResponse**](MerchantBatchReportResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A report of the batches generated. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merchant_batch_request**
> MerchantBatchResponse merchant_batch_request(merchantid, batch_no)

Merchant Batch Request

Retrieves a report of merchant a merchant batch for a specified batch number.

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.merchant_batch_response import MerchantBatchResponse
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
    api_instance = citypay.ReportingApi(api_client)
    merchantid = 56 # int | A merchant ID (MID) for which data is requested. This field allows for filtering of the request by a specific merchant account.
    batch_no = 'batch_no_example' # str | The batch number that is being requested.

    try:
        # Merchant Batch Request
        api_response = api_instance.merchant_batch_request(merchantid, batch_no)
        print("The response of ReportingApi->merchant_batch_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->merchant_batch_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchantid** | **int**| A merchant ID (MID) for which data is requested. This field allows for filtering of the request by a specific merchant account. | 
 **batch_no** | **str**| The batch number that is being requested. | 

### Return type

[**MerchantBatchResponse**](MerchantBatchResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A report of a single batch. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remittance_range_report**
> RemittanceReportResponse remittance_range_report(clientid, remittance_report_request)

Remittance Report Request

Fetches remittance reports for financial transactions within a specified date range, covering all client-related activities. This report consolidates all batches disbursed to a client, with each remittance summarising the aggregation of batches leading up to settlement. Additionally, the net remittance amount presented in the final settlement will reflect any deductions made by the acquirer. 

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.remittance_report_request import RemittanceReportRequest
from citypay.models.remittance_report_response import RemittanceReportResponse
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
    api_instance = citypay.ReportingApi(api_client)
    clientid = 'clientid_example' # str | A client Id for which data is requested.
    remittance_report_request = citypay.RemittanceReportRequest() # RemittanceReportRequest | 

    try:
        # Remittance Report Request
        api_response = api_instance.remittance_range_report(clientid, remittance_report_request)
        print("The response of ReportingApi->remittance_range_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->remittance_range_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **str**| A client Id for which data is requested. | 
 **remittance_report_request** | [**RemittanceReportRequest**](RemittanceReportRequest.md)|  | 

### Return type

[**RemittanceReportResponse**](RemittanceReportResponse.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: application/json, text/xml
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A report of financial remittance data for a range of dates. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remittance_report_request**
> RemittedClientData remittance_report_request(clientid, var_date)

Remittance Date Report Request

Fetches remittance reports for financial transactions for a given date,  covering all client-related activities. This report consolidates all batches disbursed to a  client, with each remittance summarising the aggregation of batches leading up to settlement.  Additionally, the net remittance amount presented in the final settlement will reflect any  deductions made by the acquirer.  The process also supports the notion of *today* deferring the date to today's date or *latest* reflecting the latest remittance date available. 

### Example

* Api Key Authentication (cp-api-key):

```python
import citypay
from citypay.models.remitted_client_data import RemittedClientData
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
    api_instance = citypay.ReportingApi(api_client)
    clientid = 'clientid_example' # str | A client Id for which data is requested.
    var_date = 'var_date_example' # str | Date (YYYY-MM-DD) to filter the request for.

    try:
        # Remittance Date Report Request
        api_response = api_instance.remittance_report_request(clientid, var_date)
        print("The response of ReportingApi->remittance_report_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->remittance_report_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientid** | **str**| A client Id for which data is requested. | 
 **var_date** | **str**| Date (YYYY-MM-DD) to filter the request for. | 

### Return type

[**RemittedClientData**](RemittedClientData.md)

### Authorization

[cp-api-key](../README.md#cp-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A report of the financial remittance data for a given date. |  -  |
**400** | Bad Request. Should the incoming data not be validly determined. |  -  |
**401** | Unauthorized. No api key has been provided and is required for this operation. |  -  |
**403** | Forbidden. The api key was provided and understood but is either incorrect or does not have permission to access the account provided on the request. |  -  |
**422** | Unprocessable Entity. Should a failure occur that prevents processing of the API call. |  -  |
**500** | Server Error. The server was unable to complete the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

