# DirectPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195.  | 
**avs_postcode_policy** | **str** | A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are:   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   &#x60;2&#x60; to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   &#x60;3&#x60; to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation.  | [optional] 
**bill_to** | [**ContactDetails**](ContactDetails.md) |  | [optional] 
**cardnumber** | **str** | The card number (PAN) with a variable length to a maximum of 21 digits in numerical form. Any non numeric characters will be stripped out of the card number, this includes whitespace or separators internal of the provided value.  The card number must be treated as sensitive data. We only provide an obfuscated value in logging and reporting.  The plaintext value is encrypted in our database using AES 256 GMC bit encryption for settlement or refund purposes.  When providing the card number to our gateway through the authorisation API you will be handling the card data on your application. This will require further PCI controls to be in place and this value must never be stored.  | [optional] 
**csc** | **str** | The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify possession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm.  | [optional] 
**csc_policy** | **str** | A policy value which determines whether a CSC policy is enforced or bypassed.  Values are:   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   &#x60;2&#x60; to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   &#x60;3&#x60; to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation.  | [optional] 
**currency** | **str** | The processing currency for the transaction. Will default to the merchant account currency. | [optional] 
**duplicate_policy** | **str** | A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   &#x60;2&#x60; to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   &#x60;3&#x60; to ignore. Transactions that are ignored will have the same affect as bypass.  | [optional] 
**expmonth** | **int** | The month of expiry of the card. The month value should be a numerical value between 1 and 12.  | [optional] 
**expyear** | **int** | The year of expiry of the card.  | [optional] 
**identifier** | **str** | The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different.  | 
**mac** | **str** | A message authentication code ensures the data is authentic and that the intended amount has not been tampered with. The mac value is generated using a hash-based mac value. The following algorithm is used. - A key (k) is derived from your licence key - A value (v) is produced by concatenating the nonce, amount value and identifier, such as a purchase   with nonce &#x60;0123456789ABCDEF&#x60; an amount of £275.95 and an identifier of OD-12345678 would become   &#x60;0123456789ABCDEF27595OD-12345678&#x60; and extracting the UTF-8 byte values - The result from HMAC_SHA256(k, v) is hex-encoded (upper-case) - For instance, a licence key of &#x60;LK123456789&#x60;, a nonce of &#x60;0123456789ABCDEF&#x60;, an amount of &#x60;27595&#x60; and an identifier of &#x60;OD-12345678&#x60;  would generate a MAC of &#x60;163DBAB194D743866A9BCC7FC9C8A88FCD99C6BBBF08D619291212D1B91EE12E&#x60;.  | 
**match_avsa** | **str** | A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are:   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   &#x60;2&#x60; to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   &#x60;3&#x60; to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation.  | [optional] 
**name_on_card** | **str** | The card holder name as appears on the card such as MR N E BODY. Required for some acquirers.  | [optional] 
**nonce** | **str** | A random value Hex string (uppercase) which is provided to the API to perform a digest. The value will be used in any digest function.  | [optional] 
**pre_auth** | **str** | A policy value which determines whether a pre auth policy is enforced or bypassed.  Values are:   &#x60;0&#x60; for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   &#x60;1&#x60; for an enforced policy.  Enforces pre-authorisation when it does not pre-auth by default.   &#x60;2&#x60; to bypass. Bypasses pre-authorisation when it is enabled to pre auth by default.   &#x60;3&#x60; to ignore. The same as the default policy (0). Although it currently mirrors the default, this option is included for compatibility with other policies.  | [optional] 
**redirect_failure** | **str** | The URL used to redirect back to your site when a transaction has been rejected or declined. Required if a url-encoded request.  | [optional] 
**redirect_success** | **str** | The URL used to redirect back to your site when a transaction has been tokenised or authorised. Required if a url-encoded request.  | [optional] 
**ship_to** | [**ContactDetails**](ContactDetails.md) |  | [optional] 
**tag** | **List[str]** |  | [optional] 
**threedsecure** | [**ThreeDSecure**](ThreeDSecure.md) |  | [optional] 
**trans_info** | **str** | Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id. | [optional] 
**trans_type** | **str** | The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field. | [optional] 
**uuid** | **str** | A uuid for the session. The value tracks through 3ds session and therefore should be a valid v4 uuid. | [optional] 

## Example

```python
from citypay.models.direct_post_request import DirectPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DirectPostRequest from a JSON string
direct_post_request_instance = DirectPostRequest.from_json(json)
# print the JSON string representation of the object
print(DirectPostRequest.to_json())

# convert the object into a dict
direct_post_request_dict = direct_post_request_instance.to_dict()
# create an instance of DirectPostRequest from a dict
direct_post_request_from_dict = DirectPostRequest.from_dict(direct_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


