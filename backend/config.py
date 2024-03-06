import os

# EN CASO DE QUE SE USEN LOS SECRETS DE DOCKER
# secret_file_path = os.environ.get('DATABASE_URL')
# if os.path.exists(secret_file_path):
#     try:
#         with open(secret_file_path, 'r') as file:
#             secret = file.read().strip()
#     except Exception as e:
#         print(f'Error: {e}')

# oracle_local_base = secret

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