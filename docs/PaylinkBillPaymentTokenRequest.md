# PaylinkBillPaymentTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addressee** | **str** | Who the bill payment request intended for. This should be a readable name such as a person or company. | [optional] 
**adjustments** | [**Adjustments**](Adjustments.md) |  | [optional] 
**attachments** | [**List[PaylinkAttachmentRequest]**](PaylinkAttachmentRequest.md) |  | [optional] 
**descriptor** | **str** | A descriptor for the bill payment used to describe what the payment request is for for instance \&quot;Invoice\&quot;.  The descriptor can be used as descriptive text on emails or the payment page. For instance an invoice may have a button saying \&quot;View Invoice\&quot; or an email may say \&quot;to pay your Invoice online\&quot;.  | [optional] 
**due** | **date** | A date that the invoice is due. This can be displayed on the payment page. | [optional] 
**email_notification_path** | [**PaylinkEmailNotificationPath**](PaylinkEmailNotificationPath.md) |  | [optional] 
**memo** | **str** | A memo that can be added to the payment page and email to provide to the customer. | [optional] 
**request** | [**PaylinkTokenRequestModel**](PaylinkTokenRequestModel.md) |  | 
**sms_notification_path** | [**PaylinkSMSNotificationPath**](PaylinkSMSNotificationPath.md) |  | [optional] 

## Example

```python
from citypay.models.paylink_bill_payment_token_request import PaylinkBillPaymentTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkBillPaymentTokenRequest from a JSON string
paylink_bill_payment_token_request_instance = PaylinkBillPaymentTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PaylinkBillPaymentTokenRequest.to_json())

# convert the object into a dict
paylink_bill_payment_token_request_dict = paylink_bill_payment_token_request_instance.to_dict()
# create an instance of PaylinkBillPaymentTokenRequest from a dict
paylink_bill_payment_token_request_from_dict = PaylinkBillPaymentTokenRequest.from_dict(paylink_bill_payment_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


