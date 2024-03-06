from flask import Blueprint, request
from ..controllers.student import StudentController

student_bp = Blueprint('student', __name__)

@student_bp.route('/', methods=['POST'])
def create_student():
  return StudentController.create_student(request.get_json())

@student_bp.route('/join_group/<int:student_id>/<string:group_code>', methods=['POST'])
def join_group(student_id, group_code):
  return StudentController.join_group(student_id, group_code)