from flask import Blueprint, request
from ..controllers.group import GroupController

group_bp = Blueprint('group', __name__)

# TODO: Protect this route, only teachers should be able to create groups
@group_bp.route('/', methods=['POST'])
def create_group():
  return GroupController.create_group(request.get_json())

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
