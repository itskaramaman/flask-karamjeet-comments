from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
	"""Login form for User."""
	email = StringField('Email', [validators.Length(min=1)])
	password = PasswordField('Password', [validators.Length(min=1)])
