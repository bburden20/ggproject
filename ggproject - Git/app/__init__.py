from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app2 = Flask(__name__)
app2.config.from_object(Config)
db = SQLAlchemy(app2)
migrate = Migrate(app2, db)

from app import routes, models