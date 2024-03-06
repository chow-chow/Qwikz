from flask import Flask
from flask_cors import CORS

from .extensions import db, flask_bcrypt
from .config import config_by_name
from .routes.teacher import teacher_bp
from .routes.student import student_bp
from .routes.group import group_bp


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(teacher_bp, url_prefix='/teacher')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(group_bp, url_prefix='/group')

    return app