# CardHolderAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account id of the card holder account provided by the merchant which uniquely identifies the account.  | 
**cards** | [**List[Card]**](Card.md) |  | [optional] 
**contact** | [**ContactDetails**](ContactDetails.md) |  | 
**date_created** | **datetime** | The date and time the account was created. | [optional] 
**default_card_id** | **str** | The id of the default card. | [optional] 
**default_card_index** | **int** | The index in the array of the default card. | [optional] 
**last_modified** | **datetime** | The date and time the account was last modified. | [optional] 
**status** | **str** | Defines the status of the account for processing valid values are   - ACTIVE for active accounts that are able to process   - DISABLED for accounts that are currently disabled for processing.  | [optional] 
**unique_id** | **str** | A unique id of the card holder account which uniquely identifies the stored account. This value is not searchable. | [optional] 

## Example

```python
from citypay.models.card_holder_account import CardHolderAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CardHolderAccount from a JSON string
card_holder_account_instance = CardHolderAccount.from_json(json)
# print the JSON string representation of the object
print(CardHolderAccount.to_json())

# convert the object into a dict
card_holder_account_dict = card_holder_account_instance.to_dict()
# create an instance of CardHolderAccount from a dict
card_holder_account_from_dict = CardHolderAccount.from_dict(card_holder_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


