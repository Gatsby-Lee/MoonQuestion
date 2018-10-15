"""
@author Gatsby Lee
@since 2018-10-14
"""
import logging
from sqlalchemy import create_engine

LOGGER = logging.getLogger(__name__)


class AppEngineFactory(object):

    _engines = {}

    def __init__(self, engines):
        """
            Args:
                engines tuple of tuple('name', 'dialet')
        """
        for k, dialect in engines.items():
            LOGGER.info('create saengine %s => %s', k, dialect)
            self._engines[k] = create_engine(dialect)

    def get_engine(self):
        return self._engines['master']


def get_engine():
    return create_engine('sqlite:///moonquestion.db')
