# ProcessBatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Information regarding the processing request. | [optional] 
**valid** | **bool** | true if the request has been accepted for processing and is valid. | 

## Example

```python
from citypay.models.process_batch_response import ProcessBatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessBatchResponse from a JSON string
process_batch_response_instance = ProcessBatchResponse.from_json(json)
# print the JSON string representation of the object
print ProcessBatchResponse.to_json()

# convert the object into a dict
process_batch_response_dict = process_batch_response_instance.to_dict()
# create an instance of ProcessBatchResponse from a dict
process_batch_response_form_dict = process_batch_response.from_dict(process_batch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


