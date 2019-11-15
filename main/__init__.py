from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iktoyoltxsavlq:b0ba0117d74cb73fd8d24e5d626bf9580834166fd63fdeef6e63efe5aba8065c@ec2-54-235-180-123.compute-1.amazonaws.com:5432/d27r6jqgojbre5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_shhh'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
from main.models import Post, User, MyModelView
admin = Admin(app)
admin.add_view(MyModelView(Post, db.session))
admin.add_view(MyModelView(User, db.session))
migrate = Migrate(app, db)


@login_manager.user_loader
def getUser(user_id):
	return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('login_required.html')

from main.views import dashboard_bp, post_bp, register_bp, login_bp, logout_bp, profile_bp
app.register_blueprint(dashboard_bp)
app.register_blueprint(post_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(profile_bp)
