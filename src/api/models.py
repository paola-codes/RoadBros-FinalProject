from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(120), nullable=True)
    full_name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), unique=False, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    phone = db.Column(db.String(120), unique=False, nullable=True)
    rating = db.Column(db.String(120), nullable=True)
    vehicle = db.relationship('Vehicle', backref='user')
    request = db.relationship('Request', backref='user')

    def __repr__(self):
        return '<User %r>' % self.full_name # add more representations

    def serialize(self):
        return {
            "id": self.id,
            "user_type": self.user_type,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "rating": self.rating,
            "vehicle": [vehicle.serialize() for vehicle in self.vehicle],
            "request": [request.serialize() for request in self.request]
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(80), unique=False, nullable=True)
    vehicle_model = db.Column(db.String(80), unique=False, nullable=True)
    vehicle_make = db.Column(db.String(80), unique=False, nullable=True)
    vehicle_year = db.Column(db.String(80), unique=False, nullable=True)
    vehicle_color = db.Column(db.String(80), unique=False, nullable=True)
    vehicle_plate = db.Column(db.String(80), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.vehicle_type # add more representations

    def serialize(self):
        return {
            "id": self.id,
            "vehicle_type": self.vehicle_type,
            "vehicle_model": self.vehicle_model,
            "vehicle_make": self.vehicle_make,
            "vehicle_year": self.vehicle_year,
            "vehicle_color": self.vehicle_color,
            "vehicle_plate": self.vehicle_plate,
            "user_id": self.user_id
        }

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.String(120), unique=False, nullable=True)
    service = db.Column(db.String(120), unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=False, nullable=True)
    trucker_id = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username # add more representations

    def serialize(self):
        return {
            "id": self.id,
            "zip_code": self.zip_code,
            "service": self.service,
            "user_id": self.user_id,
            "trucker_id": self.trucker_id
        }