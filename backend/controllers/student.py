from flask import jsonify
from ..services.student import StudentService

class StudentController:
  @staticmethod
  def create_student(data):
    student = StudentService().insert(data)
    return jsonify(student.to_JSON()), 201
  
  @staticmethod
  def join_group(student_id, group_code):
    return jsonify(StudentService().join_group(student_id,group_code)), 204