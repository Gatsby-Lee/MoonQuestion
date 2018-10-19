"""
@author Gatsby Lee
@since 2018-10-18
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    MetaData,
    Column,
    String,
    Integer,
)

# Recommended naming convention used by Alembic, as various different database
# providers will autogenerate vastly different names making migrations more
# difficult. See: http://alembic.readthedocs.org/en/latest/naming.html
SA_NAMING_CONVENTION = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

SA_METADATA = MetaData(naming_convention=SA_NAMING_CONVENTION)
TABLE_BASE_CLASS = declarative_base(metadata=SA_METADATA)


# this is another way to add Table metadata after building table base class.
class Question(TABLE_BASE_CLASS):
    __tablename__ = "questions"
    qid = Column(Integer, primary_key=True)
    qtitle = Column(String, nullable=False)
