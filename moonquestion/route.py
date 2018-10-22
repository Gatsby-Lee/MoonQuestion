"""
Dispatch request.
"""


def includeme(config):
    config.add_route('home', '/')
    config.add_route('get_questions', '/q/')
