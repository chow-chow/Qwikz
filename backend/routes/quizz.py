from flask import Blueprint, jsonify, request, g, send_file
from io import BytesIO
from ..controllers.quizz import QuizzController
from ..decorators.decorators import verify_token, verify_student_claim, verify_teacher_claim
from ..models.quizz_gif import QUIZZ_GIF

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
@verify_student_claim
def get_quizz():
  """
    Get a quizz by QUIZZ_ID to send it to a student.

    :return: A JSON response with the quizz data and the quizz_application.
  """
  student_uid = g.uid
  return QuizzController.query_student_quizz(request.get_json(), student_uid)

@quizz_bp.route('/score_quizz', methods=['POST'])
# @verify_student_claim
def score_quizz():
  """
    Score a quizz by QUIZZ_APPLICATION_ID to update the student results. 

    :return: A JSON response with the quizz_application data and the score stored on the database.
  """
  return QuizzController.score_student_quizz(request.get_json())

@quizz_bp.route('/get_quizz_results', methods=['POST'])
# @verify_teacher_claim
def get_quizz_results():
    """
    Get all the results of a quiz by QUIZZ_ID.

    :return: A JSON response with the results of every student that took the quiz or still hasn't taken it.
    """
    data = request.get_json()
    quizz_id = data.get('QUIZZ_ID')
    if not quizz_id:
        return jsonify({"error": "QUIZZ_ID is required"}), 400

    return QuizzController.query_quizz_results(quizz_id)

@quizz_bp.route('/delete', methods=['POST'])
@verify_teacher_claim
def delete_quizz():
    """
    Delete a quizz by QUIZZ_ID.

    :return: A JSON response with the confirmation of the deletion.
    """
    data = request.get_json()
    quizz_id = data.get('quizzId')

    if not quizz_id:
        return jsonify({"error": "QUIZZ_ID is required"}), 400
    
    print("Mi quizz_id", quizz_id)

    return QuizzController.delete_quizz(quizz_id)

@quizz_bp.route('/get_gif', methods=['POST'])
def get_gif():
    data = request.get_json()
    score = data.get('score')
    
    if score is None:
        return jsonify({"error": "Score is required"}), 400

    try:
        if 0 <= score <= 5:
            gif = QUIZZ_GIF.query.filter(QUIZZ_GIF.MIN_SCORE <= 5, QUIZZ_GIF.MAX_SCORE >= 0).first()
        elif 6 <= score <= 8:
            gif = QUIZZ_GIF.query.filter(QUIZZ_GIF.MIN_SCORE <= 8, QUIZZ_GIF.MAX_SCORE >= 6).first()
        elif 9 <= score <= 10:
            gif = QUIZZ_GIF.query.filter(QUIZZ_GIF.MIN_SCORE <= 10, QUIZZ_GIF.MAX_SCORE >= 9).first()
        else:
            return jsonify({"error": "Invalid score range"}), 400

        if gif is None:
            return jsonify({"error": "No GIF found for the given score, im stupid"}), 404

        return send_file(
            BytesIO(gif.GIF_BLOB),
            mimetype='image/gif',
            as_attachment=True,
            download_name='result.gif'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
