from flask import Blueprint, jsonify
from jobtracker.models import jobs

bp = Blueprint('jobs', __name__, url_prefix='/jobs')

@bp.route('/')
def get_jobs():
    return jsonify(jobs)
