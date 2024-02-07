# DomainKeyCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_key** | **str** | The domain key to check.  | 

## Example

```python
from citypay.models.domain_key_check_request import DomainKeyCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainKeyCheckRequest from a JSON string
domain_key_check_request_instance = DomainKeyCheckRequest.from_json(json)
# print the JSON string representation of the object
print DomainKeyCheckRequest.to_json()

# convert the object into a dict
domain_key_check_request_dict = domain_key_check_request_instance.to_dict()
# create an instance of DomainKeyCheckRequest from a dict
domain_key_check_request_form_dict = domain_key_check_request.from_dict(domain_key_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


