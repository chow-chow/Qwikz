from sqlalchemy import Sequence
from .. import db
import json

class QUIZZ(db.Model):
    """ QUIZZ Model for storing quizz related details """
    
    __tablename__ = 'QUIZZ'
    QUIZZ_SEQ = Sequence('QUIZZ_SEQ', metadata=db.metadata)

    # Columns
    QUIZZ_ID   = db.Column(db.Integer, QUIZZ_SEQ, primary_key=True, server_default=QUIZZ_SEQ.next_value())
    QUIZZ_CODE = db.Column(db.String(7), unique=True, nullable=False)
    QUIZZ_NAME = db.Column(db.String(30))
    LIMIT_TIME = db.Column(db.Integer)
    MAX_RETRY  = db.Column(db.Integer)
    QWIKZGROUP_ID = db.Column(db.Integer, db.ForeignKey('QWIKZGROUP.QWIKZGROUP_ID'), nullable=False)

    # Parent-Child relationships
    QUIZZ_MEDIA = db.relationship('QUIZZ_MEDIA', backref='QUIZZ', lazy='select')
    QUIZZ_APPLICATION = db.relationship('QUIZZ_APPLICATION', backref='QUIZZ', lazy='select')


    QUIZZ_QUESTIONS = db.relationship('QUIZZ_QUESTIONS', uselist=False, lazy='select')

    def to_JSON(self):
        return {
            'QUIZZ_ID': self.QUIZZ_ID,
            'QUIZZ_CODE': self.QUIZZ_CODE,
            'QUIZZ_NAME': self.QUIZZ_NAME,
            'LIMIT_TIME': self.LIMIT_TIME,
            'MAX_RETRY': self.MAX_RETRY,
            'QWIKZGROUP_ID': self.QWIKZGROUP_ID,
            'QUESTIONS': self.QUIZZ_QUESTIONS.questions
        }

"""     @property
    def questions(self):
        return json.loads(self.QUESTIONS)

    @questions.setter
    def questions(self, value):
        self.QUESTIONS = json.dumps(value, ensure_ascii=False) """