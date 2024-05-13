DECLARE
    v_quizz_id INTEGER;
BEGIN
    -- Insertar un nuevo registro en la tabla QUIZZ
    INSERT INTO QUIZZ (QUIZZ_CODE, QUIZZ_NAME, LIMIT_TIME, MAX_RETRY, QWIKZGROUP_ID)
    VALUES ('A31-0X2', 'QUIZZ_NAME_2_Test', 60, 1, 1)
    RETURNING QUIZZ_ID INTO v_quizz_id;

    -- Llamar al procedimiento para crear registros en QUIZZ_APPLICATION
    CREATE_QUIZZ_APPLICATION(v_quizz_id);
END;
/

SELECT 
    Q.QUIZZ_ID, Q.QUIZZ_CODE, QUIZZ_NAME, QG.GROUP_NAME, QG.QWIKZGROUP_ID
FROM
    QUIZZ Q
JOIN
    QWIKZGROUP QG
ON
    QG.QWIKZGROUP_ID = Q.QWIKZGROUP_ID
WHERE
    QG.QWIKZGROUP_ID = 21;

select * from quizz;

select * from student;

SELECT 
    s.DISPLAY_NAME AS student_name,
    s.EMAIL AS student_email,
    q.QUIZZ_CODE,
    q.QUIZZ_NAME,
    qa.RESULTS,
    qa.IS_COMPLETED,
    qa.RETRY_NUMBER
FROM 
    QUIZZ_APPLICATION qa
JOIN 
    GROUP_STUDENT gs ON qa.GROUP_STUDENT_ID = gs.GROUP_STUDENT_ID
JOIN 
    STUDENT s ON gs.STUDENT_ID = s.STUDENT_ID
JOIN 
    QUIZZ q ON qa.QUIZZ_ID = q.QUIZZ_ID
WHERE 
    q.QUIZZ_ID = 41;
    
    
SELECT
    s.display_name, s.email, s.student_id, q.quizz_id, q.quizz_name, q.quizz_code, q.limit_time, q.max_retry
FROM
    STUDENT S
JOIN
    GROUP_STUDENT gs
ON 
    gs.student_id = s.student_id
JOIN
    QWIKZGROUP qg
ON
    qg.qwikzgroup_id = gs.qwikzgroup_id
JOIN
    quizz_application qa
ON 
    qa.group_student_id = gs.group_student_id
JOIN
    quizz q
ON
    q.quizz_id = qa.quizz_id
JOIN
    quizz_questions qq
ON 
    qq.quizz_id = q.quizz_id
WHERE
    q.quizz_id = 45
AND
    qg.qwikzgroup_id = 21
AND
    s.student_id = 1;
    
SELECT 
    s.display_name, s.email, qa.quizz_application_id, q.quizz_id, q.quizz_name, qq.questions, qg.qwikzgroup_id, qg.group_name, q.limit_time, q.max_retry, qa.is_completed
FROM 
    quizz_application qa 
JOIN 
    quizz q 
ON 
    qa.quizz_id = q.quizz_id
JOIN
    quizz_questions qq
ON
    q.quizz_id = qq.quizz_id
JOIN
    group_student gs
ON 
    qa.group_student_id = gs.group_student_id
JOIN
    qwikzgroup qg
ON
    gs.qwikzgroup_id = q.qwikzgroup_id
JOIN
    student s
ON
    gs.student_id = s.student_id
WHERE
    q.quizz_id = 46
AND
    qg.qwikzgroup_id = 21
AND
    s.student_id = 1;

SELECT * FROM QUIZZ;

SELECT * FROM QUIZZ_APPLICATION;


