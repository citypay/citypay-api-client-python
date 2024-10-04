# Card


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bin_commercial** | **bool** | Defines whether the card is a commercial card. | [optional] 
**bin_corporate** | **bool** | Defines whether the card is a corporate business card. | [optional] 
**bin_country_issued** | **str** | The determined country where the card was issued. | [optional] 
**bin_credit** | **bool** | Defines whether the card is a credit card. | [optional] 
**bin_currency** | **str** | The default currency determined for the card. | [optional] 
**bin_debit** | **bool** | Defines whether the card is a debit card. | [optional] 
**bin_description** | **str** | A description of the bin on the card to identify what type of product the card is. | [optional] 
**bin_eu** | **bool** | Defines whether the card is regulated within the EU. | [optional] 
**card_id** | **str** | The id of the card that is returned. Should be used for referencing the card when perform any changes. | [optional] 
**card_status** | **str** | The status of the card such, valid values are   - ACTIVE the card is active for processing   - INACTIVE the card is not active for processing   - EXPIRED for cards that have passed their expiry date.  | [optional] 
**date_created** | **datetime** | The date time of when the card was created. | [optional] 
**default** | **bool** | Determines if the card is the default card for the account and should be regarded as the first option to be used for processing. | [optional] 
**expmonth** | **int** | The expiry month of the card. | [optional] 
**expyear** | **int** | The expiry year of the card. | [optional] 
**label** | **str** | A label which identifies this card. | [optional] 
**label2** | **str** | A label which also provides the expiry date of the card. | [optional] 
**last4digits** | **str** | The last 4 digits of the card to aid in identification. | [optional] 
**name_on_card** | **str** | The name on the card. | [optional] 
**scheme** | **str** | The scheme that issued the card. | [optional] 
**token** | **str** | A token that can be used to process against the card. | [optional] 

## Example

```python
from citypay.models.card import Card

# TODO update the JSON string below
json = "{}"
# create an instance of Card from a JSON string
card_instance = Card.from_json(json)
# print the JSON string representation of the object
print(Card.to_json())

# convert the object into a dict
card_dict = card_instance.to_dict()
# create an instance of Card from a dict
card_from_dict = Card.from_dict(card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


