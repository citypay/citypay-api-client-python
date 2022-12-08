# PaylinkTokenRequestModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Specifies the intended value of the transaction in the lowest denomination with no spacing characters or decimal point. This is the net total to be processed. An example of £74.95 would be presented as 7495. | 
**identifier** | **str** | Identifies a particular transaction linked to a Merchant account. It enables accurate duplicate checking within a pre-configured time period, as well as transaction reporting and tracing. The identifier should be unique to prevent payment card processing attempts from being rejected due to duplication.  | 
**merchantid** | **int** | The merchant id you wish to process this transaction with. | 
**accountno** | **str** | Specifies an alpha-numeric account number that the Paylink service uses when creating a Cardholder Account. The value should be no longer than 20 characters in length. | [optional] 
**cardholder** | [**PaylinkCardHolder**](PaylinkCardHolder.md) |  | [optional] 
**cart** | [**PaylinkCart**](PaylinkCart.md) |  | [optional] 
**client_version** | **str** | The clientVersion field is used to specify the version of your application that has invoked the Paylink payment process. This feature is typically used for tracing issues relating to application deployments, or any Paylink integration module or plugin. | [optional] 
**config** | [**PaylinkConfig**](PaylinkConfig.md) |  | [optional] 
**email** | **str** | The email field is used for the Merchant to be notified on completion of the transaction . The value may be supplied to override the default stored value. Emails sent to this address by the Paylink service should not be forwarded on to the cardholder as it may contain certain information that is used by the Paylink service to validate and authenticate Paylink Token Requests: for example, the Merchant ID and the licence key.  | [optional] 
**subscription_id** | **str** | an id associated with a subscription to link the token request against. | [optional] 
**tx_type** | **str** | A value to override the transaction type if requested by your account manager. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


