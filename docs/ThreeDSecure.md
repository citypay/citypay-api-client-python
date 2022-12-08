# ThreeDSecure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_headers** | **str** | Required for 3DSv1. Optional if the &#x60;cp_bx&#x60; value is provided otherwise required for 3Dv2 processing operating in browser authentication mode.  The &#x60;cp_bx&#x60; value will override any value supplied to this field.  The content of the HTTP accept header as sent to the merchant from the cardholder&#39;s user agent.  This value will be validated by the ACS when the card holder authenticates themselves to verify that no intermediary is performing this action. Required for 3DSv1.  | [optional] 
**browser_color_depth** | **str** | BrowserColorDepth field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_ip** | **str** | BrowserIP field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_java_enabled** | **str** | BrowserJavaEnabled field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_language** | **str** | BrowserLanguage field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_screen_height** | **str** | BrowserScreenHeight field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_screen_width** | **str** | BrowserScreenWidth field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**browser_tz** | **str** | BrowserTZ field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the &#x60;bx&#x60; function to gather this value. | [optional] 
**cp_bx** | **str** | Required for 3DSv2.  Browser extension value produced by the citypay.js &#x60;bx&#x60; function. See [https://sandbox.citypay.com/3dsv2/bx](https://sandbox.citypay.com/3dsv2/bx) for  details.  | [optional] 
**downgrade1** | **bool** | Where a merchant is configured for 3DSv2, setting this option will attempt to downgrade the transaction to  3DSv1.  | [optional] 
**merchant_termurl** | **str** | A controller URL for 3D-Secure processing that any response from an authentication request or challenge request should be sent to.  The controller should forward on the response from the URL back via this API for subsequent processing.  | [optional] 
**tds_policy** | **str** | A policy value which determines whether ThreeDSecure is enforced or bypassed. Note that this will only work for e-commerce transactions and accounts that have 3DSecure enabled and fully registered with Visa, MasterCard or American Express. It is useful when transactions may be wanted to bypass processing rules.  Note that this may affect the liability shift of transactions and may occur a higher fee with the acquiring bank.  Values are   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy. Transactions will be enabled for 3DS processing   &#x60;2&#x60; to bypass. Transactions that are bypassed will switch off 3DS processing.  | [optional] 
**user_agent** | **str** | Required for 3DSv1.  Optional if the &#x60;cp_bx&#x60; value is provided otherwise required 3Dv2 processing operating in browser authentication mode.  The &#x60;cp_bx&#x60; value will override any value supplied to this field.  The content of the HTTP user-agent header as sent to the merchant from the cardholder&#39;s user agent.  This value will be validated by the ACS when the card holder authenticates themselves to verify that no intermediary is performing this action. Required for 3DSv1.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


