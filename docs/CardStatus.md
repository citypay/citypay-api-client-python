# CardStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_status** | **str** | The status of the card to set, valid values are ACTIVE or INACTIVE. | [optional] 
**default** | **bool** | Defines if the card is set as the default. | [optional] 

## Example

```python
from citypay.models.card_status import CardStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CardStatus from a JSON string
card_status_instance = CardStatus.from_json(json)
# print the JSON string representation of the object
print CardStatus.to_json()

# convert the object into a dict
card_status_dict = card_status_instance.to_dict()
# create an instance of CardStatus from a dict
card_status_form_dict = card_status.from_dict(card_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


