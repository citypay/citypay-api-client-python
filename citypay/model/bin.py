# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by  Visa and MasterCard and the PCI Security Standards Council. These include  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from citypay import schemas  # noqa: F401


class Bin(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            bin_commercial = schemas.BoolSchema
            bin_corporate = schemas.BoolSchema
            bin_country_issued = schemas.StrSchema
            bin_credit = schemas.BoolSchema
            bin_currency = schemas.StrSchema
            bin_debit = schemas.BoolSchema
            bin_description = schemas.StrSchema
            bin_eu = schemas.BoolSchema
            scheme = schemas.StrSchema
            __annotations__ = {
                "bin_commercial": bin_commercial,
                "bin_corporate": bin_corporate,
                "bin_country_issued": bin_country_issued,
                "bin_credit": bin_credit,
                "bin_currency": bin_currency,
                "bin_debit": bin_debit,
                "bin_description": bin_description,
                "bin_eu": bin_eu,
                "scheme": scheme,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_commercial"]) -> MetaOapg.properties.bin_commercial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_corporate"]) -> MetaOapg.properties.bin_corporate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_country_issued"]) -> MetaOapg.properties.bin_country_issued: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_credit"]) -> MetaOapg.properties.bin_credit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_currency"]) -> MetaOapg.properties.bin_currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_debit"]) -> MetaOapg.properties.bin_debit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_description"]) -> MetaOapg.properties.bin_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bin_eu"]) -> MetaOapg.properties.bin_eu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scheme"]) -> MetaOapg.properties.scheme: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bin_commercial", "bin_corporate", "bin_country_issued", "bin_credit", "bin_currency", "bin_debit", "bin_description", "bin_eu", "scheme", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_commercial"]) -> typing.Union[MetaOapg.properties.bin_commercial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_corporate"]) -> typing.Union[MetaOapg.properties.bin_corporate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_country_issued"]) -> typing.Union[MetaOapg.properties.bin_country_issued, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_credit"]) -> typing.Union[MetaOapg.properties.bin_credit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_currency"]) -> typing.Union[MetaOapg.properties.bin_currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_debit"]) -> typing.Union[MetaOapg.properties.bin_debit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_description"]) -> typing.Union[MetaOapg.properties.bin_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bin_eu"]) -> typing.Union[MetaOapg.properties.bin_eu, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scheme"]) -> typing.Union[MetaOapg.properties.scheme, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bin_commercial", "bin_corporate", "bin_country_issued", "bin_credit", "bin_currency", "bin_debit", "bin_description", "bin_eu", "scheme", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bin_commercial: typing.Union[MetaOapg.properties.bin_commercial, bool, schemas.Unset] = schemas.unset,
        bin_corporate: typing.Union[MetaOapg.properties.bin_corporate, bool, schemas.Unset] = schemas.unset,
        bin_country_issued: typing.Union[MetaOapg.properties.bin_country_issued, str, schemas.Unset] = schemas.unset,
        bin_credit: typing.Union[MetaOapg.properties.bin_credit, bool, schemas.Unset] = schemas.unset,
        bin_currency: typing.Union[MetaOapg.properties.bin_currency, str, schemas.Unset] = schemas.unset,
        bin_debit: typing.Union[MetaOapg.properties.bin_debit, bool, schemas.Unset] = schemas.unset,
        bin_description: typing.Union[MetaOapg.properties.bin_description, str, schemas.Unset] = schemas.unset,
        bin_eu: typing.Union[MetaOapg.properties.bin_eu, bool, schemas.Unset] = schemas.unset,
        scheme: typing.Union[MetaOapg.properties.scheme, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Bin':
        return super().__new__(
            cls,
            *args,
            bin_commercial=bin_commercial,
            bin_corporate=bin_corporate,
            bin_country_issued=bin_country_issued,
            bin_credit=bin_credit,
            bin_currency=bin_currency,
            bin_debit=bin_debit,
            bin_description=bin_description,
            bin_eu=bin_eu,
            scheme=scheme,
            _configuration=_configuration,
            **kwargs,
        )
