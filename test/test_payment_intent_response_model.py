# coding: utf-8

"""
    CityPay Payment API

     Welcome to the CityPay API, a robust HTTP API payment solution designed for seamless server-to-server  transactional processing. Our API facilitates a wide array of payment operations, catering to diverse business needs.  Whether you're integrating Internet payments, handling Mail Order/Telephone Order (MOTO) transactions, managing  Subscriptions with Recurring and Continuous Authority payments, or navigating the complexities of 3-D Secure  authentication, our API is equipped to support your requirements. Additionally, we offer functionalities for  Authorisation, Refunding, Pre-Authorisation, Cancellation/Voids, and Completion processing, alongside the capability  for tokenised payments.  ## Compliance and Security Overview <aside class=\"notice\">   Ensuring the security of payment transactions and compliance with industry standards is paramount. Our API is    designed with stringent security measures and compliance protocols to safeguard sensitive information and meet    the rigorous requirements of Visa, MasterCard, and the PCI Security Standards Council. </aside>  ### Key Compliance and Security Measures  * **TLS Encryption**: All data transmissions must utilise TLS version 1.2 or higher, employing [strong cryptography](#enabled-tls-ciphers). Our infrastructure strictly enforces this requirement to maintain the integrity and confidentiality of data in transit. We conduct regular scans and assessments of our TLS endpoints to identify and mitigate vulnerabilities. * **Data Storage Prohibitions**: Storing sensitive cardholder data (CHD), such as the card security code (CSC) or primary account number (PAN), is strictly prohibited. Our API is designed to minimize your exposure to sensitive data, thereby reducing your compliance burden. * **Data Masking**: For consumer protection and compliance, full card numbers must not be displayed on receipts or any customer-facing materials. Our API automatically masks PANs, displaying only the last four digits to facilitate safe receipt generation. * **Network Scans**: If your application is web-based, regular scans of your hosting environment are mandatory to identify and rectify potential vulnerabilities. This proactive measure is crucial for maintaining a secure and compliant online presence. * **PCI Compliance**: Adherence to PCI DSS standards is not optional; it's a requirement for operating securely and legally in the payments ecosystem. For detailed information on compliance requirements and resources, please visit the PCI Security Standards Council website [https://www.pcisecuritystandards.org/](https://www.pcisecuritystandards.org/). * **Request Validation**: Our API includes mechanisms to verify the legitimacy of each request, ensuring it pertains to a valid account and originates from a trusted source. We leverage remote IP address verification alongside sophisticated application firewall technologies to thwart a wide array of common security threats.  ## Getting Started Before integrating with the CityPay API, ensure your application and development practices align with the outlined compliance and security measures. This preparatory step is crucial for a smooth integration process and the long-term success of your payment processing operations.  For further details on API endpoints, request/response formats, and code examples, proceed to the subsequent sections of our documentation. Our aim is to provide you with all the necessary tools and information to integrate our payment processing capabilities seamlessly into your application.  Thank you for choosing CityPay API. We look forward to supporting your payment processing needs with our secure, compliant, and versatile API solution. 

    Contact: support@citypay.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from citypay.models.payment_intent_response_model import PaymentIntentResponseModel

class TestPaymentIntentResponseModel(unittest.TestCase):
    """PaymentIntentResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentIntentResponseModel:
        """Test PaymentIntentResponseModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentIntentResponseModel`
        """
        model = PaymentIntentResponseModel()
        if include_optional:
            return PaymentIntentResponseModel(
                adjustments = citypay.models.adjustments.Adjustments(
                    accumulate = '', 
                    adjustment = '', 
                    amount = 19995, 
                    conditions = citypay.models.adjustment_condition.AdjustmentCondition(
                        anchor = '', 
                        discount_code = '', 
                        duration = 7, 
                        end_date = 'Sat Aug 31 00:00:00 UTC 2024', 
                        start_date = 'Thu Aug 01 00:00:00 UTC 2024', ), 
                    description = '10% discount for loyalty program members', 
                    percentage = 17.5, ),
                amount = 19995,
                created = '2025-07-04T15:05:47Z',
                currency = 'GBP',
                due = 'Fri Jul 04 00:00:00 UTC 2025',
                expires = 'Fri Jul 04 00:00:00 UTC 2025',
                external_ref = 'ABC123',
                external_ref_source = 'xero',
                identifier = '95b857a1-5955-4b86-963c-5a6dbfc4fb95',
                intent_status = 'open',
                merchantid = 11223344,
                payment_type = '',
                payment_intent_id = 'p13t1111222233334444',
                transactions = citypay.models.auth_reference.AuthReference(
                    address = 'Mielles House, St Helier, Jersey', 
                    amount = '20.0', 
                    amount_value = 3600, 
                    atrn = '', 
                    authcode = '001245A', 
                    authen_result = '', 
                    batchno = '', 
                    bin_commercial = True, 
                    bin_consumer = True, 
                    bin_corporate = True, 
                    bin_credit = True, 
                    bin_debit = True, 
                    cardholder_agreement = '', 
                    currency = 'GBP', 
                    datetime = '2025-01-02T18:32:28Z', 
                    eci = '5', 
                    email = 'card.holder@citypay.com', 
                    env = '', 
                    identifier = '95b857a1-5955-4b86-963c-5a6dbfc4fb95', 
                    initiation = '', 
                    instrument = 'Card', 
                    maskedpan = '4***********0002', 
                    merchantid = 11223344, 
                    meta = {
                        'key' : ''
                        }, 
                    name_on_card = 'MR NE BODY', 
                    postcode = 'L6 12W', 
                    result = '', 
                    result_id = '', 
                    scheme = 'Visa', 
                    scheme_logo = 'https://cdn.citypay.com/img/cs/visa-logo.svg', 
                    trans_status = '', 
                    trans_type = 'A', 
                    transno = 78416, 
                    type = '', 
                    utc = 1746299303000, )
            )
        else:
            return PaymentIntentResponseModel(
                identifier = '95b857a1-5955-4b86-963c-5a6dbfc4fb95',
                merchantid = 11223344,
                payment_intent_id = 'p13t1111222233334444',
        )
        """

    def testPaymentIntentResponseModel(self):
        """Test PaymentIntentResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
