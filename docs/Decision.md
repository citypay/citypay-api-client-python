# Decision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_response** | [**AuthResponse**](AuthResponse.md) |  | [optional] 
**request_challenged** | [**RequestChallenged**](RequestChallenged.md) |  | [optional] 

## Example

```python
from citypay.models.decision import Decision

# TODO update the JSON string below
json = "{}"
# create an instance of Decision from a JSON string
decision_instance = Decision.from_json(json)
# print the JSON string representation of the object
print(Decision.to_json())

# convert the object into a dict
decision_dict = decision_instance.to_dict()
# create an instance of Decision from a dict
decision_from_dict = Decision.from_dict(decision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


