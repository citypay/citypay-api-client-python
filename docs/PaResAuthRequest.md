# PaResAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md** | **str** | The Merchant Data (MD) which is a unique ID to reference the authentication session.  This value will be created by CityPay when required. When responding from the ACS, this value will be returned by the ACS.  | 
**pares** | **str** | The Payer Authentication Response packet which is returned by the ACS containing the  response of the authentication session including verification values. The response  is a base64 encoded packet and should be forwarded to CityPay untouched.  | 

## Example

```python
from citypay.models.pa_res_auth_request import PaResAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaResAuthRequest from a JSON string
pa_res_auth_request_instance = PaResAuthRequest.from_json(json)
# print the JSON string representation of the object
print PaResAuthRequest.to_json()

# convert the object into a dict
pa_res_auth_request_dict = pa_res_auth_request_instance.to_dict()
# create an instance of PaResAuthRequest from a dict
pa_res_auth_request_form_dict = pa_res_auth_request.from_dict(pa_res_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


