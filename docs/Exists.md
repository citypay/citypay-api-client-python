# Exists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Boolean value whether the entity is active. | [optional] 
**exists** | **bool** | Boolean value whether the entity exists. | 
**last_modified** | **datetime** | The last modified date of the entity. | [optional] 

## Example

```python
from citypay.models.exists import Exists

# TODO update the JSON string below
json = "{}"
# create an instance of Exists from a JSON string
exists_instance = Exists.from_json(json)
# print the JSON string representation of the object
print(Exists.to_json())

# convert the object into a dict
exists_dict = exists_instance.to_dict()
# create an instance of Exists from a dict
exists_from_dict = Exists.from_dict(exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


