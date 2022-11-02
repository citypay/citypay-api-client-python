# CardHolderAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account id of the card holder account provided by the merchant which uniquely identifies the account.  | 
**contact** | [**ContactDetails**](ContactDetails.md) |  | 
**cards** | [**[Card]**](Card.md) |  | [optional] 
**date_created** | **datetime** | The date and time the account was created. | [optional] 
**default_card_id** | **str** | The id of the default card. | [optional] 
**default_card_index** | **int** | The index in the array of the default card. | [optional] 
**last_modified** | **datetime** | The date and time the account was last modified. | [optional] 
**status** | **str** | Defines the status of the account for processing valid values are   - ACTIVE for active accounts that are able to process   - DISABLED for accounts that are currently disabled for processing.  | [optional] 
**unique_id** | **str** | A unique id of the card holder account which uniquely identifies the stored account. This value is not searchable. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


