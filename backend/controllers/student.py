from flask import jsonify
from ..services.student import StudentService
from ..services.group import GroupService

class StudentController:
  @staticmethod
  def create_student(data):
    student = StudentService().insert(data)
    return jsonify(student.to_JSON()), 201
  
  @staticmethod
  def get_students():
    students = StudentService().get_all()
    students_json = [student.to_JSON() for student in students]
    return jsonify(students_json), 200
  
  @staticmethod
  def join_group(student_uid, access_token):
    group = StudentService().join_group(student_uid, access_token)
    group_data = GroupService().get_byID(group.QWIKZGROUP_ID)
    return jsonify(group_data.to_JSON()), 201
  
  @staticmethod
  def get_student(student_id):
    student = StudentService().get(student_id)
    return jsonify(student.to_JSON()), 200
  
  @staticmethod
  def delete_student(student_id):
    return jsonify(StudentService().delete(student_id)), 204
  
  @staticmethod
  def update_student(student_id, data):
    student = StudentService().update(student_id, data)
    return jsonify(student.to_JSON()), 200
  
  @staticmethod
  def get_student_groups(student_uid):
    groups = StudentService().get_groups(student_uid)
    groups_json = [group.to_JSON() for group in groups]
    return jsonify(groups_json), 200