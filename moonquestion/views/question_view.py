"""
@author Gatsby Lee
@since 2018-10-14

View for Questions
"""
import logging

from pyramid.view import view_config

from moonqpy.applogic import QuestionApplogic

LOGGER = logging.getLogger(__name__)


@view_config(route_name='list_questions', renderer='json')
def list_questions(request):
    saengines = request.registry.saengines
    qlist = QuestionApplogic(saengines).get_questions()
    return {'qlist': qlist}
