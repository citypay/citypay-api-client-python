# PaylinkCustomParam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_mode** | **str** | The type of entry mode. A value of &#39;pre&#39; will pre-render the custom parameter before the payment screen. Any other value will result in the custom parameter being displayed on the payment screen. | [optional] 
**field_type** | **str** | the type of html5 field, defaults to &#39;text&#39;. Other options are &#39;dob&#39; for a date of birth series of select list entry. | [optional] 
**group** | **str** | a group the parameter is linked with, allows for grouping with a title. | [optional] 
**label** | **str** | a label to show alongside the input. | [optional] 
**locked** | **bool** | whether the parameter is locked from entry. | [optional] 
**name** | **str** | the name of the custom parameter used to converse with the submitter. | 
**order** | **int** | an index order for the parameter. | [optional] 
**pattern** | **str** | a regex pattern to validate the custom parameter with. | [optional] 
**placeholder** | **str** | a placehold value to display in the input. | [optional] 
**required** | **bool** | whether the field is required. | [optional] 
**value** | **str** | a default value for the field. | [optional] 

## Example

```python
from citypay.models.paylink_custom_param import PaylinkCustomParam

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkCustomParam from a JSON string
paylink_custom_param_instance = PaylinkCustomParam.from_json(json)
# print the JSON string representation of the object
print PaylinkCustomParam.to_json()

# convert the object into a dict
paylink_custom_param_dict = paylink_custom_param_instance.to_dict()
# create an instance of PaylinkCustomParam from a dict
paylink_custom_param_form_dict = paylink_custom_param.from_dict(paylink_custom_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


