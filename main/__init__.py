from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://murderer:murderer@localhost:5432/comments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_shhh'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from main.models import Post, User
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(User, db.session))
migrate = Migrate(app, db)

@login_manager.user_loader
def getUser(user_id):
	return User.query.get(int(user_id))


from main.views import dashboard_bp, post_bp, register_bp, login_bp, logout_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(post_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
