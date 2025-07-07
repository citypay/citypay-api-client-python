# RegisterCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardnumber** | **str** | The primary number of the card. | 
**default** | **bool** | Determines whether the card should be the new default card. | [optional] 
**expmonth** | **int** | The expiry month of the card. | 
**expyear** | **int** | The expiry year of the card. | 
**name_on_card** | **str** | The card holder name as it appears on the card. The value is required if the account is to be used for 3dsv2 processing, otherwise it is optional. | [optional] 

## Example

```python
from citypay.models.register_card import RegisterCard

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterCard from a JSON string
register_card_instance = RegisterCard.from_json(json)
# print the JSON string representation of the object
print(RegisterCard.to_json())

# convert the object into a dict
register_card_dict = register_card_instance.to_dict()
# create an instance of RegisterCard from a dict
register_card_from_dict = RegisterCard.from_dict(register_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


