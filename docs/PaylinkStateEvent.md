# PaylinkStateEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datetime** | **datetime** | the date and time of the event. | [optional] 
**message** | **str** | a message associated with the event. | [optional] 
**state** | **str** | The name of the event that was actioned. | [optional] 

## Example

```python
from citypay.models.paylink_state_event import PaylinkStateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkStateEvent from a JSON string
paylink_state_event_instance = PaylinkStateEvent.from_json(json)
# print the JSON string representation of the object
print PaylinkStateEvent.to_json()

# convert the object into a dict
paylink_state_event_dict = paylink_state_event_instance.to_dict()
# create an instance of PaylinkStateEvent from a dict
paylink_state_event_form_dict = paylink_state_event.from_dict(paylink_state_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


