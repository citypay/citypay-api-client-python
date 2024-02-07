# AclCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | An ip address to check for an ACL against. The address should be a publicly routable IPv4 address. | 

## Example

```python
from citypay.models.acl_check_request import AclCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AclCheckRequest from a JSON string
acl_check_request_instance = AclCheckRequest.from_json(json)
# print the JSON string representation of the object
print AclCheckRequest.to_json()

# convert the object into a dict
acl_check_request_dict = acl_check_request_instance.to_dict()
# create an instance of AclCheckRequest from a dict
acl_check_request_form_dict = acl_check_request.from_dict(acl_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


