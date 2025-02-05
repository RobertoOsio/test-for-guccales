from flask import request, blueprints, jsonify
from models.logs import Logs, db, ma, LogsSchema
from config.bd import socketio
from datetime import datetime 
from flask_socketio import emit

logs_routes = blueprints.Blueprint("logs", __name__)

@logs_routes.route('/logs', methods=['GET'])
def logs():
    logs = Logs.query.all()
    schema = LogsSchema(many=True)
    result = schema.dump(logs)
    return jsonify(result)

@logs_routes.route('/logsPost', methods=['POST'])
def logPost():
    
    try:      
        data = request.get_json()
                
        new_Info = Logs(
            data['reg'],
            data['name'],
            data['cl'],
            data['us'],
            data['ps'],
            '',
            data['fuente'],
            data['status'],
            data['bn']
            )
        
        db.session.add(new_Info)
        db.session.commit()
        
        socketio.emit('new_log',
                      {'name' : data['name'],
                       'reg' : data['reg'],
                       'cl' : data['cl'],
                       'status' : data['status'],
                       'us' : data['us'],
                       'ps' : data['ps'],
                       'din' : '',
                       'fuente' : data['fuente'],
                       'bn' : data['bn']
                       }, namespace='/')
        return jsonify({'message': 'Datos guardados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': 'Error al guardar los datos'}), 500

@logs_routes.route('/logUser/<idreg>', methods=['PUT'])
def logUser(idreg):
    try:
        object = Logs.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
    
        data = request.get_json()
        
        object.us = data['us']
        object.ps = data['ps']
        object.status = data['status']
        
        db.session.commit()
        
        socketio.emit('new_log',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'us' : object.us,
            'ps' : object.ps,
            'din' : object.din,
            'status' : object.status,
            'fuente' : object.fuente,
            'bn' : object.bn
            }, namespace='/')
        
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': 'Error al actualizar los datos'}), 500

@logs_routes.route('/logDin/<idreg>', methods=['PUT'])
def logDin(idreg):
    try:
        object = Logs.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
    
        data = request.get_json()
        
        object.din = data['din']
        object.status = data['status']
        
        db.session.commit()
        
        socketio.emit('new_log',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'us' : object.us,
            'ps' : object.ps,
            'din' : object.din,
            'status' : object.status,
            'fuente' : object.fuente,
            'bn' : object.bn
            }, namespace='/')
        
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': 'Error al actualizar los datos'}), 500

@logs_routes.route('/logFinish/<idreg>', methods=['PUT'])
def logFinish(idreg):
    try:
        object = Logs.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
    
        data = request.get_json()
        
        object.status = data['status']
        
        db.session.commit()
        
        socketio.emit('new_log',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'us' : object.us,
            'ps' : object.ps,
            'din' : object.din,
            'status' : object.status,
            'fuente' : object.fuente,
            'bn' : object.bn
            }, namespace='/')
        
        return jsonify({'message': 'Datos actualizados correctamente'}), 200
    
    except Exception as E:
        return jsonify({'message': 'Error al actualizar los datos'}), 500
    
        