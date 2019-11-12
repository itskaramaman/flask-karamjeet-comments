from datetime import datetime
from main import db

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	title = db.Column(db.String(255), nullable=False)
	content = db.Column(db.Text, nullable=False)
	posted_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	
	def __init__(self, title, content, author_id):
		self.title = title
		self.content = content
		self.author_id = author_id

		
	def __repr__(self):
		return "<Post(id=%s, title=%s, content=%s, author_id=%s, posted_on=%s)>" % (
			self.id, self.title, self.content, self.author_id, self.posted_on)
