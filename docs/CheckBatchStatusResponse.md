# CheckBatchStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batches** | [**List[Batch]**](Batch.md) |  | [optional] 

## Example

```python
from citypay.models.check_batch_status_response import CheckBatchStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckBatchStatusResponse from a JSON string
check_batch_status_response_instance = CheckBatchStatusResponse.from_json(json)
# print the JSON string representation of the object
print CheckBatchStatusResponse.to_json()

# convert the object into a dict
check_batch_status_response_dict = check_batch_status_response_instance.to_dict()
# create an instance of CheckBatchStatusResponse from a dict
check_batch_status_response_form_dict = check_batch_status_response.from_dict(check_batch_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


