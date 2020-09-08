# CaptureRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airline_data** | [**AirlineAdvice**](AirlineAdvice.md) |  | [optional] 
**amount** | **int** | The completion amount provided in the lowest unit of currency for the specific currency of the merchant, with a variable length to a maximum of 12 digits. No decimal points to be included. For example with GBP 75.45 use the value 7545. Please check that you do not supply divisional characters such as 1,024 in the request which may be caused by some number formatters. If no amount is supplied, the original processing amount is used.  | [optional] 
**identifier** | **str** | The identifier of the transaction to capture. If an empty value is supplied then a &#x60;trans_no&#x60; value must be supplied. | [optional] 
**merchantid** | **int** | Identifies the merchant account to perform the capture for. | 
**sdk** | **str** | An optional reference value for the calling client such as a version number i.e. | [optional] 
**transno** | **int** | The transaction number of the transaction to look up and capture. If an empty value is supplied then an identifier value must be supplied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

