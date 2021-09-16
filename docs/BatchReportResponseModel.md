# BatchReportResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The batch account id that the batch was processed with. | 
**amount** | **int** | The total amount that the batch contains. | 
**batch_date** | **datetime** | The date and time of the batch in ISO-8601 format. | 
**batch_id** | **int** | The batch id specified in the batch processing request. | 
**batch_status** | **str** | The status of the batch. Possible values are. | 
**transactions** | [**[BatchTransactionResultModel]**](BatchTransactionResultModel.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


