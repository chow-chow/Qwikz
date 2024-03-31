from sqlalchemy import Sequence
from datetime import datetime
from .. import db

class GROUP_STUDENT(db.Model):
    """ GROUP_STUDENT Model for storing student inscriptions in groups """

    __tablename__ = 'GROUP_STUDENT'
    GROUP_STUDENT_SEQ = Sequence('GROUP_STUDENT_SEQ', metadata=db.metadata)

    # Columns
    GROUP_STUDENT_ID = db.Column(db.Integer, GROUP_STUDENT_SEQ, primary_key=True, server_default=GROUP_STUDENT_SEQ.next_value())
    QWIKZGROUP_ID = db.Column(db.Integer, db.ForeignKey('QWIKZGROUP.QWIKZGROUP_ID'), nullable=False)
    STUDENT_ID = db.Column(db.Integer, db.ForeignKey('STUDENT.STUDENT_ID'), nullable=False)
    ENROLLMENT_DATE = db.Column(db.DateTime, nullable=False, default=datetime.now())

    # Parent-Child relationships
    QUIZZ_APPLICATION = db.relationship('QUIZZ_APPLICATION', backref='GROUP_STUDENT', lazy='select')
    
    def to_JSON(self):
        return {
            'GROUP_STUDENT_ID': self.GROUP_STUDENT_ID,
            'QWIKZGROUP_ID': self.QWIKZGROUP_ID,
            'STUDENT_ID': self.STUDENT_ID,
            'ENROLLMENT_DATE': self.ENROLLMENT_DATE.isoformat()
        }