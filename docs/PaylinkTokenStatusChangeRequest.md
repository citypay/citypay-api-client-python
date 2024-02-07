# PaylinkTokenStatusChangeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | **datetime** | identifies the date and time to lookup changes after. | 
**max_results** | **int** | the maximum number of results between 5 and 250 to return. Default is 50. | [optional] 
**merchantid** | **int** | the merchant id to review tokens for. | 
**next_token** | **str** | the next token value when more results are available. | [optional] 
**order_by** | **List[str]** |  | [optional] 

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


