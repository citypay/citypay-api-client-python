# EventDataModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_end_date** | **date** | The date when the event ends in ISO format (yyyy-MM-dd). | [optional] 
**event_id** | **str** | An id of the event. | [optional] 
**event_organiser_id** | **str** | An id of the event organiser. | [optional] 
**event_start_date** | **date** | The date when the event starts in ISO format (yyyy-MM-dd). | [optional] 
**payment_type** | **str** | The type of payment such as &#x60;deposit&#x60; or &#x60;balance&#x60;. | [optional] 

## Example

```python
from citypay.models.event_data_model import EventDataModel

# TODO update the JSON string below
json = "{}"
# create an instance of EventDataModel from a JSON string
event_data_model_instance = EventDataModel.from_json(json)
# print the JSON string representation of the object
print EventDataModel.to_json()

# convert the object into a dict
event_data_model_dict = event_data_model_instance.to_dict()
# create an instance of EventDataModel from a dict
event_data_model_form_dict = event_data_model.from_dict(event_data_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


