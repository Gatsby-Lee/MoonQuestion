"""
@author Gatsby Lee
@since 2018-10-14

View for Questions
"""
import logging

from pyramid.view import view_config

from moonqpy.applogic import QuestionApp

LOGGER = logging.getLogger(__name__)


@view_config(route_name='home-esm-client-compiler', renderer='moonquestion:templates/home_build_client_compiler.html')
@view_config(route_name='home-umd', renderer='moonquestion:templates/home_umd.html')
def home(request):
    return {}


@view_config(route_name='get_questions', renderer='json')
def list_questions(request):
    saengines = request.registry.saengines
    qlist = QuestionApp.get_questions(saengines)
    return {'qlist': qlist}
