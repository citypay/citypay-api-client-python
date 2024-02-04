# RequestChallenged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | The url of the Access Control Server (ACS) to forward the user to.  | [optional] 
**creq** | **str** | The challenge request data which is encoded for usage by the ACS. | [optional] 
**merchantid** | **int** | The merchant id that processed this transaction. | [optional] 
**threedserver_trans_id** | **str** | The 3DSv2 trans id reference for the challenge process. May be used to create the ThreeDSSessionData value to send to the ACS. | [optional] 
**transno** | **int** | The transaction number for the challenge, ordered incrementally from 1 for every merchant_id.  | [optional] 

## Example

```python
from citypay.models.request_challenged import RequestChallenged

# TODO update the JSON string below
json = "{}"
# create an instance of RequestChallenged from a JSON string
request_challenged_instance = RequestChallenged.from_json(json)
# print the JSON string representation of the object
print RequestChallenged.to_json()

# convert the object into a dict
request_challenged_dict = request_challenged_instance.to_dict()
# create an instance of RequestChallenged from a dict
request_challenged_form_dict = request_challenged.from_dict(request_challenged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


