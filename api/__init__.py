from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
import secrets

conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)

app = Flask(__name__)
CORS(app)

# app.config['SECRET_KEY'] =
app.config['SQL_ALCHEMY_URI'] = conn

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Running...'