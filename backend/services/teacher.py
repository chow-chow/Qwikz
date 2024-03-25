from ..models.teacher import TEACHER as Teacher
from ..models.qwikzgroup import QWIKZGROUP as QwikzGroup 
from .. import db

class TeacherService:
  @staticmethod

  # Should work now
  def insert(data):

    teacher = Teacher(
      FIREBASE_UID=data['FIREBASE_UID'],
      INSTITUTION_ID= None # Usamos .get para que sea opcional
    )
    
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
  def get_groups(teacher_uid):
    # Query the teacher by the teacher_uid
    teacher = Teacher.query.filter_by(FIREBASE_UID=teacher_uid).first()
    print(teacher)

    # Use the relationship to get the groups
    return teacher.QWIKZGROUPS