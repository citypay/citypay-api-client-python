# TransactionReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** |  | [optional] 
**var_from** | **datetime** | The date and time of transactions from. | 
**include_authorised** | **bool** | Include transactions fully authorised in the results. | [optional] 
**include_cancelled** | **bool** | Include transactions that were cancelled in the results. | [optional] 
**include_declined** | **bool** | Include transactions that were declined or not honoured in the results. | [optional] 
**include_rejected** | **bool** | Include transactions that were rejected due to validation issues. | [optional] 
**include_unfulfilled** | **bool** | Includes transactions that were initiated but not completed—e.g. those pending authentication or challenge responses that were never fulfilled. | [optional] 
**max_results** | **int** | The maximum number of results to return in a single response. This value is used to limit the size of data returned by the API, enhancing performance and manageability. Values should be between 5 and 250. | [optional] 
**merchantid** | **int** | The merchant id of the transactions to review. | 
**mode** | **str** | Defines a preset profile for the level of detail in the returned fields. This simplifies response formatting for common use cases. Available values:  - &#x60;basic&#x60; (default): Returns a minimal, high-level view with key fields for reporting or dashboards.  - &#x60;extended&#x60;: Adds fields useful for customer support, settlement analysis, or more in-depth tracking, while still omitting sensitive personal or low-level fields.  - &#x60;full&#x60;: Returns all available transaction fields, including internal flags, personal data (where applicable), and detailed metadata. Use with care.  | [optional] 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 
**order_by** | **str** | Specifies the field by which results are ordered. Available fields are [trans_no,date_when,amount]. By default, fields are ordered by OrderByExpression(trans_no,ASC). To order in descending order, prefix with &#39;-&#39; or suffix with &#39; DESC&#39;. | [optional] 
**pii_masked** | **bool** | Defines whether personal identifiable information is masked which it is by default. | [optional] 
**type_refund** | **bool** | Include refunds in the results. | [optional] 
**type_sale** | **bool** | Include sales in the results. | [optional] 
**type_verify** | **bool** | Include verifications in the results. | [optional] 
**until** | **datetime** | The date and time of transactions until. | 

## Example

```python
from citypay.models.transaction_report_request import TransactionReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReportRequest from a JSON string
transaction_report_request_instance = TransactionReportRequest.from_json(json)
# print the JSON string representation of the object
print(TransactionReportRequest.to_json())

# convert the object into a dict
transaction_report_request_dict = transaction_report_request_instance.to_dict()
# create an instance of TransactionReportRequest from a dict
transaction_report_request_from_dict = TransactionReportRequest.from_dict(transaction_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


