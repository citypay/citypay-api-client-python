# PaylinkFieldGuardModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_type** | **str** | A type of HTML element that should be displayed such as text, password, url. Any HTML5 input type value may be supplied. | [optional] 
**label** | **str** | A label for the field guard to display on the authentication page. | [optional] 
**maxlen** | **int** | A maximum length of any value supplied in the field guard form. Used for validating entry. | [optional] 
**minlen** | **int** | A minimum length of any value supplied in the field guard form. Used for validating entry. | [optional] 
**name** | **str** | A field name which is used to refer to a field which is guarded. | [optional] 
**regex** | **str** | A JavaScript regular expression value which can be used to validate the data provided in the field guard entry form. Used for validating entry. | [optional] 
**value** | **str** | A value directly associated with the field guard. Any value provided at this level will be considered as sensitive and not logged. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


