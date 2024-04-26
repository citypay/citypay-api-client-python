# MerchantBatchReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[MerchantBatchResponse]**](MerchantBatchResponse.md) |  | 
**count** | **int** | The count of items returned in this page. | [optional] 
**max_results** | **int** | The max results requested in this page. | [optional] 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 

## Example

```python
from citypay.models.merchant_batch_report_response import MerchantBatchReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantBatchReportResponse from a JSON string
merchant_batch_report_response_instance = MerchantBatchReportResponse.from_json(json)
# print the JSON string representation of the object
print MerchantBatchReportResponse.to_json()

# convert the object into a dict
merchant_batch_report_response_dict = merchant_batch_report_response_instance.to_dict()
# create an instance of MerchantBatchReportResponse from a dict
merchant_batch_report_response_form_dict = merchant_batch_report_response.from_dict(merchant_batch_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


