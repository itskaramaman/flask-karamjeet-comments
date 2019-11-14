from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from flask_login import login_user, current_user
from passlib.hash import sha256_crypt
from main.forms import LoginForm
from main.models import User


login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
	"""Login function for user."""
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		email_credential = request.form['email']
		password_credential = request.form['password']
		user = User.query.filter_by(email=email_credential).first()
		if user and sha256_crypt.verify(password_credential, user.password):
			login_user(user)
			session['logged_in'] = True
			session['name'] = user.name
			flash('Welcome back ' + current_user.name.title(), 'success')
			return redirect(url_for('dashboard_bp.dashboard'))
		else:
			flash('Wrong Credentials', 'danger')
			return redirect(url_for('login_bp.login'))
	return render_template('login.html', form=form)
