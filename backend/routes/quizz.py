from flask import Blueprint, request, g
from ..controllers.quizz import QuizzController
from ..decorators.decorators import verify_token

quizz_bp = Blueprint('quizz', __name__)

@quizz_bp.route('/create', methods=['POST'])
#@verify_teacher_claim
def create_quizz():
  """
    Create a quizz using teacher claims.

    :return: A JSON response with the quizz details.
  """
  print("Mi petición", request.get_json())
  return QuizzController.create_quizz(request.get_json())

@quizz_bp.route('/get_quizzes', methods=['POST'])
#@verify_token
def get_quizzes():
  """
    Get all the quizzes assigned to a group.

    :return: A JSON response with all the queried quizzes.
  """
  return QuizzController.query_quizz(request.get_json())

@quizz_bp.route('/get_quizz', methods=['POST'])

def get_quizz():
# @verify_student_claim
  """
    Get a quizz by QUIZZ_ID to send it to a student.

    :return: A JSON response with the quizz data and the quizz_application.
  """
  return QuizzController.query_quizz(request.get_json())