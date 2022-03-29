# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.commit_type import CommitType  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestWriteController(BaseTestCase):
    """WriteController integration test stubs"""

    def test_write_commit(self):
        """Test case for write_commit

        adds commit to database
        """
        body = CommitType()
        query_string = [('overwrite', true)]
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/write_commit'.format(project_id='project_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
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

    def test_write_project(self):
        """Test case for write_project

        adds an Project item
        """
        body = ProjectType()
        query_string = [('overwrite', true)]
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/write_project',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
