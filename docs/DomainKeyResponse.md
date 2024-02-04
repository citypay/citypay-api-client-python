# DomainKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | The date the domain key was generated.  | [optional] 
**domain** | **List[str]** |  | 
**domain_key** | **str** | The domain key generated.  | [optional] 
**live** | **bool** | true if this key is a production key.  | [optional] 
**merchantid** | **int** | The merchant id the domain key is to be used for.  | 

## Example

```python
from citypay.models.domain_key_response import DomainKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DomainKeyResponse from a JSON string
domain_key_response_instance = DomainKeyResponse.from_json(json)
# print the JSON string representation of the object
print DomainKeyResponse.to_json()

# convert the object into a dict
domain_key_response_dict = domain_key_response_instance.to_dict()
# create an instance of DomainKeyResponse from a dict
domain_key_response_form_dict = domain_key_response.from_dict(domain_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


