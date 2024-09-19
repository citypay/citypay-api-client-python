# CheckBatchStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **List[int]** |  | 
**client_account_id** | **str** | The batch account id to obtain the batch for. Defaults to your client id if not provided. | [optional] 

## Example

```python
from citypay.models.check_batch_status import CheckBatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CheckBatchStatus from a JSON string
check_batch_status_instance = CheckBatchStatus.from_json(json)
# print the JSON string representation of the object
print(CheckBatchStatus.to_json())

# convert the object into a dict
check_batch_status_dict = check_batch_status_instance.to_dict()
# create an instance of CheckBatchStatus from a dict
check_batch_status_from_dict = CheckBatchStatus.from_dict(check_batch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


