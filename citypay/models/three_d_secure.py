# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is an HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokenized payments using cardholder Accounts.  ## Compliance and Security Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by  Visa and MasterCard and the PCI Security Standards Council. These include  * Data must be collected using TLS version 1.2 using [strong cryptography](https://citypay.github.io/api-docs/payment-api/#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive cardholder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities. 

    Contact: support@citypay.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ThreeDSecure(BaseModel):
    """
    ThreeDSecure
    """ # noqa: E501
    accept_headers: Optional[StrictStr] = Field(default=None, description="Required for 3DSv1. Optional if the `cp_bx` value is provided otherwise required for 3Dv2 processing operating in browser authentication mode.  The `cp_bx` value will override any value supplied to this field.  The content of the HTTP accept header as sent to the merchant from the cardholder's user agent.  This value will be validated by the ACS when the card holder authenticates themselves to verify that no intermediary is performing this action. Required for 3DSv1. ")
    browser_color_depth: Optional[StrictStr] = Field(default=None, description="BrowserColorDepth field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserColorDepth")
    browser_ip: Optional[StrictStr] = Field(default=None, description="BrowserIP field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserIP")
    browser_java_enabled: Optional[StrictStr] = Field(default=None, description="BrowserJavaEnabled field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserJavaEnabled")
    browser_language: Optional[StrictStr] = Field(default=None, description="BrowserLanguage field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserLanguage")
    browser_screen_height: Optional[StrictStr] = Field(default=None, description="BrowserScreenHeight field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserScreenHeight")
    browser_screen_width: Optional[StrictStr] = Field(default=None, description="BrowserScreenWidth field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserScreenWidth")
    browser_tz: Optional[StrictStr] = Field(default=None, description="BrowserTZ offset field used for 3DSv2 browser enablement. Recommendation is to use citypay.js and the `bx` function to gather this value.", alias="browserTZ")
    cp_bx: Optional[StrictStr] = Field(default=None, description="Required for 3DSv2.  Browser extension value produced by the citypay.js `bx` function. See [https://sandbox.citypay.com/3dsv2/bx](https://sandbox.citypay.com/3dsv2/bx) for  details. ")
    downgrade1: Optional[StrictBool] = Field(default=None, description="Where a merchant is configured for 3DSv2, setting this option will attempt to downgrade the transaction to  3DSv1. ")
    merchant_termurl: Optional[StrictStr] = Field(default=None, description="A controller URL for 3D-Secure processing that any response from an authentication request or challenge request should be sent to.  The controller should forward on the response from the URL back via this API for subsequent processing. ")
    tds_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether ThreeDSecure is enforced or bypassed. Note that this will only work for e-commerce transactions and accounts that have 3DSecure enabled and fully registered with Visa, MasterCard or American Express. It is useful when transactions may be wanted to bypass processing rules.  Note that this may affect the liability shift of transactions and may occur a higher fee with the acquiring bank.  Values are   `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions will be enabled for 3DS processing   `2` to bypass. Transactions that are bypassed will switch off 3DS processing. ")
    user_agent: Optional[StrictStr] = Field(default=None, description="Required for 3DSv1.  Optional if the `cp_bx` value is provided otherwise required 3Dv2 processing operating in browser authentication mode.  The `cp_bx` value will override any value supplied to this field.  The content of the HTTP user-agent header as sent to the merchant from the cardholder's user agent.  This value will be validated by the ACS when the card holder authenticates themselves to verify that no intermediary is performing this action. Required for 3DSv1. ")
    __properties: ClassVar[List[str]] = ["accept_headers", "browserColorDepth", "browserIP", "browserJavaEnabled", "browserLanguage", "browserScreenHeight", "browserScreenWidth", "browserTZ", "cp_bx", "downgrade1", "merchant_termurl", "tds_policy", "user_agent"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ThreeDSecure from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ThreeDSecure from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accept_headers": obj.get("accept_headers"),
            "browserColorDepth": obj.get("browserColorDepth"),
            "browserIP": obj.get("browserIP"),
            "browserJavaEnabled": obj.get("browserJavaEnabled"),
            "browserLanguage": obj.get("browserLanguage"),
            "browserScreenHeight": obj.get("browserScreenHeight"),
            "browserScreenWidth": obj.get("browserScreenWidth"),
            "browserTZ": obj.get("browserTZ"),
            "cp_bx": obj.get("cp_bx"),
            "downgrade1": obj.get("downgrade1"),
            "merchant_termurl": obj.get("merchant_termurl"),
            "tds_policy": obj.get("tds_policy"),
            "user_agent": obj.get("user_agent")
        })
        return _obj

