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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AdjustmentCondition(BaseModel):
    """
    AdjustmentCondition
    """ # noqa: E501
    anchor: Optional[StrictStr] = Field(default=None, description="Specifies the reference point (\"anchor\") and optional duration/range for when an adjustment  (such as a surcharge or discount) becomes effective in relation to the payment intent's lifecycle.   The period for which an adjustment is effective is determined by combining:    - An \"anchor\": a reference event, timestamp, or explicit date.    - A `duration`: an integer offset in days, whose meaning depends on the anchor.    - Optionally an explicit `startDate` and/or `endDate`, which take precedence.   Anchor types:   - Explicit Dates:    If both `startDate` and `endDate` are provided, these take priority as the exact active range.   - after_creation:      Starts `duration` days after the intent's creation date.      If an `endDate` is supplied, it is used as the end of the range.      If not, the adjustment remains open-ended (no explicit end).   - after_due_date:      Starts `duration` days after the intent's due date (if available).      If an `endDate` is specified, it is used as the end of the range.      Otherwise, the adjustment remains open-ended.   - on_due_date:      Starts on the due date.      If an `endDate` is specified and is after the due date, it is used as the end.      Otherwise, the end is computed as the due date plus `duration` days.   - until_due_date:      If `duration >= 0`, starts `duration` days after creation, and ends at due date.      If `duration < 0`, starts at creation and ends `abs(duration)` days before due date.   - before_expiry:      Starts at expiry date minus `duration` days (if expiry date is available).      Range extends up to expiry (default) or effectively open-ended.      If an `endDate` is specified and before expiry, the range is limited accordingly.   - yyyy-MM-dd (a valid ISO date string):      Effective on a specific date (midnight, or explicit time if provided), plus optional `duration` days.      In this case, the range is a single day, unless otherwise specified.    Example usages:    - Adjust 2 days after due: `anchor = \"after_due_date\", duration = 2`    - Early-bird: `anchor = \"until_due_date\", duration = -3` // from creation until 3 days before due    - From creation until due: `anchor = \"until_due_date\", duration = 0`    - Discount for a single date: `anchor = \"2024-07-01\"`   Notes:    - If `startDate` and `endDate` are both set, those take precedence over anchor/duration.    - If only `endDate` is specified with an anchor, the range starts at the anchor and ends at that date.    - If dates or anchor-related context are missing, no adjustment will be scheduled. ")
    discount_code: Optional[StrictStr] = Field(default=None, description="The discount code condition ensures that an adjustment is only applied if the correct promotional code is provided during the transaction.  Example: A 10% discount might only apply if the customer enters the discount code SEP24. ")
    duration: Optional[StrictInt] = Field(default=None, description="The duration specifies the time frame in days relative to the anchor point when the adjustment should be applied.")
    end_date: Optional[date] = Field(default=None, description="Define the exact date range within which an adjustment is valid, useful for promotional periods or specific events.")
    start_date: Optional[date] = Field(default=None, description="Define the exact date range within which an adjustment is valid, useful for promotional periods or specific events.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["anchor", "discount_code", "duration", "end_date", "start_date"]

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
        """Create an instance of AdjustmentCondition from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AdjustmentCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anchor": obj.get("anchor"),
            "discount_code": obj.get("discount_code"),
            "duration": obj.get("duration"),
            "end_date": obj.get("end_date"),
            "start_date": obj.get("start_date")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


