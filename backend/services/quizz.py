from ..models.quizz import QUIZZ as Quizz
from .. import db
import json

class QuizzService:
    @staticmethod
    def insert(data):
        questions_json = json.dumps(data['QUESTIONS'])

        quizz = Quizz(
            QUIZZ_CODE=data['QUIZZ_CODE'],
            QUIZZ_NAME=data['QUIZZ_NAME'],
            LIMIT_TIME=data['LIMIT_TIME'],
            MAX_RETRY=data['MAX_RETRY'],
            QUESTIONS=questions_json,
            QWIKZGROUP_ID=data['QWIKZGROUP_ID']
        )
        db.session.add(quizz)
        db.session.commit()
        return quizz
    
    @staticmethod
    def query(qwikzgroup_id):
        quizzes = Quizz.query.filter_by(QWIKZGROUP_ID=qwikzgroup_id).all()
        print(quizzes)
        return [quizz.to_JSON() for quizz in quizzes]