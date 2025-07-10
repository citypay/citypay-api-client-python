# PaylinkConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_mode** | **str** | Specifies the approach to be adopted by the Paylink form when displaying a 3-D Secure challenge window. The values may be   - &#x60;iframe&#x60; shows the 3-D Secure ACS in an iframe dialog, neatly embedding it in Paylink. This provides a more seamless flow for the cardholder who is able to validate and authenticate their card using a dialog provided by their card issuer.  - &#x60;inline&#x60; an inline mode transfers the full browser window to the authentication server, allowing the payment cardholder to see their payment card issuer&#39;s URL and the certificate status in the browser.  If you request an iframe mode and the browser width is deemed as being small (&lt; 768px) then an inline mode will be enforced. This is to ensure that mobile users have an appropriate user experience.  The default type if not supplied is **iframe**.  | [optional] 
**custom_params** | [**List[PaylinkCustomParam]**](PaylinkCustomParam.md) |  | [optional] 
**descriptor** | **str** | Directly specify the merchant descriptor used for the transaction to be displayed on the payment page. | [optional] 
**expire_in** | **str** | Specifies a period of time in seconds after which the token cannot be used. A value of 0 defines that the token will never expire. The API will convert an expiry time based on a string value.  For instance: -  s - Time in seconds, for example 90s. -  m - Time in minutes, for example 20m. -  h - Time in hours, for example 4h. -  w - Time in weeks, for example 4w. -  M - Time in months, for example 6M. -  y - Time in years, for example 1y. -  Defaults to 30 minutes.  | [optional] 
**field_guard** | [**List[PaylinkFieldGuardModel]**](PaylinkFieldGuardModel.md) |  | [optional] 
**lock_params** | **List[str]** |  | [optional] 
**merch_logo** | **str** | A URL of a logo to include in the form. The URL should be delivered using HTTPS. | [optional] 
**merch_terms** | **str** | A URL of the merchant terms and conditions for payment. If a value is supplied, a checkbox will be required to be completed to confirm that the cardholder agrees to these conditions before payment. A modal dialogue is displayed with the content of the conditions displayed. | [optional] 
**meta_data** | **Dict[str, str]** |  | [optional] 
**options** | **List[str]** |  | [optional] 
**part_payments** | [**PaylinkPartPayments**](PaylinkPartPayments.md) |  | [optional] 
**pass_through_data** | **Dict[str, str]** |  | [optional] 
**pass_through_headers** | **Dict[str, str]** |  | [optional] 
**postback** | **str** | Specifies a URL to use for a call back when the payment is completed. see Postback Handling }. | [optional] 
**postback_password** | **str** | A password to be added to the postback for HTTP Basic Authentication. | [optional] 
**postback_policy** | **str** | The policy setting for the postback see Postback Handling. | [optional] 
**postback_username** | **str** | A username to be added to the postback for HTTP Basic Authentication. | [optional] 
**redirect_delay** | **int** | A value which can delay the redirection in seconds. A value of 0 will redirect immediately. | [optional] 
**redirect_failure** | **str** | A URL which the browser is redirected to on non-completion of a transaction. | [optional] 
**redirect_success** | **str** | A URL which the browser is redirected to on authorisation of a transaction. | [optional] 
**renderer** | **str** | The Paylink renderer engine to use. | [optional] 
**return_params** | **bool** | If a value of true is specified, any redirection will include the transaction result in parameters. It is recommended to use the postback integration rather than redirection parameters. | [optional] 
**ui** | [**PaylinkUI**](PaylinkUI.md) |  | [optional] 

## Example

```python
from citypay.models.paylink_config import PaylinkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PaylinkConfig from a JSON string
paylink_config_instance = PaylinkConfig.from_json(json)
# print the JSON string representation of the object
print(PaylinkConfig.to_json())

# convert the object into a dict
paylink_config_dict = paylink_config_instance.to_dict()
# create an instance of PaylinkConfig from a dict
paylink_config_from_dict = PaylinkConfig.from_dict(paylink_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


