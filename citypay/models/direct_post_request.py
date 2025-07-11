# coding: utf-8

"""
    CityPay Payment API

     Welcome to the CityPay API, a robust HTTP API payment solution designed for seamless server-to-server  transactional processing. Our API facilitates a wide array of payment operations, catering to diverse business needs.  Whether you're integrating Internet payments, handling Mail Order/Telephone Order (MOTO) transactions, managing  Subscriptions with Recurring and Continuous Authority payments, or navigating the complexities of 3-D Secure  authentication, our API is equipped to support your requirements. Additionally, we offer functionalities for  Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids, and Completion processing, alongside the capability  for tokenised payments.  ## Compliance and Security Overview <aside class=\"notice\">   Ensuring the security of payment transactions and compliance with industry standards is paramount. Our API is    designed with stringent security measures and compliance protocols to safeguard sensitive information and meet    the rigorous requirements of Visa, MasterCard, and the PCI Security Standards Council. </aside>  ### Key Compliance and Security Measures  * **TLS Encryption**: All data transmissions must utilise TLS version 1.2 or higher, employing [strong cryptography](#enabled-tls-ciphers). Our infrastructure strictly enforces this requirement to maintain the integrity and confidentiality of data in transit. We conduct regular scans and assessments of our TLS endpoints to identify and mitigate vulnerabilities. * **Data Storage Prohibitions**: Storing sensitive cardholder data (CHD), such as the card security code (CSC) or primary account number (PAN), is strictly prohibited. Our API is designed to minimize your exposure to sensitive data, thereby reducing your compliance burden. * **Data Masking**: For consumer protection and compliance, full card numbers must not be displayed on receipts or any customer-facing materials. Our API automatically masks PANs, displaying only the last four digits to facilitate safe receipt generation. * **Network Scans**: If your application is web-based, regular scans of your hosting environment are mandatory to identify and rectify potential vulnerabilities. This proactive measure is crucial for maintaining a secure and compliant online presence. * **PCI Compliance**: Adherence to PCI DSS standards is not optional; it's a requirement for operating securely and legally in the payments ecosystem. For detailed information on compliance requirements and resources, please visit the PCI Security Standards Council website [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/). * **Request Validation**: Our API includes mechanisms to verify the legitimacy of each request, ensuring it pertains to a valid account and originates from a trusted source. We leverage remote IP address verification alongside sophisticated application firewall technologies to thwart a wide array of common security threats.  ## Getting Started Before integrating with the CityPay API, ensure your application and development practices align with the outlined compliance and security measures. This preparatory step is crucial for a smooth integration process and the long-term success of your payment processing operations.  For further details on API endpoints, request/response formats, and code examples, proceed to the subsequent sections of our documentation. Our aim is to provide you with all the necessary tools and information to integrate our payment processing capabilities seamlessly into your application.  Thank you for choosing CityPay API. We look forward to supporting your payment processing needs with our secure, compliant, and versatile API solution. 

    Contact: support@citypay.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from citypay.models.contact_details import ContactDetails
from citypay.models.three_d_secure import ThreeDSecure
from typing import Optional, Set
from typing_extensions import Self

class DirectPostRequest(BaseModel):
    """
    DirectPostRequest
    """ # noqa: E501
    amount: Annotated[int, Field(strict=True)] = Field(description="The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. ")
    avs_postcode_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are:   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. ")
    bill_to: Optional[ContactDetails] = None
    cardnumber: Optional[Annotated[str, Field(min_length=12, strict=True, max_length=22)]] = Field(default=None, description="The card number (PAN) with a variable length to a maximum of 21 digits in numerical form. Any non numeric characters will be stripped out of the card number, this includes whitespace or separators internal of the provided value.  The card number must be treated as sensitive data. We only provide an obfuscated value in logging and reporting.  The plaintext value is encrypted in our database using AES 256 GMC bit encryption for settlement or refund purposes.  When providing the card number to our gateway through the authorisation API you will be handling the card data on your application. This will require further PCI controls to be in place and this value must never be stored. ")
    csc: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]] = Field(default=None, description="The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify possession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. ")
    csc_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether a CSC policy is enforced or bypassed.  Values are:   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. ")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="The processing currency for the transaction. Will default to the merchant account currency.")
    duplicate_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. ")
    expmonth: Optional[Annotated[int, Field(le=12, strict=True, ge=1)]] = Field(default=None, description="The month of expiry of the card. The month value should be a numerical value between 1 and 12. ")
    expyear: Optional[Annotated[int, Field(le=2100, strict=True, ge=2000)]] = Field(default=None, description="The year of expiry of the card. ")
    identifier: Annotated[str, Field(min_length=4, strict=True, max_length=50)] = Field(description="The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. ")
    mac: StrictStr = Field(description="A message authentication code ensures the data is authentic and that the intended amount has not been tampered with. The mac value is generated using a hash-based mac value. The following algorithm is used. - A key (k) is derived from your licence key - A value (v) is produced by concatenating the nonce, amount value and identifier, such as a purchase   with nonce `0123456789ABCDEF` an amount of £275.95 and an identifier of OD-12345678 would become   `0123456789ABCDEF27595OD-12345678` and extracting the UTF-8 byte values - The result from HMAC_SHA256(k, v) is hex-encoded (upper-case) - For instance, a licence key of `LK123456789`, a nonce of `0123456789ABCDEF`, an amount of `27595` and an identifier of `OD-12345678`  would generate a MAC of `163DBAB194D743866A9BCC7FC9C8A88FCD99C6BBBF08D619291212D1B91EE12E`. ")
    match_avsa: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are:   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. ")
    name_on_card: Optional[Annotated[str, Field(min_length=2, strict=True, max_length=45)]] = Field(default=None, description="The card holder name as appears on the card such as MR N E BODY. Required for some acquirers. ")
    nonce: Optional[StrictStr] = Field(default=None, description="A random value Hex string (uppercase) which is provided to the API to perform a digest. The value will be used in any digest function. ")
    pre_auth: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether a pre auth policy is enforced or bypassed.  Values are:   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy.  Enforces pre-authorisation when it does not pre-auth by default.   `2` to bypass. Bypasses pre-authorisation when it is enabled to pre auth by default.   `3` to ignore. The same as the default policy (0). Although it currently mirrors the default, this option is included for compatibility with other policies. ")
    redirect_failure: Optional[StrictStr] = Field(default=None, description="The URL used to redirect back to your site when a transaction has been rejected or declined. Required if a url-encoded request. ")
    redirect_success: Optional[StrictStr] = Field(default=None, description="The URL used to redirect back to your site when a transaction has been tokenised or authorised. Required if a url-encoded request. ")
    ship_to: Optional[ContactDetails] = None
    tag: Optional[List[StrictStr]] = None
    threedsecure: Optional[ThreeDSecure] = None
    trans_info: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.")
    trans_type: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field.")
    uuid: Optional[Annotated[str, Field(min_length=36, strict=True, max_length=36)]] = Field(default=None, description="A uuid for the session. The value tracks through 3ds session and therefore should be a valid v4 uuid.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["amount", "avs_postcode_policy", "bill_to", "cardnumber", "csc", "csc_policy", "currency", "duplicate_policy", "expmonth", "expyear", "identifier", "mac", "match_avsa", "name_on_card", "nonce", "pre_auth", "redirect_failure", "redirect_success", "ship_to", "tag", "threedsecure", "trans_info", "trans_type", "uuid"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DirectPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of bill_to
        if self.bill_to:
            _dict['bill_to'] = self.bill_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to
        if self.ship_to:
            _dict['ship_to'] = self.ship_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threedsecure
        if self.threedsecure:
            _dict['threedsecure'] = self.threedsecure.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DirectPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "avs_postcode_policy": obj.get("avs_postcode_policy"),
            "bill_to": ContactDetails.from_dict(obj["bill_to"]) if obj.get("bill_to") is not None else None,
            "cardnumber": obj.get("cardnumber"),
            "csc": obj.get("csc"),
            "csc_policy": obj.get("csc_policy"),
            "currency": obj.get("currency"),
            "duplicate_policy": obj.get("duplicate_policy"),
            "expmonth": obj.get("expmonth"),
            "expyear": obj.get("expyear"),
            "identifier": obj.get("identifier"),
            "mac": obj.get("mac"),
            "match_avsa": obj.get("match_avsa"),
            "name_on_card": obj.get("name_on_card"),
            "nonce": obj.get("nonce"),
            "pre_auth": obj.get("pre_auth"),
            "redirect_failure": obj.get("redirect_failure"),
            "redirect_success": obj.get("redirect_success"),
            "ship_to": ContactDetails.from_dict(obj["ship_to"]) if obj.get("ship_to") is not None else None,
            "tag": obj.get("tag"),
            "threedsecure": ThreeDSecure.from_dict(obj["threedsecure"]) if obj.get("threedsecure") is not None else None,
            "trans_info": obj.get("trans_info"),
            "trans_type": obj.get("trans_type"),
            "uuid": obj.get("uuid")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


