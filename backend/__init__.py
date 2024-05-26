from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import text
from .extensions import db, flask_bcrypt
from .config import config_by_name
from .routes.teacher import teacher_bp
from .routes.student import student_bp
from .routes.group import group_bp
from .routes.authorization import auth_bp
from .routes.quizz import quizz_bp
from .models.quizz_gif import QUIZZ_GIF

def insert_gifs():
    existing_gifs = db.session.query(QUIZZ_GIF).count()
    if existing_gifs == 0:
        db.session.execute(text("""
        DECLARE
        l_blob1 BLOB;
        l_blob2 BLOB;
        l_blob3 BLOB;
        l_bfile1 BFILE := BFILENAME('GIFS_DIR', 'mad.gif');
        l_bfile2 BFILE := BFILENAME('GIFS_DIR', 'easy.gif');
        l_bfile3 BFILE := BFILENAME('GIFS_DIR', 'pedro.gif');
        BEGIN
        -- Insertar el primer GIF
        INSERT INTO QUIZZ_GIF (MIN_SCORE, MAX_SCORE, GIF_BLOB)
        VALUES (0, 5, EMPTY_BLOB())
        RETURNING GIF_BLOB INTO l_blob1;

        DBMS_LOB.FILEOPEN(l_bfile1, DBMS_LOB.FILE_READONLY);
        DBMS_LOB.LOADFROMFILE(l_blob1, l_bfile1, DBMS_LOB.GETLENGTH(l_bfile1));
        DBMS_LOB.FILECLOSE(l_bfile1);

        -- Insertar el segundo GIF
        INSERT INTO QUIZZ_GIF (MIN_SCORE, MAX_SCORE, GIF_BLOB)
        VALUES (6, 8, EMPTY_BLOB())
        RETURNING GIF_BLOB INTO l_blob2;

        DBMS_LOB.FILEOPEN(l_bfile2, DBMS_LOB.FILE_READONLY);
        DBMS_LOB.LOADFROMFILE(l_blob2, l_bfile2, DBMS_LOB.GETLENGTH(l_bfile2));
        DBMS_LOB.FILECLOSE(l_bfile2);

        -- Insertar el tercer GIF
        INSERT INTO QUIZZ_GIF (MIN_SCORE, MAX_SCORE, GIF_BLOB)
        VALUES (9, 10, EMPTY_BLOB())
        RETURNING GIF_BLOB INTO l_blob3;

        DBMS_LOB.FILEOPEN(l_bfile3, DBMS_LOB.FILE_READONLY);
        DBMS_LOB.LOADFROMFILE(l_blob3, l_bfile3, DBMS_LOB.GETLENGTH(l_bfile3));
        DBMS_LOB.FILECLOSE(l_bfile3);
        END;
        """))
        db.session.commit()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    """with app.app_context():
        db.create_all() """
    
    with app.app_context():
        insert_gifs()

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
    app.register_blueprint(quizz_bp, url_prefix='/quizz')

    return app