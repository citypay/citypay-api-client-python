# CardTokenisationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cp_card_token** | **str** | The tokenised card value. The token is encrypted with integrity checks and scoped to a client id only allowing for the card value to be used.  The value may be used up and until the expiry date of the card. | 
**last4digits** | **str** | The last 4 digits of the card. | [optional] 
**scheme** | **str** | The card scheme of the card. | [optional] 
**scheme_logo** | **str** | The url of the logo card scheme of the card. | [optional] 

## Example

```python
from citypay.models.card_tokenisation_response import CardTokenisationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CardTokenisationResponse from a JSON string
card_tokenisation_response_instance = CardTokenisationResponse.from_json(json)
# print the JSON string representation of the object
print(CardTokenisationResponse.to_json())

# convert the object into a dict
card_tokenisation_response_dict = card_tokenisation_response_instance.to_dict()
# create an instance of CardTokenisationResponse from a dict
card_tokenisation_response_from_dict = CardTokenisationResponse.from_dict(card_tokenisation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


