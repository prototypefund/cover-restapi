# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.package_type import PackageType  # noqa: F401,E501
from swagger_server.models.sources_type import SourcesType  # noqa: F401,E501
from swagger_server import util


class ParserFormat(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, version: str=None, timestamp: str=None, lines_valid: int=None, lines_covered: int=None, line_rate: int=None, branches_covered: int=None, branches_valid: int=None, branch_rate: int=None, complexity: int=None, sources: List[SourcesType]=None, packages: List[PackageType]=None):  # noqa: E501
        """ParserFormat - a model defined in Swagger

        :param version: The version of this ParserFormat.  # noqa: E501
        :type version: str
        :param timestamp: The timestamp of this ParserFormat.  # noqa: E501
        :type timestamp: str
        :param lines_valid: The lines_valid of this ParserFormat.  # noqa: E501
        :type lines_valid: int
        :param lines_covered: The lines_covered of this ParserFormat.  # noqa: E501
        :type lines_covered: int
        :param line_rate: The line_rate of this ParserFormat.  # noqa: E501
        :type line_rate: int
        :param branches_covered: The branches_covered of this ParserFormat.  # noqa: E501
        :type branches_covered: int
        :param branches_valid: The branches_valid of this ParserFormat.  # noqa: E501
        :type branches_valid: int
        :param branch_rate: The branch_rate of this ParserFormat.  # noqa: E501
        :type branch_rate: int
        :param complexity: The complexity of this ParserFormat.  # noqa: E501
        :type complexity: int
        :param sources: The sources of this ParserFormat.  # noqa: E501
        :type sources: List[SourcesType]
        :param packages: The packages of this ParserFormat.  # noqa: E501
        :type packages: List[PackageType]
        """
        self.swagger_types = {
            'version': str,
            'timestamp': str,
            'lines_valid': int,
            'lines_covered': int,
            'line_rate': int,
            'branches_covered': int,
            'branches_valid': int,
            'branch_rate': int,
            'complexity': int,
            'sources': List[SourcesType],
            'packages': List[PackageType]
        }

        self.attribute_map = {
            'version': 'version',
            'timestamp': 'timestamp',
            'lines_valid': 'lines-valid',
            'lines_covered': 'lines-covered',
            'line_rate': 'line-rate',
            'branches_covered': 'branches-covered',
            'branches_valid': 'branches-valid',
            'branch_rate': 'branch-rate',
            'complexity': 'complexity',
            'sources': 'sources',
            'packages': 'packages'
        }
        self._version = version
        self._timestamp = timestamp
        self._lines_valid = lines_valid
        self._lines_covered = lines_covered
        self._line_rate = line_rate
        self._branches_covered = branches_covered
        self._branches_valid = branches_valid
        self._branch_rate = branch_rate
        self._complexity = complexity
        self._sources = sources
        self._packages = packages

    @classmethod
    def from_dict(cls, dikt) -> 'ParserFormat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParserFormat of this ParserFormat.  # noqa: E501
        :rtype: ParserFormat
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this ParserFormat.


        :return: The version of this ParserFormat.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this ParserFormat.


        :param version: The version of this ParserFormat.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def timestamp(self) -> str:
        """Gets the timestamp of this ParserFormat.


        :return: The timestamp of this ParserFormat.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: str):
        """Sets the timestamp of this ParserFormat.


        :param timestamp: The timestamp of this ParserFormat.
        :type timestamp: str
        """

        self._timestamp = timestamp

    @property
    def lines_valid(self) -> int:
        """Gets the lines_valid of this ParserFormat.


        :return: The lines_valid of this ParserFormat.
        :rtype: int
        """
        return self._lines_valid

    @lines_valid.setter
    def lines_valid(self, lines_valid: int):
        """Sets the lines_valid of this ParserFormat.


        :param lines_valid: The lines_valid of this ParserFormat.
        :type lines_valid: int
        """

        self._lines_valid = lines_valid

    @property
    def lines_covered(self) -> int:
        """Gets the lines_covered of this ParserFormat.


        :return: The lines_covered of this ParserFormat.
        :rtype: int
        """
        return self._lines_covered

    @lines_covered.setter
    def lines_covered(self, lines_covered: int):
        """Sets the lines_covered of this ParserFormat.


        :param lines_covered: The lines_covered of this ParserFormat.
        :type lines_covered: int
        """

        self._lines_covered = lines_covered

    @property
    def line_rate(self) -> int:
        """Gets the line_rate of this ParserFormat.


        :return: The line_rate of this ParserFormat.
        :rtype: int
        """
        return self._line_rate

    @line_rate.setter
    def line_rate(self, line_rate: int):
        """Sets the line_rate of this ParserFormat.


        :param line_rate: The line_rate of this ParserFormat.
        :type line_rate: int
        """

        self._line_rate = line_rate

    @property
    def branches_covered(self) -> int:
        """Gets the branches_covered of this ParserFormat.


        :return: The branches_covered of this ParserFormat.
        :rtype: int
        """
        return self._branches_covered

    @branches_covered.setter
    def branches_covered(self, branches_covered: int):
        """Sets the branches_covered of this ParserFormat.


        :param branches_covered: The branches_covered of this ParserFormat.
        :type branches_covered: int
        """

        self._branches_covered = branches_covered

    @property
    def branches_valid(self) -> int:
        """Gets the branches_valid of this ParserFormat.


        :return: The branches_valid of this ParserFormat.
        :rtype: int
        """
        return self._branches_valid

    @branches_valid.setter
    def branches_valid(self, branches_valid: int):
        """Sets the branches_valid of this ParserFormat.


        :param branches_valid: The branches_valid of this ParserFormat.
        :type branches_valid: int
        """

        self._branches_valid = branches_valid

    @property
    def branch_rate(self) -> int:
        """Gets the branch_rate of this ParserFormat.


        :return: The branch_rate of this ParserFormat.
        :rtype: int
        """
        return self._branch_rate

    @branch_rate.setter
    def branch_rate(self, branch_rate: int):
        """Sets the branch_rate of this ParserFormat.


        :param branch_rate: The branch_rate of this ParserFormat.
        :type branch_rate: int
        """

        self._branch_rate = branch_rate

    @property
    def complexity(self) -> int:
        """Gets the complexity of this ParserFormat.


        :return: The complexity of this ParserFormat.
        :rtype: int
        """
        return self._complexity

    @complexity.setter
    def complexity(self, complexity: int):
        """Sets the complexity of this ParserFormat.


        :param complexity: The complexity of this ParserFormat.
        :type complexity: int
        """

        self._complexity = complexity

    @property
    def sources(self) -> List[SourcesType]:
        """Gets the sources of this ParserFormat.


        :return: The sources of this ParserFormat.
        :rtype: List[SourcesType]
        """
        return self._sources

    @sources.setter
    def sources(self, sources: List[SourcesType]):
        """Sets the sources of this ParserFormat.


        :param sources: The sources of this ParserFormat.
        :type sources: List[SourcesType]
        """
        if sources is None:
            raise ValueError("Invalid value for `sources`, must not be `None`")  # noqa: E501

        self._sources = sources

    @property
    def packages(self) -> List[PackageType]:
        """Gets the packages of this ParserFormat.


        :return: The packages of this ParserFormat.
        :rtype: List[PackageType]
        """
        return self._packages

    @packages.setter
    def packages(self, packages: List[PackageType]):
        """Sets the packages of this ParserFormat.


        :param packages: The packages of this ParserFormat.
        :type packages: List[PackageType]
        """
        if packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages