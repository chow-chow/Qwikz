from ..extensions import db
from .institution import INSTITUTION

class TEACHER(db.Model):
    """ Teacher Model for storing teacher related details """
    __tablename__ = 'TEACHER'

    TEACHER_ID = db.Column(db.Integer, primary_key=True)
    FIREBASE_UID = db.Column(db.String(50), unique=True, nullable=False)
    INSTITUTION_ID = db.Column(db.Integer, db.ForeignKey('INSTITUTION.INSTITUTION_ID'), nullable=True)
    
    def to_JSON(self):
        return {
            'teacher_id': self.teacher_id,
            'firebase_uid': self.firebase_uid,
            'institution_id': self.institution_id
        }