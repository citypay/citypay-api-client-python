"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities..   # noqa: E501

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
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.acl_check_request import AclCheckRequest
from citypay.model.acl_check_response_model import AclCheckResponseModel
from citypay.model.error import Error
from citypay.model.list_merchants_response import ListMerchantsResponse
from citypay.model.ping import Ping


class OperationalApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __acl_check_request(
            self,
            acl_check_request,
            **kwargs
        ):
            """ACL Check Request  # noqa: E501

            Allows the checking of IP addresses against configured ACLs. Requests can perform a lookup of addresses in subnets and services such as AWS or Azure to check that those addresses are listed in the ACLs.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.acl_check_request(acl_check_request, async_req=True)
            >>> result = thread.get()

            Args:
                acl_check_request (AclCheckRequest):

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
                AclCheckResponseModel
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
            kwargs['acl_check_request'] = \
                acl_check_request
            return self.call_with_http_info(**kwargs)

        self.acl_check_request = _Endpoint(
            settings={
                'response_type': (AclCheckResponseModel,),
                'auth': [
                    'cp-api-key'
                ],
                'endpoint_path': '/acl/check',
                'operation_id': 'acl_check_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'acl_check_request',
                ],
                'required': [
                    'acl_check_request',
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
                    'acl_check_request':
                        (AclCheckRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'acl_check_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/xml'
                ],
                'content_type': [
                    'application/json',
                    'text/xml'
                ]
            },
            api_client=api_client,
            callable=__acl_check_request
        )

        def __list_merchants_request(
            self,
            clientid,
            **kwargs
        ):
            """List Merchants Request  # noqa: E501

            An operational request to list current merchants for a client.  ### Sorting  Sorting can be performed by include a query parameter i.e. `/merchants/?sort=merchantid`  Fields that can be sorted are `merchantid` or `name`.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_merchants_request(clientid, async_req=True)
            >>> result = thread.get()

            Args:
                clientid (str): The client id to return merchants for, specifying \"default\" will use the value in your api key.

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
                ListMerchantsResponse
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
            kwargs['clientid'] = \
                clientid
            return self.call_with_http_info(**kwargs)

        self.list_merchants_request = _Endpoint(
            settings={
                'response_type': (ListMerchantsResponse,),
                'auth': [
                    'cp-api-key'
                ],
                'endpoint_path': '/merchants/{clientid}',
                'operation_id': 'list_merchants_request',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'clientid',
                ],
                'required': [
                    'clientid',
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
                    'clientid':
                        (str,),
                },
                'attribute_map': {
                    'clientid': 'clientid',
                },
                'location_map': {
                    'clientid': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/xml'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_merchants_request
        )

        def __ping_request(
            self,
            ping,
            **kwargs
        ):
            """Ping Request  # noqa: E501

            A ping request which performs a connection and authentication test to the CityPay API server. The request will return a standard Acknowledgement with a response code `044` to signify a successful ping.  The ping call is useful to confirm that you will be able to access  the API from behind any firewalls and that the permission model is granting access from your source.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.ping_request(ping, async_req=True)
            >>> result = thread.get()

            Args:
                ping (Ping):

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
                Acknowledgement
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
            kwargs['ping'] = \
                ping
            return self.call_with_http_info(**kwargs)

        self.ping_request = _Endpoint(
            settings={
                'response_type': (Acknowledgement,),
                'auth': [
                    'cp-api-key'
                ],
                'endpoint_path': '/ping',
                'operation_id': 'ping_request',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ping',
                ],
                'required': [
                    'ping',
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
                    'ping':
                        (Ping,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'ping': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/xml'
                ],
                'content_type': [
                    'application/json',
                    'text/xml'
                ]
            },
            api_client=api_client,
            callable=__ping_request
        )
