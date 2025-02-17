from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'cabrnKey'

#TODO ZONA DE PERSONALIZACION
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gubase_user:wcddvcGfTyb7h1T65DwIWkx0SJZe8Kri@dpg-cuhokjl6l47c73duj8cg-a/gubase'
allowed_socket_origins = [
    "https://test-for-guccales.onrender.com",
    "https://portalfacturasrecaudos.vercel.app",
    "https://portalfacturasclaro.vercel.app",
    "https://abonateyafebrero.vercel.app"
]
#TODO ZONA DE PERSONALIZACION


# Permitir CORS para todas las APIs
CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins=allowed_socket_origins, async_mode='gevent')
ma = Marshmallow(app)


@app.after_request
def apply_cors(response):
    origin = request.headers.get('Origin') if 'Origin' in request.headers else None
    if origin in allowed_socket_origins or origin is None:
        response.headers['Access-Control-Allow-Origin'] = origin or '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response
