from flask import Blueprint, jsonify
from jobtracker.models import users

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/')
def get_users():
    return jsonify(users)
