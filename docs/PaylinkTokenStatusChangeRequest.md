# PaylinkTokenStatusChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **datetime** | identifies the date and time to lookup changes after. | 
**max_results** | **int** | The maximum number of results to return in a single response. This value is used to limit the size of data returned by the API, enhancing performance and manageability. Values should be between 5 and 250. | [optional] 
**merchantid** | **int** | the merchant id to review tokens for. | 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 
**order_by** | **str** | Specifies the field by which results are ordered. Available fields are [p.id]. By default, fields are ordered by OrderByExpression(p.id,ASC). To order in descending order, prefix with &#39;-&#39; or suffix with &#39; DESC&#39;. | [optional] 

## Example

```python
from citypay.models.paylink_token_status_change_request import PaylinkTokenStatusChangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkTokenStatusChangeRequest from a JSON string
paylink_token_status_change_request_instance = PaylinkTokenStatusChangeRequest.from_json(json)
# print the JSON string representation of the object
print PaylinkTokenStatusChangeRequest.to_json()

# convert the object into a dict
paylink_token_status_change_request_dict = paylink_token_status_change_request_instance.to_dict()
# create an instance of PaylinkTokenStatusChangeRequest from a dict
paylink_token_status_change_request_form_dict = paylink_token_status_change_request.from_dict(paylink_token_status_change_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


