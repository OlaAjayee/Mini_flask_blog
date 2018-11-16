from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes


# from werkzeug.security import check_password_hash, generate_password_hash

# print('Starting...')
# password = u'olaoluwa'
# password_hash = 'pbkdf2:sha256:50000$Sn52w9kn$2e44ce5daf988306f7e5ca8e3387c13e2aac57ba1635fa949ab4a1df88692e6e'
# check_password_result = check_password_hash(password_hash, password)

# print('Check password: ' + str(check_password_result))