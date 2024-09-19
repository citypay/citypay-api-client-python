# RemittanceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created** | **datetime** | Represents the date and time when the remittance was processed. This timestamp follows the ISO 8601 format for datetime representation. | [optional] 
**net_amount** | **int** | Represents the net amount after accounting for refunds. This is calculated as SalesAmount - RefundAmount and expressed in the smallest currency unit. | [optional] 
**refund_amount** | **int** | The total amount refunded to customers. | [optional] 
**refund_count** | **int** | The total number of refund transactions processed. This figure helps in understanding the frequency of refunds relative to sales. | [optional] 
**sales_amount** | **int** | The total monetary amount of sales transactions. | [optional] 
**sales_count** | **int** | Indicates the total number of sales transactions that occurred. This count provides insight into the volume of sales. | [optional] 

## Example

```python
from citypay.models.remittance_data import RemittanceData

# TODO update the JSON string below
json = "{}"
# create an instance of RemittanceData from a JSON string
remittance_data_instance = RemittanceData.from_json(json)
# print the JSON string representation of the object
print(RemittanceData.to_json())

# convert the object into a dict
remittance_data_dict = remittance_data_instance.to_dict()
# create an instance of RemittanceData from a dict
remittance_data_from_dict = RemittanceData.from_dict(remittance_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


