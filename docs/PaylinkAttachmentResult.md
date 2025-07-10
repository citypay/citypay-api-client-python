# PaylinkAttachmentResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the attachment. | 
**result** | **str** | The result of an uploaded attachment such as &#x60;OK&#x60; or &#x60;UPLOAD&#x60;. | 
**url** | **str** | If the attachment is to be uploaded, a URL that can be used for Multipart upload of the attachment. | [optional] 

## Example

```python
from citypay.models.paylink_attachment_result import PaylinkAttachmentResult

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkAttachmentResult from a JSON string
paylink_attachment_result_instance = PaylinkAttachmentResult.from_json(json)
# print the JSON string representation of the object
print(PaylinkAttachmentResult.to_json())

# convert the object into a dict
paylink_attachment_result_dict = paylink_attachment_result_instance.to_dict()
# create an instance of PaylinkAttachmentResult from a dict
paylink_attachment_result_from_dict = PaylinkAttachmentResult.from_dict(paylink_attachment_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


