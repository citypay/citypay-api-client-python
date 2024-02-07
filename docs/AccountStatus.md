# AccountStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the account to set, valid values are ACTIVE or DISABLED. | [optional] 

## Example

```python
from citypay.models.account_status import AccountStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStatus from a JSON string
account_status_instance = AccountStatus.from_json(json)
# print the JSON string representation of the object
print AccountStatus.to_json()

# convert the object into a dict
account_status_dict = account_status_instance.to_dict()
# create an instance of AccountStatus from a dict
account_status_form_dict = account_status.from_dict(account_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


