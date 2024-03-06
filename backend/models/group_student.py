from .. import db

group_student = db.Table('group_student',
  db.Column('group_id', db.Integer, db.ForeignKey('group.group_id'), primary_key=True),
  db.Column('student_id', db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
)