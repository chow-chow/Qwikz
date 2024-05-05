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
    q.QUIZZ_ID = 3;

SELECT * FROM QUIZZ;
