# coding: utf-8

"""
    CityPay Payment API

     This CityPay API is a HTTP RESTful payment API used for direct server to server transactional processing. It provides a number of payment mechanisms including: Internet, MOTO, Continuous Authority transaction processing, 3-D Secure decision handling using RFA Secure, Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids and Completion processing. The API is also capable of tokinsed payments using Card Holder Accounts.  ## Compliance and Security <aside class=\"notice\">   Before we begin a reminder that your application will need to adhere to PCI-DSS standards to operate safely   and to meet requirements set out by Visa and MasterCard and the PCI Security Standards Council including: </aside>  * Data must be collected using TLS version 1.2 using [strong cryptography](#enabled-tls-ciphers). We will not accept calls to our API at   lower grade encryption levels. We regularly scan our TLS endpoints for vulnerabilities and perform TLS assessments   as part of our compliance program. * The application must not store sensitive card holder data (CHD) such as the card security code (CSC) or   primary access number (PAN) * The application must not display the full card number on receipts, it is recommended to mask the PAN   and show the last 4 digits. The API will return this for you for ease of receipt creation * If you are developing a website, you will be required to perform regular scans on the network where you host the   application to meet your compliance obligations * You will be required to be PCI Compliant and the application must adhere to the security standard. Further information   is available from [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/) * The API verifies that the request is for a valid account and originates from a trusted source using the remote IP   address. Our application firewalls analyse data that may be an attempt to break a large number of security common   security vulnerabilities.   # noqa: E501

    Contact: support@citypay.com
    Generated by: https://openapi-generator.tech
"""

from __future__ import absolute_import
import unittest
from citypay.models.auth_references import AuthReferences  # noqa: E501
from citypay import ApiClient


class TestAuthReferences(unittest.TestCase):
    """AuthReferences unit test stubs"""

    def setUp(self):
        self.data = """
        {"auths": [
          {
              "amount": "0.12",
              "amount_value": 12,
              "atrn": "",
              "authcode": "A12345",
              "batchno": "",
              "currency": "GBP",
              "datetime": "2020-07-21T15:55:04Z",
              "identifier": "TestingAPI",
              "maskedpan": "400000******0000",
              "merchantid": 12345678,
              "result": "Accepted",
              "trans_status": "O",
              "trans_type": "S",
              "transno": 88
          }
        ]}       
        """
        self.instance = ApiClient().deserialize(self.data, "AuthReferences", "application/json")

    def tearDown(self):
        pass

    def testAuthReferences(self):
        """Test AuthReferences"""
        self.assertEqual(self.instance.auths[0].amount, "0.12")
        self.assertEqual(self.instance.auths[0].amount_value, 12)
        self.assertEqual(self.instance.auths[0].atrn, "")
        self.assertEqual(self.instance.auths[0].authcode, "A12345")
        self.assertEqual(self.instance.auths[0].batchno, "")
        self.assertEqual(self.instance.auths[0].currency, "GBP")
        self.assertEqual(self.instance.auths[0].datetime.isoformat(), "2020-07-21T15:55:04+00:00")
        self.assertEqual(self.instance.auths[0].identifier, "TestingAPI")
        self.assertEqual(self.instance.auths[0].maskedpan, "400000******0000")
        self.assertEqual(self.instance.auths[0].merchantid, 12345678)
        self.assertEqual(self.instance.auths[0].result, "Accepted")
        self.assertEqual(self.instance.auths[0].trans_status, "O")
        self.assertEqual(self.instance.auths[0].trans_type, "S")
        self.assertEqual(self.instance.auths[0].transno, 88)


if __name__ == '__main__':
    unittest.main()
