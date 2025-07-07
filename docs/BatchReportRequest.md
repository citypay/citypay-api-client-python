# BatchReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_id** | **int** | The batch id specified in the batch processing request. | 
**client_account_id** | **str** | The batch account id that the batch was processed for. Defaults to your client id if not provided. | [optional] 

## Example

```python
from citypay.models.batch_report_request import BatchReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchReportRequest from a JSON string
batch_report_request_instance = BatchReportRequest.from_json(json)
# print the JSON string representation of the object
print(BatchReportRequest.to_json())

# convert the object into a dict
batch_report_request_dict = batch_report_request_instance.to_dict()
# create an instance of BatchReportRequest from a dict
batch_report_request_from_dict = BatchReportRequest.from_dict(batch_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


