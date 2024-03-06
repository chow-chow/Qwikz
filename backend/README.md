# Qwikz API

## Ejecutar la API localmente

1. Crear la imagen para ejecutar oracle db en un contenedor de docker
   1. Clonar el repositorio: `https://github.com/oracle/docker-images.git`
   2. Descargar el zip `https://www.oracle.com/cis/database/technologies/oracle19c-linux-downloads.html#license-lightbox` para la versión 19.3.0 y moverlo a `docker-images/OracleDatabase/SingleInstance/dockerfiles/19.3.0/`
   3. Acceder a `docker-images/OracleDatabase/SingleInstance/dockerfiles/`
   4. Ejecutar el script de shell: `./buildContainer.sh -v 19.3.0 -s`
   5. Esto crea la imagen de docker: `oracle/database:19.3.0-se2`
2. Editar el archivo `compose.example.yml`:
   1. Este archivo tiene definidos dos servicios: `api` y `db`.
   2. Cambiar el nombre del archivo por `compose.yml`
   3. Asignar un valor a las variables de entorno `ORACLE_SID` (identificador del sistema) y `ORACLE_PWD` (contraseña)
   4. En función de los valores configurados anteriormente crear el string de conexión y asignarlo a la variable de entorno `DATABASE_URL`:
      `oracle+cx_oracle://system:<password>@oracle_db:1521/<sid>`
3. Levantar el contenedor para la base con `docker compose up -d db`, revisar en los logs de docker que aparezca el mensaje: `DATABASE READY TO USE`.
4. Levantar la api con `docker compose up api`

## TO-DO

- [ ] Crear un ID o autoincrementarlo en la base
- [ ] Crear las relaciones entre las tablas
- [ ] Implementar autenticación con `Firebase` o con `pyJWT`
- [ ] Validar el esquema de la respuesta
- [ ] Proteger las rutas
- [ ] Manejo de errores
- [ ] Agregar las rutas faltantes para los modelos

## Mejoras

### `compose.yml`

Para evitar exponer los datos sensibles de la base de datos en el archivo `compose.yml` un enfoque podría ser la utilización de `secrets`: <https://docs.docker.com/compose/use-secrets/>

Se intentó implementar esta característica pero hay veces en que no funciona:

> [!CAUTION] TO-DO:
> Revisar por qué falla esta implementación del archivo `compose.yml` con secrets:

```yml
version: "3.8"

services:
  # api service
  api:
    container_name: flask_api
    build:
      context: ./backend
      dockerfile: flask.Dockerfile
    ports:
      - 5000:5000
    environment:
      DATABASE_URL: /run/secrets/db_url
    depends_on:
      - db
    volumes:
      - ./backend:/app
    secrets:
      - db_url

  # db service
  db:
    container_name: oracle_db
    image: oracle/database:19.3.0-se2
    ports:
      - 1521:1521
    volumes:
      - oracle_data:/opt/oracle/oradata
    environment:
      ORACLE_SID: qwikzora
      ORACLE_PWD: /run/secrets/oracle_password
    secrets:
      - oracle_password

secrets:
  oracle_password:
    file: ./oracle_password.txt
  db_url:
    file: ./db_url.txt

volumes:
  oracle_data:
```

### Ejecutar la api en modo `debug`

Actualmente la api, que está hecha con Flask y Flask_SQLAlchemy (ORM) no activa el modo de depuración a pesar de que se configuró a través del archivo `config.py`:

```py
import os

oracle_local_base = os.environ.get('DATABASE_URL')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False

# cambio momentaneo
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = oracle_local_base
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = oracle_local_base
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = oracle_local_base
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
```

La configuración se hace en el archivo `__init__.py` de la raíz, algo tiene que ver esto con el error:

```py
from flask import Flask
from flask_cors import CORS

from .extensions import db, flask_bcrypt
from .config import config_by_name
from .routes.teacher import teacher_bp


def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    # 👇 Aquí se hace la configuración de la app
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(teacher_bp, url_prefix='/teacher')

    return app
```
