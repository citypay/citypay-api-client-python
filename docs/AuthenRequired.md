# AuthenRequired


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | The url of the Access Control Server (ACS) to forward the user to.  | [optional] 
**md** | **str** | Merchant Data (MD) which should be sent to the ACS to establish and reference the authentication session.  | [optional] 
**pareq** | **str** | The Payer Authentication Request packet which should be &#x60;POSTed&#x60; to the Url of the ACS to establish the authentication session. Data should be sent untouched.  | [optional] 

## Example

```python
from citypay.models.authen_required import AuthenRequired

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenRequired from a JSON string
authen_required_instance = AuthenRequired.from_json(json)
# print the JSON string representation of the object
print AuthenRequired.to_json()

# convert the object into a dict
authen_required_dict = authen_required_instance.to_dict()
# create an instance of AuthenRequired from a dict
authen_required_form_dict = authen_required.from_dict(authen_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


