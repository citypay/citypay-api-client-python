# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A response code providing a result of the process. | [optional] 
**context** | **str** | A context id of the process used for referencing transactions through support. | [optional] 
**identifier** | **str** | An identifier if presented in the original request. | [optional] 
**message** | **str** | A response message providing a description of the result of the process. | [optional] 
**response_dt** | **datetime** | The ISO-8601 UTC date and time of the response data. | [optional] 

## Example

```python
from citypay.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


