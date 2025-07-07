# WebHookSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** |  | [optional] 
**clientid** | **str** | The client id that the hook is being registered for.  | 
**live** | **bool** | Specifies if the key is to be used for production. Defaults to false.  | [optional] 
**merchant_id** | **List[int]** |  | [optional] 
**triggers** | **List[str]** |  | [optional] 

## Example

```python
from citypay.models.web_hook_subscription_request import WebHookSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookSubscriptionRequest from a JSON string
web_hook_subscription_request_instance = WebHookSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(WebHookSubscriptionRequest.to_json())

# convert the object into a dict
web_hook_subscription_request_dict = web_hook_subscription_request_instance.to_dict()
# create an instance of WebHookSubscriptionRequest from a dict
web_hook_subscription_request_from_dict = WebHookSubscriptionRequest.from_dict(web_hook_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


