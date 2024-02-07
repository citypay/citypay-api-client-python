# BatchTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The card holder account id to process against. | 
**amount** | **int** | The amount required to process in the lowest denomination. | 
**identifier** | **str** | An identifier used to reference the transaction set by your integration. The value should be used to refer to the transaction in future calls. | [optional] 
**merchantid** | **int** | The CityPay merchant id used to process the transaction. | [optional] 

## Example

```python
from citypay.models.batch_transaction import BatchTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of BatchTransaction from a JSON string
batch_transaction_instance = BatchTransaction.from_json(json)
# print the JSON string representation of the object
print BatchTransaction.to_json()

# convert the object into a dict
batch_transaction_dict = batch_transaction_instance.to_dict()
# create an instance of BatchTransaction from a dict
batch_transaction_form_dict = batch_transaction.from_dict(batch_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


