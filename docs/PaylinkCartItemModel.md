# PaylinkCartItemModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The net amount of the item. The Paylink Payment Form does not multiply this figure by the value provided by the count value for the cart item, this is principally to avoid rounding errors to introduce discrepancies between the value of the goods charged for and the total amount represented by the collection of cart items. | [optional] 
**brand** | **str** | The brand of the item such as Nike. | [optional] 
**category** | **str** | The category of the item such as shoes. | [optional] 
**count** | **int** | The count of how many of this item is being purchased, should the cart be editable, this value should be the default count required. The Paylink Payment Form assumes a count of 1 in the event that no value for the count field is provided for a cart item. | [optional] 
**label** | **str** | The label which describes the item. | [optional] 
**max** | **int** | For an editable cart, the maximum number of items that can be purchased, defaults to 5. | [optional] 
**sku** | **str** | The stock control unit value. | [optional] 
**variant** | **str** | The variant field refers to the variant of the cart item to enable similar items to be distinguished according to certain criteria. For example, similar items may be distinguished in terms of size, weight and power. The Paylink Payment Form does not constrain the value of the variant field to a particular set of metrics. | [optional] 

## Example

```python
from citypay.models.paylink_cart_item_model import PaylinkCartItemModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkCartItemModel from a JSON string
paylink_cart_item_model_instance = PaylinkCartItemModel.from_json(json)
# print the JSON string representation of the object
print(PaylinkCartItemModel.to_json())

# convert the object into a dict
paylink_cart_item_model_dict = paylink_cart_item_model_instance.to_dict()
# create an instance of PaylinkCartItemModel from a dict
paylink_cart_item_model_from_dict = PaylinkCartItemModel.from_dict(paylink_cart_item_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


