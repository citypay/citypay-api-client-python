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


class Card(object):
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
        'bin_commercial': 'bool',
        'bin_corporate': 'bool',
        'bin_country_issued': 'str',
        'bin_credit': 'bool',
        'bin_currency': 'str',
        'bin_debit': 'bool',
        'bin_description': 'str',
        'bin_eu': 'bool',
        'card_id': 'str',
        'card_status': 'str',
        'date_created': 'datetime',
        'default': 'bool',
        'expmonth': 'int',
        'expyear': 'int',
        'label': 'str',
        'label2': 'str',
        'last4digits': 'str',
        'scheme': 'str',
        'token': 'str'
    }

    attribute_map = {
        'bin_commercial': 'bin_commercial',
        'bin_corporate': 'bin_corporate',
        'bin_country_issued': 'bin_country_issued',
        'bin_credit': 'bin_credit',
        'bin_currency': 'bin_currency',
        'bin_debit': 'bin_debit',
        'bin_description': 'bin_description',
        'bin_eu': 'bin_eu',
        'card_id': 'card_id',
        'card_status': 'card_status',
        'date_created': 'date_created',
        'default': 'default',
        'expmonth': 'expmonth',
        'expyear': 'expyear',
        'label': 'label',
        'label2': 'label2',
        'last4digits': 'last4digits',
        'scheme': 'scheme',
        'token': 'token'
    }

    def __init__(self, bin_commercial=None, bin_corporate=None, bin_country_issued=None, bin_credit=None, bin_currency=None, bin_debit=None, bin_description=None, bin_eu=None, card_id=None, card_status=None, date_created=None, default=None, expmonth=None, expyear=None, label=None, label2=None, last4digits=None, scheme=None, token=None, local_vars_configuration=None):  # noqa: E501
        """Card - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._bin_commercial = None
        self._bin_corporate = None
        self._bin_country_issued = None
        self._bin_credit = None
        self._bin_currency = None
        self._bin_debit = None
        self._bin_description = None
        self._bin_eu = None
        self._card_id = None
        self._card_status = None
        self._date_created = None
        self._default = None
        self._expmonth = None
        self._expyear = None
        self._label = None
        self._label2 = None
        self._last4digits = None
        self._scheme = None
        self._token = None
        self.discriminator = None

        if bin_commercial is not None:
            self.bin_commercial = bin_commercial
        if bin_corporate is not None:
            self.bin_corporate = bin_corporate
        if bin_country_issued is not None:
            self.bin_country_issued = bin_country_issued
        if bin_credit is not None:
            self.bin_credit = bin_credit
        if bin_currency is not None:
            self.bin_currency = bin_currency
        if bin_debit is not None:
            self.bin_debit = bin_debit
        if bin_description is not None:
            self.bin_description = bin_description
        if bin_eu is not None:
            self.bin_eu = bin_eu
        if card_id is not None:
            self.card_id = card_id
        if card_status is not None:
            self.card_status = card_status
        if date_created is not None:
            self.date_created = date_created
        if default is not None:
            self.default = default
        if expmonth is not None:
            self.expmonth = expmonth
        if expyear is not None:
            self.expyear = expyear
        if label is not None:
            self.label = label
        if label2 is not None:
            self.label2 = label2
        if last4digits is not None:
            self.last4digits = last4digits
        if scheme is not None:
            self.scheme = scheme
        if token is not None:
            self.token = token

    @property
    def bin_commercial(self):
        """Gets the bin_commercial of this Card.  # noqa: E501

        Defines whether the card is a commercial card.  # noqa: E501

        :return: The bin_commercial of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._bin_commercial

    @bin_commercial.setter
    def bin_commercial(self, bin_commercial):
        """Sets the bin_commercial of this Card.

        Defines whether the card is a commercial card.  # noqa: E501

        :param bin_commercial: The bin_commercial of this Card.  # noqa: E501
        :type: bool
        """

        self._bin_commercial = bin_commercial

    @property
    def bin_corporate(self):
        """Gets the bin_corporate of this Card.  # noqa: E501

        Defines whether the card is a corporate business card.  # noqa: E501

        :return: The bin_corporate of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._bin_corporate

    @bin_corporate.setter
    def bin_corporate(self, bin_corporate):
        """Sets the bin_corporate of this Card.

        Defines whether the card is a corporate business card.  # noqa: E501

        :param bin_corporate: The bin_corporate of this Card.  # noqa: E501
        :type: bool
        """

        self._bin_corporate = bin_corporate

    @property
    def bin_country_issued(self):
        """Gets the bin_country_issued of this Card.  # noqa: E501

        The determined country where the card was issued.  # noqa: E501

        :return: The bin_country_issued of this Card.  # noqa: E501
        :rtype: str
        """
        return self._bin_country_issued

    @bin_country_issued.setter
    def bin_country_issued(self, bin_country_issued):
        """Sets the bin_country_issued of this Card.

        The determined country where the card was issued.  # noqa: E501

        :param bin_country_issued: The bin_country_issued of this Card.  # noqa: E501
        :type: str
        """

        self._bin_country_issued = bin_country_issued

    @property
    def bin_credit(self):
        """Gets the bin_credit of this Card.  # noqa: E501

        Defines whether the card is a credit card.  # noqa: E501

        :return: The bin_credit of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._bin_credit

    @bin_credit.setter
    def bin_credit(self, bin_credit):
        """Sets the bin_credit of this Card.

        Defines whether the card is a credit card.  # noqa: E501

        :param bin_credit: The bin_credit of this Card.  # noqa: E501
        :type: bool
        """

        self._bin_credit = bin_credit

    @property
    def bin_currency(self):
        """Gets the bin_currency of this Card.  # noqa: E501

        The default currency determined for the card.  # noqa: E501

        :return: The bin_currency of this Card.  # noqa: E501
        :rtype: str
        """
        return self._bin_currency

    @bin_currency.setter
    def bin_currency(self, bin_currency):
        """Sets the bin_currency of this Card.

        The default currency determined for the card.  # noqa: E501

        :param bin_currency: The bin_currency of this Card.  # noqa: E501
        :type: str
        """

        self._bin_currency = bin_currency

    @property
    def bin_debit(self):
        """Gets the bin_debit of this Card.  # noqa: E501

        Defines whether the card is a debit card.  # noqa: E501

        :return: The bin_debit of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._bin_debit

    @bin_debit.setter
    def bin_debit(self, bin_debit):
        """Sets the bin_debit of this Card.

        Defines whether the card is a debit card.  # noqa: E501

        :param bin_debit: The bin_debit of this Card.  # noqa: E501
        :type: bool
        """

        self._bin_debit = bin_debit

    @property
    def bin_description(self):
        """Gets the bin_description of this Card.  # noqa: E501

        A description of the bin on the card to identify what type of product the card is.  # noqa: E501

        :return: The bin_description of this Card.  # noqa: E501
        :rtype: str
        """
        return self._bin_description

    @bin_description.setter
    def bin_description(self, bin_description):
        """Sets the bin_description of this Card.

        A description of the bin on the card to identify what type of product the card is.  # noqa: E501

        :param bin_description: The bin_description of this Card.  # noqa: E501
        :type: str
        """

        self._bin_description = bin_description

    @property
    def bin_eu(self):
        """Gets the bin_eu of this Card.  # noqa: E501

        Defines whether the card is regulated within the EU.  # noqa: E501

        :return: The bin_eu of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._bin_eu

    @bin_eu.setter
    def bin_eu(self, bin_eu):
        """Sets the bin_eu of this Card.

        Defines whether the card is regulated within the EU.  # noqa: E501

        :param bin_eu: The bin_eu of this Card.  # noqa: E501
        :type: bool
        """

        self._bin_eu = bin_eu

    @property
    def card_id(self):
        """Gets the card_id of this Card.  # noqa: E501

        The id of the card that is returned. Should be used for referencing the card when perform any changes.  # noqa: E501

        :return: The card_id of this Card.  # noqa: E501
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """Sets the card_id of this Card.

        The id of the card that is returned. Should be used for referencing the card when perform any changes.  # noqa: E501

        :param card_id: The card_id of this Card.  # noqa: E501
        :type: str
        """

        self._card_id = card_id

    @property
    def card_status(self):
        """Gets the card_status of this Card.  # noqa: E501

        The status of the card such, valid values are  - ACTIVE the card is active for processing  - INACTIVE the card is not active for processing  - EXPIRED for cards that have passed their expiry date.   # noqa: E501

        :return: The card_status of this Card.  # noqa: E501
        :rtype: str
        """
        return self._card_status

    @card_status.setter
    def card_status(self, card_status):
        """Sets the card_status of this Card.

        The status of the card such, valid values are  - ACTIVE the card is active for processing  - INACTIVE the card is not active for processing  - EXPIRED for cards that have passed their expiry date.   # noqa: E501

        :param card_status: The card_status of this Card.  # noqa: E501
        :type: str
        """

        self._card_status = card_status

    @property
    def date_created(self):
        """Gets the date_created of this Card.  # noqa: E501

        The date time of when the card was created.  # noqa: E501

        :return: The date_created of this Card.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Card.

        The date time of when the card was created.  # noqa: E501

        :param date_created: The date_created of this Card.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def default(self):
        """Gets the default of this Card.  # noqa: E501

        Determines if the card is the default card for the account and should be regarded as the first option to be used for processing.  # noqa: E501

        :return: The default of this Card.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this Card.

        Determines if the card is the default card for the account and should be regarded as the first option to be used for processing.  # noqa: E501

        :param default: The default of this Card.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def expmonth(self):
        """Gets the expmonth of this Card.  # noqa: E501

        The expiry month of the card.  # noqa: E501

        :return: The expmonth of this Card.  # noqa: E501
        :rtype: int
        """
        return self._expmonth

    @expmonth.setter
    def expmonth(self, expmonth):
        """Sets the expmonth of this Card.

        The expiry month of the card.  # noqa: E501

        :param expmonth: The expmonth of this Card.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                expmonth is not None and expmonth > 12):  # noqa: E501
            raise ValueError("Invalid value for `expmonth`, must be a value less than or equal to `12`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                expmonth is not None and expmonth < 1):  # noqa: E501
            raise ValueError("Invalid value for `expmonth`, must be a value greater than or equal to `1`")  # noqa: E501

        self._expmonth = expmonth

    @property
    def expyear(self):
        """Gets the expyear of this Card.  # noqa: E501

        The expiry year of the card.  # noqa: E501

        :return: The expyear of this Card.  # noqa: E501
        :rtype: int
        """
        return self._expyear

    @expyear.setter
    def expyear(self, expyear):
        """Sets the expyear of this Card.

        The expiry year of the card.  # noqa: E501

        :param expyear: The expyear of this Card.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                expyear is not None and expyear > 2100):  # noqa: E501
            raise ValueError("Invalid value for `expyear`, must be a value less than or equal to `2100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                expyear is not None and expyear < 2000):  # noqa: E501
            raise ValueError("Invalid value for `expyear`, must be a value greater than or equal to `2000`")  # noqa: E501

        self._expyear = expyear

    @property
    def label(self):
        """Gets the label of this Card.  # noqa: E501

        A label which identifies this card.  # noqa: E501

        :return: The label of this Card.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Card.

        A label which identifies this card.  # noqa: E501

        :param label: The label of this Card.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def label2(self):
        """Gets the label2 of this Card.  # noqa: E501

        A label which also provides the expiry date of the card.  # noqa: E501

        :return: The label2 of this Card.  # noqa: E501
        :rtype: str
        """
        return self._label2

    @label2.setter
    def label2(self, label2):
        """Sets the label2 of this Card.

        A label which also provides the expiry date of the card.  # noqa: E501

        :param label2: The label2 of this Card.  # noqa: E501
        :type: str
        """

        self._label2 = label2

    @property
    def last4digits(self):
        """Gets the last4digits of this Card.  # noqa: E501

        The last 4 digits of the card to aid in identification.  # noqa: E501

        :return: The last4digits of this Card.  # noqa: E501
        :rtype: str
        """
        return self._last4digits

    @last4digits.setter
    def last4digits(self, last4digits):
        """Sets the last4digits of this Card.

        The last 4 digits of the card to aid in identification.  # noqa: E501

        :param last4digits: The last4digits of this Card.  # noqa: E501
        :type: str
        """

        self._last4digits = last4digits

    @property
    def scheme(self):
        """Gets the scheme of this Card.  # noqa: E501

        The scheme that issued the card.  # noqa: E501

        :return: The scheme of this Card.  # noqa: E501
        :rtype: str
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this Card.

        The scheme that issued the card.  # noqa: E501

        :param scheme: The scheme of this Card.  # noqa: E501
        :type: str
        """

        self._scheme = scheme

    @property
    def token(self):
        """Gets the token of this Card.  # noqa: E501

        A token that can be used to process against the card.  # noqa: E501

        :return: The token of this Card.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this Card.

        A token that can be used to process against the card.  # noqa: E501

        :param token: The token of this Card.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if not isinstance(other, Card):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Card):
            return True

        return self.to_dict() != other.to_dict()
