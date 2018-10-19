"""
@author Gatsby Lee
@since 2018-10-13
"""
import logging
import sqlalchemy as SA

LOGGER = logging.getLogger(__name__)


class QuestionApp(object):
    @classmethod
    def get_questions(cls, saengines):
        table_md = saengines.get_table_metadata('questions')
        stmt = SA.select([table_md])

        return_list = []
        engine = saengines.get_engine()
        with engine.connect() as conn:
            result_obj = conn.execute(stmt)
            for r in result_obj:
                # return_list.append(dict(r))
                return_list.append(list(r))
        return return_list

    @classmethod
    def create_question(cls, qobj):
        pass

    @classmethod
    def update_question(cls, qobj):
        pass

    @classmethod
    def delete_question(cls, qobj):
        pass
