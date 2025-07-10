# WebHookChannelDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_channel_id** | **str** | The id of the channel to be deleted.  | 

## Example

```python
from citypay.models.web_hook_channel_delete_request import WebHookChannelDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookChannelDeleteRequest from a JSON string
web_hook_channel_delete_request_instance = WebHookChannelDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(WebHookChannelDeleteRequest.to_json())

# convert the object into a dict
web_hook_channel_delete_request_dict = web_hook_channel_delete_request_instance.to_dict()
# create an instance of WebHookChannelDeleteRequest from a dict
web_hook_channel_delete_request_from_dict = WebHookChannelDeleteRequest.from_dict(web_hook_channel_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


