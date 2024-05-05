from flask import jsonify
from ..services.teacher import TeacherService

class TeacherController:
  @staticmethod
  def create_teacher(data):
    teacher = TeacherService().insert(data)
    return jsonify(teacher.to_JSON()), 201

  @staticmethod
  def delete_teacher(teacher_id):
    return jsonify(TeacherService().delete(teacher_id)), 204

  @staticmethod
  def get_teachers():
    teachers = TeacherService().get_all()
    teachers_json = [teacher.to_JSON() for teacher in teachers]
    return jsonify(teachers_json), 200

  @staticmethod
  def get_teacher(teacher_id):
    teacher = TeacherService().get(teacher_id)
    return jsonify(teacher.to_JSON()), 200

  @staticmethod
  def update_teacher(teacher_id, data):
    teacher = TeacherService().update(teacher_id, data)
    return jsonify(teacher.to_JSON()), 200

  # Updated the method signature to receive the teacher_uid
  @staticmethod
  def get_teacher_groups(teacher_uid):
    groups = TeacherService().get_groups(teacher_uid)
    groups_json = [group.to_JSON() for group in groups]
    return jsonify(groups_json), 200