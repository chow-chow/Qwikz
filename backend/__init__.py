from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import text
from .extensions import db, flask_bcrypt
from .config import config_by_name
from .routes.teacher import teacher_bp
from .routes.student import student_bp
from .routes.group import group_bp
from .routes.authorization import auth_bp

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    """with app.app_context():
        db.create_all() """

    @app.route('/list-tables')
    def list_tables():
        sql = text("""
        SELECT table_name, tablespace_name
        FROM ALL_TABLES
        """)
        with db.engine.connect() as connection:
            result = connection.execute(sql)
            # Initialize an empty list to store table info
            tables = []
            # Iterate over the result set
            for row in result:
                # Access columns by index and append to the list as a dictionary
                table_info = {'table_name': row[0], 'tablespace_name': row[1]}
                tables.append(table_info)
        return jsonify(tables)

    app.register_blueprint(teacher_bp, url_prefix='/teacher')
    app.register_blueprint(student_bp, url_prefix='/student')
    app.register_blueprint(group_bp, url_prefix='/group')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app