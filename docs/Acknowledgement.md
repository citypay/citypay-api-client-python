# Acknowledgement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A response code providing a result of the process. | [optional] 
**context** | **str** | A context id of the process used for referencing transactions through support. | [optional] 
**identifier** | **str** | An identifier if presented in the original request. | [optional] 
**message** | **str** | A response message providing a description of the result of the process. | [optional] 

## Example

```python
from citypay.models.acknowledgement import Acknowledgement

# TODO update the JSON string below
json = "{}"
# create an instance of Acknowledgement from a JSON string
acknowledgement_instance = Acknowledgement.from_json(json)
# print the JSON string representation of the object
print(Acknowledgement.to_json())

# convert the object into a dict
acknowledgement_dict = acknowledgement_instance.to_dict()
# create an instance of Acknowledgement from a dict
acknowledgement_from_dict = Acknowledgement.from_dict(acknowledgement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


