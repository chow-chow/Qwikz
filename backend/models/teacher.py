from ..extensions import db, flask_bcrypt

class Teacher(db.Model):
    """ Teacher Model for storing teacher related details """
    __tablename__ = "teacher"

    teacher_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    profile_picture = db.Column(db.LargeBinary, nullable=True)
    groups = db.relationship('Group', backref='teacher')

    @property
    def password(self):
        raise AttributeError("password: write-only field")

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def to_JSON(self):
        return {
            'teacher_id': self.teacher_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }