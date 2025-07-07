# PaylinkResendNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **bool** | Resends the bill payment email provided on the Paylink create token notification path. Emails can be sent up to 5 times per token. | [optional] 
**sms** | **bool** | Resends the bill payment SMS provided on the Paylink create token notification path. An SMS cannot be resent if it was previously sent less than 1 minute ago. There is a limit of 3 retries per token.  | [optional] 

## Example

```python
from citypay.models.paylink_resend_notification_request import PaylinkResendNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkResendNotificationRequest from a JSON string
paylink_resend_notification_request_instance = PaylinkResendNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(PaylinkResendNotificationRequest.to_json())

# convert the object into a dict
paylink_resend_notification_request_dict = paylink_resend_notification_request_instance.to_dict()
# create an instance of PaylinkResendNotificationRequest from a dict
paylink_resend_notification_request_from_dict = PaylinkResendNotificationRequest.from_dict(paylink_resend_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


