# Merchant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The currency of the merchant. | [optional] 
**merchantid** | **int** | The merchant id which uniquely identifies the merchant account. | [optional] 
**name** | **str** | The name of the merchant. | [optional] 
**status** | **str** | The status of the account. | [optional] 
**status_label** | **str** | The status label of the account. | [optional] 

## Example

```python
from citypay.models.merchant import Merchant

# TODO update the JSON string below
json = "{}"
# create an instance of Merchant from a JSON string
merchant_instance = Merchant.from_json(json)
# print the JSON string representation of the object
print Merchant.to_json()

# convert the object into a dict
merchant_dict = merchant_instance.to_dict()
# create an instance of Merchant from a dict
merchant_form_dict = merchant.from_dict(merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


