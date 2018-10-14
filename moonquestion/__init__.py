from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static')
    config.include('pyramid_jinja2')
    config.include('.route')
    config.scan('.views')
    return config.make_wsgi_app()
