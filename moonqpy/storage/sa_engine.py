"""
@author Gatsby Lee
@since 2018-10-14

SQLAlchemy Engines
"""
import logging
from sqlalchemy import create_engine

LOGGER = logging.getLogger(__name__)


class SAEngineFactory(object):

    _engines = {}

    def __init__(self, engines):
        """
            Args:
                engines tuple of tuple('name', 'dialet')
        """
        for name, dialect in engines.items():
            LOGGER.info('create saengine with %s', name)
            self._engines[name] = create_engine(dialect)

    def get_engine(self):
        """Return SA engine instance in default.
            Returns: tupul(saengine,)
        """
        return (self._engines['master'],)


def get_engine():
    return create_engine('sqlite:///moonquestion.db')
