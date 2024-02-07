# PaylinkTokenStatusChangeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_token** | **str** | If nextToken is returned, there are more results available. The value of nextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.  | [optional] 
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


