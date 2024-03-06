from ..models.student import Student
from ..models.group import Group
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
  def join_group(student_id, group_code):
    group = Group.query.filter_by(group_code=group_code).first()
    student = Student.query.filter_by(student_id=student_id).first()
    student.groups.append(group)
    db.session.commit()
    return None