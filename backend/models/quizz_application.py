from sqlalchemy import Sequence
from .. import db

class QUIZZ_APPLICATION(db.Model):
    """ QUIZZ_APPLICATION Model for storing quizz application related details """
    
    __tablename__ = 'QUIZZ_APPLICATION'
    QUIZZ_APPLICATION_SEQ = Sequence('QUIZZ_APPLICATION_SEQ', metadata=db.metadata)

    # Columns
    QUIZZ_APPLICATION_ID = db.Column(db.Integer, QUIZZ_APPLICATION_SEQ, primary_key=True, server_default=QUIZZ_APPLICATION_SEQ.next_value())
    QUIZZ_ID = db.Column(db.Integer, db.ForeignKey('QUIZZ.QUIZZ_ID'))
    GROUP_STUDENT_ID = db.Column(db.Integer, db.ForeignKey('GROUP_STUDENT.GROUP_STUDENT_ID'))
    RESULTS = db.Column(db.Integer)
    # ANSWERS = db.Column(db.JSON) Probably will be converted to a CLOB column
    IS_COMPLETED = db.Column(db.Integer)
    RETRY_NUMBER = db.Column(db.Integer)

    def to_JSON(self):
        return {
            'QUIZZ_APPLICATION_ID': self.QUIZZ_APPLICATION_ID,
            'RESULTS': self.RESULTS,
            'ANSWERS': self.ANSWERS,
            'IS_COMPLETED': self.IS_COMPLETED,
            'RETRY_NUMBER': self.RETRY_NUMBER,
            'GROUP_STUDENT_ID': self.GROUP_STUDENT_ID,
            'QUIZZ_ID': self.QUIZZ_ID
        }