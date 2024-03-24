from sqlalchemy import Sequence
from .. import db

class QWIKZGROUP(db.Model):
    """ QWIKZGROUP Model for storing groups and related details """

    __tablename__ = 'QWIKZGROUP'
    QWIKZGROUP_SEQ = Sequence('QWIKZGROUP_SEQ', metadata=db.metadata)

    # Columns
    QWIKZGROUP_ID = db.Column(db.Integer, QWIKZGROUP_SEQ, primary_key=True, server_default=QWIKZGROUP_SEQ.next_value())
    GROUP_NAME = db.Column(db.String(50))
    GROUP_CODE = db.Column(db.String(7))
    ACCESS_TOKEN = db.Column(db.String(14))
    TEACHER_ID = db.Column(db.Integer, db.ForeignKey('TEACHER.TEACHER_ID'), nullable=False)
    
    def to_JSON(self):
        return {
            'QWIKZGROUP_ID': self.QWIKZGROUP_ID,
            'GROUP_NAME': self.GROUP_NAME,
            'GROUP_CODE': self.GROUP_CODE,
            'ACCESS_TOKEN': self.ACCESS_TOKEN,
            'TEACHER_ID': self.TEACHER_ID
        }