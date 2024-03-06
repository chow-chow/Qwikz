from flask import Blueprint, request
from ..controllers.teacher import TeacherController

teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/', methods=['POST'])
def create_teacher():
  return TeacherController.create_teacher(request.get_json())

@teacher_bp.route('/', methods=['GET'])
def get_teachers():
  return TeacherController.get_teachers()

@teacher_bp.route('/<int:teacher_id>', methods=['GET'])
def get_teacher(teacher_id):
  return TeacherController.get_teacher(teacher_id)

@teacher_bp.route('/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
  return TeacherController.delete_teacher(teacher_id)

@teacher_bp.route('/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id):
  return TeacherController.update_teacher(teacher_id, request.get_json())

@teacher_bp.route('/<int:teacher_id>/groups', methods=['GET'])
def get_teacher_groups(teacher_id):
  return TeacherController.get_teacher_groups(teacher_id)
