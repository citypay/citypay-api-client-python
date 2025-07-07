# WebHookChannelCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_name** | **str** | The name of the channel we are creating.  | 
**clientid** | **str** | The client id that the hook is being registered for.  | 
**config** | [**HttpConfig**](HttpConfig.md) |  | 
**endpoint_id** | **str** | The id of the endpoint being used. The channel configuration is dependant upon the endpoint type.  | 

## Example

```python
from citypay.models.web_hook_channel_create_request import WebHookChannelCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookChannelCreateRequest from a JSON string
web_hook_channel_create_request_instance = WebHookChannelCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WebHookChannelCreateRequest.to_json())

# convert the object into a dict
web_hook_channel_create_request_dict = web_hook_channel_create_request_instance.to_dict()
# create an instance of WebHookChannelCreateRequest from a dict
web_hook_channel_create_request_from_dict = WebHookChannelCreateRequest.from_dict(web_hook_channel_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


