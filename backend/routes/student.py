from flask import Blueprint, request
from ..controllers.student import StudentController

student_bp = Blueprint('student', __name__)

@student_bp.route('/', methods=['POST'])
def create_student():
  return StudentController.create_student(request.get_json())

@student_bp.route('/', methods=['GET'])
def get_students():
  return StudentController.get_students()

@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id):
  return StudentController.get_student(student_id)

@student_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
  return StudentController.delete_student(student_id)

@student_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id):
  return StudentController.update_student(student_id, request.get_json())

@student_bp.route('/<int:student_id>/groups', methods=['GET'])
def get_student_groups(student_id):
  return StudentController.get_student_groups(student_id)

@student_bp.route('/join_group/<int:student_id>/<string:group_code>', methods=['POST'])
def join_group(student_id, group_code):
  return StudentController.join_group(student_id, group_code)