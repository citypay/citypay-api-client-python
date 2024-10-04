# PaylinkAdjustmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | An amount to adjust to. | [optional] 
**identifier** | **str** | An identifier of the original request. | [optional] 
**reason** | **str** | A textual reason for the adjustment. | [optional] 

## Example

```python
from citypay.models.paylink_adjustment_request import PaylinkAdjustmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkAdjustmentRequest from a JSON string
paylink_adjustment_request_instance = PaylinkAdjustmentRequest.from_json(json)
# print the JSON string representation of the object
print(PaylinkAdjustmentRequest.to_json())

# convert the object into a dict
paylink_adjustment_request_dict = paylink_adjustment_request_instance.to_dict()
# create an instance of PaylinkAdjustmentRequest from a dict
paylink_adjustment_request_from_dict = PaylinkAdjustmentRequest.from_dict(paylink_adjustment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


