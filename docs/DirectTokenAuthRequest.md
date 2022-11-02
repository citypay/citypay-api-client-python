# DirectTokenAuthRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | A random value string which is provided to the API to perform a digest. The value will be used by its UTF-8 byte representation of any digest function.  | [optional] 
**redirect_failure** | **str** | The URL used to redirect back to your site when a transaction has been rejected or declined. Required if a url-encoded request.  | [optional] 
**redirect_success** | **str** | The URL used to redirect back to your site when a transaction has been authorised. Required if a url-encoded request.  | [optional] 
**token** | **str** | The token required to process the transaction as presented by the direct post methodology.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


