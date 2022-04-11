# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CommitType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, message: str=None, branch: str=None):  # noqa: E501
        """CommitType - a model defined in Swagger

        :param id: The id of this CommitType.  # noqa: E501
        :type id: str
        :param message: The message of this CommitType.  # noqa: E501
        :type message: str
        :param branch: The branch of this CommitType.  # noqa: E501
        :type branch: str
        """
        self.swagger_types = {
            'id': str,
            'message': str,
            'branch': str
        }

        self.attribute_map = {
            'id': 'id',
            'message': 'message',
            'branch': 'branch'
        }
        self._id = id
        self._message = message
        self._branch = branch

    @classmethod
    def from_dict(cls, dikt) -> 'CommitType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CommitType of this CommitType.  # noqa: E501
        :rtype: CommitType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this CommitType.


        :return: The id of this CommitType.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this CommitType.


        :param id: The id of this CommitType.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def message(self) -> str:
        """Gets the message of this CommitType.


        :return: The message of this CommitType.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this CommitType.


        :param message: The message of this CommitType.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def branch(self) -> str:
        """Gets the branch of this CommitType.


        :return: The branch of this CommitType.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch: str):
        """Sets the branch of this CommitType.


        :param branch: The branch of this CommitType.
        :type branch: str
        """
        if branch is None:
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501

        self._branch = branch