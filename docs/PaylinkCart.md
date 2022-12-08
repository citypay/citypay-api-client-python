# PaylinkCart


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**[PaylinkCartItemModel]**](PaylinkCartItemModel.md) |  | [optional] 
**coupon** | **str** | A coupon redeemed with the transaction. | [optional] 
**mode** | **int** | The mode field specifies the behaviour or functionality of the cart.  Valid values are:   0 - No cart - No cart is shown  1 - Read-only - The cart is shown with a breakdown of the item details provided by objects in the contents array.  2 - Selection cart - The cart is shown as a drop-down box of available cart items that the customer can a single item select from.  3 - Dynamic cart - a text box is rendered to enable the operator to input an amount.  4 - Multi cart - The cart is displayed with items rendered with selectable quantities.  | [optional] 
**product_description** | **str** | Specifies a description about the product or service that is the subject of the transaction. It will be rendered in the header of the page with no labels. | [optional] 
**product_information** | **str** | Specifies information about the product or service that is the subject of the transaction. It will be rendered in the header of the page. | [optional] 
**shipping** | **int** | The shipping amount of the transaction in the lowest denomination of currency. | [optional] 
**tax** | **int** | The tax amount of the transaction in the lowest denomination of currency. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


