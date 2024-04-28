CREATE TABLESPACE Applications
    DATAFILE '/opt/oracle/oradata/applications.dbf' SIZE 100M
    BLOCKSIZE 8K
    LOGGING
    FORCE LOGGING;

CREATE TABLESPACE Quizz
    DATAFILE '/opt/oracle/oradata/quizz.dbf' SIZE 100M
    BLOCKSIZE 8K
    LOGGING
    FORCE LOGGING;

CREATE TABLESPACE Students  
    DATAFILE '/opt/oracle/oradata/students.dbf' SIZE 100M
    BLOCKSIZE 8K
    LOGGING
    FORCE LOGGING;

CREATE TABLESPACE Teachers
    DATAFILE '/opt/oracle/oradata/teachers.dbf' SIZE 100M
    BLOCKSIZE 8K
    LOGGING
    FORCE LOGGING;
    
CREATE TABLESPACE IndexData
    DATAFILE '/opt/oracle/oradata/indexdata.dbf' SIZE 100M
    BLOCKSIZE 8K
    LOGGING
    FORCE LOGGING;

-- Create sequences for auto-incrementing primary keys  
CREATE SEQUENCE STUDENT_SEQ;
CREATE SEQUENCE INSTITUTION_SEQ;
CREATE SEQUENCE TEACHER_SEQ;
CREATE SEQUENCE QWIKZGROUP_SEQ;
CREATE SEQUENCE GROUP_STUDENT_SEQ;
CREATE SEQUENCE QUIZZ_SEQ;
CREATE SEQUENCE QUIZZ_APPLICATION_SEQ;
CREATE SEQUENCE QUIZZ_MEDIA_SEQ;

-- Clúster para la tabla QUIZZ y QUIZZ_APPLICATION
CREATE CLUSTER quizz_cluster (QUIZZ_ID INTEGER) 
TABLESPACE QUIZZ;

CREATE TABLE INSTITUTION
(
  INSTITUTION_ID INTEGER      DEFAULT INSTITUTION_SEQ.NEXTVAL NOT NULL,
  NAME           VARCHAR2(20),
  CODE           VARCHAR2(20),
  ADDRESS        VARCHAR2(20),
  CONSTRAINT PK_INSTITUTION PRIMARY KEY (INSTITUTION_ID)
)
TABLESPACE TEACHERS;

-- CREATE TABLES
CREATE TABLE STUDENT
(
  STUDENT_ID    INTEGER      DEFAULT STUDENT_SEQ.NEXTVAL NOT NULL,
  FIREBASE_UID  VARCHAR2(50) NOT NULL,
  INSTITUTION_ID INTEGER DEFAULT NULL,
  CONSTRAINT PK_STUDENT PRIMARY KEY (STUDENT_ID),
  CONSTRAINT UK_STUDENT_FIREBASE_UID UNIQUE (FIREBASE_UID),
  CONSTRAINT FK_STUDENT_INSTITUTION FOREIGN KEY (INSTITUTION_ID)
    REFERENCES INSTITUTION (INSTITUTION_ID) ON DELETE SET NULL
)
TABLESPACE STUDENTS;

CREATE TABLE TEACHER  
(
  TEACHER_ID     INTEGER      DEFAULT TEACHER_SEQ.NEXTVAL NOT NULL,
  FIREBASE_UID   VARCHAR2(50) NOT NULL,
  INSTITUTION_ID INTEGER DEFAULT NULL,
  CONSTRAINT PK_TEACHER PRIMARY KEY (TEACHER_ID),
  CONSTRAINT UK_TEACHER_FIREBASE_UID UNIQUE (FIREBASE_UID),
  CONSTRAINT FK_TEACHER_INSTITUTION FOREIGN KEY (INSTITUTION_ID)
    REFERENCES INSTITUTION (INSTITUTION_ID) ON DELETE SET NULL
)
TABLESPACE TEACHERS;

CREATE TABLE QWIKZGROUP
(
  QWIKZGROUP_ID   INTEGER      DEFAULT QWIKZGROUP_SEQ.NEXTVAL NOT NULL,
  GROUP_NAME      VARCHAR2(50) NOT NULL,
  GROUP_CODE      VARCHAR2(7)  NOT NULL,
  ACCESS_TOKEN    VARCHAR2(14) NOT NULL,
  TEACHER_ID      INTEGER      NOT NULL,
  CONSTRAINT PK_QWIKZGROUP PRIMARY KEY (QWIKZGROUP_ID),
  CONSTRAINT FK_QWIKZGROUP_TEACHER FOREIGN KEY (TEACHER_ID)
    REFERENCES TEACHER (TEACHER_ID) ON DELETE SET NULL
)  
ORGANIZATION INDEX PCTTHRESHOLD 20 OVERFLOW TABLESPACE STUDENTS;

