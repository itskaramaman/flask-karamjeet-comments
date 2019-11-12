from wtforms import Form, StringField, TextAreaField, validators

class AddPost(Form):
	title = StringField('Title', [validators.Length(min=1, max=255)])
	content = TextAreaField('Content', [validators.Length(min=1)])