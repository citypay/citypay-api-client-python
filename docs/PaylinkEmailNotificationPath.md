# PaylinkEmailNotificationPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcc** | **List[str]** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**reply_to** | **List[str]** |  | [optional] 
**template** | **str** | An optional template name to use a template other than the default. | [optional] 
**to** | **List[str]** |  | 

## Example

```python
from citypay.models.paylink_email_notification_path import PaylinkEmailNotificationPath

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkEmailNotificationPath from a JSON string
paylink_email_notification_path_instance = PaylinkEmailNotificationPath.from_json(json)
# print the JSON string representation of the object
print(PaylinkEmailNotificationPath.to_json())

# convert the object into a dict
paylink_email_notification_path_dict = paylink_email_notification_path_instance.to_dict()
# create an instance of PaylinkEmailNotificationPath from a dict
paylink_email_notification_path_from_dict = PaylinkEmailNotificationPath.from_dict(paylink_email_notification_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


