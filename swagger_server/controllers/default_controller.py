import connexion
import six

from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server import util


def root_get():  # noqa: E501
    """default, for testing

    route for testing # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def root_post(body=None):  # noqa: E501
    """default, for testing

    route for testing # noqa: E501

    :param body: Test Object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProjectType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
