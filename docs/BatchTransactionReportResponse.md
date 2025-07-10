# BatchTransactionReportResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The count of items returned in this page. | [optional] 
**data** | [**List[AuthReference]**](AuthReference.md) |  | 
**max_results** | **int** | The max results requested in this page. | [optional] 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 

## Example

```python
from citypay.models.batch_transaction_report_response import BatchTransactionReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTransactionReportResponse from a JSON string
batch_transaction_report_response_instance = BatchTransactionReportResponse.from_json(json)
# print the JSON string representation of the object
print(BatchTransactionReportResponse.to_json())

# convert the object into a dict
batch_transaction_report_response_dict = batch_transaction_report_response_instance.to_dict()
# create an instance of BatchTransactionReportResponse from a dict
batch_transaction_report_response_from_dict = BatchTransactionReportResponse.from_dict(batch_transaction_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


