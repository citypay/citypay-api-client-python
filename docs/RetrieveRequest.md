# RetrieveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The identifier of the transaction to retrieve. Optional if a transaction number is provided. | [optional] 
**merchantid** | **int** | The merchant account to retrieve data for. | 
**transno** | **int** | The transaction number of a transaction to retrieve. Optional if an identifier is supplied. | [optional] 

## Example

```python
from citypay.models.retrieve_request import RetrieveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveRequest from a JSON string
retrieve_request_instance = RetrieveRequest.from_json(json)
# print the JSON string representation of the object
print RetrieveRequest.to_json()

# convert the object into a dict
retrieve_request_dict = retrieve_request_instance.to_dict()
# create an instance of RetrieveRequest from a dict
retrieve_request_form_dict = retrieve_request.from_dict(retrieve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


