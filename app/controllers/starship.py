from flask import Blueprint

from app.utils.api_response import create_api_response
from app.utils.http_status_code import OK, CREATED, NO_CONTENT
from app.utils.request import get_page_number

from app.services.starship import find_all, find_by_id, save, delete

bp = Blueprint('starships', __name__, url_prefix='/starships')

@bp.get('/')
def fetch_all():
    page = get_page_number()
    data = find_all(page)

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
    delete(id)

    return create_api_response(None, NO_CONTENT)