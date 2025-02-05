from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = f'https://dashboard.render.com/email-confirm/?token=Z6TbEHVzci1jdWhvajQzdHEyMWM3M2JkY2R0MIkXet8wHFCRHgnxgLKL2sMmkNqsRHgjD1S2ngcOEnz5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'guccalestestkey'

CORS(app)
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')
ma = Marshmallow(app)

@app.after_request
def apply_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response