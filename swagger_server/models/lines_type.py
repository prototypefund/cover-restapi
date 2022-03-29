# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LinesType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, lines: List[str]=None):  # noqa: E501
        """LinesType - a model defined in Swagger

        :param lines: The lines of this LinesType.  # noqa: E501
        :type lines: List[str]
        """
        self.swagger_types = {
            'lines': List[str]
        }

        self.attribute_map = {
            'lines': 'lines'
        }
        self._lines = lines

    @classmethod
    def from_dict(cls, dikt) -> 'LinesType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LinesType of this LinesType.  # noqa: E501
        :rtype: LinesType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def lines(self) -> List[str]:
        """Gets the lines of this LinesType.


        :return: The lines of this LinesType.
        :rtype: List[str]
        """
        return self._lines

    @lines.setter
    def lines(self, lines: List[str]):
        """Sets the lines of this LinesType.


        :param lines: The lines of this LinesType.
        :type lines: List[str]
        """
        if lines is None:
            raise ValueError("Invalid value for `lines`, must not be `None`")  # noqa: E501

        self._lines = lines
