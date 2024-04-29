# RemittedClientData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[MerchantBatchResponse]**](MerchantBatchResponse.md) |  | 
**clientid** | **str** | The client id that the remittance data is for. | [optional] 
**var_date** | **date** | The date of the remittance. | [optional] 
**date_created** | **datetime** | The date time that the remittance was created. | [optional] 
**net_amount** | **int** | Represents the net amount after accounting for refunds. This is calculated as SalesAmount - RefundAmount and expressed in the smallest currency unit. | [optional] 
**processed_amount** | **int** | The total monetary amount processed consisting of sale and refund transactions. | [optional] 
**processed_count** | **int** | Indicates the total number of sales and refund transactions that occurred. This count provides insight into the volume of processing. | [optional] 
**refund_amount** | **int** | The total amount refunded to customers. | [optional] 
**refund_count** | **int** | The total number of refund transactions processed. This figure helps in understanding the frequency of refunds relative to sales. | [optional] 
**remittances** | [**List[RemittanceData]**](RemittanceData.md) |  | 
**sales_amount** | **int** | The total monetary amount of sales transactions. | [optional] 
**sales_count** | **int** | Indicates the total number of sales transactions that occurred. This count provides insight into the volume of sales. | [optional] 
**settlement_implementation** | **str** | The name of the implementation. | [optional] 
**uuid** | **str** | The uuid of the settlement file processed on. | [optional] 

## Example

```python
from citypay.models.remitted_client_data import RemittedClientData

# TODO update the JSON string below
json = "{}"
# create an instance of RemittedClientData from a JSON string
remitted_client_data_instance = RemittedClientData.from_json(json)
# print the JSON string representation of the object
print RemittedClientData.to_json()

# convert the object into a dict
remitted_client_data_dict = remitted_client_data_instance.to_dict()
# create an instance of RemittedClientData from a dict
remitted_client_data_form_dict = remitted_client_data.from_dict(remitted_client_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


