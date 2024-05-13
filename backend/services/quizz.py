from sqlalchemy import text
from ..models.quizz import QUIZZ as Quizz
from ..models.quizz_questions import QUIZZ_QUESTIONS as QuizzQuestions
from .. import db
import json

class QuizzService:
    @staticmethod
    def insert(data):

        quizz = Quizz(
            QUIZZ_CODE=data['QUIZZ_CODE'],
            QUIZZ_NAME=data['QUIZZ_NAME'],
            LIMIT_TIME=data['LIMIT_TIME'],
            MAX_RETRY=data['MAX_RETRY'],
            QWIKZGROUP_ID=data['QWIKZGROUP_ID']
        )

        db.session.add(quizz)
        db.session.commit()

        # Ahora que tenemos el QUIZZ_ID, guardamos las preguntas en QUIZZ_QUESTIONS
        questions_json = json.dumps(data['QUESTIONS'], ensure_ascii=False)

        quizz_questions = QuizzQuestions(
            QUIZZ_ID=quizz.QUIZZ_ID,
            QUESTIONS=questions_json  # Almacenar el JSON de las preguntas
        )

        # Añadir y guardar QUIZZ_QUESTIONS en la base de datos
        db.session.add(quizz_questions)
        db.session.commit()

        # Llamar al procedimiento almacenado CREATE_QUIZZ_APPLICATION
        try:
            db.session.execute(text("CALL CREATE_QUIZZ_APPLICATION(:quizz_id)"), {'quizz_id': quizz.QUIZZ_ID})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error al llamar al procedimiento almacenado: {e}")
        
        return quizz
    
    @staticmethod
    def query(qwikzgroup_id):
        quizzes = Quizz.query.filter_by(QWIKZGROUP_ID=qwikzgroup_id).all()
        print(quizzes)
        return [quizz.to_JSON() for quizz in quizzes]