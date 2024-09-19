# VoidRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier of the transaction to void. If an empty value is supplied then a &#x60;trans_no&#x60; value must be supplied. | [optional] 
**merchantid** | **int** | Identifies the merchant account to perform the void for. | 
**transno** | **int** | The transaction number of the transaction to look up and void. If an empty value is supplied then an identifier value must be supplied. | [optional] 

## Example

```python
from citypay.models.void_request import VoidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoidRequest from a JSON string
void_request_instance = VoidRequest.from_json(json)
# print the JSON string representation of the object
print(VoidRequest.to_json())

# convert the object into a dict
void_request_dict = void_request_instance.to_dict()
# create an instance of VoidRequest from a dict
void_request_from_dict = VoidRequest.from_dict(void_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


