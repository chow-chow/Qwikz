from sqlalchemy import Sequence
from .. import db

class INSTITUTION(db.Model):
    """ Institution Model for storing institution related details"""

    __tablename__ = 'INSTITUTION'
    INSTITUTION_SEQ = Sequence('INSTITUTION_SEQ', metadata=db.metadata)

    # Columns
    INSTITUTION_ID = db.Column(db.Integer, INSTITUTION_SEQ, primary_key=True, server_default=INSTITUTION_SEQ.next_value())
    NAME = db.Column(db.String(20))
    CODE = db.Column(db.String(20))

    # Parent-Child relationships
    TEACHERS = db.relationship('TEACHER', backref='INSTITUTION', lazy='select')
    STUDENTS = db.relationship('STUDENT', backref='INSTITUTION', lazy='select')

    def to_JSON(self):
        return {
            'INSTITUTION_ID': self.INSTITUTION_ID,
            'NAME': self.NAME,
            'CODE': self.CODE,
        }