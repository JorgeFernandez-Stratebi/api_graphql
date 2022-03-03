from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from api.secrets import DbSecrets

credentials = DbSecrets()
conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(credentials.dbuser, credentials.dbpass, credentials.dbhost, credentials.dbname)
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Running...'