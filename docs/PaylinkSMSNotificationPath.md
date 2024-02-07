# PaylinkSMSNotificationPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** | An optional template name to use a template other than the default. | [optional] 
**to** | **str** | The phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format to send the message to. | 

## Example

```python
from citypay.models.paylink_sms_notification_path import PaylinkSMSNotificationPath

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkSMSNotificationPath from a JSON string
paylink_sms_notification_path_instance = PaylinkSMSNotificationPath.from_json(json)
# print the JSON string representation of the object
print PaylinkSMSNotificationPath.to_json()

# convert the object into a dict
paylink_sms_notification_path_dict = paylink_sms_notification_path_instance.to_dict()
# create an instance of PaylinkSMSNotificationPath from a dict
paylink_sms_notification_path_form_dict = paylink_sms_notification_path.from_dict(paylink_sms_notification_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


