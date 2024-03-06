from ..models.student import Student
from ..services.group import GroupService
from .. import db

class StudentService:
  @staticmethod
  def insert(data):
    student = Student(
      student_id=data['student_id'],
      first_name=data['first_name'],
      last_name=data['last_name'],
      email=data['email'],
    )
    student.password = data['password']
    db.session.add(student)
    db.session.commit()
    return student
  
  @staticmethod
  def get_all():
    return Student.query.all()
  
  @staticmethod
  def get(student_id):
    return Student.query.filter_by(student_id=student_id).first()
  
  @staticmethod
  def delete(student_id):
    student = StudentService.get(student_id)
    db.session.delete(student)
    db.session.commit()
    return None
  
  @staticmethod
  def update(student_id, data):
    student = StudentService.get(student_id)
    student.first_name = data['first_name']
    student.last_name = data['last_name']
    student.email = data['email']
    db.session.commit()
    return student
  
  @staticmethod
  def join_group(student_id, group_code):
    group = GroupService.get_by_code(group_code)
    student = StudentService.get(student_id)
    student.groups.append(group)
    db.session.commit()
    return None
  
  @staticmethod
  def get_groups(student_id):
    student = StudentService.get(student_id)
    return student.groups