import connexion
import six

from swagger_server.models.commit_type import CommitType  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server import util


def write_commit(project_id, body=None, overwrite=None):  # noqa: E501
    """adds commit to database

    Adds Commit to the Database # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param body: Commit Object
    :type body: dict | bytes
    :param overwrite: if Commit Entry should be overwritten when it already exist
    :type overwrite: bool

    :rtype: None
    """
    if connexion.request.is_json:
        body = CommitType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def write_coverage(project_id, commit_id, body=None):  # noqa: E501
    """For Parser to write to DB

    Route for Parser to write to DB # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param commit_id: pass commit id
    :type commit_id: str
    :param body: Commit Object
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def write_project(body=None, overwrite=None):  # noqa: E501
    """adds an Project item

    Adds an Project to the Database # noqa: E501

    :param body: Project Object
    :type body: dict | bytes
    :param overwrite: if Project Entry should be overwritten when it already exist
    :type overwrite: bool

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProjectType.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
