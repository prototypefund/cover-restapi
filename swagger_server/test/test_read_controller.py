# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.commit_type import CommitType  # noqa: E501
from swagger_server.models.lines_type import LinesType  # noqa: E501
from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestReadController(BaseTestCase):
    """ReadController integration test stubs"""

    def test_read_commit(self):
        """Test case for read_commit

        searches for commit in project
        """
        query_string = [('commit_id', 'commit_id_example')]
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/read_commit'.format(project_id='project_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_coverage(self):
        """Test case for read_coverage

        returns coverage for the Parser
        """
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/{commitID}/read_coverage/{coverageID}'.format(project_id='project_id_example', commit_id='commit_id_example', coverage_id='coverage_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_coverage_lines(self):
        """Test case for read_coverage_lines

        returns lines from coverage
        """
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/{projectID}/{commitID}/{coverageID}/read_lines'.format(project_id='project_id_example', commit_id='commit_id_example', coverage_id='coverage_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_read_project(self):
        """Test case for read_project

        searches for project
        """
        response = self.client.open(
            '/Cover-Rest/Interface-API/1.0.6/read_project/{projectID}'.format(project_id='project_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
