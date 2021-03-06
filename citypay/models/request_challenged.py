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


class RequestChallenged(object):
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
        'acs_url': 'str',
        'creq': 'str',
        'merchantid': 'int',
        'threedserver_trans_id': 'str',
        'transno': 'int'
    }

    attribute_map = {
        'acs_url': 'acs_url',
        'creq': 'creq',
        'merchantid': 'merchantid',
        'threedserver_trans_id': 'threedserver_trans_id',
        'transno': 'transno'
    }

    def __init__(self, acs_url=None, creq=None, merchantid=None, threedserver_trans_id=None, transno=None, local_vars_configuration=None):  # noqa: E501
        """RequestChallenged - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._acs_url = None
        self._creq = None
        self._merchantid = None
        self._threedserver_trans_id = None
        self._transno = None
        self.discriminator = None

        if acs_url is not None:
            self.acs_url = acs_url
        if creq is not None:
            self.creq = creq
        if merchantid is not None:
            self.merchantid = merchantid
        if threedserver_trans_id is not None:
            self.threedserver_trans_id = threedserver_trans_id
        if transno is not None:
            self.transno = transno

    @property
    def acs_url(self):
        """Gets the acs_url of this RequestChallenged.  # noqa: E501

        The url of the Access Control Server (ACS) to forward the user to.   # noqa: E501

        :return: The acs_url of this RequestChallenged.  # noqa: E501
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this RequestChallenged.

        The url of the Access Control Server (ACS) to forward the user to.   # noqa: E501

        :param acs_url: The acs_url of this RequestChallenged.  # noqa: E501
        :type: str
        """

        self._acs_url = acs_url

    @property
    def creq(self):
        """Gets the creq of this RequestChallenged.  # noqa: E501

        The challenge request data which is encoded for usage by the ACS.  # noqa: E501

        :return: The creq of this RequestChallenged.  # noqa: E501
        :rtype: str
        """
        return self._creq

    @creq.setter
    def creq(self, creq):
        """Sets the creq of this RequestChallenged.

        The challenge request data which is encoded for usage by the ACS.  # noqa: E501

        :param creq: The creq of this RequestChallenged.  # noqa: E501
        :type: str
        """

        self._creq = creq

    @property
    def merchantid(self):
        """Gets the merchantid of this RequestChallenged.  # noqa: E501

        The merchant id that processed this transaction.  # noqa: E501

        :return: The merchantid of this RequestChallenged.  # noqa: E501
        :rtype: int
        """
        return self._merchantid

    @merchantid.setter
    def merchantid(self, merchantid):
        """Sets the merchantid of this RequestChallenged.

        The merchant id that processed this transaction.  # noqa: E501

        :param merchantid: The merchantid of this RequestChallenged.  # noqa: E501
        :type: int
        """

        self._merchantid = merchantid

    @property
    def threedserver_trans_id(self):
        """Gets the threedserver_trans_id of this RequestChallenged.  # noqa: E501

        The 3DSv2 trans id reference for the challenge process.  # noqa: E501

        :return: The threedserver_trans_id of this RequestChallenged.  # noqa: E501
        :rtype: str
        """
        return self._threedserver_trans_id

    @threedserver_trans_id.setter
    def threedserver_trans_id(self, threedserver_trans_id):
        """Sets the threedserver_trans_id of this RequestChallenged.

        The 3DSv2 trans id reference for the challenge process.  # noqa: E501

        :param threedserver_trans_id: The threedserver_trans_id of this RequestChallenged.  # noqa: E501
        :type: str
        """

        self._threedserver_trans_id = threedserver_trans_id

    @property
    def transno(self):
        """Gets the transno of this RequestChallenged.  # noqa: E501

        The transaction number for the challenge, ordered incrementally from 1 for every merchant_id.   # noqa: E501

        :return: The transno of this RequestChallenged.  # noqa: E501
        :rtype: int
        """
        return self._transno

    @transno.setter
    def transno(self, transno):
        """Sets the transno of this RequestChallenged.

        The transaction number for the challenge, ordered incrementally from 1 for every merchant_id.   # noqa: E501

        :param transno: The transno of this RequestChallenged.  # noqa: E501
        :type: int
        """

        self._transno = transno

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
        if not isinstance(other, RequestChallenged):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestChallenged):
            return True

        return self.to_dict() != other.to_dict()
