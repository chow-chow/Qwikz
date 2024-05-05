CREATE OR REPLACE PROCEDURE CREATE_QUIZZ_APPLICATION (p_quizz_id IN INTEGER) AS
BEGIN
    -- Buscar los GROUP_STUDENT_ID asociados al QWIKZGROUP_ID del QUIZZ
    FOR rec IN (SELECT GROUP_STUDENT_ID
                FROM GROUP_STUDENT
                WHERE QWIKZGROUP_ID = (SELECT QWIKZGROUP_ID FROM QUIZZ WHERE QUIZZ_ID = p_quizz_id)) 
    LOOP
        -- Insertar un registro en QUIZZ_APPLICATION para cada GROUP_STUDENT_ID encontrado
        INSERT INTO QUIZZ_APPLICATION (QUIZZ_ID, GROUP_STUDENT_ID, IS_COMPLETED)
        VALUES (p_quizz_id, rec.GROUP_STUDENT_ID, 0); -- IS_COMPLETED inicialmente se establece como 0 (no completado)
    END LOOP;
    COMMIT; -- Confirmar la transacción
END;
/
