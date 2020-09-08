# coding: utf-8

from __future__ import absolute_import

import os
import unittest
import datetime

import citypay
from citypay.rest import ApiException
from citypay.models.api_key import *
from citypay.api_client import ApiClient



class TestApiIntegration(unittest.TestCase):
    """Error unit test stubs"""

    @classmethod
    def setUpClass(self):

        self.client_id = os.environ['CP_CLIENT_ID']
        self.licence_key = os.environ['CP_LICENCE_KEY']
        self.merchant_id = os.environ['CP_MERCHANT_ID']


    def setUp(self):
        # create new api key on each call
        client_api_key = api_key_generate(self.client_id, self.licence_key)
        self.api_client = citypay.ApiClient(citypay.Configuration(
            host="https://sandbox.citypay.com/v6",
            api_key={'cp-api-key': str(client_api_key)}
        ))

    def testPing(self):
        api_response = citypay.OperationalApi(self.api_client).ping_request(citypay.Ping(
            identifier="it_test"
        ))
        self.assertEqual("044", api_response.code)


    def tearDown(self):
        self.api_client.close()

if __name__ == '__main__':
    unittest.main()
