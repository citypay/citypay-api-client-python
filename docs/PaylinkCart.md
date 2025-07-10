# PaylinkCart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[PaylinkCartItemModel]**](PaylinkCartItemModel.md) |  | [optional] 
**coupon** | **str** | A coupon redeemed with the transaction. | [optional] 
**mode** | **int** | The mode field specifies the behaviour or functionality of the cart.  Valid values are:  - &#x60;0&#x60; No cart - No cart is shown - &#x60;1&#x60; Read-only - The cart is shown with a breakdown of the item details provided by objects in the contents array. - &#x60;2&#x60; Selection cart - The cart is shown as a drop-down box of available cart items that the customer can a single item select from. - &#x60;3&#x60; Dynamic cart - a text box is rendered to enable the operator to input an amount. - &#x60;4&#x60; Multi cart - The cart is displayed with items rendered with selectable quantities.  | [optional] 
**product_description** | **str** | Specifies a description about the product or service that is the subject of the transaction. It will be rendered in the header of the page with no labels. | [optional] 
**product_information** | **str** | Specifies information about the product or service that is the subject of the transaction. It will be rendered in the header of the page. | [optional] 
**shipping** | **int** | The shipping amount of the transaction in the lowest denomination of currency. | [optional] 
**tax** | **int** | The tax amount of the transaction in the lowest denomination of currency. | [optional] 

## Example

```python
from citypay.models.paylink_cart import PaylinkCart

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkCart from a JSON string
paylink_cart_instance = PaylinkCart.from_json(json)
# print the JSON string representation of the object
print(PaylinkCart.to_json())

# convert the object into a dict
paylink_cart_dict = paylink_cart_instance.to_dict()
# create an instance of PaylinkCart from a dict
paylink_cart_from_dict = PaylinkCart.from_dict(paylink_cart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


