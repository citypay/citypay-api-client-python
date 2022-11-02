# PaylinkTokenCreated


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique id of the request. | 
**result** | **int** | The result field contains the result for the Paylink Token Request. 0 - indicates that an error was encountered while creating the token. 1 - which indicates that a Token was successfully created. | 
**token** | **str** | A token generated for the request used to refer to the transaction in consequential calls. | 
**attachments** | [**PaylinkAttachmentResult**](PaylinkAttachmentResult.md) |  | [optional] 
**bps** | **str** | true if BPS has been enabled on this token. | [optional] 
**date_created** | **datetime** | Date and time the token was generated. | [optional] 
**errors** | [**[PaylinkErrorCode]**](PaylinkErrorCode.md) |  | [optional] 
**identifier** | **str** | The identifier as presented in the TokenRequest. | [optional] 
**mode** | **str** | Determines whether the token is &#x60;live&#x60; or &#x60;test&#x60;. | [optional] 
**qr_code** | **str** | A URL of a qrcode which can be used to refer to the token URL. | [optional] 
**server_version** | **str** | the version of the server performing the call. | [optional] 
**source** | **str** | The incoming IP address of the call. | [optional] 
**url** | **str** | The Paylink token URL used to checkout by the card holder. | [optional] 
**usc** | **str** | A UrlShortCode (USC) used for short links. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


