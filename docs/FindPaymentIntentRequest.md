# FindPaymentIntentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ref** | **str** | An external reference to lookup. | [optional] 
**external_ref_source** | **str** | An external reference source to lookup. | [optional] 
**merchantid** | **int** | The merchant id the payment intent is registered for. | [optional] 
**payment_intent_id** | **str** | The payment intent id, if known. | [optional] 

## Example

```python
from citypay.models.find_payment_intent_request import FindPaymentIntentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FindPaymentIntentRequest from a JSON string
find_payment_intent_request_instance = FindPaymentIntentRequest.from_json(json)
# print the JSON string representation of the object
print(FindPaymentIntentRequest.to_json())

# convert the object into a dict
find_payment_intent_request_dict = find_payment_intent_request_instance.to_dict()
# create an instance of FindPaymentIntentRequest from a dict
find_payment_intent_request_from_dict = FindPaymentIntentRequest.from_dict(find_payment_intent_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


