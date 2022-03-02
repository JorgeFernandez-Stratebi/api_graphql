from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql
import secrets

# conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpass, secrets.dbhost, secrets.dbname)
conn = "mysql+pymysql://root:root@localhost/dw_adventureworks"
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Running...'