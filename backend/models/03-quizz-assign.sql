CREATE OR REPLACE PROCEDURE CREATE_QUIZZ_APPLICATION (p_quizz_id IN INTEGER) AS
BEGIN
    -- Buscar los GROUP_STUDENT_ID asociados al QWIKZGROUP_ID del QUIZZ
    FOR rec IN (
        SELECT gs.GROUP_STUDENT_ID
        FROM GROUP_STUDENT gs
        LEFT JOIN QUIZZ_APPLICATION qa ON gs.GROUP_STUDENT_ID = qa.GROUP_STUDENT_ID AND qa.QUIZZ_ID = p_quizz_id
        WHERE gs.QWIKZGROUP_ID = (SELECT QWIKZGROUP_ID FROM QUIZZ WHERE QUIZZ_ID = p_quizz_id)
        AND qa.GROUP_STUDENT_ID IS NULL -- Solo considerar GROUP_STUDENT_IDs que no tienen un registro en QUIZZ_APPLICATION para este QUIZZ_ID
    ) 
    LOOP
        -- Insertar un registro en QUIZZ_APPLICATION para cada GROUP_STUDENT_ID encontrado que no tenga ya un registro
        INSERT INTO QUIZZ_APPLICATION (QUIZZ_ID, GROUP_STUDENT_ID, IS_COMPLETED)
        VALUES (p_quizz_id, rec.GROUP_STUDENT_ID, 0); -- IS_COMPLETED inicialmente se establece como 0 (no completado)
    END LOOP;
    COMMIT; -- Confirmar la transacción
END;
/