from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from flask_migrate import Migrate

POSTGRES = {
    'user': 'postgres',
    'pw': 'password',
    'db': 'my_database',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)
# migrate = Migrate(app, db)

app.config['DEBUG'] = True


from app import routes, models