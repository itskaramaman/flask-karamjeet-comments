from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from flask_login import login_required, logout_user


logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout')
@login_required
def logout():
	session.clear()
	logout_user()
	flash('You have succesfully logged out.', 'success')
	return redirect(url_for('dashboard_bp.dashboard'))
