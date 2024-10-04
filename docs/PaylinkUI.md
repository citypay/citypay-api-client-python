# PaylinkUI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_mandatory** | **bool** | whether the address is forced as mandatory. | [optional] 
**form_auto_complete** | **str** | specify the form autocomplete setting, default to on. If set to off the UI will set autocomplete&#x3D;\&quot;off\&quot; on the form level and prevent elements from adding it. | [optional] 
**ordering** | **int** | the logical ordering of the ui groups. | [optional] 
**postcode_mandatory** | **bool** | whether the postcode is forced as mandatory. | [optional] 

## Example

```python
from citypay.models.paylink_ui import PaylinkUI

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkUI from a JSON string
paylink_ui_instance = PaylinkUI.from_json(json)
# print the JSON string representation of the object
print(PaylinkUI.to_json())

# convert the object into a dict
paylink_ui_dict = paylink_ui_instance.to_dict()
# create an instance of PaylinkUI from a dict
paylink_ui_from_dict = PaylinkUI.from_dict(paylink_ui_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


