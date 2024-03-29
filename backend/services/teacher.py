from ..models.teacher import Teacher
from .. import db

class TeacherService:
  @staticmethod
  def insert(data):
    teacher = Teacher(
      teacher_id=data['teacher_id'],
      first_name=data['first_name'],
      last_name=data['last_name'],
      email=data['email'],
    )
    teacher.password = data['password']
    db.session.add(teacher)
    db.session.commit()
    return teacher

  @staticmethod
  def delete(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    db.session.delete(teacher)
    db.session.commit()
    return None
  
  @staticmethod
  def get_all():
    return Teacher.query.all()
  
  @staticmethod
  def get(teacher_id):
    return Teacher.query.filter_by(teacher_id=teacher_id).first()
  
  @staticmethod
  def update(teacher_id, data):
    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    teacher.first_name = data['first_name']
    teacher.last_name = data['last_name']
    teacher.email = data['email']
    db.session.commit()
    return teacher
  
  @staticmethod
  def get_groups(teacher_id):
    teacher = Teacher.query.filter_by(teacher_id=teacher_id).first()
    return teacher.groups