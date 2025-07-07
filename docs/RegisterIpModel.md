# RegisterIpModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exp** | **int** | When the ip address expires. At most an IP address can be registered for up to 720 hours. Will default to 12 hours if not supplied. | [optional] 
**ip** | **str** | The remote ip address to register. Will default to your current IP. | [optional] 

## Example

```python
from citypay.models.register_ip_model import RegisterIpModel

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterIpModel from a JSON string
register_ip_model_instance = RegisterIpModel.from_json(json)
# print the JSON string representation of the object
print(RegisterIpModel.to_json())

# convert the object into a dict
register_ip_model_dict = register_ip_model_instance.to_dict()
# create an instance of RegisterIpModel from a dict
register_ip_model_from_dict = RegisterIpModel.from_dict(register_ip_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


