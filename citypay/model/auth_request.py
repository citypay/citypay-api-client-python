"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by  Visa and MasterCard and the PCI Security Standards Council. These include  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from citypay.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from citypay.exceptions import ApiAttributeError


def lazy_import():
    from citypay.model.airline_advice import AirlineAdvice
    from citypay.model.contact_details import ContactDetails
    from citypay.model.event_data_model import EventDataModel
    from citypay.model.external_mpi import ExternalMPI
    from citypay.model.mcc6012 import MCC6012
    from citypay.model.three_d_secure import ThreeDSecure
    globals()['AirlineAdvice'] = AirlineAdvice
    globals()['ContactDetails'] = ContactDetails
    globals()['EventDataModel'] = EventDataModel
    globals()['ExternalMPI'] = ExternalMPI
    globals()['MCC6012'] = MCC6012
    globals()['ThreeDSecure'] = ThreeDSecure


class AuthRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('amount',): {
        },
        ('cardnumber',): {
            'max_length': 22,
            'min_length': 12,
        },
        ('expmonth',): {
            'inclusive_maximum': 12,
            'inclusive_minimum': 1,
        },
        ('expyear',): {
            'inclusive_maximum': 2100,
            'inclusive_minimum': 2000,
        },
        ('identifier',): {
            'max_length': 50,
            'min_length': 4,
        },
        ('csc',): {
            'max_length': 4,
            'min_length': 3,
        },
        ('currency',): {
            'max_length': 3,
            'min_length': 3,
        },
        ('name_on_card',): {
            'max_length': 45,
            'min_length': 2,
        },
        ('trans_info',): {
            'max_length': 50,
        },
        ('trans_type',): {
            'max_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'amount': (int,),  # noqa: E501
            'cardnumber': (str,),  # noqa: E501
            'expmonth': (int,),  # noqa: E501
            'expyear': (int,),  # noqa: E501
            'identifier': (str,),  # noqa: E501
            'merchantid': (int,),  # noqa: E501
            'airline_data': (AirlineAdvice,),  # noqa: E501
            'avs_postcode_policy': (str,),  # noqa: E501
            'bill_to': (ContactDetails,),  # noqa: E501
            'csc': (str,),  # noqa: E501
            'csc_policy': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'duplicate_policy': (str,),  # noqa: E501
            'event_management': (EventDataModel,),  # noqa: E501
            'external_mpi': (ExternalMPI,),  # noqa: E501
            'match_avsa': (str,),  # noqa: E501
            'mcc6012': (MCC6012,),  # noqa: E501
            'name_on_card': (str,),  # noqa: E501
            'ship_to': (ContactDetails,),  # noqa: E501
            'threedsecure': (ThreeDSecure,),  # noqa: E501
            'trans_info': (str,),  # noqa: E501
            'trans_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'cardnumber': 'cardnumber',  # noqa: E501
        'expmonth': 'expmonth',  # noqa: E501
        'expyear': 'expyear',  # noqa: E501
        'identifier': 'identifier',  # noqa: E501
        'merchantid': 'merchantid',  # noqa: E501
        'airline_data': 'airline_data',  # noqa: E501
        'avs_postcode_policy': 'avs_postcode_policy',  # noqa: E501
        'bill_to': 'bill_to',  # noqa: E501
        'csc': 'csc',  # noqa: E501
        'csc_policy': 'csc_policy',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'duplicate_policy': 'duplicate_policy',  # noqa: E501
        'event_management': 'event_management',  # noqa: E501
        'external_mpi': 'external_mpi',  # noqa: E501
        'match_avsa': 'match_avsa',  # noqa: E501
        'mcc6012': 'mcc6012',  # noqa: E501
        'name_on_card': 'name_on_card',  # noqa: E501
        'ship_to': 'ship_to',  # noqa: E501
        'threedsecure': 'threedsecure',  # noqa: E501
        'trans_info': 'trans_info',  # noqa: E501
        'trans_type': 'trans_type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, amount, cardnumber, expmonth, expyear, identifier, merchantid, *args, **kwargs):  # noqa: E501
        """AuthRequest - a model defined in OpenAPI

        Args:
            amount (int): The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. 
            cardnumber (str): The card number (PAN) with a variable length to a maximum of 21 digits in numerical form. Any non numeric characters will be stripped out of the card number, this includes whitespace or separators internal of the provided value.  The card number must be treated as sensitive data. We only provide an obfuscated value in logging and reporting.  The plaintext value is encrypted in our database using AES 256 GMC bit encryption for settlement or refund purposes.  When providing the card number to our gateway through the authorisation API you will be handling the card data on your application. This will require further PCI controls to be in place and this value must never be stored. 
            expmonth (int): The month of expiry of the card. The month value should be a numerical value between 1 and 12. 
            expyear (int): The year of expiry of the card. 
            identifier (str): The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. 
            merchantid (int): Identifies the merchant account to perform processing for.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            airline_data (AirlineAdvice): [optional]  # noqa: E501
            avs_postcode_policy (str): A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. . [optional]  # noqa: E501
            bill_to (ContactDetails): [optional]  # noqa: E501
            csc (str): The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify posession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. . [optional]  # noqa: E501
            csc_policy (str): A policy value which determines whether a CSC policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. . [optional]  # noqa: E501
            currency (str): The processing currency for the transaction. Will default to the merchant account currency.. [optional]  # noqa: E501
            duplicate_policy (str): A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. . [optional]  # noqa: E501
            event_management (EventDataModel): [optional]  # noqa: E501
            external_mpi (ExternalMPI): [optional]  # noqa: E501
            match_avsa (str): A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. . [optional]  # noqa: E501
            mcc6012 (MCC6012): [optional]  # noqa: E501
            name_on_card (str): The card holder name as appears on the card such as MR N E BODY. Required for some acquirers. . [optional]  # noqa: E501
            ship_to (ContactDetails): [optional]  # noqa: E501
            threedsecure (ThreeDSecure): [optional]  # noqa: E501
            trans_info (str): Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.. [optional]  # noqa: E501
            trans_type (str): The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.cardnumber = cardnumber
        self.expmonth = expmonth
        self.expyear = expyear
        self.identifier = identifier
        self.merchantid = merchantid
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, amount, cardnumber, expmonth, expyear, identifier, merchantid, *args, **kwargs):  # noqa: E501
        """AuthRequest - a model defined in OpenAPI

        Args:
            amount (int): The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. 
            cardnumber (str): The card number (PAN) with a variable length to a maximum of 21 digits in numerical form. Any non numeric characters will be stripped out of the card number, this includes whitespace or separators internal of the provided value.  The card number must be treated as sensitive data. We only provide an obfuscated value in logging and reporting.  The plaintext value is encrypted in our database using AES 256 GMC bit encryption for settlement or refund purposes.  When providing the card number to our gateway through the authorisation API you will be handling the card data on your application. This will require further PCI controls to be in place and this value must never be stored. 
            expmonth (int): The month of expiry of the card. The month value should be a numerical value between 1 and 12. 
            expyear (int): The year of expiry of the card. 
            identifier (str): The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. 
            merchantid (int): Identifies the merchant account to perform processing for.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            airline_data (AirlineAdvice): [optional]  # noqa: E501
            avs_postcode_policy (str): A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. . [optional]  # noqa: E501
            bill_to (ContactDetails): [optional]  # noqa: E501
            csc (str): The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify posession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. . [optional]  # noqa: E501
            csc_policy (str): A policy value which determines whether a CSC policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. . [optional]  # noqa: E501
            currency (str): The processing currency for the transaction. Will default to the merchant account currency.. [optional]  # noqa: E501
            duplicate_policy (str): A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. . [optional]  # noqa: E501
            event_management (EventDataModel): [optional]  # noqa: E501
            external_mpi (ExternalMPI): [optional]  # noqa: E501
            match_avsa (str): A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. . [optional]  # noqa: E501
            mcc6012 (MCC6012): [optional]  # noqa: E501
            name_on_card (str): The card holder name as appears on the card such as MR N E BODY. Required for some acquirers. . [optional]  # noqa: E501
            ship_to (ContactDetails): [optional]  # noqa: E501
            threedsecure (ThreeDSecure): [optional]  # noqa: E501
            trans_info (str): Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.. [optional]  # noqa: E501
            trans_type (str): The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.amount = amount
        self.cardnumber = cardnumber
        self.expmonth = expmonth
        self.expyear = expyear
        self.identifier = identifier
        self.merchantid = merchantid
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
