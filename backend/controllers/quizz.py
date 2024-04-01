from flask import jsonify
from ..services.quizz import QuizzService


class QuizzController:
    @staticmethod
    def create_quizz(data):
        quizz = QuizzService().insert(data)
        return jsonify(quizz), 201
    
    @staticmethod
    def query_quizz(data):
        qwikzgroup_id = data['QWIKZGROUP_ID']
        quizzes = QuizzService().query(qwikzgroup_id)
        return jsonify(quizzes), 200