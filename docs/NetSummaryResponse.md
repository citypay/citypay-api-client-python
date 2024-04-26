# NetSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_items_amount** | **str** | The total value of refund (credit) transaction items. Represents the sum of funds returned to customers. | [optional] 
**credit_items_count** | **int** | The count of refund (credit) transaction items. Reflects the number of refund transactions processed. | [optional] 
**credit_items_value** | **int** | The total value of refund (credit) transaction items. Represents the sum of funds returned to customers. | [optional] 
**debit_items_amount** | **str** | The total value of charge (debit) transaction items. Represents the sum of funds received from charges. | [optional] 
**debit_items_count** | **int** | The count of charge (debit) transaction items. Indicates the number of charge transactions processed. | [optional] 
**debit_items_value** | **int** | The total value of charge (debit) transaction items. Represents the sum of funds received from charges. | [optional] 
**net_amount** | **int** | The absolute net value, reflecting the net gain or loss from transactions. | [optional] 
**total_count** | **int** | The total count of all transaction items. | [optional] 

## Example

```python
from citypay.models.net_summary_response import NetSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetSummaryResponse from a JSON string
net_summary_response_instance = NetSummaryResponse.from_json(json)
# print the JSON string representation of the object
print NetSummaryResponse.to_json()

# convert the object into a dict
net_summary_response_dict = net_summary_response_instance.to_dict()
# create an instance of NetSummaryResponse from a dict
net_summary_response_form_dict = net_summary_response.from_dict(net_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


