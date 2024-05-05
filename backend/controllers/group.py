from flask import jsonify
from ..services.group import GroupService
from ..services.teacher import TeacherService
from ..helpers.group_helpers import prepare_group_object

class GroupController:
  @staticmethod
  def create_group(data, teacher_uid):
    group_name = data.get('groupName')
    teacher_id = TeacherService.get(teacher_uid)
    group_data = prepare_group_object(group_name, teacher_id)
    group = GroupService().insert(group_data)
    return jsonify(group), 201
  
  @staticmethod
  def get_groups():
    groups = GroupService().get_all()
    groups_json = [group.to_JSON() for group in groups]
    return jsonify(groups_json), 200
  
  @staticmethod
  def get_group_by_code(group_code):
    group = GroupService().get_by_code(group_code)
    return jsonify(group.to_JSON()), 200
  
  @staticmethod
  def get_group_by_id(group_id):
    group = GroupService().get(group_id)
    return jsonify(group.to_JSON()), 200
  
  @staticmethod
  def delete_group(group_id):
    return jsonify(GroupService().delete(group_id)), 204
  
  @staticmethod
  def update_group(group_id, data):
    group = GroupService().update(group_id, data)
    return jsonify(group.to_JSON()), 200
  
  @staticmethod
  def get_group_students(group_id):
    students = GroupService().get_students(group_id)
    students_json = [student.to_JSON() for student in students]
    return jsonify(students_json), 200