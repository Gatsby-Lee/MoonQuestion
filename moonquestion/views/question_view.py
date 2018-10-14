"""
@author Gatsby Lee
@since 2018-10-14

View for Questions
"""

from pyramid.view import view_config

from moonqpy.applogic import QuestionApplogic


@view_config(route_name='list_questions', renderer='json')
def list_questions(request):
    qlist = QuestionApplogic().get_questions()
    return {'qlist': qlist}
