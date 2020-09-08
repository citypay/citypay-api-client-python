# coding: utf-8

from __future__ import absolute_import

import os
import unittest
import datetime

import citypay
from citypay.rest import ApiException
from citypay.models.api_key import *
from citypay.api_client import ApiClient

client_id = os.environ['CP_CLIENT_ID']
licence_key = os.environ['CP_LICENCE_KEY']
merchant_id = os.environ['CP_MERCHANT_ID']


class TestApiIntegration(unittest.TestCase):
    """Error unit test stubs"""

    @classmethod
    def setUpClass(self):
        client_api_key = api_key_generate(client_id, licence_key)
        print(client_api_key)
        configuration = citypay.Configuration(
            host="https://sandbox.citypay.com/v6",
            api_key={'cp-api-key': str(client_api_key)}
        )

        with citypay.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = citypay.OperationalApi(api_client)
            ping = citypay.Ping()  # Ping |
            try:
                # Ping Request
                self.api_response = api_instance.ping_request(ping)
            except ApiException as e:
                print("Exception when calling OperationalApi->ping_request: %s\n" % e)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPing(self):
        """Test Ping"""
        self.assertEqual(self.api_response.code, "044")


if __name__ == '__main__':
    unittest.main()
