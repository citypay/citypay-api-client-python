# CResAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cres** | **str** | The challenge response data forwarded by the ACS in 3D-Secure V2 processing. Data should be forwarded to CityPay unchanged for subsequent authorisation and processing.  | [optional] 

## Example

```python
from citypay.models.c_res_auth_request import CResAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CResAuthRequest from a JSON string
c_res_auth_request_instance = CResAuthRequest.from_json(json)
# print the JSON string representation of the object
print(CResAuthRequest.to_json())

# convert the object into a dict
c_res_auth_request_dict = c_res_auth_request_instance.to_dict()
# create an instance of CResAuthRequest from a dict
c_res_auth_request_from_dict = CResAuthRequest.from_dict(c_res_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


