"""
Dispatch request.
"""


def includeme(config):
    config.add_route('home', '/')
    config.add_route('home-umd', '/umd/')
    config.add_route('home-esm-client-compiler', '/home-esm-client-compiler/')
    config.add_route('get_questions', '/q/')
