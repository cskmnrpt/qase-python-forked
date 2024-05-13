# coding: utf-8

"""
    Qase.io TestOps API v1

    Qase TestOps API v1 Specification.

    The version of the OpenAPI document: 1.0.0
    Contact: support@qase.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from qase.api_client_v1.models.test_step import TestStep

class TestTestStep(unittest.TestCase):
    """TestStep unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestStep:
        """Test TestStep
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestStep`
        """
        model = TestStep()
        if include_optional:
            return TestStep(
                hash = '',
                shared_step_hash = '',
                shared_step_nested_hash = '',
                position = 56,
                action = '',
                expected_result = '',
                data = '',
                attachments = [
                    qase.api_client_v1.models.attachment.Attachment(
                        size = 56, 
                        mime = '', 
                        filename = '', 
                        url = '', )
                    ],
                steps = [
                    None
                    ]
            )
        else:
            return TestStep(
        )
        """

    def testTestStep(self):
        """Test TestStep"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()