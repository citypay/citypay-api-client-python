# PaylinkTokenStatusChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The count of items returned in this page. | [optional] 
**max_results** | **int** | The max results requested in this page. | [optional] 
**next_token** | **str** | A token that identifies the starting point of the page of results to be returned. An empty value indicates the start of the dataset. When supplied, it is validated and used to fetch the subsequent page of results. This token is typically obtained from the response of a previous pagination request. | [optional] 
**tokens** | [**List[PaylinkTokenStatus]**](PaylinkTokenStatus.md) |  | 

## Example

```python
from citypay.models.paylink_token_status_change_response import PaylinkTokenStatusChangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkTokenStatusChangeResponse from a JSON string
paylink_token_status_change_response_instance = PaylinkTokenStatusChangeResponse.from_json(json)
# print the JSON string representation of the object
print PaylinkTokenStatusChangeResponse.to_json()

# convert the object into a dict
paylink_token_status_change_response_dict = paylink_token_status_change_response_instance.to_dict()
# create an instance of PaylinkTokenStatusChangeResponse from a dict
paylink_token_status_change_response_form_dict = paylink_token_status_change_response.from_dict(paylink_token_status_change_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


