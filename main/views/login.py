from flask import Blueprint, request, render_template, flash, redirect, url_for, session, g
from flask_login import login_user, current_user
from main import db
from main.forms import LoginForm
from main.models import User


login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		email_credential = request.form['email']
		password_credential = request.form['password']
		user = User.query.filter_by(email=email_credential, password=password_credential).first()
		if user!=None:
			login_user(user)
			session['logged_in'] = True
			session['name'] = user.name
			flash('Welcome back ' + current_user.name.title(), 'success')
			return redirect(url_for('dashboard_bp.dashboard'))
		else:
			flash('Wrong Credentials', 'danger')
			return redirect(url_for('login_bp.login'))
	return render_template('login.html', form=form)
