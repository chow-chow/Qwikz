from flask import jsonify
from ..services.quizz import QuizzService


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