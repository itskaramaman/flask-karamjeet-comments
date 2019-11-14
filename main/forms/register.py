"""USer Registeration Form."""
from wtforms import Form, StringField, PasswordField, validators, ValidationError
from main.models import User


class RegisterForm(Form):
    """User Registeration Form."""

    name = StringField('Name', [validators.Length(min=1, max=255)])
    email = StringField('Email', [validators.Length(min=1, max=255)])
    password = PasswordField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message="Password didn\'t matched!!!")])
    confirm = PasswordField('Confirm Password', [validators.Length(min=1)])

    def validate_email(self, email):
    	user = User.query.filter_by(email=email.data).first()
    	if user:
    		raise ValidationError('That email is already taken. Please choose a different email!!')

