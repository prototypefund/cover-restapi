# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_root_get(self):
        """Test case for root_get

        default, for testing
        """
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.9/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_post(self):
        """Test case for root_post

        default, for testing
        """
        body = ProjectType()
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.9/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
