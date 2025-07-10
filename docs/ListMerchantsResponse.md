# ListMerchantsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_name** | **str** | The client name that was requested. | [optional] 
**clientid** | **str** | The client id requested. | [optional] 
**merchants** | [**List[Merchant]**](Merchant.md) |  | [optional] 

## Example

```python
from citypay.models.list_merchants_response import ListMerchantsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListMerchantsResponse from a JSON string
list_merchants_response_instance = ListMerchantsResponse.from_json(json)
# print the JSON string representation of the object
print(ListMerchantsResponse.to_json())

# convert the object into a dict
list_merchants_response_dict = list_merchants_response_instance.to_dict()
# create an instance of ListMerchantsResponse from a dict
list_merchants_response_from_dict = ListMerchantsResponse.from_dict(list_merchants_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


