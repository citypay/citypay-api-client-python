# DirectTokenAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** | A random value string which is provided to the API to perform a digest. The value will be used by its UTF-8 byte representation of any digest function.  | [optional] 
**redirect_failure** | **str** | The URL used to redirect back to your site when a transaction has been rejected or declined. Required if a url-encoded request.  | [optional] 
**redirect_success** | **str** | The URL used to redirect back to your site when a transaction has been authorised. Required if a url-encoded request.  | [optional] 
**token** | **str** | The token required to process the transaction as presented by the direct post methodology.  | [optional] 

## Example

```python
from citypay.models.direct_token_auth_request import DirectTokenAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DirectTokenAuthRequest from a JSON string
direct_token_auth_request_instance = DirectTokenAuthRequest.from_json(json)
# print the JSON string representation of the object
print(DirectTokenAuthRequest.to_json())

# convert the object into a dict
direct_token_auth_request_dict = direct_token_auth_request_instance.to_dict()
# create an instance of DirectTokenAuthRequest from a dict
direct_token_auth_request_from_dict = DirectTokenAuthRequest.from_dict(direct_token_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


