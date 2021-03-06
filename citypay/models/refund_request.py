# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from citypay.configuration import Configuration


class RefundRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'int',
        'identifier': 'str',
        'merchantid': 'int',
        'refund_ref': 'int',
        'trans_info': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'identifier': 'identifier',
        'merchantid': 'merchantid',
        'refund_ref': 'refund_ref',
        'trans_info': 'trans_info'
    }

    def __init__(self, amount=None, identifier=None, merchantid=None, refund_ref=None, trans_info=None, local_vars_configuration=None):  # noqa: E501
        """RefundRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._identifier = None
        self._merchantid = None
        self._refund_ref = None
        self._trans_info = None
        self.discriminator = None

        self.amount = amount
        self.identifier = identifier
        self.merchantid = merchantid
        self.refund_ref = refund_ref
        if trans_info is not None:
            self.trans_info = trans_info

    @property
    def amount(self):
        """Gets the amount of this RefundRequest.  # noqa: E501

        The amount to refund in the lowest unit of currency with a variable length to a maximum of 12 digits. The amount should be the total amount required to refund for the transaction up to the original processed amount. No decimal points are to be included and no divisional characters such as 1,024. For example with GBP £1,021.95 the amount value is 102195.   # noqa: E501

        :return: The amount of this RefundRequest.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this RefundRequest.

        The amount to refund in the lowest unit of currency with a variable length to a maximum of 12 digits. The amount should be the total amount required to refund for the transaction up to the original processed amount. No decimal points are to be included and no divisional characters such as 1,024. For example with GBP £1,021.95 the amount value is 102195.   # noqa: E501

        :param amount: The amount of this RefundRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def identifier(self):
        """Gets the identifier of this RefundRequest.  # noqa: E501

        The identifier of the refund to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different.   # noqa: E501

        :return: The identifier of this RefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this RefundRequest.

        The identifier of the refund to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different.   # noqa: E501

        :param identifier: The identifier of this RefundRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) > 50):
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) < 4):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `4`")  # noqa: E501

        self._identifier = identifier

    @property
    def merchantid(self):
        """Gets the merchantid of this RefundRequest.  # noqa: E501

        Identifies the merchant account to perform the refund for.  # noqa: E501

        :return: The merchantid of this RefundRequest.  # noqa: E501
        :rtype: int
        """
        return self._merchantid

    @merchantid.setter
    def merchantid(self, merchantid):
        """Sets the merchantid of this RefundRequest.

        Identifies the merchant account to perform the refund for.  # noqa: E501

        :param merchantid: The merchantid of this RefundRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and merchantid is None:  # noqa: E501
            raise ValueError("Invalid value for `merchantid`, must not be `None`")  # noqa: E501

        self._merchantid = merchantid

    @property
    def refund_ref(self):
        """Gets the refund_ref of this RefundRequest.  # noqa: E501

        A reference to the original transaction number that is wanting to be refunded. The original  transaction must be on the same merchant id, previously authorised.   # noqa: E501

        :return: The refund_ref of this RefundRequest.  # noqa: E501
        :rtype: int
        """
        return self._refund_ref

    @refund_ref.setter
    def refund_ref(self, refund_ref):
        """Sets the refund_ref of this RefundRequest.

        A reference to the original transaction number that is wanting to be refunded. The original  transaction must be on the same merchant id, previously authorised.   # noqa: E501

        :param refund_ref: The refund_ref of this RefundRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and refund_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `refund_ref`, must not be `None`")  # noqa: E501

        self._refund_ref = refund_ref

    @property
    def trans_info(self):
        """Gets the trans_info of this RefundRequest.  # noqa: E501

        Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.  # noqa: E501

        :return: The trans_info of this RefundRequest.  # noqa: E501
        :rtype: str
        """
        return self._trans_info

    @trans_info.setter
    def trans_info(self, trans_info):
        """Sets the trans_info of this RefundRequest.

        Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.  # noqa: E501

        :param trans_info: The trans_info of this RefundRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                trans_info is not None and len(trans_info) > 50):
            raise ValueError("Invalid value for `trans_info`, length must be less than or equal to `50`")  # noqa: E501

        self._trans_info = trans_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RefundRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RefundRequest):
            return True

        return self.to_dict() != other.to_dict()
