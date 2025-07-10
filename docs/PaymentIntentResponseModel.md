# PaymentIntentResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | [**Adjustments**](Adjustments.md) |  | [optional] 
**amount** | **int** | An amount of the intent. | [optional] 
**created** | **datetime** | A date time of when the intent was created. | [optional] 
**currency** | **str** | The currency of the intent. | [optional] 
**due** | **date** | A due date of the intent. | [optional] 
**expires** | **date** | An expiration date of the intent. | [optional] 
**external_ref** | **str** | An external reference of the intent. | [optional] 
**external_ref_source** | **str** | An external reference source of the intent. | [optional] 
**identifier** | **str** | An identifier of the intent. | 
**intent_status** | **str** | A status of the intent such as &#x60;unknown&#x60;, &#x60;open&#x60;, &#x60;requires_payment_method&#x60;, &#x60;requires_confirmation&#x60;, &#x60;requires_confirmation&#x60;, &#x60;requires_action&#x60;, &#x60;processing&#x60;, &#x60;succeeded&#x60;, &#x60;cancelled&#x60;, &#x60;requires_capture&#x60;, &#x60;failed&#x60;, &#x60;expired&#x60;, &#x60;requires_refund&#x60;, &#x60;refunded&#x60;. | [optional] 
**merchantid** | **int** | The merchant id of the intent. | 
**payment_type** | **str** | A type of the intent such as &#x60;None&#x60;, &#x60;Single&#x60;, &#x60;Subscription&#x60;. | [optional] 
**payment_intent_id** | **str** | The id of the intent. | 
**transactions** | [**AuthReference**](AuthReference.md) |  | [optional] 

## Example

```python
from citypay.models.payment_intent_response_model import PaymentIntentResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentResponseModel from a JSON string
payment_intent_response_model_instance = PaymentIntentResponseModel.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentResponseModel.to_json())

# convert the object into a dict
payment_intent_response_model_dict = payment_intent_response_model_instance.to_dict()
# create an instance of PaymentIntentResponseModel from a dict
payment_intent_response_model_from_dict = PaymentIntentResponseModel.from_dict(payment_intent_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


