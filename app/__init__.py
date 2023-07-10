from sqlalchemy import engine_from_config

from app.infrastructure.migration import initialize_sql

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.scan('app.infrastructure.migration') # the "important" line
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    # other statements here
    config.add_handler('main', '/{action}',
                     'app.handlers:MyHandler')
    return config.make_wsgi_app()