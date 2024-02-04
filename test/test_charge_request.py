# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import
import unittest
from citypay.models.charge_request import ChargeRequest  # noqa: E501


class TestChargeRequest(unittest.TestCase):
    """ChargeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ChargeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = citypay.models.charge_request.ChargeRequest()  # noqa: E501

        if include_optional:
            return ChargeRequest(
                amount=3600,
                avs_postcode_policy='0',
                csc='123',
                csc_policy='0',
                currency='GBP',
                duplicate_policy='0',
                identifier='95b857a1-5955-4b86-963c-5a6dbfc4fb95',
                match_avsa='0',
                merchantid=11223344,
                token='ctPCAPyNyCkx3Ry8wGyv8khC3ch2hUSB3Db..Qzr',
                trans_info='0',
                trans_type='0'
            )
        else:
            return ChargeRequest(
                amount=3600,
                identifier='95b857a1-5955-4b86-963c-5a6dbfc4fb95',
                merchantid=11223344,
                token='ctPCAPyNyCkx3Ry8wGyv8khC3ch2hUSB3Db..Qzr',
            )

    def testChargeRequest(self):
        """Test ChargeRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
