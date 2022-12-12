# PaylinkBillPaymentTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**PaylinkTokenRequestModel**](PaylinkTokenRequestModel.md) |  | 
**addressee** | **str** | Who the bill payment request intended for. This should be a readable name such as a person or company. | [optional] 
**attachments** | [**[PaylinkAttachmentRequest]**](PaylinkAttachmentRequest.md) |  | [optional] 
**descriptor** | **str** | A descriptor for the bill payment used to describe what the payment request is for for instance \&quot;Invoice\&quot;.  The descriptor can be used as descriptive text on emails or the payment page. For instance an invoice may have a button saying \&quot;View Invoice\&quot; or an email may say \&quot;to pay your Invoice online\&quot;.  | [optional] 
**due** | **date** | A date that the invoice is due. This can be displayed on the payment page. | [optional] 
**email_notification_path** | [**PaylinkEmailNotificationPath**](PaylinkEmailNotificationPath.md) |  | [optional] 
**memo** | **str** | A memo that can be added to the payment page and email to provide to the customer. | [optional] 
**sms_notification_path** | [**PaylinkSMSNotificationPath**](PaylinkSMSNotificationPath.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


