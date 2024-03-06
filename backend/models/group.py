from .. import db
from .group_student import group_student

class Group(db.Model):
  """ Group Model for storing Group related details """
  __tablename__ = "group"

  group_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(50), nullable=False)
  group_code = db.Column(db.String(255), nullable=False)
  group_picture = db.Column(db.LargeBinary, nullable=True)
  teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.teacher_id'), nullable=False)
  students = db.relationship('Student', secondary=group_student, back_populates='groups')

  def to_JSON(self):
    return {
      'group_id': self.group_id,
      'name': self.name,
      'group_code': self.group_code
    }