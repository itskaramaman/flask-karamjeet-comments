from main import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	"""User Registeration Model."""
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(255), nullable=False)
	email = db.Column(db.String(255), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False)
	posts =  db.relationship('Post', backref='user', lazy=True)

	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password

	def __repr__(self):
		return "<User(id=%s, name=%s, email=%s, password=%s)" % (self.id, self.name, self.email, self.password)	
