"""Dashboard business logic."""
from flask import Blueprint, render_template
from main.models import Post, User

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/')
def dashboard():
    """Dashboard business logic."""
    posts = Post.query.join(User).all()
    posts.reverse()
    return render_template('dashboard.html', posts=posts)
