from sqlalchemy import Sequence
from .. import db

class QUIZZ_MEDIA(db.Model):
    """ QUIZZ_MEDIA Model for storing media related to quizz questions """

    __tablename__ = 'QUIZZ_MEDIA'
    QUIZZ_MEDIA_SEQ = Sequence('QUIZZ_MEDIA_SEQ', metadata=db.metadata)

    # Columns
    QUIZZ_MEDIA_ID = db.Column(db.Integer, QUIZZ_MEDIA_SEQ, primary_key=True, server_default=QUIZZ_MEDIA_SEQ.next_value())
    QUIZZ_ID = db.Column(db.Integer, db.ForeignKey('QUIZZ.QUIZZ_ID'), nullable=False, primary_key=True)
    MEDIA = db.Column(db.BLOB)
    QUESTION = db.Column(db.Integer)
    
    def to_JSON(self):
        return {
            'QUIZZ_ID': self.QUIZZ_ID,
            'QUIZZ_MEDIA_ID': self.QUIZZ_MEDIA_ID,
            'QUESTION': self.QUESTION
        }