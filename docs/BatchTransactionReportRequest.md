# BatchTransactionReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_results** | **int** | The maximum number of results to return in a single response. This value is used to limit the size of data returned by the API, enhancing performance and manageability. Values should be between 5 and 250. | [optional] 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 
**order_by** | **str** | Specifies the field by which results are ordered. Available fields are [trans_no,date_when,amount]. By default, fields are ordered by OrderByExpression(trans_no,ASC). To order in descending order, prefix with &#39;-&#39; or suffix with &#39; DESC&#39;. | [optional] 

## Example

```python
from citypay.models.batch_transaction_report_request import BatchTransactionReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTransactionReportRequest from a JSON string
batch_transaction_report_request_instance = BatchTransactionReportRequest.from_json(json)
# print the JSON string representation of the object
print(BatchTransactionReportRequest.to_json())

# convert the object into a dict
batch_transaction_report_request_dict = batch_transaction_report_request_instance.to_dict()
# create an instance of BatchTransactionReportRequest from a dict
batch_transaction_report_request_from_dict = BatchTransactionReportRequest.from_dict(batch_transaction_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


