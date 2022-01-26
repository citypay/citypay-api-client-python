# BatchReportResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The total amount that the batch contains. | 
**batch_date** | **date** | The date and time of the batch in ISO-8601 format. | 
**batch_id** | **[int]** |  | 
**batch_status** | **str** | The status of the batch. Possible values are - CANCELLED. The file has been cancelled by an administrator or server process.  - COMPLETE. The file has passed through the processing cycle and is determined as being complete further information should be obtained on the results of the processing - ERROR_IN_PROCESSING. Errors have occurred in the processing that has deemed that processing can not continue. - INITIALISED. The file has been initialised and no action has yet been performed - LOCKED. The file has been locked for processing - QUEUED. The file has been queued for processing yet no processing has yet been performed - UNKNOWN. The file is of an unknown status, that is the file can either not be determined by the information requested of the file has not yet been received.  | 
**client_account_id** | **str** | The batch account id that the batch was processed with. | 
**transactions** | [**[BatchTransactionResultModel]**](BatchTransactionResultModel.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


