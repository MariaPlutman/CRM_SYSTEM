from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
   id = db.Column(db.Integer, primary_key=True)
   password = db.Column(db.String(100))
	name = db.Column(db.String(100))

class Request(ModelMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(100), nullable=False)
	message = db.Column(db.String(2000), nullable=False)

class Client(ModelMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	citizen_id = db.Column(db.String(9),unique = True, nullable=False)
	name = db.Column(db.String(100), nullable=False)
	school_sign = db.Column(db.String(6), nullable=False)

class Project(ModelMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)




    


