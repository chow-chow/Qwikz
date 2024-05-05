from flask import Blueprint, request, g
from ..controllers.group import GroupController
from ..decorators.decorators import verify_teacher_claim

group_bp = Blueprint('group', __name__)

# TODO: Protect this route, only teachers should be able to create groups
@group_bp.route('/create', methods=['POST'])
@verify_teacher_claim
def create_group():
  """
  Creates a group in request from a teacher.

  :return: A JSON response with a confirmation, and the group details (unique key and access token).
  """
  return GroupController.create_group(request.get_json(), g.uid)

@group_bp.route('/', methods=['GET'])
def get_groups():
  return GroupController.get_groups()

@group_bp.route('/<string:group_code>', methods=['GET'])
def get_group_by_code(group_code):
  return GroupController.get_group_by_code(group_code)

@group_bp.route('/<int:group_id>', methods=['GET'])
def get_group_by_id(group_id):
  return GroupController.get_group_by_id(group_id)

@group_bp.route('/<int:group_id>', methods=['DELETE'])
def delete_group(group_id):
  return GroupController.delete_group(group_id)

@group_bp.route('/<int:group_id>/', methods=['PUT'])
def update_group(group_id):
  return GroupController.update_group(group_id, request.get_json())

@group_bp.route('/<int:group_id>/students', methods=['GET'])
def get_group_students(group_id):
  return GroupController.get_group_students(group_id)
