# PaylinkTokenCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**PaylinkAttachmentResult**](PaylinkAttachmentResult.md) |  | [optional] 
**bps** | **str** | true if BPS has been enabled on this token. | [optional] 
**date_created** | **datetime** | Date and time the token was generated. | [optional] 
**errors** | [**List[PaylinkErrorCode]**](PaylinkErrorCode.md) |  | [optional] 
**id** | **str** | A unique id of the request. | 
**identifier** | **str** | The identifier as presented in the TokenRequest. | [optional] 
**mode** | **str** | Determines whether the token is &#x60;live&#x60; or &#x60;test&#x60;. | [optional] 
**qrcode** | **str** | A URL of a qrcode which can be used to refer to the token URL. | [optional] 
**result** | **int** | The result field contains the result for the Paylink Token Request. 0 - indicates that an error was encountered while creating the token. 1 - which indicates that a Token was successfully created. | 
**server_version** | **str** | the version of the server performing the call. | [optional] 
**source** | **str** | The incoming IP address of the call. | [optional] 
**token** | **str** | A token generated for the request used to refer to the transaction in consequential calls. | 
**url** | **str** | The Paylink token URL used to checkout by the card holder. | [optional] 
**usc** | **str** | A UrlShortCode (USC) used for short links. | [optional] 

## Example

```python
from citypay.models.paylink_token_created import PaylinkTokenCreated

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkTokenCreated from a JSON string
paylink_token_created_instance = PaylinkTokenCreated.from_json(json)
# print the JSON string representation of the object
print PaylinkTokenCreated.to_json()

# convert the object into a dict
paylink_token_created_dict = paylink_token_created_instance.to_dict()
# create an instance of PaylinkTokenCreated from a dict
paylink_token_created_form_dict = paylink_token_created.from_dict(paylink_token_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


