"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by  Visa and MasterCard and the PCI Security Standards Council. These include  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from citypay.api_client import ApiClient, Endpoint as _Endpoint
from citypay.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from citypay.model.auth_response import AuthResponse
from citypay.model.direct_post_request import DirectPostRequest
from citypay.model.direct_token_auth_request import DirectTokenAuthRequest
from citypay.model.error import Error
from citypay.model.tokenisation_response_model import TokenisationResponseModel


class DirectPostApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __direct_c_res_auth_request(
            self,
            uuid,
            **kwargs
        ):
            """Handles a CRes response from ACS, returning back the result of authorisation  # noqa: E501

            Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData` value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to perform a `Direct Post` integration who wish to handle the challenge flow themselves.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.direct_c_res_auth_request(uuid, async_req=True)
            >>> result = thread.get()

            Args:
                uuid (str): An identifier used to track the CReq/CRes cycle.

            Keyword Args:
                cres (str): The CRES from the ACS.. [optional]
                three_ds_session_data (str): The session data from the ACS.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AuthResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['uuid'] = \
                uuid
            return self.call_with_http_info(**kwargs)

        self.direct_c_res_auth_request = _Endpoint(
            settings={
                'response_type': (AuthResponse,),
                'auth': [],
                'endpoint_path': '/direct/cres/auth/{uuid}',
                'operation_id': 'direct_c_res_auth_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'cres',
                    'three_ds_session_data',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'cres':
                        (str,),
                    'three_ds_session_data':
                        (str,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'cres': 'cres',
                    'three_ds_session_data': 'threeDSSessionData',
                },
                'location_map': {
                    'uuid': 'path',
                    'cres': 'form',
                    'three_ds_session_data': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/x-www-form-urlencoded'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client,
            callable=__direct_c_res_auth_request
        )

        def __direct_c_res_tokenise_request(
            self,
            uuid,
            **kwargs
        ):
            """Handles a CRes response from ACS, returning back a token for future authorisation  # noqa: E501

            Used to post from an ACS during a ThreeDSecure direct flow process. The endpoint requires a valid `threeDSSessionData` value which defines the unique transaction through its workflow. This endpoint may be used by merchants wishing to perform a `Direct Post` integration who wish to handle the challenge flow themselves.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.direct_c_res_tokenise_request(uuid, async_req=True)
            >>> result = thread.get()

            Args:
                uuid (str): An identifier used to track the CReq/CRes cycle.

            Keyword Args:
                cres (str): The CRES from the ACS.. [optional]
                three_ds_session_data (str): The session data from the ACS.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                TokenisationResponseModel
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['uuid'] = \
                uuid
            return self.call_with_http_info(**kwargs)

        self.direct_c_res_tokenise_request = _Endpoint(
            settings={
                'response_type': (TokenisationResponseModel,),
                'auth': [],
                'endpoint_path': '/direct/cres/tokenise/{uuid}',
                'operation_id': 'direct_c_res_tokenise_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'uuid',
                    'cres',
                    'three_ds_session_data',
                ],
                'required': [
                    'uuid',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'uuid':
                        (str,),
                    'cres':
                        (str,),
                    'three_ds_session_data':
                        (str,),
                },
                'attribute_map': {
                    'uuid': 'uuid',
                    'cres': 'cres',
                    'three_ds_session_data': 'threeDSSessionData',
                },
                'location_map': {
                    'uuid': 'path',
                    'cres': 'form',
                    'three_ds_session_data': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/x-www-form-urlencoded'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client,
            callable=__direct_c_res_tokenise_request
        )

        def __direct_post_auth_request(
            self,
            direct_post_request,
            **kwargs
        ):
            """Direct Post Auth Request  # noqa: E501

            Used to initiate a direct post request transaction flow.  <pre class=\"inline-code language-bash\"> <code> curl https://api.citypay.com/v6/direct?cp-domain-key=n834ytqp84y... \\  -d \"amount=7500&identifier=example_trans&cardnumber=4000000000000002&expmonth=9&expyear=2028&bill_to_postcode=L1+7ZW </code> </pre>.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.direct_post_auth_request(direct_post_request, async_req=True)
            >>> result = thread.get()

            Args:
                direct_post_request (DirectPostRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AuthResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['direct_post_request'] = \
                direct_post_request
            return self.call_with_http_info(**kwargs)

        self.direct_post_auth_request = _Endpoint(
            settings={
                'response_type': (AuthResponse,),
                'auth': [
                    'cp-api-key',
                    'cp-domain-key'
                ],
                'endpoint_path': '/direct/auth',
                'operation_id': 'direct_post_auth_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'direct_post_request',
                ],
                'required': [
                    'direct_post_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'direct_post_request':
                        (DirectPostRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'direct_post_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ]
            },
            api_client=api_client,
            callable=__direct_post_auth_request
        )

        def __direct_post_tokenise_request(
            self,
            direct_post_request,
            **kwargs
        ):
            """Direct Post Tokenise Request  # noqa: E501

            Used to initiate a direct post request transaction flow.  <pre class=\"inline-code language-bash\"> <code> curl https://api.citypay.com/v6/direct?cp-domain-key=n834ytqp84y... \\  -d \"amount=7500&identifier=example_trans&cardnumber=4000000000000002&expmonth=9&expyear=2028&bill_to_postcode=L1+7ZW </code> </pre>.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.direct_post_tokenise_request(direct_post_request, async_req=True)
            >>> result = thread.get()

            Args:
                direct_post_request (DirectPostRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AuthResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['direct_post_request'] = \
                direct_post_request
            return self.call_with_http_info(**kwargs)

        self.direct_post_tokenise_request = _Endpoint(
            settings={
                'response_type': (AuthResponse,),
                'auth': [
                    'cp-api-key',
                    'cp-domain-key'
                ],
                'endpoint_path': '/direct/tokenise',
                'operation_id': 'direct_post_tokenise_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'direct_post_request',
                ],
                'required': [
                    'direct_post_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'direct_post_request':
                        (DirectPostRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'direct_post_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ]
            },
            api_client=api_client,
            callable=__direct_post_tokenise_request
        )

        def __token_request(
            self,
            direct_token_auth_request,
            **kwargs
        ):
            """Direct Post Token Request  # noqa: E501

            Perform a request for authorisation for a previously generated token. This flow will return an authorisation response stating that the transaction was approved or declined.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.token_request(direct_token_auth_request, async_req=True)
            >>> result = thread.get()

            Args:
                direct_token_auth_request (DirectTokenAuthRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AuthResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['direct_token_auth_request'] = \
                direct_token_auth_request
            return self.call_with_http_info(**kwargs)

        self.token_request = _Endpoint(
            settings={
                'response_type': (AuthResponse,),
                'auth': [
                    'cp-api-key',
                    'cp-domain-key'
                ],
                'endpoint_path': '/direct/token',
                'operation_id': 'token_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'direct_token_auth_request',
                ],
                'required': [
                    'direct_token_auth_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'direct_token_auth_request':
                        (DirectTokenAuthRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'direct_token_auth_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'text/xml'
                ]
            },
            api_client=api_client,
            callable=__token_request
        )
