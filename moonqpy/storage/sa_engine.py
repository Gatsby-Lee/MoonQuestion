"""
@author Gatsby Lee
@since 2018-10-14

SQLAlchemy Engines
"""
import logging
import sqlalchemy

from moonqpy.storage.sa_metadata import SA_METADATA

LOGGER = logging.getLogger(__name__)


class SAEngineFactory(object):
    """Providing functionalities related SQLAlchemy Engines."""
    _engines = {}
    _saversion = sqlalchemy.__version__

    def __init__(self, engines):
        """
            Args:
                engines tuple of tuple('name', 'dialet')
        """
        for name, dialect in engines.items():
            LOGGER.info('[%s] create saengine with %s', self._saversion, name)
            self._engines[name] = sqlalchemy.create_engine(dialect)

    def get_table_metadata(self, table_name):
        """Return SQLAlchemy table metadata
            Args: table_name str
            Returns: table metadata obj
        """
        return SA_METADATA.tables[table_name]

    def get_engine(self):
        """Return SQLAlchemy engine instance in default.
            Returns: tupul(saengine,)
        """
        return self._engines['master']
