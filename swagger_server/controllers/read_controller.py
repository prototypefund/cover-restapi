import connexion
import six

from swagger_server.models.commit_type import CommitType  # noqa: E501
from swagger_server.models.lines_type import LinesType  # noqa: E501
from swagger_server.models.project_type import ProjectType  # noqa: E501
from swagger_server import util


def read_commit(project_id, commit_id=None):  # noqa: E501
    """searches for commit in project

    read all commit in project or by passing commit id or ids only those  # noqa: E501

    :param project_id: get commits in project or commits in project by id/ids
    :type project_id: str
    :param commit_id: pass commit id to get it
    :type commit_id: List[str]

    :rtype: List[CommitType]
    """
    return 'do some magic!'


def read_coverage(project_id, commit_id, coverage_id):  # noqa: E501
    """returns coverage for the Parser

    reads Coverage for the Parser # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param commit_id: pass commit id
    :type commit_id: str
    :param coverage_id: pass coverage id to get it
    :type coverage_id: str

    :rtype: object
    """
    return 'do some magic!'


def read_coverage_lines(project_id, commit_id, coverage_id):  # noqa: E501
    """returns lines from coverage

    read lines from coverage # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param commit_id: pass commit id to get it
    :type commit_id: str
    :param coverage_id: pass coverage id to get it
    :type coverage_id: str

    :rtype: LinesType
    """
    return 'do some magic!'


def read_project(project_id):  # noqa: E501
    """searches for project

    read all Projects in the Database or by passing project id or ids only those  # noqa: E501

    :param project_id: get projects in database or project by id/ids
    :type project_id: List[str]

    :rtype: List[ProjectType]
    """
    return 'do some magic!'
