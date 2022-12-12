# CityPay API Client for Python

[![Build Status](https://api.travis-ci.com/citypay/citypay-api-client-python.svg?branch=master)](https://app.travis-ci.com/github/citypay/citypay-api-client-python)
This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It
provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing,
3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and
Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.

## Compliance and Security
Your application will need to adhere to PCI-DSS standards to operate safely and to meet requirements set out by 
Visa and MasterCard and the PCI Security Standards Council. These include

* Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at
  lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments
  as part of our compliance program.
* The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or
  primary access number (PAN)
* The application must not display the full card number on receipts, it is recommended to mask the PAN
  and show the last 4 digits. The API will return this for you for ease of receipt creation
* If you are developing a website, you will be required to perform regular scans on the network where you host the
  application to meet your compliance obligations
* You will be required to be PCI Compliant and the application must adhere to the security standard. Further information
  is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/)
* The API verifies that the request is for a valid account and originates from a trusted source using the remote IP
  address. Our application firewalls analyse data that may be an attempt to break a large number of security common
  security vulnerabilities.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 6.4.18
- Package version: 1.1.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://citypay.com/customer-centre/technical-support.html](https://citypay.com/customer-centre/technical-support.html)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/citypay/citypay-api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/citypay/citypay-api-client-python.git`)

Then import the package:
```python
import citypay
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import citypay
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import citypay
from pprint import pprint
from citypay.api import authorisation_and_payment_api
from citypay.model.acknowledgement import Acknowledgement
from citypay.model.auth_references import AuthReferences
from citypay.model.auth_request import AuthRequest
from citypay.model.auth_response import AuthResponse
from citypay.model.bin import Bin
from citypay.model.bin_lookup import BinLookup
from citypay.model.c_res_auth_request import CResAuthRequest
from citypay.model.capture_request import CaptureRequest
from citypay.model.decision import Decision
from citypay.model.error import Error
from citypay.model.pa_res_auth_request import PaResAuthRequest
from citypay.model.refund_request import RefundRequest
from citypay.model.retrieve_request import RetrieveRequest
from citypay.model.void_request import VoidRequest
# Defining the host is optional and defaults to https://api.citypay.com
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-api-key
configuration.api_key['cp-api-key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'


# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authorisation_and_payment_api.AuthorisationAndPaymentApi(api_client)
    auth_request = AuthRequest(
        airline_data=AirlineAdvice(
            carrier_name="EG Air",
            conjunction_ticket_indicator=False,
            eticket_indicator=True,
            no_air_segments=2,
            number_in_party=2,
            original_ticket_no="original_ticket_no_example",
            passenger_name="NE Person",
            segment1=AirlineSegment(
                arrival_location_code="SOU",
                carrier_code="ZZ",
                class_service_code="CC",
                departure_date=dateutil_parser('Sat Aug 01 00:00:00 UTC 2020').date(),
                departure_location_code="JER",
                flight_number="772",
                segment_fare=7500,
                stop_over_indicator="1",
            ),
            segment2=AirlineSegment(
                arrival_location_code="SOU",
                carrier_code="ZZ",
                class_service_code="CC",
                departure_date=dateutil_parser('Sat Aug 01 00:00:00 UTC 2020').date(),
                departure_location_code="JER",
                flight_number="772",
                segment_fare=7500,
                stop_over_indicator="1",
            ),
            segment3=AirlineSegment(
                arrival_location_code="SOU",
                carrier_code="ZZ",
                class_service_code="CC",
                departure_date=dateutil_parser('Sat Aug 01 00:00:00 UTC 2020').date(),
                departure_location_code="JER",
                flight_number="772",
                segment_fare=7500,
                stop_over_indicator="1",
            ),
            segment4=AirlineSegment(
                arrival_location_code="SOU",
                carrier_code="ZZ",
                class_service_code="CC",
                departure_date=dateutil_parser('Sat Aug 01 00:00:00 UTC 2020').date(),
                departure_location_code="JER",
                flight_number="772",
                segment_fare=7500,
                stop_over_indicator="1",
            ),
            ticket_issue_city="London",
            ticket_issue_date=dateutil_parser('Sat Aug 01 00:00:00 UTC 2020').date(),
            ticket_issue_name="Issue Name",
            ticket_no="A112233",
            transaction_type="TKT",
        ),
        amount=3600,
        avs_postcode_policy="avs_postcode_policy_example",
        bill_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        cardnumber="4000 0000 0000 0002",
        csc="10",
        csc_policy="csc_policy_example",
        currency="GBP",
        duplicate_policy="duplicate_policy_example",
        event_management=EventDataModel(
            event_end_date=dateutil_parser('1970-01-01').date(),
            event_id="event_id_example",
            event_organiser_id="event_organiser_id_example",
            event_start_date=dateutil_parser('1970-01-01').date(),
            payment_type="payment_type_example",
        ),
        expmonth=9,
        expyear=2025,
        external_mpi=ExternalMPI(
            authen_result="authen_result_example",
            cavv="cavv_example",
            eci=1,
            enrolled="enrolled_example",
            xid="xid_example",
        ),
        identifier="95b857a1-5955-4b86-963c-5a6dbfc4fb95",
        match_avsa="match_avsa_example",
        mcc6012=MCC6012(
            recipient_account="recipient_account_example",
            recipient_dob="recipient_dob_example",
            recipient_lastname="recipient_lastname_example",
            recipient_postcode="recipient_postcode_example",
        ),
        merchantid=11223344,
        name_on_card="MR NE BODY",
        ship_to=ContactDetails(
            address1="79 Parliament St",
            address2="Westminster",
            address3="address3_example",
            area="London",
            company="Acme Ltd",
            country="GB",
            email="card.holder@citypay.com",
            firstname="John",
            lastname="Smith",
            mobile_no="447790123456",
            postcode="L1 789",
            telephone_no="442030123456",
            title="Mr",
        ),
        threedsecure=ThreeDSecure(
            accept_headers="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            browser_color_depth="browser_color_depth_example",
            browser_ip="browser_ip_example",
            browser_java_enabled="browser_java_enabled_example",
            browser_language="browser_language_example",
            browser_screen_height="browser_screen_height_example",
            browser_screen_width="browser_screen_width_example",
            browser_tz="browser_tz_example",
            cp_bx="FjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAx...",
            downgrade1=True,
            merchant_termurl="https://mysite.com/acs/return",
            tds_policy="tds_policy_example",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        ),
        trans_info="trans_info_example",
        trans_type="trans_type_example",
    ) # AuthRequest | 

    try:
        # Authorisation
        api_response = api_instance.authorisation_request(auth_request)
        pprint(api_response)
    except citypay.ApiException as e:
        print("Exception when calling AuthorisationAndPaymentApi->authorisation_request: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.citypay.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorisationAndPaymentApi* | [**authorisation_request**](docs/AuthorisationAndPaymentApi.md#authorisation_request) | **POST** /v6/authorise | Authorisation
*AuthorisationAndPaymentApi* | [**bin_range_lookup_request**](docs/AuthorisationAndPaymentApi.md#bin_range_lookup_request) | **POST** /v6/bin | Bin Lookup
*AuthorisationAndPaymentApi* | [**c_res_request**](docs/AuthorisationAndPaymentApi.md#c_res_request) | **POST** /v6/cres | CRes
*AuthorisationAndPaymentApi* | [**capture_request**](docs/AuthorisationAndPaymentApi.md#capture_request) | **POST** /v6/capture | Capture
*AuthorisationAndPaymentApi* | [**pa_res_request**](docs/AuthorisationAndPaymentApi.md#pa_res_request) | **POST** /v6/pares | PaRes
*AuthorisationAndPaymentApi* | [**refund_request**](docs/AuthorisationAndPaymentApi.md#refund_request) | **POST** /v6/refund | Refund
*AuthorisationAndPaymentApi* | [**retrieval_request**](docs/AuthorisationAndPaymentApi.md#retrieval_request) | **POST** /v6/retrieve | Retrieval
*AuthorisationAndPaymentApi* | [**void_request**](docs/AuthorisationAndPaymentApi.md#void_request) | **POST** /v6/void | Void
*BatchProcessingApi* | [**batch_process_request**](docs/BatchProcessingApi.md#batch_process_request) | **POST** /v6/batch/process | Batch Process Request
*BatchProcessingApi* | [**batch_report_request**](docs/BatchProcessingApi.md#batch_report_request) | **POST** /v6/batch/retrieve | BatchReportRequest
*BatchProcessingApi* | [**check_batch_status_request**](docs/BatchProcessingApi.md#check_batch_status_request) | **POST** /v6/batch/status | CheckBatchStatus
*CardHolderAccountApi* | [**account_card_delete_request**](docs/CardHolderAccountApi.md#account_card_delete_request) | **DELETE** /v6/account/{accountid}/card/{cardId} | Card Deletion
*CardHolderAccountApi* | [**account_card_register_request**](docs/CardHolderAccountApi.md#account_card_register_request) | **POST** /v6/account/{accountid}/register | Card Registration
*CardHolderAccountApi* | [**account_card_status_request**](docs/CardHolderAccountApi.md#account_card_status_request) | **POST** /v6/account/{accountid}/card/{cardId}/status | Card Status
*CardHolderAccountApi* | [**account_change_contact_request**](docs/CardHolderAccountApi.md#account_change_contact_request) | **POST** /v6/account/{accountid}/contact | Contact Details Update
*CardHolderAccountApi* | [**account_create**](docs/CardHolderAccountApi.md#account_create) | **POST** /v6/account/create | Account Create
*CardHolderAccountApi* | [**account_delete_request**](docs/CardHolderAccountApi.md#account_delete_request) | **DELETE** /v6/account/{accountid} | Account Deletion
*CardHolderAccountApi* | [**account_exists_request**](docs/CardHolderAccountApi.md#account_exists_request) | **GET** /v6/account-exists/{accountid} | Account Exists
*CardHolderAccountApi* | [**account_retrieve_request**](docs/CardHolderAccountApi.md#account_retrieve_request) | **GET** /v6/account/{accountid} | Account Retrieval
*CardHolderAccountApi* | [**account_status_request**](docs/CardHolderAccountApi.md#account_status_request) | **POST** /v6/account/{accountid}/status | Account Status
*CardHolderAccountApi* | [**charge_request**](docs/CardHolderAccountApi.md#charge_request) | **POST** /v6/charge | Charge
*DirectPostApi* | [**direct_c_res_auth_request**](docs/DirectPostApi.md#direct_c_res_auth_request) | **POST** /direct/cres/auth/{uuid} | Handles a CRes response from ACS, returning back the result of authorisation
*DirectPostApi* | [**direct_c_res_tokenise_request**](docs/DirectPostApi.md#direct_c_res_tokenise_request) | **POST** /direct/cres/tokenise/{uuid} | Handles a CRes response from ACS, returning back a token for future authorisation
*DirectPostApi* | [**direct_post_auth_request**](docs/DirectPostApi.md#direct_post_auth_request) | **POST** /direct/auth | Direct Post Auth Request
*DirectPostApi* | [**direct_post_tokenise_request**](docs/DirectPostApi.md#direct_post_tokenise_request) | **POST** /direct/tokenise | Direct Post Tokenise Request
*DirectPostApi* | [**token_request**](docs/DirectPostApi.md#token_request) | **POST** /direct/token | Direct Post Token Request
*OperationalFunctionsApi* | [**acl_check_request**](docs/OperationalFunctionsApi.md#acl_check_request) | **POST** /v6/acl/check | ACL Check Request
*OperationalFunctionsApi* | [**domain_key_check_request**](docs/OperationalFunctionsApi.md#domain_key_check_request) | **POST** /dk/check | Domain Key Check Request
*OperationalFunctionsApi* | [**domain_key_gen_request**](docs/OperationalFunctionsApi.md#domain_key_gen_request) | **POST** /dk/gen | Domain Key Generation Request
*OperationalFunctionsApi* | [**list_merchants_request**](docs/OperationalFunctionsApi.md#list_merchants_request) | **GET** /v6/merchants/{clientid} | List Merchants Request
*OperationalFunctionsApi* | [**ping_request**](docs/OperationalFunctionsApi.md#ping_request) | **POST** /v6/ping | Ping Request
*PaylinkApi* | [**token_adjustment_request**](docs/PaylinkApi.md#token_adjustment_request) | **POST** /paylink/{token}/adjustment | Paylink Token Adjustment
*PaylinkApi* | [**token_close_request**](docs/PaylinkApi.md#token_close_request) | **PUT** /paylink/{token}/close | Close Paylink Token
*PaylinkApi* | [**token_create_bill_payment_request**](docs/PaylinkApi.md#token_create_bill_payment_request) | **POST** /paylink/bill-payment | Create Bill Payment Paylink Token
*PaylinkApi* | [**token_create_request**](docs/PaylinkApi.md#token_create_request) | **POST** /paylink/create | Create Paylink Token
*PaylinkApi* | [**token_purge_attachments_request**](docs/PaylinkApi.md#token_purge_attachments_request) | **PUT** /paylink/{token}/purge-attachments | Purges any attachments for a Paylink Token
*PaylinkApi* | [**token_reconciled_request**](docs/PaylinkApi.md#token_reconciled_request) | **PUT** /paylink/{token}/reconciled | Reconcile Paylink Token
*PaylinkApi* | [**token_reopen_request**](docs/PaylinkApi.md#token_reopen_request) | **PUT** /paylink/{token}/reopen | Reopen Paylink Token
*PaylinkApi* | [**token_status_changes_request**](docs/PaylinkApi.md#token_status_changes_request) | **POST** /paylink/token/changes | Paylink Token Audit
*PaylinkApi* | [**token_status_request**](docs/PaylinkApi.md#token_status_request) | **GET** /paylink/{token}/status | Paylink Token Status


## Documentation For Models

 - [AccountCreate](docs/AccountCreate.md)
 - [AccountStatus](docs/AccountStatus.md)
 - [Acknowledgement](docs/Acknowledgement.md)
 - [AclCheckRequest](docs/AclCheckRequest.md)
 - [AclCheckResponseModel](docs/AclCheckResponseModel.md)
 - [AirlineAdvice](docs/AirlineAdvice.md)
 - [AirlineSegment](docs/AirlineSegment.md)
 - [AuthReference](docs/AuthReference.md)
 - [AuthReferences](docs/AuthReferences.md)
 - [AuthRequest](docs/AuthRequest.md)
 - [AuthResponse](docs/AuthResponse.md)
 - [AuthenRequired](docs/AuthenRequired.md)
 - [Batch](docs/Batch.md)
 - [BatchReportRequest](docs/BatchReportRequest.md)
 - [BatchReportResponseModel](docs/BatchReportResponseModel.md)
 - [BatchTransaction](docs/BatchTransaction.md)
 - [BatchTransactionResultModel](docs/BatchTransactionResultModel.md)
 - [Bin](docs/Bin.md)
 - [BinLookup](docs/BinLookup.md)
 - [CResAuthRequest](docs/CResAuthRequest.md)
 - [CaptureRequest](docs/CaptureRequest.md)
 - [Card](docs/Card.md)
 - [CardHolderAccount](docs/CardHolderAccount.md)
 - [CardStatus](docs/CardStatus.md)
 - [ChargeRequest](docs/ChargeRequest.md)
 - [CheckBatchStatus](docs/CheckBatchStatus.md)
 - [CheckBatchStatusResponse](docs/CheckBatchStatusResponse.md)
 - [ContactDetails](docs/ContactDetails.md)
 - [Decision](docs/Decision.md)
 - [DirectPostRequest](docs/DirectPostRequest.md)
 - [DirectTokenAuthRequest](docs/DirectTokenAuthRequest.md)
 - [DomainKeyCheckRequest](docs/DomainKeyCheckRequest.md)
 - [DomainKeyRequest](docs/DomainKeyRequest.md)
 - [DomainKeyResponse](docs/DomainKeyResponse.md)
 - [Error](docs/Error.md)
 - [EventDataModel](docs/EventDataModel.md)
 - [Exists](docs/Exists.md)
 - [ExternalMPI](docs/ExternalMPI.md)
 - [ListMerchantsResponse](docs/ListMerchantsResponse.md)
 - [MCC6012](docs/MCC6012.md)
 - [Merchant](docs/Merchant.md)
 - [PaResAuthRequest](docs/PaResAuthRequest.md)
 - [PaylinkAddress](docs/PaylinkAddress.md)
 - [PaylinkAdjustmentRequest](docs/PaylinkAdjustmentRequest.md)
 - [PaylinkAttachmentRequest](docs/PaylinkAttachmentRequest.md)
 - [PaylinkAttachmentResult](docs/PaylinkAttachmentResult.md)
 - [PaylinkBillPaymentTokenRequest](docs/PaylinkBillPaymentTokenRequest.md)
 - [PaylinkCardHolder](docs/PaylinkCardHolder.md)
 - [PaylinkCart](docs/PaylinkCart.md)
 - [PaylinkCartItemModel](docs/PaylinkCartItemModel.md)
 - [PaylinkConfig](docs/PaylinkConfig.md)
 - [PaylinkCustomParam](docs/PaylinkCustomParam.md)
 - [PaylinkEmailNotificationPath](docs/PaylinkEmailNotificationPath.md)
 - [PaylinkErrorCode](docs/PaylinkErrorCode.md)
 - [PaylinkFieldGuardModel](docs/PaylinkFieldGuardModel.md)
 - [PaylinkPartPayments](docs/PaylinkPartPayments.md)
 - [PaylinkSMSNotificationPath](docs/PaylinkSMSNotificationPath.md)
 - [PaylinkStateEvent](docs/PaylinkStateEvent.md)
 - [PaylinkTokenCreated](docs/PaylinkTokenCreated.md)
 - [PaylinkTokenRequestModel](docs/PaylinkTokenRequestModel.md)
 - [PaylinkTokenStatus](docs/PaylinkTokenStatus.md)
 - [PaylinkTokenStatusChangeRequest](docs/PaylinkTokenStatusChangeRequest.md)
 - [PaylinkTokenStatusChangeResponse](docs/PaylinkTokenStatusChangeResponse.md)
 - [PaylinkUI](docs/PaylinkUI.md)
 - [Ping](docs/Ping.md)
 - [ProcessBatchRequest](docs/ProcessBatchRequest.md)
 - [ProcessBatchResponse](docs/ProcessBatchResponse.md)
 - [RefundRequest](docs/RefundRequest.md)
 - [RegisterCard](docs/RegisterCard.md)
 - [RequestChallenged](docs/RequestChallenged.md)
 - [RetrieveRequest](docs/RetrieveRequest.md)
 - [ThreeDSecure](docs/ThreeDSecure.md)
 - [TokenisationResponseModel](docs/TokenisationResponseModel.md)
 - [VoidRequest](docs/VoidRequest.md)


## Documentation For Authorization


## cp-api-key

- **Type**: API key
- **API key parameter name**: cp-api-key
- **Location**: HTTP header


## cp-domain-key

- **Type**: API key
- **API key parameter name**: cp-domain-key
- **Location**: URL query string


## Author

support@citypay.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in citypay.apis and citypay.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from citypay.api.default_api import DefaultApi`
- `from citypay.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import citypay
from citypay.apis import *
from citypay.models import *
```

