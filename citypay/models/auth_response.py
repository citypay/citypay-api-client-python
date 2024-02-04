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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AuthResponse(BaseModel):
    """
    AuthResponse
    """ # noqa: E501
    amount: Optional[StrictInt] = Field(default=None, description="The amount of the transaction processed.")
    atrn: Optional[StrictStr] = Field(default=None, description="A reference number provided by the acquirer for a transaction it can be used to cross reference transactions with an Acquirers reporting panel. ")
    atsd: Optional[StrictStr] = Field(default=None, description="Additional Transaction Security Data used for ecommerce transactions to decipher security capabilities and attempts against a transaction.")
    authcode: Optional[StrictStr] = Field(default=None, description="The authorisation code as returned by the card issuer or acquiring bank when a transaction has successfully   been authorised. Authorisation codes contain alphanumeric values. Whilst the code confirms authorisation it   should not be used to determine whether a transaction was successfully processed. For instance an auth code   may be returned when a transaction has been subsequently declined due to a CSC mismatch. ")
    authen_result: Optional[StrictStr] = Field(default=None, description="The result of any authentication using 3d_secure authorisation against ecommerce transactions. Values are:  <table> <tr> <th>Value</th> <th>Description</th> </tr> <tr> <td>Y</td> <td>Authentication Successful. The Cardholder's password was successfully validated.</td> </tr> <tr> <td>N</td> <td>Authentication Failed. Customer failed or cancelled authentication, transaction denied.</td> </tr> <tr> <td>A</td> <td>Attempts Processing Performed Authentication could not be completed but a proof of authentication attempt (CAVV) was generated.</td> </tr> <tr> <td>U</td> <td>Authentication Could Not Be Performed Authentication could not be completed, due to technical or other problem.</td> </tr> </table> ")
    authorised: Optional[StrictBool] = Field(default=None, description="A boolean definition that indicates that the transaction was authorised. It will return false if the transaction  was declined, rejected or cancelled due to CSC matching failures.  Attention should be referenced to the AuthResult and Response code for accurate determination of the result. ")
    avs_result: Optional[StrictStr] = Field(default=None, description="The AVS result codes determine the result of checking the AVS values within the Address Verification fraud system. If a transaction is declined due to the AVS code not matching, this value can help determine the reason for the decline.  <table> <tr> <th>Code</th> <th>Description</th> </tr> <tr><td>Y</td><td>Address and 5 digit post code match</td></tr> <tr><td>M</td><td>Street address and Postal codes match for international transaction</td></tr> <tr><td>U</td><td>No AVS data available from issuer auth system</td></tr> <tr><td>A</td><td>Addres matches, post code does not</td></tr> <tr><td>I</td><td>Address information verified for international transaction</td></tr> <tr><td>Z</td><td>5 digit post code matches, Address does not</td></tr> <tr><td>W</td><td>9 digit post code matches, Address does not</td></tr> <tr><td>X</td><td>Postcode and address match</td></tr> <tr><td>B</td><td>Postal code not verified due to incompatible formats</td></tr> <tr><td>P</td><td>Postal codes match. Street address not verified due to to incompatible formats</td></tr> <tr><td>E</td><td>AVS Error</td></tr> <tr><td>C</td><td>Street address and Postal code not verified due to incompatible formats</td></tr> <tr><td>D</td><td>Street address and postal codes match</td></tr> <tr><td> </td><td>No information</td></tr> <tr><td>N</td><td>Neither postcode nor address match</td></tr> <tr><td>R</td><td>Retry, System unavailble or Timed Out</td></tr> <tr><td>S</td><td>AVS Service not supported by issuer or processor</td></tr> <tr><td>G</td><td>Issuer does not participate in AVS</td></tr> </table> ")
    bin_commercial: Optional[StrictBool] = Field(default=None, description="Determines whether the bin range was found to be a commercial or business card.")
    bin_debit: Optional[StrictBool] = Field(default=None, description="Determines whether the bin range was found to be a debit card. If false the card was considered as a credit card.")
    bin_description: Optional[StrictStr] = Field(default=None, description="A description of the bin range found for the card.")
    cavv: Optional[StrictStr] = Field(default=None, description="The cardholder authentication verification value which can be returned for verification purposes of the authenticated  transaction for dispute realisation. ")
    context: Optional[StrictStr] = Field(default=None, description="The context which processed the transaction, can be used for support purposes to trace transactions.")
    csc_result: Optional[StrictStr] = Field(default=None, description="The CSC rseult codes determine the result of checking the provided CSC value within the Card Security Code fraud system. If a transaction is declined due to the CSC code not matching, this value can help determine the reason for the decline.  <table> <tr> <th>Code</th> <th>Description</th> </tr> <tr><td> </td><td>No information</td></tr> <tr><td>M</td><td>Card verification data matches</td></tr> <tr><td>N</td><td>Card verification data was checked but did not match</td></tr> <tr><td>P</td><td>Card verification was not processed</td></tr> <tr><td>S</td><td>The card verification data should be on the card but the merchant indicates that it is not</td></tr> <tr><td>U</td><td>The card issuer is not certified</td></tr> </table> ")
    currency: Optional[StrictStr] = Field(default=None, description="The currency the transaction was processed in. This is an `ISO4217` alpha currency value.")
    date_time: Optional[datetime] = Field(default=None, description="The UTC date time of the transaction in ISO data time format. ")
    eci: Optional[StrictStr] = Field(default=None, description="An Electronic Commerce Indicator (ECI) used to identify the result of authentication using 3DSecure. ")
    identifier: Optional[StrictStr] = Field(default=None, description="The identifier provided within the request.")
    live: Optional[StrictBool] = Field(default=None, description="Used to identify that a transaction was processed on a live authorisation platform.")
    maskedpan: Optional[StrictStr] = Field(default=None, description="A masked value of the card number used for processing displaying limited values that can be used on a receipt. ")
    merchantid: StrictInt = Field(description="The merchant id that processed this transaction.")
    result: StrictInt = Field(description="An integer result that indicates the outcome of the transaction. The Code value below maps to the result value  <table> <tr> <th>Code</th> <th>Abbrev</th> <th>Description</th> </tr> <tr><td>0</td><td>Declined</td><td>Declined</td></tr> <tr><td>1</td><td>Accepted</td><td>Accepted</td></tr> <tr><td>2</td><td>Rejected</td><td>Rejected</td></tr> <tr><td>3</td><td>Not Attempted</td><td>Not Attempted</td></tr> <tr><td>4</td><td>Referred</td><td>Referred</td></tr> <tr><td>5</td><td>PinRetry</td><td>Perform PIN Retry</td></tr> <tr><td>6</td><td>ForSigVer</td><td>Force Signature Verification</td></tr> <tr><td>7</td><td>Hold</td><td>Hold</td></tr> <tr><td>8</td><td>SecErr</td><td>Security Error</td></tr> <tr><td>9</td><td>CallAcq</td><td>Call Acquirer</td></tr> <tr><td>10</td><td>DNH</td><td>Do Not Honour</td></tr> <tr><td>11</td><td>RtnCrd</td><td>Retain Card</td></tr> <tr><td>12</td><td>ExprdCrd</td><td>Expired Card</td></tr> <tr><td>13</td><td>InvldCrd</td><td>Invalid Card No</td></tr> <tr><td>14</td><td>PinExcd</td><td>Pin Tries Exceeded</td></tr> <tr><td>15</td><td>PinInvld</td><td>Pin Invalid</td></tr> <tr><td>16</td><td>AuthReq</td><td>Authentication Required</td></tr> <tr><td>17</td><td>AuthenFail</td><td>Authentication Failed</td></tr> <tr><td>18</td><td>Verified</td><td>Card Verified</td></tr> <tr><td>19</td><td>Cancelled</td><td>Cancelled</td></tr> <tr><td>20</td><td>Un</td><td>Unknown</td></tr> <tr><td>21</td><td>Challenged</td><td>Challenged</td></tr> <tr><td>22</td><td>Decoupled</td><td>Decoupled</td></tr> <tr><td>23</td><td>Denied</td><td>Permission Denied</td></tr> </table> ")
    result_code: StrictStr = Field(description="The result code as defined in the Response Codes Reference for example 000 is an accepted live transaction whilst 001 is an accepted test transaction. Result codes identify the source of success and failure.  Codes may start with an alpha character i.e. C001 indicating a type of error such as a card validation error. ")
    result_message: StrictStr = Field(description="The message regarding the result which provides further narrative to the result code. ")
    scheme: Optional[StrictStr] = Field(default=None, description="The name of the card scheme of the transaction that processed the transaction such as Visa or MasterCard. ")
    scheme_id: Optional[StrictStr] = Field(default=None, description="The name of the card scheme of the transaction such as VI or MC. ")
    scheme_logo: Optional[StrictStr] = Field(default=None, description="A url containing a logo of the card scheme. ")
    sha256: Optional[StrictStr] = Field(default=None, description="A SHA256 digest value of the transaction used to validate the response data The digest is calculated by concatenating   * authcode   * amount   * response_code   * merchant_id   * trans_no   * identifier   * licence_key - which is not provided in the response. ")
    trans_status: Optional[StrictStr] = Field(default=None, description="Used to identify the status of a transaction. The status is used to track a transaction through its life cycle.  <table> <tr> <th>Id</th> <th>Description</th> </tr> <tr> <td>O</td> <td>Transaction is open for settlement</td> </tr> <tr> <td>A</td> <td>Transaction is assigned for settlement and can no longer be voided</td> </tr> <tr> <td>S</td> <td>Transaction has been settled</td> </tr> <tr> <td>D</td> <td>Transaction has been declined</td> </tr> <tr> <td>R</td> <td>Transaction has been rejected</td> </tr> <tr> <td>P</td> <td>Transaction has been authorised only and awaiting a capture. Used in pre-auth situations</td> </tr> <tr> <td>C</td> <td>Transaction has been cancelled</td> </tr> <tr> <td>E</td> <td>Transaction has expired</td> </tr> <tr> <td>I</td> <td>Transaction has been initialised but no action was able to be carried out</td> </tr> <tr> <td>H</td> <td>Transaction is awaiting authorisation</td> </tr> <tr> <td>.</td> <td>Transaction is on hold</td> </tr> <tr> <td>V</td> <td>Transaction has been verified</td> </tr> </table> ")
    transno: Optional[StrictInt] = Field(default=None, description="The resulting transaction number, ordered incrementally from 1 for every merchant_id. The value will default to less than 1 for transactions that do not have a transaction number issued. ")
    __properties: ClassVar[List[str]] = ["amount", "atrn", "atsd", "authcode", "authen_result", "authorised", "avs_result", "bin_commercial", "bin_debit", "bin_description", "cavv", "context", "csc_result", "currency", "date_time", "eci", "identifier", "live", "maskedpan", "merchantid", "result", "result_code", "result_message", "scheme", "scheme_id", "scheme_logo", "sha256", "trans_status", "transno"]

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
        """Create an instance of AuthResponse from a JSON string"""
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
        """Create an instance of AuthResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "atrn": obj.get("atrn"),
            "atsd": obj.get("atsd"),
            "authcode": obj.get("authcode"),
            "authen_result": obj.get("authen_result"),
            "authorised": obj.get("authorised"),
            "avs_result": obj.get("avs_result"),
            "bin_commercial": obj.get("bin_commercial"),
            "bin_debit": obj.get("bin_debit"),
            "bin_description": obj.get("bin_description"),
            "cavv": obj.get("cavv"),
            "context": obj.get("context"),
            "csc_result": obj.get("csc_result"),
            "currency": obj.get("currency"),
            "date_time": obj.get("datetime"),
            "eci": obj.get("eci"),
            "identifier": obj.get("identifier"),
            "live": obj.get("live"),
            "maskedpan": obj.get("maskedpan"),
            "merchantid": obj.get("merchantid"),
            "result": obj.get("result"),
            "result_code": obj.get("result_code"),
            "result_message": obj.get("result_message"),
            "scheme": obj.get("scheme"),
            "scheme_id": obj.get("scheme_id"),
            "scheme_logo": obj.get("scheme_logo"),
            "sha256": obj.get("sha256"),
            "trans_status": obj.get("trans_status"),
            "transno": obj.get("transno")
        })
        return _obj

