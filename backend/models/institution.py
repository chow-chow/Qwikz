from ..extensions import db

class INSTITUTION(db.Model):
    """ Institution Model for storing institution related details """
    __tablename__ = 'INSTITUTION'

    INSTITUTION_ID = db.Column(db.Integer, primary_key=True)
    NAME = db.Column(db.String(20))
    CODE = db.Column(db.String(20))
    ADDRESS = db.Column(db.String(20))

    TEACHERS = db.relationship('TEACHER', backref='INSTITUTION', lazy=True)

    def to_JSON(self):
        return {
            'institution_id': self.INSTITUTION_ID,
            'name': self.NAME,
            'code': self.CODE,
            'address': self.ADDRESS
        }