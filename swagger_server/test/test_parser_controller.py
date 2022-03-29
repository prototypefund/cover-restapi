# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.test import BaseTestCase


class TestParserController(BaseTestCase):
    """ParserController integration test stubs"""

    def test_read_coverage(self):
        """Test case for read_coverage

        returns coverage for the Parser
        """
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/{commitID}/read_coverage/{coverageID}'.format(project_id='project_id_example', commit_id='commit_id_example', coverage_id='coverage_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_write_coverage(self):
        """Test case for write_coverage

        For Parser to write to DB
        """
        body = None
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/{commitID}/write_coverage'.format(project_id='project_id_example', commit_id='commit_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
