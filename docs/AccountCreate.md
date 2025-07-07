# AccountCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A card holder account id used for uniquely identifying the account. This value will be used for future referencing of the account oand to link your system to this API. This value is immutable and never changes.  | 
**contact** | [**ContactDetails**](ContactDetails.md) |  | [optional] 

## Example

```python
from citypay.models.account_create import AccountCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreate from a JSON string
account_create_instance = AccountCreate.from_json(json)
# print the JSON string representation of the object
print(AccountCreate.to_json())

# convert the object into a dict
account_create_dict = account_create_instance.to_dict()
# create an instance of AccountCreate from a dict
account_create_from_dict = AccountCreate.from_dict(account_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


