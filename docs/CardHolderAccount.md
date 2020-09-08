# CardHolderAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account id of the card holder account provided by the merchant which uniquely identifies the account.  | 
**cards** | [**list[Card]**](Card.md) |  | [optional] 
**contact** | [**ContactDetails**](ContactDetails.md) |  | 
**date_created** | **datetime** | The date and time the account was created. | [optional] 
**default_card_id** | **str** | The id of the default card. | [optional] 
**default_card_index** | **int** | The index in the array of the default card. | [optional] 
**status** | **str** | Defines the status of the account for processing valid values are   - ACTIVE for active accounts that are able to process  - DISABLED for accounts that are currently disabled for processing.  | [optional] 
**unique_id** | **str** | A unique id of the card holder account which uniquely identifies the stored account. This value is not searchable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


