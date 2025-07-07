# WebHookChannelCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | The resultant config object. | [optional] 
**endpoint_id** | **str** | The id of the endpoint being used. | [optional] 
**web_channel_id** | **str** | The id returned for the generated channel. | [optional] 

## Example

```python
from citypay.models.web_hook_channel_create_response import WebHookChannelCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebHookChannelCreateResponse from a JSON string
web_hook_channel_create_response_instance = WebHookChannelCreateResponse.from_json(json)
# print the JSON string representation of the object
print(WebHookChannelCreateResponse.to_json())

# convert the object into a dict
web_hook_channel_create_response_dict = web_hook_channel_create_response_instance.to_dict()
# create an instance of WebHookChannelCreateResponse from a dict
web_hook_channel_create_response_from_dict = WebHookChannelCreateResponse.from_dict(web_hook_channel_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


