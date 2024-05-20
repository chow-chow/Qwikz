from datetime import datetime
from ..models.student import STUDENT as Student
from ..models.group_student import GROUP_STUDENT as GroupStudent
from ..models.qwikzgroup import QWIKZGROUP as Group
from ..services.group import GroupService
from ..models.quizz import QUIZZ as Quizz
from sqlalchemy import text
from .. import db

class StudentService:
  @staticmethod
  def insert(data):
    student = Student(
      FIREBASE_UID=data['FIREBASE_UID'],
      INSTITUTION_ID= None,
      DISPLAY_NAME=data['DISPLAY_NAME'],
      EMAIL=data['EMAIL']
    )
    db.session.add(student)
    db.session.commit()
    return student
  
  @staticmethod
  def get_all():
    return Student.query.all()
  
  @staticmethod
  def get(student_uid):
    """Return the STUDENT_ID by the student_uid"""
    student = Student.query.filter_by(FIREBASE_UID=student_uid).first()
    if student:
      return student.STUDENT_ID
  
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
  def join_group(student_uid, access_token):
    group = GroupService().get(access_token)
    qwikzgroup_id = group['QWIKZGROUP_ID']
    student_id = StudentService().get(student_uid)

    new_group_student = GroupStudent(
      STUDENT_ID=student_id,
      QWIKZGROUP_ID=qwikzgroup_id,
    )

    db.session.add(new_group_student)
    db.session.commit()

    existing_quizzes = Quizz.query.filter_by(QWIKZGROUP_ID=qwikzgroup_id).all()

    for quizz in existing_quizzes:
      try:
          db.session.execute(text("CALL CREATE_QUIZZ_APPLICATION(:quizz_id)"), {'quizz_id': quizz.QUIZZ_ID})
          db.session.commit()
      except Exception as e:
          db.session.rollback()
          print(f"Error al llamar al procedimiento almacenado: {e}")

    return new_group_student
  
  @staticmethod
  def get_groups(student_uid):
    """Return the groups in which the student is enrolled querying by student_uid"""
    student = Student.query.filter_by(FIREBASE_UID=student_uid).first()
    group_ids = [gs.QWIKZGROUP_ID for gs in student.GROUP_STUDENTS]
    groups = Group.query.filter(Group.QWIKZGROUP_ID.in_(group_ids)).all()
    return groups