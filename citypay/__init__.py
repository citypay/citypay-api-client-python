# coding: utf-8

# flake8: noqa

"""
    CityPay Payment API

     This CityPay API is an HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokenized payments using cardholder Accounts.  ## Compliance and Security Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by  Visa and MasterCard and the PCI Security Standards Council. These include  * Data must be collected using TLS version 1.2 using [strong cryptography](https://citypay.github.io/api-docs/payment-api/#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive cardholder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities. 

    Contact: support@citypay.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.2"

# import apis into sdk package
from citypay.api.authorisation_and_payment_api import AuthorisationAndPaymentApi
from citypay.api.batch_processing_api import BatchProcessingApi
from citypay.api.card_holder_account_api import CardHolderAccountApi
from citypay.api.direct_post_api import DirectPostApi
from citypay.api.operational_functions_api import OperationalFunctionsApi
from citypay.api.paylink_api import PaylinkApi

# import ApiClient
from citypay.api_response import ApiResponse
from citypay.api_client import ApiClient
from citypay.configuration import Configuration
from citypay.exceptions import OpenApiException
from citypay.exceptions import ApiTypeError
from citypay.exceptions import ApiValueError
from citypay.exceptions import ApiKeyError
from citypay.exceptions import ApiAttributeError
from citypay.exceptions import ApiException

# import models into sdk package
from citypay.models.account_create import AccountCreate
from citypay.models.account_status import AccountStatus
from citypay.models.acknowledgement import Acknowledgement
from citypay.models.acl_check_request import AclCheckRequest
from citypay.models.acl_check_response_model import AclCheckResponseModel
from citypay.models.airline_advice import AirlineAdvice
from citypay.models.airline_segment import AirlineSegment
from citypay.models.auth_reference import AuthReference
from citypay.models.auth_references import AuthReferences
from citypay.models.auth_request import AuthRequest
from citypay.models.auth_response import AuthResponse
from citypay.models.authen_required import AuthenRequired
from citypay.models.batch import Batch
from citypay.models.batch_report_request import BatchReportRequest
from citypay.models.batch_report_response_model import BatchReportResponseModel
from citypay.models.batch_transaction import BatchTransaction
from citypay.models.batch_transaction_result_model import BatchTransactionResultModel
from citypay.models.bin import Bin
from citypay.models.bin_lookup import BinLookup
from citypay.models.c_res_auth_request import CResAuthRequest
from citypay.models.capture_request import CaptureRequest
from citypay.models.card import Card
from citypay.models.card_holder_account import CardHolderAccount
from citypay.models.card_status import CardStatus
from citypay.models.charge_request import ChargeRequest
from citypay.models.check_batch_status import CheckBatchStatus
from citypay.models.check_batch_status_response import CheckBatchStatusResponse
from citypay.models.contact_details import ContactDetails
from citypay.models.decision import Decision
from citypay.models.direct_post_request import DirectPostRequest
from citypay.models.direct_token_auth_request import DirectTokenAuthRequest
from citypay.models.domain_key_check_request import DomainKeyCheckRequest
from citypay.models.domain_key_request import DomainKeyRequest
from citypay.models.domain_key_response import DomainKeyResponse
from citypay.models.error import Error
from citypay.models.event_data_model import EventDataModel
from citypay.models.exists import Exists
from citypay.models.external_mpi import ExternalMPI
from citypay.models.list_merchants_response import ListMerchantsResponse
from citypay.models.mcc6012 import MCC6012
from citypay.models.merchant import Merchant
from citypay.models.pa_res_auth_request import PaResAuthRequest
from citypay.models.paylink_address import PaylinkAddress
from citypay.models.paylink_adjustment_request import PaylinkAdjustmentRequest
from citypay.models.paylink_attachment_request import PaylinkAttachmentRequest
from citypay.models.paylink_attachment_result import PaylinkAttachmentResult
from citypay.models.paylink_bill_payment_token_request import PaylinkBillPaymentTokenRequest
from citypay.models.paylink_card_holder import PaylinkCardHolder
from citypay.models.paylink_cart import PaylinkCart
from citypay.models.paylink_cart_item_model import PaylinkCartItemModel
from citypay.models.paylink_config import PaylinkConfig
from citypay.models.paylink_custom_param import PaylinkCustomParam
from citypay.models.paylink_email_notification_path import PaylinkEmailNotificationPath
from citypay.models.paylink_error_code import PaylinkErrorCode
from citypay.models.paylink_field_guard_model import PaylinkFieldGuardModel
from citypay.models.paylink_part_payments import PaylinkPartPayments
from citypay.models.paylink_sms_notification_path import PaylinkSMSNotificationPath
from citypay.models.paylink_state_event import PaylinkStateEvent
from citypay.models.paylink_token_created import PaylinkTokenCreated
from citypay.models.paylink_token_request_model import PaylinkTokenRequestModel
from citypay.models.paylink_token_status import PaylinkTokenStatus
from citypay.models.paylink_token_status_change_request import PaylinkTokenStatusChangeRequest
from citypay.models.paylink_token_status_change_response import PaylinkTokenStatusChangeResponse
from citypay.models.paylink_ui import PaylinkUI
from citypay.models.ping import Ping
from citypay.models.process_batch_request import ProcessBatchRequest
from citypay.models.process_batch_response import ProcessBatchResponse
from citypay.models.refund_request import RefundRequest
from citypay.models.register_card import RegisterCard
from citypay.models.request_challenged import RequestChallenged
from citypay.models.retrieve_request import RetrieveRequest
from citypay.models.three_d_secure import ThreeDSecure
from citypay.models.tokenisation_response_model import TokenisationResponseModel
from citypay.models.void_request import VoidRequest
from citypay.models.api_key import api_key_generate
