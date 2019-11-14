from flask import Blueprint, request, render_template, flash, redirect, url_for
from passlib.hash import sha256_crypt
from main import db
from main.forms import RegisterForm
from main.models import User


register_bp = Blueprint('register_bp', __name__)


@register_bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		name = request.form['name']
		email = request.form['email']
		password = sha256_crypt.hash(request.form['password'])
		try:
			user = User(name, email, password)
			db.session.add(user)
			db.session.commit()
			flash('You have been successfully registered.', 'success')
			return redirect(url_for('login_bp.login'))
		except:
			flash('Sorry you can\'t be registered')
			return redirect(url_for('register_bp.register'))
	return render_template('register.html', form=form)
