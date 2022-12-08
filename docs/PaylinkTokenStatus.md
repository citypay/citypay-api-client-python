# PaylinkTokenStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_paid** | **int** | the amount that has been paid against the session. | [optional] 
**auth_code** | **str** | an authorisation code if the transaction was processed and isPaid is true. | [optional] 
**card** | **str** | a description of the card that was used for payment if paid. | [optional] 
**created** | **datetime** | the date and time that the session was created. | [optional] 
**datetime** | **datetime** | the date and time of the current status. | [optional] 
**identifier** | **str** | the merchant identifier, to help identifying the token. | [optional] 
**is_attachment** | **bool** | true if an attachment exists. | [optional] 
**is_cancelled** | **bool** | true if the session was cancelled either by the user or by a system request. | [optional] 
**is_closed** | **bool** | true if the token has been closed. | [optional] 
**is_customer_receipt_email_sent** | **bool** | true if a customer receipt has been sent. | [optional] 
**is_email_sent** | **bool** | true if an email was sent. | [optional] 
**is_expired** | **bool** | true if the session has expired. | [optional] 
**is_form_viewed** | **bool** | true if the form was ever displayed to the addressee. | [optional] 
**is_merchant_notification_email_sent** | **bool** | true if a merchant notification receipt was sent. | [optional] 
**is_open_for_payment** | **bool** | true if the session is still open for payment or false if it has been closed. | [optional] 
**is_paid** | **bool** | whether the session has been paid and therefore can be considered as complete. | [optional] 
**is_payment_attempted** | **bool** | true if payment has been attempted. | [optional] 
**is_postback_ok** | **bool** | true if a post back was executed successfully. | [optional] 
**is_request_challenged** | **bool** | true if the request has been challenged using 3-D Secure. | [optional] 
**is_sms_sent** | **bool** | true if an SMS was sent. | [optional] 
**is_validated** | **bool** | whether the token generation was successfully validated. | [optional] 
**last_event_date_time** | **datetime** | the date and time that the session last had an event actioned against it. | [optional] 
**last_payment_result** | **str** | the result of the last payment if one exists. | [optional] 
**mid** | **str** | identifies the merchant account. | [optional] 
**payment_attempts_count** | **int** | the number of attempts made to pay. | [optional] 
**state_history** | [**[PaylinkStateEvent]**](PaylinkStateEvent.md) |  | [optional] 
**token** | **str** | the token value which uniquely identifies the session. | [optional] 
**trans_no** | **int** | a transaction number if the transacstion was processed and isPaid is true. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


