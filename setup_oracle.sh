#!/bin/bash
# Esperar a que Oracle esté listo para las conexiones
until echo 'SELECT 1 FROM DUAL;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba; do
    sleep 10
done

# Cambiar a modo UPGRADE y establecer MAX_STRING_SIZE a EXTENDED
echo 'SHUTDOWN IMMEDIATE;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba
echo 'STARTUP UPGRADE;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba
echo 'ALTER SYSTEM SET MAX_STRING_SIZE=EXTENDED SCOPE=SPFILE;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba

# Ejecutar utl32k.sql para modificar estructuras existentes
echo '@?/rdbms/admin/utl32k.sql;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba

# Reiniciar en modo NORMAL
echo 'SHUTDOWN IMMEDIATE;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba
echo 'STARTUP;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba

# Recompilar objetos inválidos
echo '@?/rdbms/admin/utlrp.sql;' | sqlplus -S sys/Oracle_123@//localhost:1521/ORCLCDB as sysdba
