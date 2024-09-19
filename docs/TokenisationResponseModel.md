# TokenisationResponseModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authen_result** | **str** | The result of any authentication using 3d_secure authorisation against ecommerce transactions. Values are:  &lt;table&gt; &lt;tr&gt; &lt;th&gt;Value&lt;/th&gt; &lt;th&gt;Description&lt;/th&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;Y&lt;/td&gt; &lt;td&gt;Authentication Successful. The Cardholder&#39;s password was successfully validated.&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;N&lt;/td&gt; &lt;td&gt;Authentication Failed. Customer failed or cancelled authentication, transaction denied.&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;A&lt;/td&gt; &lt;td&gt;Attempts Processing Performed Authentication could not be completed but a proof of authentication attempt (CAVV) was generated.&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;U&lt;/td&gt; &lt;td&gt;Authentication Could Not Be Performed Authentication could not be completed, due to technical or other problem.&lt;/td&gt; &lt;/tr&gt; &lt;/table&gt;  | [optional] 
**bin_commercial** | **bool** | Determines whether the bin range was found to be a commercial or business card. | [optional] 
**bin_debit** | **bool** | Determines whether the bin range was found to be a debit card. If false the card was considered as a credit card. | [optional] 
**bin_description** | **str** | A description of the bin range found for the card. | [optional] 
**eci** | **str** | An Electronic Commerce Indicator (ECI) used to identify the result of authentication using 3DSecure.  | [optional] 
**identifier** | **str** | The identifier provided within the request. | [optional] 
**maskedpan** | **str** | A masked value of the card number used for processing displaying limited values that can be used on a receipt.  | [optional] 
**scheme** | **str** | The name of the card scheme of the transaction that processed the transaction such as Visa or MasterCard.  | [optional] 
**sig_id** | **str** | A Base58 encoded SHA-256 digest generated from the token value Base58 decoded and appended with the nonce value UTF-8 decoded. | [optional] 
**token** | **str** | The token used for presentment to authorisation later in the processing flow. | [optional] 

## Example

```python
from citypay.models.tokenisation_response_model import TokenisationResponseModel

# TODO update the JSON string below
json = "{}"
# create an instance of TokenisationResponseModel from a JSON string
tokenisation_response_model_instance = TokenisationResponseModel.from_json(json)
# print the JSON string representation of the object
print(TokenisationResponseModel.to_json())

# convert the object into a dict
tokenisation_response_model_dict = tokenisation_response_model_instance.to_dict()
# create an instance of TokenisationResponseModel from a dict
tokenisation_response_model_from_dict = TokenisationResponseModel.from_dict(tokenisation_response_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


