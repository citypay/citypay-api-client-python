# DomainKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **List[str]** |  | 
**live** | **bool** | Specifies if the key is to be used for production. Defaults to false.  | [optional] 
**merchantid** | **int** | The merchant id the domain key is to be used for.  | 
**nonce** | **str** | Specifies a random value for integrity. The value is used to generate the domain key to provide further integrity to the key.  | [optional] 

## Example

```python
from citypay.models.domain_key_request import DomainKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DomainKeyRequest from a JSON string
domain_key_request_instance = DomainKeyRequest.from_json(json)
# print the JSON string representation of the object
print(DomainKeyRequest.to_json())

# convert the object into a dict
domain_key_request_dict = domain_key_request_instance.to_dict()
# create an instance of DomainKeyRequest from a dict
domain_key_request_from_dict = DomainKeyRequest.from_dict(domain_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


