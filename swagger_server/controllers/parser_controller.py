import connexion
import six

from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.parser_format import ParserFormat  # noqa: E501
from swagger_server import util


def read_coverage(project_id, commit_id, coverage_id):  # noqa: E501
    """returns coverage for the Parser

    reads Coverage for the Parser # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param commit_id: pass commit id
    :type commit_id: str
    :param coverage_id: pass coverage id to get it
    :type coverage_id: str

    :rtype: ParserFormat
    """
    return 'do some magic!'


def write_coverage(project_id, commit_id, coverage_id, body=None):  # noqa: E501
    """For Parser to write to DB

    Route for Parser to write to DB # noqa: E501

    :param project_id: pass project id
    :type project_id: str
    :param commit_id: pass commit id
    :type commit_id: str
    :param coverage_id: pass coverage id to get it
    :type coverage_id: str
    :param body: Commit Object
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = ParserFormat.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
