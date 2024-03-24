from .. import db
from sqlalchemy import Sequence

class STUDENT(db.Model):
    __tablename__ = 'STUDENT'
    
    # Use the sequence for STUDENT_ID in uppercase
    STUDENT_ID = db.Column(db.Integer, primary_key=True)
    FIREBASE_UID = db.Column('FIREBASE_UID', db.String(50), unique=True, nullable=False)

    def to_JSON(self):
        return {
            'student_id': self.STUDENT_ID,
            'firebase_uid': self.FIREBASE_UID
        }