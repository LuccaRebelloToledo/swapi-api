from flask import Blueprint

from app.utils.http_status_code import OK, CREATED, NO_CONTENT
from app.utils.api_response import create_api_response

from app.services.people import find_all, find_by_id, save, delete

bp = Blueprint('people', __name__, url_prefix='/peoples')

@bp.get('/')
def fetch_all():
    data = find_all()

    return create_api_response(data, OK)

@bp.get('/<int:id>')
def fetch_by_id(id):
    data = find_by_id(id)

    return create_api_response(data, OK)

@bp.post('/<int:id>/save')
def save_record(id):
    data = save(id)

    return create_api_response(data, CREATED)

@bp.delete('/<int:id>/delete')
def delete_record(id):
    data = delete(id)

    return create_api_response(data, NO_CONTENT)