from sqlalchemy import Sequence
from .. import db

class TEACHER(db.Model):
    """ Teacher Model for storing teacher related details """

    __tablename__ = 'TEACHER'
    TEACHER_SEQ = Sequence('TEACHER_SEQ', metadata=db.metadata)

    # Columns
    TEACHER_ID = db.Column(db.Integer, TEACHER_SEQ, primary_key=True, server_default=TEACHER_SEQ.next_value())
    FIREBASE_UID = db.Column(db.String(50), unique=True, nullable=False)
    INSTITUTION_ID = db.Column(db.Integer, db.ForeignKey('INSTITUTION.INSTITUTION_ID'), nullable=True)

    # Parent-Child relationships
    QWIKZGROUPS = db.relationship('QWIKZGROUP', backref='TEACHER', lazy='select')
    
    def to_JSON(self):
        return {
            'TEACHER_ID': self.TEACHER_ID,
            'FIREBASE_UID': self.FIREBASE_UID,
            'INSTITUTION_ID': self.INSTITUTION_ID
        }