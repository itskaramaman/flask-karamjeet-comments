from flask import render_template
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyModelView(ModelView):
	def is_accessible(self):
		if current_user.is_authenticated and current_user.email == 'singhkaramjeetaman@gmail.com':
			return True

	def inaccessible_callback(self, name, **kwargs):
		return render_template('not_admin.html')
