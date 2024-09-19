# PaylinkAttachmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | base64 encoding of the file if less than 32kb in size. | [optional] 
**filename** | **str** | The name of the attachment normally taken from the filename. You should not include the filename path as appropriate. | 
**mime_type** | **str** | The mime type of the attachment as defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html). Currently only &#x60;application/pdf&#x60; is supported. | 
**name** | **str** | A name for the file to identify it to the card holder when it is displayed in the payment form. For example Invoice, Statement. | [optional] 
**retention** | **int** | The retention period in days of the attachment. Defaults to 180 days. | [optional] 

## Example

```python
from citypay.models.paylink_attachment_request import PaylinkAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkAttachmentRequest from a JSON string
paylink_attachment_request_instance = PaylinkAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print(PaylinkAttachmentRequest.to_json())

# convert the object into a dict
paylink_attachment_request_dict = paylink_attachment_request_instance.to_dict()
# create an instance of PaylinkAttachmentRequest from a dict
paylink_attachment_request_from_dict = PaylinkAttachmentRequest.from_dict(paylink_attachment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


