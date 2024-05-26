from sqlalchemy import Sequence
from .. import db

class QUIZZ_GIF(db.Model):
  """ QuizzGif Model for storing quizz gif related details """
  __tablename__ = 'QUIZZ_GIF'
  QUIZZ_GIF_SEQ = Sequence('QUIZZ_GIF_SEQ', metadata=db.metadata)

  # Columns
  GIF_ID = db.Column(db.Integer, QUIZZ_GIF_SEQ, primary_key=True, server_default=QUIZZ_GIF_SEQ.next_value())
  MIN_SCORE = db.Column(db.Integer, nullable=False)
  MAX_SCORE = db.Column(db.Integer, nullable=False)
  GIF_BLOB = db.Column(db.LargeBinary, nullable=False)

  def to_JSON(self):
    return {
      'GIF_ID': self.GIF_ID,
      'MIN_SCORE': self.MIN_SCORE,
      'MAX_SCORE': self.MAX_SCORE,
      'GIF_BLOB': self.GIF_BLOB,
    }