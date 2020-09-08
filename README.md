# CityPay API Client for Python

This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It
provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing,
3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and
Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.

## Compliance and Security
<aside class=\"notice\">
  Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely
  and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including:
</aside>

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

- API version: 6.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://citypay.com/customer-centre/technical-support.html](https://citypay.com/customer-centre/technical-support.html)

## Requirements.

Python 2.7 and 3.4+

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
from __future__ import print_function

import time
import citypay
from citypay.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.citypay.com/v6
# See configuration.py for a list of all supported configuration parameters.
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cp-api-key
configuration = citypay.Configuration(
    host = "https://api.citypay.com/v6",
    api_key = {
        'cp-api-key': citypay.api_key_generate('PC2', 'LK')
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cp-api-key'] = 'Bearer'


# Enter a context with an instance of the API client
with citypay.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = citypay.CardHolderAccountApi(api_client)
    accountid = 'accountid_example' # str | The account id that refers to the customer's account no. This value will have been provided when setting up the card holder account.
card_id = 'card_id_example' # str | The id of the card that is presented by a call to retrieve a card holder account.

    try:
        # Card Deletion
        api_response = api_instance.account_card_delete_request(accountid, card_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CardHolderAccountApi->account_card_delete_request: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://api.citypay.com/v6*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CardHolderAccountApi* | [**account_card_delete_request**](docs/CardHolderAccountApi.md#account_card_delete_request) | **DELETE** /account/{accountid}/card/{cardId} | Card Deletion
*CardHolderAccountApi* | [**account_card_register_request**](docs/CardHolderAccountApi.md#account_card_register_request) | **POST** /account/{accountid}/register | Card Registration
*CardHolderAccountApi* | [**account_card_status_request**](docs/CardHolderAccountApi.md#account_card_status_request) | **POST** /account/{accountid}/card/{cardId}/status | Card Status
*CardHolderAccountApi* | [**account_change_contact_request**](docs/CardHolderAccountApi.md#account_change_contact_request) | **POST** /account/{accountid}/contact | Contact Details Update
*CardHolderAccountApi* | [**account_create**](docs/CardHolderAccountApi.md#account_create) | **POST** /account/create | Account Create
*CardHolderAccountApi* | [**account_delete_request**](docs/CardHolderAccountApi.md#account_delete_request) | **DELETE** /account/{accountid} | Account Deletion
*CardHolderAccountApi* | [**account_retrieve_request**](docs/CardHolderAccountApi.md#account_retrieve_request) | **GET** /account/{accountid} | Account Retrieval
*CardHolderAccountApi* | [**account_status_request**](docs/CardHolderAccountApi.md#account_status_request) | **POST** /account/{accountid}/status | Account Status
*CardHolderAccountApi* | [**charge_request**](docs/CardHolderAccountApi.md#charge_request) | **POST** /charge | Charge
*OperationalApi* | [**list_merchants_request**](docs/OperationalApi.md#list_merchants_request) | **GET** /merchants/{clientid} | List Merchants Request
*OperationalApi* | [**ping_request**](docs/OperationalApi.md#ping_request) | **POST** /ping | Ping Request
*PaymentProcessingApi* | [**authorisation_request**](docs/PaymentProcessingApi.md#authorisation_request) | **POST** /authorise | Authorisation
*PaymentProcessingApi* | [**c_res_request**](docs/PaymentProcessingApi.md#c_res_request) | **POST** /cres | CRes
*PaymentProcessingApi* | [**capture_request**](docs/PaymentProcessingApi.md#capture_request) | **POST** /capture | Capture
*PaymentProcessingApi* | [**pa_res_request**](docs/PaymentProcessingApi.md#pa_res_request) | **POST** /pares | PaRes
*PaymentProcessingApi* | [**retrieval_request**](docs/PaymentProcessingApi.md#retrieval_request) | **POST** /retrieve | Retrieval
*PaymentProcessingApi* | [**void_request**](docs/PaymentProcessingApi.md#void_request) | **POST** /void | Void


## Documentation For Models

 - [AccountCreate](docs/AccountCreate.md)
 - [AccountStatus](docs/AccountStatus.md)
 - [Acknowledgement](docs/Acknowledgement.md)
 - [AirlineAdvice](docs/AirlineAdvice.md)
 - [AirlineSegment](docs/AirlineSegment.md)
 - [AuthReference](docs/AuthReference.md)
 - [AuthReferences](docs/AuthReferences.md)
 - [AuthRequest](docs/AuthRequest.md)
 - [AuthResponse](docs/AuthResponse.md)
 - [AuthenRequired](docs/AuthenRequired.md)
 - [CResAuthRequest](docs/CResAuthRequest.md)
 - [CaptureRequest](docs/CaptureRequest.md)
 - [Card](docs/Card.md)
 - [CardHolderAccount](docs/CardHolderAccount.md)
 - [CardStatus](docs/CardStatus.md)
 - [ChargeRequest](docs/ChargeRequest.md)
 - [ContactDetails](docs/ContactDetails.md)
 - [Decision](docs/Decision.md)
 - [Error](docs/Error.md)
 - [ExternalMPI](docs/ExternalMPI.md)
 - [ListMerchantsResponse](docs/ListMerchantsResponse.md)
 - [MCC6012](docs/MCC6012.md)
 - [Merchant](docs/Merchant.md)
 - [PaResAuthRequest](docs/PaResAuthRequest.md)
 - [Ping](docs/Ping.md)
 - [RegisterCard](docs/RegisterCard.md)
 - [RequestChallenged](docs/RequestChallenged.md)
 - [RetrieveRequest](docs/RetrieveRequest.md)
 - [ThreeDSecure](docs/ThreeDSecure.md)
 - [VoidRequest](docs/VoidRequest.md)


## Documentation For Authorization


## cp-api-key

- **Type**: API key
- **API key parameter name**: cp-api-key
- **Location**: HTTP header


## Author

support@citypay.com

