"""
Dispatch request.
"""


def includeme(config):
    config.add_route('list_questions', '/')
