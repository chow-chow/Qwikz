from sqlalchemy import Sequence
from .. import db

class STUDENT(db.Model):
    """ Student Model for storing student related details """

    __tablename__ = 'STUDENT'
    STUDENT_SEQ = Sequence('STUDENT_SEQ', metadata=db.metadata)
    
    # Columns
    STUDENT_ID = db.Column(db.Integer, STUDENT_SEQ, primary_key=True, server_default=STUDENT_SEQ.next_value())
    FIREBASE_UID = db.Column(db.String(50), unique=True, nullable=False)
    INSTITUTION_ID = db.Column(db.Integer, db.ForeignKey('INSTITUTION.INSTITUTION_ID'), nullable=True)

    # Parent-Child relationships
    GROUP_STUDENTS = db.relationship('GROUP_STUDENT', backref='STUDENT', lazy='select')

    def to_JSON(self):
        return {
            'STUDENT_ID': self.STUDENT_ID,
            'FIREBASE_UID': self.FIREBASE_UID,
            'INSTITUTION_ID': self.INSTITUTION_ID
        }