from flask import jsonify
from ..services.quizz import QuizzService
from ..services.student import StudentService
from ..models.student import STUDENT
from ..models.quizz import QUIZZ
from ..models.quizz_application import QUIZZ_APPLICATION
from ..models.quizz_questions import QUIZZ_QUESTIONS
from ..models.group_student import GROUP_STUDENT
from ..models.qwikzgroup import QWIKZGROUP
from .. import db
import json

class QuizzController:
    @staticmethod
    def create_quizz(data):
        quizz = QuizzService().insert(data)
        quizz_dict = quizz.to_JSON()  # Convertir a diccionario
        return jsonify(quizz_dict), 201

    @staticmethod
    def query_quizz(data):
        qwikzgroup_id = data['QWIKZGROUP_ID']
        quizzes = QuizzService().query(qwikzgroup_id)
        return jsonify(quizzes), 200

    @staticmethod
    def query_student_quizz(data, student_uid):
        # Desempaquetar el objeto data
        quizz_id = data['queryQuizz']['QUIZZ_ID']
        qwikzgroup_id = data['queryQuizz']['QWIKZGROUP_ID']
        student_id = StudentService().get(student_uid)

        # Buscar el quizz con una consulta compuesta
        result = db.session.query(
            STUDENT.DISPLAY_NAME.label('DISPLAY_NAME'),
            STUDENT.EMAIL.label('EMAIL'),
            QUIZZ_APPLICATION.QUIZZ_APPLICATION_ID.label(
                'QUIZZ_APPLICATION_ID'),
            QUIZZ.QUIZZ_ID.label('QUIZZ_ID'),
            QUIZZ.QUIZZ_NAME.label('QUIZZ_NAME'),
            QUIZZ_QUESTIONS.QUESTIONS.label('QUESTIONS'),
            QWIKZGROUP.QWIKZGROUP_ID.label('QWIKZGROUP_ID'),
            QWIKZGROUP.GROUP_NAME.label('GROUP_NAME'),
            QUIZZ.LIMIT_TIME.label('LIMIT_TIME'),
            QUIZZ.MAX_RETRY.label('MAX_RETRY'),
            QUIZZ_APPLICATION.IS_COMPLETED.label('IS_COMPLETED')
        ).join(GROUP_STUDENT, STUDENT.GROUP_STUDENTS).join(QUIZZ_APPLICATION, GROUP_STUDENT.QUIZZ_APPLICATION).join(QUIZZ, QUIZZ_APPLICATION.QUIZZ).join(QUIZZ_QUESTIONS, QUIZZ.QUIZZ_QUESTIONS).join(QWIKZGROUP, GROUP_STUDENT.QWIKZGROUP).filter(
            QUIZZ.QUIZZ_ID == quizz_id,
            QWIKZGROUP.QWIKZGROUP_ID == qwikzgroup_id,
            STUDENT.STUDENT_ID == student_id
        ).all()

        # Convertir los resultados en una lista de diccionarios y procesar QUESTIONS para enviarlo de vuelta formateado
        result_list = []
        for row in result:
            row_dict = row._asdict()
            if row_dict['QUESTIONS']:
                row_dict['QUESTIONS'] = json.loads(row_dict['QUESTIONS'])
            result_list.append(row_dict)

        return jsonify(result_list), 200
