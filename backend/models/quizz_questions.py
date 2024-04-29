""" from sqlalchemy import ForeignKey, Integer, CLOB
from .. import db

class QUIZZ_QUESTIONS(db.Model):

    __tablename__ = 'QUIZZ_QUESTIONS'

    # Clave primaria y clave foránea referenciando QUIZZ.QUIZZ_ID
    QUIZZ_ID = db.Column(db.Integer, db.ForeignKey('QUIZZ.QUIZZ_ID', ondelete='CASCADE'), primary_key=True)
    
    # Columna para almacenar las preguntas como CLOB
    QUESTIONS = db.Column(CLOB)

    # Estableciendo la relación con QUIZZ
    # QUIZZ = db.relationship('QUIZZ', back_populates='QUIZZ_QUESTIONS', uselist=False)
"""