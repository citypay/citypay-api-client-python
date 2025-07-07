# WebHookUnsubscribeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientid** | **str** | The client id that the hook is registered for.  | 
**web_hook_id** | **str** | The webhook id that is to be removed.  | 

## Example

```python
from citypay.models.web_hook_unsubscribe_request import WebHookUnsubscribeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookUnsubscribeRequest from a JSON string
web_hook_unsubscribe_request_instance = WebHookUnsubscribeRequest.from_json(json)
# print the JSON string representation of the object
print(WebHookUnsubscribeRequest.to_json())

# convert the object into a dict
web_hook_unsubscribe_request_dict = web_hook_unsubscribe_request_instance.to_dict()
# create an instance of WebHookUnsubscribeRequest from a dict
web_hook_unsubscribe_request_from_dict = WebHookUnsubscribeRequest.from_dict(web_hook_unsubscribe_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


