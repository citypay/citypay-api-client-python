# Batch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_date** | **date** | The date that the file was created in ISO-8601 format. | 
**batch_id** | **int** | The batch id requested. | [optional] 
**batch_status** | **str** | The status of the batch. Possible values are:    - CANCELLED. The file has been cancelled by an administrator or server process.  - COMPLETE. The file has passed through the processing cycle and is determined as being complete further information should be obtained on the results of the processing - ERROR_IN_PROCESSING. Errors have occurred in the processing that has deemed that processing can not continue. - INITIALISED. The file has been initialised and no action has yet been performed - LOCKED. The file has been locked for processing - QUEUED. The file has been queued for processing yet no processing has yet been performed - UNKNOWN. The file is of an unknown status, that is the file can either not be determined by the information requested of the file has not yet been received.  | 

## Example

```python
from citypay.models.batch import Batch

# TODO update the JSON string below
json = "{}"
# create an instance of Batch from a JSON string
batch_instance = Batch.from_json(json)
# print the JSON string representation of the object
print Batch.to_json()

# convert the object into a dict
batch_dict = batch_instance.to_dict()
# create an instance of Batch from a dict
batch_form_dict = batch.from_dict(batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


