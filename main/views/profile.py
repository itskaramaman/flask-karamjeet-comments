from flask import Blueprint, render_template
from flask_login import current_user, login_required
from main.models import User, Post

profile_bp = Blueprint('profile_bp', __name__)


@profile_bp.route('/profile')
@login_required
def profile():
	"""Author profile page."""
	author = User.query.get(current_user.id)
	return render_template('profile.html', author=author)
