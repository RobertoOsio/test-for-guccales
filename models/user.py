from config.bd import db, ma, app

class User(db.Model):
    __tablename__ = "User"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(100))
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
with app.app_context():
        db.create_all()
    
class UserSchema(ma.Schema):
        class Meta:
            fields = ('id', 'name', 'password')