CREATE TABLE GROUP_STUDENT
(
  GROUP_STUDENT_ID INTEGER    DEFAULT GROUP_STUDENT_SEQ.NEXTVAL NOT NULL,
  STUDENT_ID       INTEGER    NOT NULL,
  QWIKZGROUP_ID    INTEGER    NOT NULL,
  ENROLLMENT_DATE  TIMESTAMP  NOT NULL, 
  CONSTRAINT PK_GROUP_STUDENT PRIMARY KEY (GROUP_STUDENT_ID),
  CONSTRAINT FK_GROUP_STUDENT_STUDENT FOREIGN KEY (STUDENT_ID)
    REFERENCES STUDENT (STUDENT_ID),
  CONSTRAINT FK_GROUP_STUDENT_QWIKZGROUP FOREIGN KEY (QWIKZGROUP_ID)
    REFERENCES QWIKZGROUP (QWIKZGROUP_ID),
  CONSTRAINT UQ_STUDENT_QWIKZGROUP UNIQUE (STUDENT_ID, QWIKZGROUP_ID)
)
TABLESPACE STUDENTS;

CREATE TABLE QUIZZ
(
  QUIZZ_ID   INTEGER      DEFAULT QUIZZ_SEQ.NEXTVAL NOT NULL,
  QUIZZ_CODE VARCHAR2(7)  NOT NULL,
  QUIZZ_NAME VARCHAR2(30) NOT NULL,
  LIMIT_TIME INTEGER      NOT NULL,
  MAX_RETRY  INTEGER      NOT NULL,
  QUESTIONS  VARCHAR2(4000)         NOT NULL,
  QWIKZGROUP_ID   INTEGER NOT NULL,
  CONSTRAINT PK_QUIZZ PRIMARY KEY (QUIZZ_ID),
  CONSTRAINT FK_QUIZZ_QWIKZGROUP FOREIGN KEY (QWIKZGROUP_ID)
    REFERENCES QWIKZGROUP (QWIKZGROUP_ID) ON DELETE SET NULL
)
CLUSTER quizz_cluster (QUIZZ_ID);

CREATE TABLE QUIZZ_APPLICATION  
(
  QUIZZ_APPLICATION_ID    INTEGER     DEFAULT QUIZZ_APPLICATION_SEQ.NEXTVAL NOT NULL,
  QUIZZ_ID                INTEGER     NOT NULL,
  GROUP_STUDENT_ID        INTEGER     NOT NULL,
  RESULTS                 NUMBER(2),
  ANSWERS                 VARCHAR2(4000),
  IS_COMPLETED            NUMBER(1)   NOT NULL,
  RETRY_NUMBER            INTEGER     DEFAULT 0,
  CONSTRAINT PK_QUIZZ_APPLICATION PRIMARY KEY (QUIZZ_APPLICATION_ID),
  CONSTRAINT FK_QUIZZ_APP_GROUP_STUDENT FOREIGN KEY (GROUP_STUDENT_ID)
    REFERENCES GROUP_STUDENT (GROUP_STUDENT_ID) ON DELETE SET NULL,
  CONSTRAINT FK_QUIZZ_APP_QUIZZ FOREIGN KEY (QUIZZ_ID)
    REFERENCES QUIZZ (QUIZZ_ID)
) CLUSTER quizz_cluster (QUIZZ_ID);

CREATE BITMAP INDEX idx_quizz_application_is_completed
ON QUIZZ_APPLICATION (IS_COMPLETED)
TABLESPACE IndexData;

CREATE TABLE QUIZZ_MEDIA
(
  MEDIA     BLOB,
  QUESTION  NUMBER(2),
  MEDIA_ID  INTEGER   DEFAULT QUIZZ_MEDIA_SEQ.NEXTVAL NOT NULL,
  QUIZZ_ID  INTEGER  NOT NULL,
  CONSTRAINT PK_QUIZZ_MEDIA PRIMARY KEY (MEDIA_ID, QUIZZ_ID),
  CONSTRAINT FK_QUIZZ_MEDIA_QUIZZ FOREIGN KEY (QUIZZ_ID)
    REFERENCES QUIZZ (QUIZZ_ID)
)
TABLESPACE QUIZZ CACHE;
