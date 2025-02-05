from flask import Flask, request, jsonify, render_template, redirect, session
from models import *
from config.bd import db, app, socketio
from flask_socketio import SocketIO
from functools import wraps

from APIS.user_route import users_routes
from APIS.info_route import info_routes
from APIS.logs_route import logs_routes
from APIS.buttons_route import buttons_routes

app.register_blueprint(users_routes, url_prefix='/users')
app.register_blueprint(info_routes, url_prefix='/info')
app.register_blueprint(logs_routes, url_prefix='/logs')
app.register_blueprint(buttons_routes, url_prefix='/buttons')


TK = 'guccales'

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        if not token or token != TK:
            return redirect("https://www.faithward.org/es/que-es-la-iglesia/")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@token_required
def index():
    return render_template('login.html')

@app.route('/monitoring')
def monitoring():
    if 'username' not in session:
        return redirect('/')
    return render_template('monitoring.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, port=port, allow_unsafe_werkzeug=True)