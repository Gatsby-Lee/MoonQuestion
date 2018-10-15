"""
@author Gatsby Lee
@since 2018-10-14
"""
import logging

from pyramid.config import Configurator

from moonqpy.storage.sa_engine import AppEngineFactory

LOGGER = logging.getLogger(__name__)


def _get_rdbms(settings):

    rdbms_dict = {}
    for x in settings:
        if x.startswith('rdbms'):
            k = x[x.rindex('.') + 1:]
            v = settings[x]
            rdbms_dict[k] = v

    return rdbms_dict


def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    # @ref: https://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static')
    config.include('pyramid_jinja2')
    config.registry.db = AppEngineFactory(_get_rdbms(settings))
    config.include('.route')
    config.scan('.views')
    return config.make_wsgi_app()
