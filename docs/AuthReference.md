# AuthReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The amount of the transaction in decimal currency format. | [optional] 
**amount_value** | **int** | The amount of the transaction in integer/request format. | [optional] 
**atrn** | **str** | A reference number provided by the acquiring services. | [optional] 
**authcode** | **str** | The authorisation code of the transaction returned by the acquirer or card issuer. | [optional] 
**batchno** | **str** | A batch number which the transaction has been end of day batched towards. | [optional] 
**currency** | **str** | The currency of the transaction in ISO 4217 code format. | [optional] 
**datetime** | **datetime** | The date and time of the transaction. | [optional] 
**identifier** | **str** | The identifier of the transaction used to process the transaction. | [optional] 
**maskedpan** | **str** | A masking of the card number which was used to process the tranasction. | [optional] 
**merchantid** | **int** | The merchant id of the transaction result. | [optional] 
**result** | **str** | The result of the transaction. | [optional] 
**trans_status** | **str** | The current status of the transaction through it&#39;s lifecycle. | [optional] 
**trans_type** | **str** | The type of transaction that was processed. | [optional] 
**transno** | **int** | The transaction number of the transaction. | [optional] 

## Example

```python
from citypay.models.auth_reference import AuthReference

# TODO update the JSON string below
json = "{}"
# create an instance of AuthReference from a JSON string
auth_reference_instance = AuthReference.from_json(json)
# print the JSON string representation of the object
print(AuthReference.to_json())

# convert the object into a dict
auth_reference_dict = auth_reference_instance.to_dict()
# create an instance of AuthReference from a dict
auth_reference_from_dict = AuthReference.from_dict(auth_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


