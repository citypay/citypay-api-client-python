# AclCheckResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | **str** | The name or value of the acl which was found to match the ip address. | [optional] 
**cache** | **bool** | Whether the ACL was returned via a cached instance. | [optional] 
**ip** | **str** | The IP address used in the lookup. | [optional] 
**provider** | **str** | The source provider of the ACL such as cloud, subnet, country or IP based. | [optional] 

## Example

```python
from citypay.models.acl_check_response_model import AclCheckResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of AclCheckResponseModel from a JSON string
acl_check_response_model_instance = AclCheckResponseModel.from_json(json)
# print the JSON string representation of the object
print(AclCheckResponseModel.to_json())

# convert the object into a dict
acl_check_response_model_dict = acl_check_response_model_instance.to_dict()
# create an instance of AclCheckResponseModel from a dict
acl_check_response_model_from_dict = AclCheckResponseModel.from_dict(acl_check_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


