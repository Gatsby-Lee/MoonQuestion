"""
View for Questions
"""
from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='list_questions')
def list_questions(request):
    print('Incoming request')
    return Response('<body><h1>Hello World!</h1></body>')
