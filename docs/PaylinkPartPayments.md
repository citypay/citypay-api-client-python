# PaylinkPartPayments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **str** | Determines if part payments is enabled. Default is false. | [optional] 
**floor** | **str** | The floor amount specifies a value that the minimum rate cannot go under. If 0 the amount of min rate is applied. | [optional] 
**max** | **str** | a maximum percentage to charge i.e. 90%. | [optional] 
**max_rate** | **str** | a rate as fixed or percentage. | [optional] 
**min** | **str** | a minimum percentage to charge i.e. 10. | [optional] 
**min_rate** | **str** | a rate as fixed or percentage. | [optional] 

## Example

```python
from citypay.models.paylink_part_payments import PaylinkPartPayments

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkPartPayments from a JSON string
paylink_part_payments_instance = PaylinkPartPayments.from_json(json)
# print the JSON string representation of the object
print PaylinkPartPayments.to_json()

# convert the object into a dict
paylink_part_payments_dict = paylink_part_payments_instance.to_dict()
# create an instance of PaylinkPartPayments from a dict
paylink_part_payments_form_dict = paylink_part_payments.from_dict(paylink_part_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


