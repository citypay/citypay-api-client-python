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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from citypay.models.three_d_secure import ThreeDSecure
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ChargeRequest(BaseModel):
    """
    ChargeRequest
    """ # noqa: E501
    amount: Annotated[int, Field(strict=True)] = Field(description="The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. ")
    avs_postcode_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. ")
    cardholder_agreement: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Merchant-initiated transactions (MITs) are payments you trigger, where the cardholder has previously consented to you carrying out such payments. These may be scheduled (such as recurring payments and installments) or unscheduled (like account top-ups triggered by balance thresholds and no-show charges).  Scheduled --- These are regular payments using stored card details, like installments or a monthly subscription fee.  - `I` Instalment - A single purchase of goods or services billed to a cardholder in multiple transactions, over a period of time agreed by the cardholder and you.  - `R` Recurring - Transactions processed at fixed, regular intervals not to exceed one year between transactions, representing an agreement between a cardholder and you to purchase goods or services provided over a period of time.  Unscheduled --- These are payments using stored card details that do not occur on a regular schedule, like top-ups for a digital wallet triggered by the balance falling below a certain threshold.  - `A` Reauthorisation - a purchase made after the original purchase. A common scenario is delayed/split shipments.  - `C` Unscheduled Payment - A transaction using a stored credential for a fixed or variable amount that does not occur on a scheduled or regularly occurring transaction date. This includes account top-ups triggered by balance thresholds.  - `D` Delayed Charge - A delayed charge is typically used in hotel, cruise lines and vehicle rental environments to perform a supplemental account charge after original services are rendered.  - `L` Incremental - An incremental authorisation is typically found in hotel and car rental environments, where the cardholder has agreed to pay for any service incurred during the duration of the contract. An incremental authorisation is where you need to seek authorisation of further funds in addition to what you have originally requested. A common scenario is additional services charged to the contract, such as extending a stay in a hotel.  - `S` Resubmission - When the original purchase occurred, but you were not able to get authorisation at the time the goods or services were provided. It should be only used where the goods or services have already been provided, but the authorisation request is declined for insufficient funds.  - `X` No-show - A no-show is a transaction where you are enabled to charge for services which the cardholder entered into an agreement to purchase, but the cardholder did not meet the terms of the agreement. ")
    csc: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]] = Field(default=None, description="The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify posession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. ")
    csc_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether a CSC policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. ")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="The processing currency for the transaction. Will default to the merchant account currency.")
    duplicate_policy: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. ")
    identifier: Annotated[str, Field(min_length=4, strict=True, max_length=50)] = Field(description="The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. ")
    initiation: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="Transactions charged using the API are defined as:  **Cardholder Initiated**: A _cardholder initiated transaction_ (CIT) is where the cardholder selects the card for use for a purchase using previously stored details. An example would be a customer buying an item from your website after being present with their saved card details at checkout.  **Merchant Intiated**: A _merchant initiated transaction_ (MIT) is an authorisation initiated where you as the  merchant submit a cardholders previously stored details without the cardholder's participation. An example would  be a subscription to a membership scheme to debit their card monthly.  MITs have different reasons such as reauthorisation, delayed, unscheduled, incremental, recurring, instalment, no-show or resubmission.  The following values apply   - `M` - specifies that the transaction is initiated by the merchant   - `C` - specifies that the transaction is initiated by the cardholder  Where transactions are merchant initiated, a valid cardholder agreement must be defined. ")
    match_avsa: Optional[StrictStr] = Field(default=None, description="A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. ")
    merchantid: StrictInt = Field(description="Identifies the merchant account to perform processing for.")
    tag: Optional[StrictStr] = Field(default=None, description="A \"tag\" is a label that you can attach to a payment authorization. Tags can help you group transactions together based on certain criteria, like a work job or a ticket number. They can also assist in filtering transactions when you're generating reports.  Multiple Tags You can add more than one tag to a transaction by separating them with commas.  Limitations There is a maximum limit of 3 tags that can be added to a single transaction. Each tag can be no longer than 20 characters and alphanumeric with no spaces.  Example: Let's say you're a software company and you have different teams working on various projects. When a team makes a purchase or incurs an expense, they can tag the transaction with the project name, the team name, and the type of expense.  Project Name: Project_X Team Name: Team_A Type of Expense: Hardware So, the tag for a transaction might look like: Project_X,Team_A,Hardware  This way, when you're looking at your financial reports, you can easily filter transactions based on these tags to see how much each project or team is spending on different types of expenses. ")
    threedsecure: Optional[ThreeDSecure] = None
    token: StrictStr = Field(description="A tokenised form of a card that belongs to a card holder's account and that has been previously registered. The token is time based and will only be active for a short duration. The value is therefore designed not to be stored remotely for future use.   Tokens will start with ct and are resiliently tamper proof using HMacSHA-256. No sensitive card data is stored internally within the token.   Each card will contain a different token and the value may be different on any retrieval call.   The value can be presented for payment as a selection value to an end user in a web application. ")
    trans_info: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.")
    trans_type: Optional[Annotated[str, Field(strict=True, max_length=1)]] = Field(default=None, description="The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field.")
    __properties: ClassVar[List[str]] = ["amount", "avs_postcode_policy", "cardholder_agreement", "csc", "csc_policy", "currency", "duplicate_policy", "identifier", "initiation", "match_avsa", "merchantid", "tag", "threedsecure", "token", "trans_info", "trans_type"]

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
        """Create an instance of ChargeRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of threedsecure
        if self.threedsecure:
            _dict['threedsecure'] = self.threedsecure.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ChargeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "avs_postcode_policy": obj.get("avs_postcode_policy"),
            "cardholder_agreement": obj.get("cardholder_agreement"),
            "csc": obj.get("csc"),
            "csc_policy": obj.get("csc_policy"),
            "currency": obj.get("currency"),
            "duplicate_policy": obj.get("duplicate_policy"),
            "identifier": obj.get("identifier"),
            "initiation": obj.get("initiation"),
            "match_avsa": obj.get("match_avsa"),
            "merchantid": obj.get("merchantid"),
            "tag": obj.get("tag"),
            "threedsecure": ThreeDSecure.from_dict(obj.get("threedsecure")) if obj.get("threedsecure") is not None else None,
            "token": obj.get("token"),
            "trans_info": obj.get("trans_info"),
            "trans_type": obj.get("trans_type")
        })
        return _obj


