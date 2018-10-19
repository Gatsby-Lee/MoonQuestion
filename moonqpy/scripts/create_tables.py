"""
@author Gatsby Lee
@since 2018-10-18
"""

from moonqpy.storage.sa_engine import SAEngineFactory
from moonqpy.storage.sa_metadata import TABLE_BASE_CLASS

engine_factory = SAEngineFactory({'master': 'sqlite:///moonquestion.db'})
engine = engine_factory.get_engine()
TABLE_BASE_CLASS.metadata.create_all(engine)
