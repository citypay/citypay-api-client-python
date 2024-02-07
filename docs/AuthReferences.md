# AuthReferences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auths** | [**List[AuthReference]**](AuthReference.md) |  | [optional] 

## Example

```python
from citypay.models.auth_references import AuthReferences

# TODO update the JSON string below
json = "{}"
# create an instance of AuthReferences from a JSON string
auth_references_instance = AuthReferences.from_json(json)
# print the JSON string representation of the object
print AuthReferences.to_json()

# convert the object into a dict
auth_references_dict = auth_references_instance.to_dict()
# create an instance of AuthReferences from a dict
auth_references_form_dict = auth_references.from_dict(auth_references_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


