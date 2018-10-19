"""
@author Gatsby Lee
@since 2018-10-13
"""
import logging
import sqlalchemy as SA

LOGGER = logging.getLogger(__name__)


class QuestionApplogic(object):

    _saengines = None

    def __init__(self, saengines):
        self._saengines = saengines
        self.md = self._saengines.get_table_metadata('questions')

    def get_questions(self):
        engine = self._saengines.get_engine()
        stmt = SA.select([self.md])
        return_list = []
        with engine.connect() as conn:
            result_obj = conn.execute(stmt)
            for r in result_obj:
                # return_list.append(dict(r))
                return_list.append(list(r))
        return return_list

    def create_question(self, qobj):
        pass

    def update_question(self, qobj):
        pass

    def delete_question(self, qobj):
        pass
