# PaylinkTokenRequestModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountno** | **str** | Specifies an alpha-numeric account number that the Paylink service uses when creating a Cardholder Account. The value should be no longer than 20 characters in length. | [optional] 
**amount** | **int** | Specifies the intended value of the transaction in the lowest denomination with no spacing characters or decimal point. This is the net total to be processed. An example of £74.95 would be presented as 7495. | 
**cardholder** | [**PaylinkCardHolder**](PaylinkCardHolder.md) |  | [optional] 
**cart** | [**PaylinkCart**](PaylinkCart.md) |  | [optional] 
**client_version** | **str** | The clientVersion field is used to specify the version of your application that has invoked the Paylink payment process. This feature is typically used for tracing issues relating to application deployments, or any Paylink integration module or plugin. | [optional] 
**config** | [**PaylinkConfig**](PaylinkConfig.md) |  | [optional] 
**currency** | **str** | A currency for the token. This value should be only used on multi-currency accounts and be an appropriate currency which the account is configured for. | [optional] 
**email** | **str** | The email field is used for the Merchant to be notified on completion of the transaction . The value may be supplied to override the default stored value. Emails sent to this address by the Paylink service should not be forwarded on to the cardholder as it may contain certain information that is used by the Paylink service to validate and authenticate Paylink Token Requests: for example, the Merchant ID and the licence key.  | [optional] 
**identifier** | **str** | Identifies a particular transaction linked to a Merchant account. It enables accurate duplicate checking within a pre-configured time period, as well as transaction reporting and tracing. The identifier should be unique to prevent payment card processing attempts from being rejected due to duplication.  | 
**merchantid** | **int** | The merchant id you wish to process this transaction with. | 
**recurring** | **bool** | True if the intent of this cardholder initiated transaction is to establish a recurring payment model, processable as merchant initiated transactions. | [optional] 
**subscription_id** | **str** | an id associated with a subscription to link the token request against. | [optional] 
**tx_type** | **str** | A value to override the transaction type if requested by your account manager. | [optional] 

## Example

```python
from citypay.models.paylink_token_request_model import PaylinkTokenRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkTokenRequestModel from a JSON string
paylink_token_request_model_instance = PaylinkTokenRequestModel.from_json(json)
# print the JSON string representation of the object
print(PaylinkTokenRequestModel.to_json())

# convert the object into a dict
paylink_token_request_model_dict = paylink_token_request_model_instance.to_dict()
# create an instance of PaylinkTokenRequestModel from a dict
paylink_token_request_model_from_dict = PaylinkTokenRequestModel.from_dict(paylink_token_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


