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
    OpenApiModel
)
from citypay.exceptions import ApiAttributeError


def lazy_import():
    from citypay.model.three_d_secure import ThreeDSecure
    globals()['ThreeDSecure'] = ThreeDSecure


class ChargeRequest(ModelNormal):
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
        ('identifier',): {
            'max_length': 50,
            'min_length': 4,
        },
        ('cardholder_agreement',): {
            'max_length': 1,
        },
        ('csc',): {
            'max_length': 4,
            'min_length': 3,
        },
        ('currency',): {
            'max_length': 3,
            'min_length': 3,
        },
        ('initiation',): {
            'max_length': 1,
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
            'identifier': (str,),  # noqa: E501
            'merchantid': (int,),  # noqa: E501
            'token': (str,),  # noqa: E501
            'avs_postcode_policy': (str,),  # noqa: E501
            'cardholder_agreement': (str,),  # noqa: E501
            'csc': (str,),  # noqa: E501
            'csc_policy': (str,),  # noqa: E501
            'currency': (str,),  # noqa: E501
            'duplicate_policy': (str,),  # noqa: E501
            'initiation': (str,),  # noqa: E501
            'match_avsa': (str,),  # noqa: E501
            'threedsecure': (ThreeDSecure,),  # noqa: E501
            'trans_info': (str,),  # noqa: E501
            'trans_type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount': 'amount',  # noqa: E501
        'identifier': 'identifier',  # noqa: E501
        'merchantid': 'merchantid',  # noqa: E501
        'token': 'token',  # noqa: E501
        'avs_postcode_policy': 'avs_postcode_policy',  # noqa: E501
        'cardholder_agreement': 'cardholder_agreement',  # noqa: E501
        'csc': 'csc',  # noqa: E501
        'csc_policy': 'csc_policy',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'duplicate_policy': 'duplicate_policy',  # noqa: E501
        'initiation': 'initiation',  # noqa: E501
        'match_avsa': 'match_avsa',  # noqa: E501
        'threedsecure': 'threedsecure',  # noqa: E501
        'trans_info': 'trans_info',  # noqa: E501
        'trans_type': 'trans_type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, amount, identifier, merchantid, token, *args, **kwargs):  # noqa: E501
        """ChargeRequest - a model defined in OpenAPI

        Args:
            amount (int): The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. 
            identifier (str): The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. 
            merchantid (int): Identifies the merchant account to perform processing for.
            token (str): A tokenised form of a card that belongs to a card holder's account and that has been previously registered. The token is time based and will only be active for a short duration. The value is therefore designed not to be stored remotely for future use.   Tokens will start with ct and are resiliently tamper proof using HMacSHA-256. No sensitive card data is stored internally within the token.   Each card will contain a different token and the value may be different on any retrieval call.   The value can be presented for payment as a selection value to an end user in a web application. 

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
            avs_postcode_policy (str): A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. . [optional]  # noqa: E501
            cardholder_agreement (str): Merchant-initiated transactions (MITs) are payments you trigger, where the cardholder has previously consented to you carrying out such payments. These may be scheduled (such as recurring payments and installments) or unscheduled (like account top-ups triggered by balance thresholds and no-show charges).  Scheduled --- These are regular payments using stored card details, like installments or a monthly subscription fee.  - `I` Instalment - A single purchase of goods or services billed to a cardholder in multiple transactions, over a period of time agreed by the cardholder and you.  - `R` Recurring - Transactions processed at fixed, regular intervals not to exceed one year between transactions, representing an agreement between a cardholder and you to purchase goods or services provided over a period of time.  Unscheduled --- These are payments using stored card details that do not occur on a regular schedule, like top-ups for a digital wallet triggered by the balance falling below a certain threshold.  - `A` Reauthorisation - a purchase made after the original purchase. A common scenario is delayed/split shipments.  - `C` Unscheduled Payment - A transaction using a stored credential for a fixed or variable amount that does not occur on a scheduled or regularly occurring transaction date. This includes account top-ups triggered by balance thresholds.  - `D` Delayed Charge - A delayed charge is typically used in hotel, cruise lines and vehicle rental environments to perform a supplemental account charge after original services are rendered.  - `L` Incremental - An incremental authorisation is typically found in hotel and car rental environments, where the cardholder has agreed to pay for any service incurred during the duration of the contract. An incremental authorisation is where you need to seek authorisation of further funds in addition to what you have originally requested. A common scenario is additional services charged to the contract, such as extending a stay in a hotel.  - `S` Resubmission - When the original purchase occurred, but you were not able to get authorisation at the time the goods or services were provided. It should be only used where the goods or services have already been provided, but the authorisation request is declined for insufficient funds.  - `X` No-show - A no-show is a transaction where you are enabled to charge for services which the cardholder entered into an agreement to purchase, but the cardholder did not meet the terms of the agreement. . [optional]  # noqa: E501
            csc (str): The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify posession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. . [optional]  # noqa: E501
            csc_policy (str): A policy value which determines whether a CSC policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. . [optional]  # noqa: E501
            currency (str): The processing currency for the transaction. Will default to the merchant account currency.. [optional]  # noqa: E501
            duplicate_policy (str): A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. . [optional]  # noqa: E501
            initiation (str): Transactions charged using the API are defined as:  **Cardholder Initiated**: A _cardholder initiated transaction_ (CIT) is where the cardholder selects the card for use for a purchase using previously stored details. An example would be a customer buying an item from your website after being present with their saved card details at checkout.  **Merchant Intiated**: A _merchant initiated transaction_ (MIT) is an authorisation initiated where you as the  merchant submit a cardholders previously stored details without the cardholder's participation. An example would  be a subscription to a membership scheme to debit their card monthly.  MITs have different reasons such as reauthorisation, delayed, unscheduled, incremental, recurring, instalment, no-show or resubmission.  The following values apply   - `M` - specifies that the transaction is initiated by the merchant   - `C` - specifies that the transaction is initiated by the cardholder  Where transactions are merchant initiated, a valid cardholder agreement must be defined. . [optional]  # noqa: E501
            match_avsa (str): A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. . [optional]  # noqa: E501
            threedsecure (ThreeDSecure): [optional]  # noqa: E501
            trans_info (str): Further information that can be added to the transaction will display in reporting. Can be used for flexible values such as operator id.. [optional]  # noqa: E501
            trans_type (str): The type of transaction being submitted. Normally this value is not required and your account manager may request that you set this field.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
        self.identifier = identifier
        self.merchantid = merchantid
        self.token = token
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
    def __init__(self, amount, identifier, merchantid, token, *args, **kwargs):  # noqa: E501
        """ChargeRequest - a model defined in OpenAPI

        Args:
            amount (int): The amount to authorise in the lowest unit of currency with a variable length to a maximum of 12 digits.  No decimal points are to be included and no divisional characters such as 1,024.  The amount should be the total amount required for the transaction.  For example with GBP £1,021.95 the amount value is 102195. 
            identifier (str): The identifier of the transaction to process. The value should be a valid reference and may be used to perform  post processing actions and to aid in reconciliation of transactions.  The value should be a valid printable string with ASCII character ranges from 0x32 to 0x127.  The identifier is recommended to be distinct for each transaction such as a [random unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier) this will aid in ensuring each transaction is identifiable.  When transactions are processed they are also checked for duplicate requests. Changing the identifier on a subsequent request will ensure that a transaction is considered as different. 
            merchantid (int): Identifies the merchant account to perform processing for.
            token (str): A tokenised form of a card that belongs to a card holder's account and that has been previously registered. The token is time based and will only be active for a short duration. The value is therefore designed not to be stored remotely for future use.   Tokens will start with ct and are resiliently tamper proof using HMacSHA-256. No sensitive card data is stored internally within the token.   Each card will contain a different token and the value may be different on any retrieval call.   The value can be presented for payment as a selection value to an end user in a web application. 

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
            avs_postcode_policy (str): A policy value which determines whether an AVS postcode policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS postcode numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the postcode did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send postcode details for authorisation. . [optional]  # noqa: E501
            cardholder_agreement (str): Merchant-initiated transactions (MITs) are payments you trigger, where the cardholder has previously consented to you carrying out such payments. These may be scheduled (such as recurring payments and installments) or unscheduled (like account top-ups triggered by balance thresholds and no-show charges).  Scheduled --- These are regular payments using stored card details, like installments or a monthly subscription fee.  - `I` Instalment - A single purchase of goods or services billed to a cardholder in multiple transactions, over a period of time agreed by the cardholder and you.  - `R` Recurring - Transactions processed at fixed, regular intervals not to exceed one year between transactions, representing an agreement between a cardholder and you to purchase goods or services provided over a period of time.  Unscheduled --- These are payments using stored card details that do not occur on a regular schedule, like top-ups for a digital wallet triggered by the balance falling below a certain threshold.  - `A` Reauthorisation - a purchase made after the original purchase. A common scenario is delayed/split shipments.  - `C` Unscheduled Payment - A transaction using a stored credential for a fixed or variable amount that does not occur on a scheduled or regularly occurring transaction date. This includes account top-ups triggered by balance thresholds.  - `D` Delayed Charge - A delayed charge is typically used in hotel, cruise lines and vehicle rental environments to perform a supplemental account charge after original services are rendered.  - `L` Incremental - An incremental authorisation is typically found in hotel and car rental environments, where the cardholder has agreed to pay for any service incurred during the duration of the contract. An incremental authorisation is where you need to seek authorisation of further funds in addition to what you have originally requested. A common scenario is additional services charged to the contract, such as extending a stay in a hotel.  - `S` Resubmission - When the original purchase occurred, but you were not able to get authorisation at the time the goods or services were provided. It should be only used where the goods or services have already been provided, but the authorisation request is declined for insufficient funds.  - `X` No-show - A no-show is a transaction where you are enabled to charge for services which the cardholder entered into an agreement to purchase, but the cardholder did not meet the terms of the agreement. . [optional]  # noqa: E501
            csc (str): The Card Security Code (CSC) (also known as CV2/CVV2) is normally found on the back of the card (American Express has it on the front). The value helps to identify posession of the card as it is not available within the chip or magnetic swipe.  When forwarding the CSC, please ensure the value is a string as some values start with 0 and this will be stripped out by any integer parsing.  The CSC number aids fraud prevention in Mail Order and Internet payments.  Business rules are available on your account to identify whether to accept or decline transactions based on mismatched results of the CSC.  The Payment Card Industry (PCI) requires that at no stage of a transaction should the CSC be stored.  This applies to all entities handling card data.  It should also not be used in any hashing process.  CityPay do not store the value and have no method of retrieving the value once the transaction has been processed. For this reason, duplicate checking is unable to determine the CSC in its duplication check algorithm. . [optional]  # noqa: E501
            csc_policy (str): A policy value which determines whether a CSC policy is enforced or bypassed.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the CSC value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the CSC did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send the CSC details for authorisation. . [optional]  # noqa: E501
            currency (str): The processing currency for the transaction. Will default to the merchant account currency.. [optional]  # noqa: E501
            duplicate_policy (str): A policy value which determines whether a duplication policy is enforced or bypassed. A duplication check has a window of time set against your account within which it can action. If a previous transaction with matching values occurred within the window, any subsequent transaction will result in a T001 result.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be checked for duplication within the duplication window.   `2` to bypass. Transactions that are bypassed will not be checked for duplication within the duplication window.   `3` to ignore. Transactions that are ignored will have the same affect as bypass. . [optional]  # noqa: E501
            initiation (str): Transactions charged using the API are defined as:  **Cardholder Initiated**: A _cardholder initiated transaction_ (CIT) is where the cardholder selects the card for use for a purchase using previously stored details. An example would be a customer buying an item from your website after being present with their saved card details at checkout.  **Merchant Intiated**: A _merchant initiated transaction_ (MIT) is an authorisation initiated where you as the  merchant submit a cardholders previously stored details without the cardholder's participation. An example would  be a subscription to a membership scheme to debit their card monthly.  MITs have different reasons such as reauthorisation, delayed, unscheduled, incremental, recurring, instalment, no-show or resubmission.  The following values apply   - `M` - specifies that the transaction is initiated by the merchant   - `C` - specifies that the transaction is initiated by the cardholder  Where transactions are merchant initiated, a valid cardholder agreement must be defined. . [optional]  # noqa: E501
            match_avsa (str): A policy value which determines whether an AVS address policy is enforced, bypassed or ignored.  Values are  `0` for the default policy (default value if not supplied). Your default values are determined by your account manager on setup of the account.   `1` for an enforced policy. Transactions that are enforced will be rejected if the AVS address numeric value does not match.   `2` to bypass. Transactions that are bypassed will be allowed through even if the address did not match.   `3` to ignore. Transactions that are ignored will bypass the result and not send address numeric details for authorisation. . [optional]  # noqa: E501
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
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
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
        self.identifier = identifier
        self.merchantid = merchantid
        self.token = token
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
