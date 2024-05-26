from flask import Blueprint, request, g
from ..controllers.student import StudentController
from ..decorators.decorators import verify_student_claim

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

@student_bp.route('/groups', methods=['POST'])
@verify_student_claim
def get_student_groups():
  """
  Get the groups in which a student is enrolled.

  :return: A JSON response with the groups in which the student is enrolled.
  """
  return StudentController.get_student_groups(g.uid)

@student_bp.route('/join_group', methods=['POST'])
@verify_student_claim
def join_group():
  """
  Join a group in request from a student.

  :return: A JSON response with a confirmation and the group details.
  """
  access_token = request.json.get('accessToken')
  student_uid = g.uid
  return StudentController.join_group(student_uid, access_token)

@student_bp.route('/leave_group', methods=['POST'])
@verify_student_claim
def leave_group():
  """
  Leave a group in request from a student.

  :return: A JSON response with a confirmation of leaving the group.
  """
  qwikzgroup_id = request.json.get('QWIKZGROUP_ID')
  student_uid = g.uid
  return StudentController.leave_group(student_uid, qwikzgroup_id)