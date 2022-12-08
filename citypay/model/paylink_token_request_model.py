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


class PaylinkTokenRequestModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "identifier",
            "amount",
            "merchantid",
        }
        
        class properties:
            amount = schemas.Int32Schema
            
            
            class identifier(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
                    min_length = 4
            merchantid = schemas.Int32Schema
            accountno = schemas.StrSchema
        
            @staticmethod
            def cardholder() -> typing.Type['PaylinkCardHolder']:
                return PaylinkCardHolder
        
            @staticmethod
            def cart() -> typing.Type['PaylinkCart']:
                return PaylinkCart
            client_version = schemas.StrSchema
        
            @staticmethod
            def config() -> typing.Type['PaylinkConfig']:
                return PaylinkConfig
            
            
            class email(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 254
            subscription_id = schemas.StrSchema
            tx_type = schemas.StrSchema
            __annotations__ = {
                "amount": amount,
                "identifier": identifier,
                "merchantid": merchantid,
                "accountno": accountno,
                "cardholder": cardholder,
                "cart": cart,
                "client_version": client_version,
                "config": config,
                "email": email,
                "subscription_id": subscription_id,
                "tx_type": tx_type,
            }
    
    identifier: MetaOapg.properties.identifier
    amount: MetaOapg.properties.amount
    merchantid: MetaOapg.properties.merchantid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantid"]) -> MetaOapg.properties.merchantid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountno"]) -> MetaOapg.properties.accountno: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cardholder"]) -> 'PaylinkCardHolder': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cart"]) -> 'PaylinkCart': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_version"]) -> MetaOapg.properties.client_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'PaylinkConfig': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscription_id"]) -> MetaOapg.properties.subscription_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tx_type"]) -> MetaOapg.properties.tx_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "identifier", "merchantid", "accountno", "cardholder", "cart", "client_version", "config", "email", "subscription_id", "tx_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identifier"]) -> MetaOapg.properties.identifier: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantid"]) -> MetaOapg.properties.merchantid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountno"]) -> typing.Union[MetaOapg.properties.accountno, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cardholder"]) -> typing.Union['PaylinkCardHolder', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cart"]) -> typing.Union['PaylinkCart', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_version"]) -> typing.Union[MetaOapg.properties.client_version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union['PaylinkConfig', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscription_id"]) -> typing.Union[MetaOapg.properties.subscription_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tx_type"]) -> typing.Union[MetaOapg.properties.tx_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "identifier", "merchantid", "accountno", "cardholder", "cart", "client_version", "config", "email", "subscription_id", "tx_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        identifier: typing.Union[MetaOapg.properties.identifier, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        merchantid: typing.Union[MetaOapg.properties.merchantid, decimal.Decimal, int, ],
        accountno: typing.Union[MetaOapg.properties.accountno, str, schemas.Unset] = schemas.unset,
        cardholder: typing.Union['PaylinkCardHolder', schemas.Unset] = schemas.unset,
        cart: typing.Union['PaylinkCart', schemas.Unset] = schemas.unset,
        client_version: typing.Union[MetaOapg.properties.client_version, str, schemas.Unset] = schemas.unset,
        config: typing.Union['PaylinkConfig', schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        subscription_id: typing.Union[MetaOapg.properties.subscription_id, str, schemas.Unset] = schemas.unset,
        tx_type: typing.Union[MetaOapg.properties.tx_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaylinkTokenRequestModel':
        return super().__new__(
            cls,
            *args,
            identifier=identifier,
            amount=amount,
            merchantid=merchantid,
            accountno=accountno,
            cardholder=cardholder,
            cart=cart,
            client_version=client_version,
            config=config,
            email=email,
            subscription_id=subscription_id,
            tx_type=tx_type,
            _configuration=_configuration,
            **kwargs,
        )

from citypay.model.paylink_card_holder import PaylinkCardHolder
from citypay.model.paylink_cart import PaylinkCart
from citypay.model.paylink_config import PaylinkConfig
