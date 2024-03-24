from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import json

# Custom SQLAlchemy class to handle Oracle JSON serialization
class CustomSQLAlchemy(SQLAlchemy):
    def apply_driver_hacks(self, app, info, options):
        super(CustomSQLAlchemy, self).apply_driver_hacks(app, info, options)
        if 'oracle' in info.drivername:
            options['json_serializer'] = lambda obj: json.dumps(obj, ensure_ascii=False)
            options['json_deserializer'] = lambda obj: json.loads(obj)

db = CustomSQLAlchemy()
flask_bcrypt = Bcrypt()