# RequestChallenged


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | The url of the Access Control Server (ACS) to forward the user to.  | [optional] 
**creq** | **str** | The challenge request data which is encoded for usage by the ACS. | [optional] 
**merchantid** | **int** | The merchant id that processed this transaction. | [optional] 
**threedserver_trans_id** | **str** | The 3DSv2 trans id reference for the challenge process. May be used to create the ThreeDSSessionData value to send to the ACS. | [optional] 
**transno** | **int** | The transaction number for the challenge, ordered incrementally from 1 for every merchant_id.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


