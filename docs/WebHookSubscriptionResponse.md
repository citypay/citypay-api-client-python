# WebHookSubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_hook_id** | **str** | The id returned for the generated web hook subscription. | [optional] 

## Example

```python
from citypay.models.web_hook_subscription_response import WebHookSubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookSubscriptionResponse from a JSON string
web_hook_subscription_response_instance = WebHookSubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(WebHookSubscriptionResponse.to_json())

# convert the object into a dict
web_hook_subscription_response_dict = web_hook_subscription_response_instance.to_dict()
# create an instance of WebHookSubscriptionResponse from a dict
web_hook_subscription_response_from_dict = WebHookSubscriptionResponse.from_dict(web_hook_subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


