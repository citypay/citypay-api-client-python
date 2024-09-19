# PaymentIntentReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_intent_id** | **str** | The intent id used for future referencing of the intent. | 

## Example

```python
from citypay.models.payment_intent_reference import PaymentIntentReference

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentReference from a JSON string
payment_intent_reference_instance = PaymentIntentReference.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentReference.to_json())

# convert the object into a dict
payment_intent_reference_dict = payment_intent_reference_instance.to_dict()
# create an instance of PaymentIntentReference from a dict
payment_intent_reference_from_dict = PaymentIntentReference.from_dict(payment_intent_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


