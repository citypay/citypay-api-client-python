# PaylinkErrorCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | An error code identifying the error. | 
**msg** | **str** | An error message describing the error. | 

## Example

```python
from citypay.models.paylink_error_code import PaylinkErrorCode

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkErrorCode from a JSON string
paylink_error_code_instance = PaylinkErrorCode.from_json(json)
# print the JSON string representation of the object
print(PaylinkErrorCode.to_json())

# convert the object into a dict
paylink_error_code_dict = paylink_error_code_instance.to_dict()
# create an instance of PaylinkErrorCode from a dict
paylink_error_code_from_dict = PaylinkErrorCode.from_dict(paylink_error_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


